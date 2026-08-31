#!/usr/bin/env python3
"""Parse Teams scrum attendance xlsx into data/scrum-attendance.json."""

from __future__ import annotations

import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_XLSX = ROOT / "data" / "scrum-attendance.xlsx"
OUT_PATH = ROOT / "data" / "scrum-attendance.json"
NS_MAIN = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
EXCEL_EPOCH = datetime(1899, 12, 30)


def col_row(ref: str) -> tuple[int, int]:
    col = ""
    row = ""
    for ch in ref:
        if ch.isalpha():
            col += ch
        else:
            row += ch
    n = 0
    for ch in col:
        n = n * 26 + (ord(ch) - 64)
    return n, int(row)


def load_shared_strings(zf: ZipFile) -> list[str]:
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    out = []
    for si in root.findall(f"{NS_MAIN}si"):
        texts = [t.text or "" for t in si.iter(f"{NS_MAIN}t")]
        out.append("".join(texts))
    return out


def parse_sheet(zf: ZipFile, strings: list[str], name: str) -> dict[int, dict[int, str]]:
    root = ET.fromstring(zf.read(f"xl/worksheets/{name}"))
    rows: dict[int, dict[int, str]] = {}
    for cell in root.findall(f".//{NS_MAIN}c"):
        ref = cell.get("r")
        if not ref:
            continue
        kind = cell.get("t")
        v = cell.find(f"{NS_MAIN}v")
        inline = cell.find(f"{NS_MAIN}is")
        val = None
        if kind == "s" and v is not None and v.text is not None:
            val = strings[int(v.text)]
        elif kind == "inlineStr" and inline is not None:
            val = "".join(t.text or "" for t in inline.iter(f"{NS_MAIN}t"))
        elif v is not None:
            val = v.text
        col, row = col_row(ref)
        rows.setdefault(row, {})[col] = val
    return rows


def excel_dt(value) -> datetime | None:
    if value is None or value == "":
        return None
    try:
        return EXCEL_EPOCH + timedelta(days=float(value))
    except (TypeError, ValueError):
        return None


def iso_dt(dt: datetime | None) -> str | None:
    if dt is None:
        return None
    return dt.replace(microsecond=0).isoformat()


def parse_duration(text: str | None) -> int:
    if not text:
        return 0
    s = str(text).strip().lower()
    hours = minutes = seconds = 0
    m = re.search(r"(\d+)\s*h", s)
    if m:
        hours = int(m.group(1))
    m = re.search(r"(\d+)\s*m", s)
    if m:
        minutes = int(m.group(1))
    m = re.search(r"(\d+)\s*s", s)
    if m:
        seconds = int(m.group(1))
    if hours or minutes or seconds:
        return hours * 3600 + minutes * 60 + seconds
    return 0


def sheet_names(zf: ZipFile) -> list[str]:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rid_to_target = {}
    for rel in rels:
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rid and target:
            rid_to_target[rid] = target.split("/")[-1]
    out = []
    for sh in wb.findall(f"{NS_MAIN}sheets/{NS_MAIN}sheet"):
        rid = sh.attrib.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        out.append({"name": sh.attrib.get("name"), "file": rid_to_target.get(rid)})
    return out


def parse_xlsx(path: Path) -> dict:
    with ZipFile(path) as zf:
        strings = load_shared_strings(zf)
        names = sheet_names(zf)
        by_file = {n["file"]: n["name"] for n in names}
        sheets = {}
        for fname in ("sheet1.xml", "sheet2.xml", "sheet3.xml"):
            if fname in by_file:
                sheets[by_file[fname]] = parse_sheet(zf, strings, fname)

    meetings = []
    summary = sheets.get("Meeting Summary") or {}
    for row_i in sorted(summary):
        if row_i == 1:
            continue
        row = summary[row_i]
        started = excel_dt(row.get(4))
        ended = excel_dt(row.get(5))
        day = excel_dt(row.get(1))
        meetings.append(
            {
                "date": (day or started).date().isoformat() if (day or started) else None,
                "title": row.get(2),
                "attended_participants": int(float(row.get(3) or 0)),
                "start": iso_dt(started),
                "end": iso_dt(ended),
                "duration": row.get(6),
                "duration_seconds": parse_duration(row.get(6)),
                "average_attendance": row.get(7),
                "source_file": row.get(8),
            }
        )

    participants = []
    part_sheet = sheets.get("Participants") or {}
    for row_i in sorted(part_sheet):
        if row_i == 1:
            continue
        row = part_sheet[row_i]
        day = excel_dt(row.get(1))
        first = excel_dt(row.get(3))
        last = excel_dt(row.get(4))
        participants.append(
            {
                "date": (day or first).date().isoformat() if (day or first) else None,
                "name": row.get(2),
                "first_join": iso_dt(first),
                "last_leave": iso_dt(last),
                "duration": row.get(5),
                "duration_seconds": parse_duration(row.get(5)),
                "email": row.get(6),
                "upn": row.get(7),
                "role": row.get(8),
            }
        )

    activities = []
    act_sheet = sheets.get("In-Meeting Activities") or {}
    for row_i in sorted(act_sheet):
        if row_i == 1:
            continue
        row = act_sheet[row_i]
        day = excel_dt(row.get(1))
        joined = excel_dt(row.get(3))
        left = excel_dt(row.get(4))
        activities.append(
            {
                "date": (day or joined).date().isoformat() if (day or joined) else None,
                "name": row.get(2),
                "join": iso_dt(joined),
                "leave": iso_dt(left),
                "duration": row.get(5),
                "duration_seconds": parse_duration(row.get(5)),
                "email": row.get(6),
                "role": row.get(7),
            }
        )

    return {
        "source": path.name,
        "sheets": [n["name"] for n in names],
        "meetings": meetings,
        "participants": participants,
        "join_leave_events": activities,
        "notes": [
            "Meeting Summary = one row per scrum call (date, start/end, duration, source CSV).",
            "Participants = unique person per call (first join, last leave, in-meeting duration).",
            "In-Meeting Activities = join/leave segments (Vinay has two joins on 17 and 18 Aug).",
            "Excel datetimes are serial days; wall clock is ~09:30 which matches morning IST scrum.",
        ],
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("xlsx", nargs="?", default=str(DEFAULT_XLSX))
    args = parser.parse_args()
    src = Path(args.xlsx)
    data = parse_xlsx(src)
    OUT_PATH.write_text(json.dumps(data, indent=2) + "\n")
    print(
        f"Wrote {OUT_PATH}  meetings={len(data['meetings'])}  "
        f"participants={len(data['participants'])}  events={len(data['join_leave_events'])}"
    )


if __name__ == "__main__":
    main()
