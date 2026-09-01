#!/usr/bin/env python3
"""Build August 2026 sprint retrospective from planned sheet + Jira dumps."""

from __future__ import annotations

import html
import json
import re
import shutil
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

from page_html import render_page

ROOT = Path(__file__).resolve().parents[1]
PLANNED_PATH = ROOT / "data" / "planned.json"
LEAVE_PATH = ROOT / "data" / "leave.json"
NOTES_PATH = ROOT / "data" / "person-notes.json"
SCRUM_PATH = ROOT / "data" / "scrum-attendance.json"
RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
HOURS_PER_DAY = 8.0
SEC_PER_DAY = int(HOURS_PER_DAY * 3600)
PERIOD_START = date(2026, 8, 1)
PERIOD_END = date(2026, 8, 31)
# Calendar days that are not expected workdays (shown on the heatmap).
PUBLIC_HOLIDAYS = {
    date(2026, 8, 28): "Public holiday",
}


def day_col_class(d: date) -> str:
    if d in PUBLIC_HOLIDAYS:
        return " holiday"
    if d.weekday() == 5:
        return " weekend sat"
    if d.weekday() == 6:
        return " weekend sun"
    return ""


def day_col_label(d: date) -> str:
    if d in PUBLIC_HOLIDAYS:
        return "PH"
    return d.strftime("%a")

NAME_MAP = {
    "vinay chowdary chandra": "Vinay",
    "vinay chandra": "Vinay",
    "vinay": "Vinay",
    "sahil siddiqui": "Sahil Siddiqui",
    "t n shambulinga": "Shambu",
    "shambu": "Shambu",
    "dhanush k g": "Dhanush",
    "dhanush kg": "Dhanush",
    "dhanush": "Dhanush",
    "dharshini  m": "Dharshini",
    "dharshini m": "Dharshini",
    "dharshini": "Dharshini",
    "surya pranesh": "Surya",
    "surya": "Surya",
    "rashmi waghmare": "Rashmi",
    "rashmi": "Rashmi",
    "sahil kumar": "Sahil Kumar",
    "twisha sagar": "Twisha",
    "twisha": "Twisha",
    "marish raj r": "Marish",
    "marish raj": "Marish",
    "marish": "Marish",
    "srikant kumar sutar": "Srikant",
    "srikant sutar": "Srikant",
    "srikant": "Srikant",
    "priyanshu rajput": "Priyanshu",
    "priyanshu": "Priyanshu",
    "manjunath gowda r": "Manjunath",
    "manjunath gowda": "Manjunath",
    "manjunath": "Manjunath",
    "deepak bharadwaj": "Deepak",
    "deepak": "Deepak",
    "rushika sriya": "Rushika",
    "rushika": "Rushika",
    "tarun chandra": "Tarun",
    "tarun": "Tarun",
    "sudeep b d": "Sudeep",
    "sudeep": "Sudeep",
    "nagaraju k": "Nagaraju",
    "nagaraju": "Nagaraju",
    "shambulinga": "Shambu",
    "lavanya": "Lavanya",
}

EXCLUDE_PEOPLE = frozenset({"Lavanya"})
BUG_RESOLVED_STATUSES = frozenset({"Done", "Ready for Testing"})

RAW_FILES = {
    "planned_issues": "planned_issues.json",
    "bugs_created": "bugs_created.json",
    "worklogs": [
        "worklogs_p1.json",
        "worklogs_p2.json",
        "worklogs_p3.json",
        "worklogs_p4.json",
    ],
}


def canon_name(name: str | None) -> str:
    if not name:
        return "Unassigned"
    key = re.sub(r"\s+", " ", name).strip().lower()
    return NAME_MAP.get(key, re.sub(r"\s+", " ", name).strip())


def canon_attendee(name: str | None, email: str | None = None) -> str:
    person = canon_name(name)
    key = re.sub(r"\s+", " ", name or "").strip().lower()
    if key in NAME_MAP:
        return NAME_MAP[key]
    if email:
        local = email.split("@")[0].strip().lower()
        spaced = re.sub(r"[._]+", " ", local)
        if spaced in NAME_MAP:
            return NAME_MAP[spaced]
        if local in NAME_MAP:
            return NAME_MAP[local]
        if "shambu" in local:
            return "Shambu"
    return person


def parse_iso_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def scrum_call_is_morning(start_iso: str | None) -> bool:
    dt = parse_iso_dt(start_iso)
    if dt is None:
        return True
    return dt.hour < 13


def leave_covers_scrum(
    leave: dict | None, meeting: dict
) -> bool:
    """True when leave means this person was not expected on that call."""
    if not leave:
        return False
    frac = float(leave.get("fraction") or 0)
    if frac >= 1:
        return True
    if frac <= 0:
        return False
    note = (leave.get("note") or "").lower()
    morning = scrum_call_is_morning(meeting.get("start"))
    if "first" in note:
        return morning
    if "second" in note:
        return not morning
    # Unspecified half-day: morning IST scrum is covered only if we treat it as AM leave.
    return morning


def scrum_day_expected(
    person: str,
    iso: str,
    leave_map: dict[tuple[str, str], dict],
    meeting: dict,
) -> bool:
    d = date.fromisoformat(iso)
    if d.weekday() >= 5 or d in PUBLIC_HOLIDAYS:
        return False
    return not leave_covers_scrum(leave_map.get((person, iso)), meeting)


def fmt_duration_seconds(seconds: int) -> str:
    if seconds <= 0:
        return "—"
    minutes, sec = divmod(int(seconds), 60)
    if minutes >= 60:
        hours, minutes = divmod(minutes, 60)
        return f"{hours}h {minutes}m"
    if sec and minutes:
        return f"{minutes}m {sec}s"
    if minutes:
        return f"{minutes}m"
    return f"{sec}s"


def att_pill(ratio: float | None) -> str:
    if ratio is None:
        return "na"
    if ratio >= 0.9:
        return "on-plan"
    if ratio >= 0.75:
        return "over"
    return "well-over"


def build_scrum(people: list[str], leave_map: dict[tuple[str, str], dict]) -> dict:
    raw = load_json(SCRUM_PATH)
    meetings = raw.get("meetings") or []
    meeting_by_date = {m["date"]: m for m in meetings if m.get("date")}
    call_dates = sorted(meeting_by_date)

    attended: dict[tuple[str, str], dict] = {}
    unmatched: dict[str, dict] = {}
    for row in raw.get("participants") or []:
        iso = row.get("date")
        if not iso:
            continue
        person = canon_attendee(row.get("name"), row.get("email"))
        rec = {
            "raw_name": row.get("name"),
            "email": row.get("email"),
            "duration_seconds": int(row.get("duration_seconds") or 0),
            "duration": row.get("duration") or "",
            "first_join": row.get("first_join"),
            "last_leave": row.get("last_leave"),
            "role": row.get("role"),
        }
        if person in EXCLUDE_PEOPLE:
            continue
        if person not in people:
            bucket = unmatched.setdefault(
                person,
                {"name": person, "raw_names": set(), "emails": set(), "days": []},
            )
            bucket["raw_names"].add(row.get("name") or person)
            if row.get("email"):
                bucket["emails"].add(row.get("email"))
            bucket["days"].append(iso)
            continue
        prev = attended.get((person, iso))
        if prev is None or rec["duration_seconds"] > prev["duration_seconds"]:
            attended[(person, iso)] = rec

    person_rows = []
    team_expected = 0
    team_attended = 0
    for person in people:
        expected_days = []
        attended_expected = []
        missed_days = []
        leave_days = []
        attended_on_leave = []
        durations = []
        day_status = []
        for iso in call_dates:
            meeting = meeting_by_date[iso]
            leave = leave_map.get((person, iso))
            expected = scrum_day_expected(person, iso, leave_map, meeting)
            present = (person, iso) in attended
            rec = attended.get((person, iso))
            if present:
                durations.append(rec["duration_seconds"])
            if expected:
                expected_days.append(iso)
                if present:
                    attended_expected.append(iso)
                    status = "present"
                else:
                    missed_days.append(iso)
                    status = "missed"
            elif leave:
                leave_days.append(iso)
                if present:
                    attended_on_leave.append(iso)
                    status = "leave-attended"
                else:
                    status = "leave"
            else:
                status = "skip"
            day_status.append(
                {
                    "date": iso,
                    "status": status,
                    "duration_seconds": rec["duration_seconds"] if rec else 0,
                    "duration": rec["duration"] if rec else "",
                    "leave_fraction": (leave or {}).get("fraction"),
                    "leave_note": (leave or {}).get("note") or "",
                }
            )
        expected_n = len(expected_days)
        attended_n = len(attended_expected)
        missed_n = len(missed_days)
        rate = round(attended_n / expected_n, 4) if expected_n else None
        avg_s = int(round(sum(durations) / len(durations))) if durations else 0
        team_expected += expected_n
        team_attended += attended_n
        person_rows.append(
            {
                "person": person,
                "expected": expected_n,
                "attended": attended_n,
                "missed": missed_n,
                "attended_on_leave": len(attended_on_leave),
                "leave_call_days": len(leave_days),
                "rate": rate,
                "avg_duration_seconds": avg_s,
                "avg_duration": fmt_duration_seconds(avg_s),
                "days": day_status,
                "missed_dates": missed_days,
                "attended_on_leave_dates": attended_on_leave,
            }
        )

    unmatched_rows = []
    for name, bucket in sorted(unmatched.items()):
        unmatched_rows.append(
            {
                "name": name,
                "raw_names": sorted(bucket["raw_names"]),
                "emails": sorted(bucket["emails"]),
                "days": sorted(set(bucket["days"])),
                "calls": len(set(bucket["days"])),
            }
        )

    team_rate = round(team_attended / team_expected, 4) if team_expected else None
    morning = all(scrum_call_is_morning(m.get("start")) for m in meetings) if meetings else True
    return {
        "call_dates": call_dates,
        "meetings": meetings,
        "people": person_rows,
        "unmatched": unmatched_rows,
        "team": {
            "expected": team_expected,
            "attended": team_attended,
            "missed": team_expected - team_attended,
            "rate": team_rate,
            "calls": len(call_dates),
        },
        "rules": [
            "Source: Teams Meeting Summary + Participants sheets (unique person per call).",
            "Expected call days = weekdays in Aug 2026 with a recorded scrum, excluding Fri 28 public holiday and that person's leave covering the call.",
            "No weekend calls in the export; weekends are not expected.",
            "All 20 recorded calls started ~09:30 (morning IST), so Deepak's 12 Aug first-half leave covers the call: not expected, not a miss.",
            "Full-day leave is never counted as a miss. Joining on a leave day is 'attended on leave' and does not change the rate.",
            "Rate = attended expected calls ÷ expected calls (leave-adjusted).",
        ],
        "calls_are_morning_ist": morning,
    }


def load_leave() -> dict[tuple[str, str], dict]:
    raw = json.loads(LEAVE_PATH.read_text())
    out: dict[tuple[str, str], dict] = {}
    for entry in raw["entries"]:
        iso = entry["date"]
        frac = float(entry.get("fraction", 1))
        note = entry.get("note") or ""
        for name in entry["people"]:
            person = canon_name(name)
            prev = out.get((person, iso))
            if prev:
                frac = min(1.0, prev["fraction"] + frac)
                note = ", ".join(x for x in (prev.get("note"), note) if x)
            out[(person, iso)] = {"fraction": frac, "note": note}
    return out


def is_working_day(d: date) -> bool:
    return d.weekday() < 5 and d not in PUBLIC_HOLIDAYS


def expected_days_for(person: str, leave_map: dict[tuple[str, str], dict]) -> float:
    total = 0.0
    d = PERIOD_START
    while d <= PERIOD_END:
        if is_working_day(d):
            leave_frac = leave_map.get((person, d.isoformat()), {}).get("fraction", 0)
            total += max(0.0, 1.0 - leave_frac)
        d = date.fromordinal(d.toordinal() + 1)
    return round(total, 2)


def leave_days_for(person: str, leave_map: dict[tuple[str, str], dict]) -> float:
    return round(
        sum(
            cell["fraction"]
            for (name, iso), cell in leave_map.items()
            if name == person and PERIOD_START <= date.fromisoformat(iso) <= PERIOD_END
        ),
        2,
    )


def parse_effort(value: str) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text or text.upper() == "NA":
        return None
    try:
        return float(text)
    except ValueError:
        return None


def parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


def adf_text(node) -> str:
    if node is None:
        return ""
    if isinstance(node, str):
        return node.strip()
    if isinstance(node, list):
        return " ".join(adf_text(x) for x in node).strip()
    if isinstance(node, dict):
        if node.get("type") == "text":
            return node.get("text") or ""
        return adf_text(node.get("content") or node.get("body"))
    return ""


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def merge_issues(paths: list[Path]) -> dict[str, dict]:
    by_key: dict[str, dict] = {}
    for path in paths:
        payload = load_json(path)
        for issue in payload.get("issues") or []:
            key = issue["key"]
            existing = by_key.get(key)
            if existing is None:
                by_key[key] = issue
                continue
            by_key[key] = combine_issue(existing, issue)
    return by_key


def combine_issue(a: dict, b: dict) -> dict:
    """Keep one issue dict; union worklogs and comments by id so dumps don't clobber each other."""
    fields_a = a.get("fields") or {}
    fields_b = b.get("fields") or {}
    wl_a = ((fields_a.get("worklog") or {}).get("worklogs")) or []
    wl_b = ((fields_b.get("worklog") or {}).get("worklogs")) or []
    c_a = ((fields_a.get("comment") or {}).get("comments")) or []
    c_b = ((fields_b.get("comment") or {}).get("comments")) or []
    worklogs = list({str(x.get("id")): x for x in wl_a + wl_b if x.get("id")}.values())
    comments = list({str(x.get("id")): x for x in c_a + c_b if x.get("id")}.values())
    primary = b if len(wl_b) + len(c_b) >= len(wl_a) + len(c_a) else a
    other = a if primary is b else b
    out = dict(primary)
    fields = dict(primary.get("fields") or {})
    other_fields = other.get("fields") or {}
    for key in ("summary", "issuetype", "status", "assignee", "reporter", "parent", "created", "timespent", "aggregatetimespent"):
        if not fields.get(key) and other_fields.get(key):
            fields[key] = other_fields[key]
    wl_block = dict(fields.get("worklog") or {})
    wl_block["worklogs"] = worklogs
    wl_block["total"] = max(int(wl_block.get("total") or 0), len(worklogs), int((other_fields.get("worklog") or {}).get("total") or 0))
    c_block = dict(fields.get("comment") or {})
    c_block["comments"] = comments
    c_block["total"] = max(int(c_block.get("total") or 0), len(comments), int((other_fields.get("comment") or {}).get("total") or 0))
    fields["worklog"] = wl_block
    fields["comment"] = c_block
    out["fields"] = fields
    if not out.get("changelog") and other.get("changelog"):
        out["changelog"] = other["changelog"]
    return out


def changelog_worklogs(issue: dict) -> dict[str, dict]:
    """Rebuild current worklogs from changelog timespent deltas, keyed by worklog id.

    Changelog is newest-first. We walk oldest-first so creates apply before edits.
    Date is the first (create) changelog timestamp for that id — used only when
    the worklog payload did not include this id (Jira caps payload at 20).
    """
    histories = list(reversed((issue.get("changelog") or {}).get("histories") or []))
    by_id: dict[str, dict] = {}
    for history in histories:
        items = {item["field"]: item for item in history.get("items") or []}
        ts = items.get("timespent")
        wid = items.get("WorklogId") or {}
        if ts is None:
            continue
        delta = int(ts.get("to") or 0) - int(ts.get("from") or 0)
        created = parse_dt(history.get("created"))
        author = (history.get("author") or {}).get("displayName")
        wid_from = wid.get("from")
        wid_to = wid.get("to")
        if wid_from and not wid_to:
            by_id.pop(wid_from, None)
            continue
        if not wid_to:
            continue
        rec = by_id.get(wid_to)
        if rec is None:
            by_id[wid_to] = {
                "id": wid_to,
                "seconds": delta,
                "when": created,
                "author": author,
                "source": "changelog",
            }
        else:
            rec["seconds"] += delta
    return {wid: rec for wid, rec in by_id.items() if rec["seconds"] > 0}


def collect_worklogs(issues: dict[str, dict]) -> tuple[list[dict], list[dict], dict]:
    """August worklogs, deduped by worklog id. Payload `started` wins; changelog fills gaps."""
    changelog_dir = RAW_DIR / "changelogs"
    rows: list[dict] = []
    truncated: list[dict] = []
    audit = {"issues": [], "duplicate_ids_dropped": 0, "payload_entries": 0, "changelog_fill_entries": 0}
    seen_ids: set[str] = set()

    for key, issue in issues.items():
        fields = issue.get("fields") or {}
        itype = ((fields.get("issuetype") or {}).get("name")) or ""
        summary = fields.get("summary") or ""
        timespent = int(fields.get("timespent") or 0)
        wl_block = fields.get("worklog") or {}
        logs = wl_block.get("worklogs") or []
        total = int(wl_block.get("total") or len(logs))

        changelog_issue = issue
        cl_path = changelog_dir / f"{key}.json"
        if cl_path.exists():
            changelog_issue = load_json(cl_path)

        payload_by_id: dict[str, dict] = {}
        payload_sum = 0
        for log in logs:
            wid = str(log.get("id") or "")
            started = parse_dt(log.get("started"))
            if not wid or started is None:
                continue
            sec = int(log.get("timeSpentSeconds") or 0)
            payload_sum += sec
            payload_by_id[wid] = {
                "id": wid,
                "seconds": sec,
                "when": started,
                "author": (log.get("author") or {}).get("displayName"),
                "source": "payload",
                "time_spent": log.get("timeSpent") or "",
                "comment": adf_text(log.get("comment")),
            }

        filled = dict(payload_by_id)
        cl_map = changelog_worklogs(changelog_issue) if total > len(logs) or cl_path.exists() else {}
        for wid, rec in cl_map.items():
            if wid not in filled:
                filled[wid] = rec

        reconstructed = sum(r["seconds"] for r in filled.values())
        if total > len(logs):
            truncated.append(
                {
                    "key": key,
                    "have": len(logs),
                    "total": total,
                    "timespent_h": round(timespent / 3600.0, 2),
                    "reconstructed_h": round(reconstructed / 3600.0, 2),
                    "timespent_match": abs(reconstructed - timespent) <= 3600,
                }
            )

        audit["issues"].append(
            {
                "key": key,
                "timespent": timespent,
                "payload_n": len(payload_by_id),
                "jira_total": total,
                "merged_n": len(filled),
                "reconstructed": reconstructed,
            }
        )

        for rec in filled.values():
            wid = rec["id"]
            if wid in seen_ids:
                audit["duplicate_ids_dropped"] += 1
                continue
            seen_ids.add(wid)
            when = rec.get("when")
            if when is None:
                continue
            day = when.date() if hasattr(when, "date") else when
            if day < PERIOD_START or day > PERIOD_END:
                continue
            if rec.get("source") == "payload":
                audit["payload_entries"] += 1
            else:
                audit["changelog_fill_entries"] += 1
            rows.append(
                {
                    "id": wid,
                    "key": key,
                    "summary": summary,
                    "issuetype": itype,
                    "author": canon_name(rec.get("author")),
                    "raw_author": rec.get("author"),
                    "date": day.isoformat(),
                    "seconds": int(rec["seconds"]),
                    "time_spent": rec.get("time_spent") or f"{rec['seconds'] / 3600:.2f}h",
                    "comment": rec.get("comment") or "",
                    "source": rec.get("source") or "payload",
                }
            )

    audit["august_seconds"] = sum(r["seconds"] for r in rows)
    audit["august_unique_worklogs"] = len(rows)
    return rows, truncated, audit


def collect_comments(issues: dict[str, dict]) -> list[dict]:
    rows = []
    for key, issue in issues.items():
        fields = issue.get("fields") or {}
        summary = fields.get("summary") or ""
        itype = ((fields.get("issuetype") or {}).get("name")) or ""
        for comment in (fields.get("comment") or {}).get("comments") or []:
            created = parse_dt(comment.get("created"))
            if created is None:
                continue
            day = created.date()
            if day < PERIOD_START or day > PERIOD_END:
                continue
            body = comment.get("body")
            text = body if isinstance(body, str) else adf_text(body)
            text = re.sub(r"\s+", " ", text or "").strip()
            if not text:
                continue
            rows.append(
                {
                    "id": comment.get("id"),
                    "key": key,
                    "summary": summary,
                    "issuetype": itype,
                    "author": canon_name((comment.get("author") or {}).get("displayName")),
                    "date": day.isoformat(),
                    "body": text[:500],
                }
            )
    return rows


def heat_class(seconds: int) -> str:
    h = seconds / 3600.0
    if h <= 0:
        return "h0"
    if h < 2:
        return "h1"
    if h < 4:
        return "h2"
    if h < 6:
        return "h3"
    if h < 8:
        return "h4"
    return "h5"


def mix_widths(on_s: int, off_s: int) -> tuple[float, float]:
    total = on_s + off_s
    if total <= 0:
        return 0.0, 0.0
    return round(100 * on_s / total, 1), round(100 * off_s / total, 1)


def hours(seconds: int) -> float:
    return round(seconds / 3600.0, 2)


def days(seconds: int) -> float:
    return round(seconds / SEC_PER_DAY, 2)


def accuracy(actual_days: float, planned_days: float | None) -> float | None:
    if planned_days is None or planned_days <= 0:
        return None
    return round(actual_days / planned_days, 2)


def fmt_hd(seconds: int) -> str:
    """One quantity: days first so it does not collide with 'logged of available'."""
    return f"{days(seconds):.1f}d ({hours(seconds):.0f}h)"


def fmt_vs(logged_s: int, avail_s: int) -> str:
    return (
        f"{days(logged_s):.1f} of {days(avail_s):.1f}d"
        f" ({hours(logged_s):.0f}h of {hours(avail_s):.0f}h)"
    )


def html_vs(logged_s: int, avail_s: int) -> str:
    return (
        "<span class='timepair'>"
        "<span class='line'>"
        f"<b>{days(logged_s):.1f}</b><span class='of'>of</span>"
        f"<b class='avail'>{days(avail_s):.1f}d</b>"
        "</span>"
        f"<small>{hours(logged_s):.0f}h of {hours(avail_s):.0f}h</small>"
        "</span>"
    )


def day_available_seconds(
    person: str, iso: str, leave_lookup: dict[tuple[str, str], dict]
) -> int:
    d = date.fromisoformat(iso)
    if not is_working_day(d):
        return 0
    leave = leave_lookup.get((person, iso))
    frac = float(leave["fraction"]) if leave else 0.0
    return int(round(max(0.0, 1.0 - frac) * SEC_PER_DAY))


def pill(ratio: float | None) -> str:
    if ratio is None:
        return "n/a"
    if ratio <= 1.1:
        return "on-plan"
    if ratio <= 1.5:
        return "over"
    return "well-over"


def util_pill(ratio: float | None) -> str:
    if ratio is None:
        return "na"
    if ratio >= 0.9:
        return "on-plan"
    if ratio >= 0.75:
        return "over"
    return "well-over"


def build():
    planned = load_json(PLANNED_PATH)
    planned_rows = planned["rows"]
    sheet_jira = {r["jira"] for r in planned_rows if r.get("jira")}
    planned_roots = sheet_jira | {r["parent"] for r in planned_rows if r.get("parent")}
    planned_keys = set(sheet_jira)
    leave_map = load_leave()

    planned_issues = merge_issues([RAW_DIR / RAW_FILES["planned_issues"]])
    all_issues = merge_issues(
        [RAW_DIR / name for name in RAW_FILES["worklogs"]]
        + [RAW_DIR / RAW_FILES["planned_issues"], RAW_DIR / RAW_FILES["bugs_created"]]
    )

    def issue_parent_key(key: str) -> str:
        fields = (all_issues.get(key) or {}).get("fields") or {}
        parent = fields.get("parent") or {}
        return (parent.get("key") or "") if isinstance(parent, dict) else ""

    def ancestor_keys(key: str) -> list[str]:
        out: list[str] = []
        seen: set[str] = set()
        cur = key
        while cur and cur not in seen:
            out.append(cur)
            seen.add(cur)
            cur = issue_parent_key(cur)
        return out

    def is_planned_work_key(key: str) -> bool:
        return any(k in planned_roots for k in ancestor_keys(key))

    def nearest_sheet_jira(key: str) -> str:
        for k in ancestor_keys(key):
            if k in sheet_jira:
                return k
        return ""

    def issue_summary(key: str) -> str:
        fields = (all_issues.get(key) or {}).get("fields") or {}
        return fields.get("summary") or ""

    def issue_status_name(key: str) -> str:
        fields = (all_issues.get(key) or planned_issues.get(key) or {}).get("fields") or {}
        return ((fields.get("status") or {}).get("name")) or ""

    worklogs, truncated, worklog_audit = collect_worklogs(all_issues)
    comments = collect_comments(all_issues)
    for log in worklogs:
        log["on_sheet"] = is_planned_work_key(log["key"])
    for comment in comments:
        comment["on_sheet"] = is_planned_work_key(comment["key"])
    planned_keys = {
        log["key"] for log in worklogs if log["on_sheet"]
    } | {c["key"] for c in comments if c["on_sheet"]} | set(sheet_jira)

    people_on_key: dict[str, set[str]] = defaultdict(set)
    for log in worklogs:
        if log["author"] not in EXCLUDE_PEOPLE and log["author"] != "Unassigned":
            people_on_key[log["key"]].add(log["author"])
    for comment in comments:
        if comment["author"] not in EXCLUDE_PEOPLE and comment["author"] != "Unassigned":
            people_on_key[comment["key"]].add(comment["author"])

    by_ticket_seconds: dict[str, int] = defaultdict(int)
    by_ticket_people: dict[str, set[str]] = defaultdict(set)
    rolled_seconds: dict[str, int] = defaultdict(int)
    rolled_people: dict[str, set[str]] = defaultdict(set)
    for log in worklogs:
        by_ticket_seconds[log["key"]] += log["seconds"]
        by_ticket_people[log["key"]].add(log["author"])
        root = nearest_sheet_jira(log["key"])
        if root:
            rolled_seconds[root] += log["seconds"]
            rolled_people[root].add(log["author"])

    sheet_by_jira = {r["jira"]: r for r in planned_rows if r.get("jira")}

    ticket_rows = []
    for row in planned_rows:
        key = row.get("jira") or ""
        est = parse_effort(row.get("effort"))
        actual_s = rolled_seconds.get(key, 0) if key else 0
        actual_d = days(actual_s)
        ratio = accuracy(actual_d, est)
        if canon_name(row.get("assignee")) in EXCLUDE_PEOPLE:
            continue
        assignee = canon_name(row.get("assignee"))
        ticket_rows.append(
            {
                **row,
                "kind": "sheet",
                "estimated_days": est,
                "actual_seconds": actual_s,
                "actual_hours": hours(actual_s),
                "actual_days": actual_d,
                "accuracy": ratio,
                "accuracy_band": pill(ratio),
                "jira_status": issue_status_name(key),
                "logged_by": sorted(rolled_people.get(key, set())),
                "touched_by": [assignee] if assignee not in EXCLUDE_PEOPLE else [],
            }
        )

    extra_keys = sorted(
        (
            {log["key"] for log in worklogs if log["on_sheet"] and log["key"] not in sheet_jira}
            | {c["key"] for c in comments if c["on_sheet"] and c["key"] not in sheet_jira}
        )
    )
    subtask_rows_by_parent: dict[str, list[dict]] = defaultdict(list)
    for key in extra_keys:
        parent_jira = nearest_sheet_jira(key)
        ctx = sheet_by_jira.get(parent_jira)
        if not ctx:
            for anc in ancestor_keys(key):
                matches = [r for r in planned_rows if r.get("parent") == anc]
                if matches:
                    ctx = matches[0]
                    parent_jira = ctx.get("jira") or anc
                    break
        if not ctx or canon_name(ctx.get("assignee")) in EXCLUDE_PEOPLE:
            continue
        assignee = canon_name(ctx.get("assignee"))
        actual_s = by_ticket_seconds.get(key, 0)
        summary = issue_summary(key) or key
        subtask_rows_by_parent[parent_jira].append(
            {
                "group": ctx.get("group") or "",
                "feature": f"Subtask of {parent_jira} · {summary}",
                "team": ctx.get("team") or "",
                "assignee": assignee,
                "owner": ctx.get("owner") or "",
                "parent": parent_jira,
                "effort": "",
                "due": ctx.get("due") or "",
                "jira": key,
                "kind": "subtask",
                "estimated_days": None,
                "actual_seconds": actual_s,
                "actual_hours": hours(actual_s),
                "actual_days": days(actual_s),
                "accuracy": None,
                "accuracy_band": "n/a",
                "jira_status": issue_status_name(key),
                "logged_by": sorted(by_ticket_people.get(key, set())),
                "touched_by": [assignee],
            }
        )

    interleaved = []
    for row in ticket_rows:
        interleaved.append(row)
        interleaved.extend(sorted(subtask_rows_by_parent.get(row["jira"], []), key=lambda r: r["jira"]))
    ticket_rows = interleaved

    # Person-level
    people = sorted(
        name
        for name in (
            {
                canon_name(r["assignee"])
                for r in planned_rows
                if r.get("assignee")
            }
            | {log["author"] for log in worklogs}
            | {c["author"] for c in comments}
        )
        if name not in EXCLUDE_PEOPLE
    )

    keys_with_plan_pd = {
        r["jira"]
        for r in planned_rows
        if r.get("jira") and parse_effort(r.get("effort")) is not None
    }

    person_rows = []
    for person in people:
        planned_days = sum(
            parse_effort(r.get("effort")) or 0
            for r in planned_rows
            if canon_name(r.get("assignee")) == person
        )
        planned_has_estimate = any(
            parse_effort(r.get("effort")) is not None
            for r in planned_rows
            if canon_name(r.get("assignee")) == person
        )
        all_s = sum(l["seconds"] for l in worklogs if l["author"] == person)
        planned_s = sum(
            l["seconds"]
            for l in worklogs
            if l["author"] == person and l["on_sheet"]
        )
        estimated_planned_s = sum(
            l["seconds"]
            for l in worklogs
            if l["author"] == person and nearest_sheet_jira(l["key"]) in keys_with_plan_pd
        )
        bug_s = sum(
            l["seconds"]
            for l in worklogs
            if l["author"] == person and l["issuetype"] == "Bug"
        )
        task_s = sum(
            l["seconds"]
            for l in worklogs
            if l["author"] == person
            and l["issuetype"] in ("Task", "Sub-task", "Story", "Epic")
        )
        est = planned_days if planned_has_estimate else None
        off_s = all_s - planned_s
        expected_d = expected_days_for(person, leave_map)
        leave_d = leave_days_for(person, leave_map)
        expected_s = int(round(expected_d * SEC_PER_DAY))
        util = round(days(all_s) / expected_d, 2) if expected_d else None
        person_rows.append(
            {
                "person": person,
                "planned_days": round(planned_days, 1) if planned_has_estimate else None,
                "leave_days": leave_d,
                "expected_days": expected_d,
                "expected_seconds": expected_s,
                "utilization": util,
                "actual_all_seconds": all_s,
                "actual_planned_seconds": planned_s,
                "actual_estimated_planned_seconds": estimated_planned_s,
                "actual_offsheet_seconds": off_s,
                "bug_fix_seconds": bug_s,
                "task_seconds": task_s,
                "accuracy_all": accuracy(days(all_s), est),
                "accuracy_planned_tickets": accuracy(days(estimated_planned_s), est),
                "comment_count": sum(1 for c in comments if c["author"] == person),
                "worklog_count": sum(1 for l in worklogs if l["author"] == person),
                "offsheet_worklog_count": sum(
                    1 for l in worklogs if l["author"] == person and not l["on_sheet"]
                ),
                "offsheet_comment_count": sum(
                    1 for c in comments if c["author"] == person and not c["on_sheet"]
                ),
            }
        )
    person_rows.sort(key=lambda r: r["actual_all_seconds"], reverse=True)

    def key_issuetype(key: str) -> str:
        fields = (all_issues.get(key) or {}).get("fields") or {}
        named = ((fields.get("issuetype") or {}).get("name")) or ""
        if named:
            return named
        return next((l["issuetype"] for l in worklogs if l["key"] == key), "") or next(
            (c.get("issuetype") or "" for c in comments if c["key"] == key), ""
        )

    bug_hours_by_key: dict[str, int] = defaultdict(int)
    bug_workers: dict[str, set[str]] = defaultdict(set)
    for log in worklogs:
        if log["issuetype"] != "Bug":
            continue
        bug_hours_by_key[log["key"]] += log["seconds"]
        if log["author"] not in EXCLUDE_PEOPLE and log["author"] != "Unassigned":
            bug_workers[log["key"]].add(log["author"])
    for comment in comments:
        if (comment.get("issuetype") or key_issuetype(comment["key"])) != "Bug":
            continue
        if comment["author"] not in EXCLUDE_PEOPLE and comment["author"] != "Unassigned":
            bug_workers[comment["key"]].add(comment["author"])

    worked_bug_keys = sorted(
        {log["key"] for log in worklogs if log["issuetype"] == "Bug"}
        | {
            c["key"]
            for c in comments
            if (c.get("issuetype") or key_issuetype(c["key"])) == "Bug"
        }
    )

    bugs = []
    bugs_by_person: dict[str, int] = defaultdict(int)
    bugs_resolved = 0
    bugs_open = 0
    bugs_under_7334 = 0
    for key in worked_bug_keys:
        issue = all_issues.get(key) or {}
        fields = issue.get("fields") or {}
        status = ((fields.get("status") or {}).get("name")) or ""
        parent = (fields.get("parent") or {}).get("key") or ""
        workers = sorted(bug_workers.get(key, set()))
        if status in BUG_RESOLVED_STATUSES:
            bugs_resolved += 1
        else:
            bugs_open += 1
        if parent == "HIEV-7334":
            bugs_under_7334 += 1
        bugs.append(
            {
                "key": key,
                "summary": fields.get("summary")
                or next((l["summary"] for l in worklogs if l["key"] == key), "")
                or next((c["summary"] for c in comments if c["key"] == key), ""),
                "status": status,
                "parent": parent,
                "worked_by": workers,
                "august_seconds": bug_hours_by_key.get(key, 0),
            }
        )
        for person in workers:
            bugs_by_person[person] += 1
    bugs.sort(key=lambda b: (-b["august_seconds"], b["key"]))
    for row in person_rows:
        row["bugs_worked"] = bugs_by_person.get(row["person"], 0)

    comments_by_key: dict[str, int] = defaultdict(int)
    for comment in comments:
        comments_by_key[comment["key"]] += 1

    offsheet_tickets = []
    offsheet_keys = sorted(
        {log["key"] for log in worklogs if not log["on_sheet"]}
        | {c["key"] for c in comments if not c["on_sheet"]}
    )
    type_counts: dict[str, int] = defaultdict(int)
    for key in offsheet_keys:
        issue = all_issues.get(key) or {}
        fields = issue.get("fields") or {}
        itype = ((fields.get("issuetype") or {}).get("name")) or (
            next((l["issuetype"] for l in worklogs if l["key"] == key), "")
        )
        summary = fields.get("summary") or next(
            (l["summary"] for l in worklogs if l["key"] == key), ""
        )
        status = ((fields.get("status") or {}).get("name")) or ""
        assignee = canon_name((fields.get("assignee") or {}).get("displayName"))
        type_counts[itype or "Unknown"] += 1
        offsheet_tickets.append(
            {
                "key": key,
                "summary": summary,
                "issuetype": itype or "Unknown",
                "jira_status": status,
                "assignee": assignee,
                "actual_seconds": by_ticket_seconds.get(key, 0),
                "comment_count": comments_by_key.get(key, 0),
                "logged_by": sorted(by_ticket_people.get(key, [])),
                "touched_by": sorted(people_on_key.get(key, set())),
            }
        )
    offsheet_tickets.sort(key=lambda t: t["actual_seconds"], reverse=True)

    bug_hours_s = sum(l["seconds"] for l in worklogs if l["issuetype"] == "Bug")
    task_hours_s = sum(
        l["seconds"]
        for l in worklogs
        if l["issuetype"] in ("Task", "Sub-task", "Story", "Epic")
    )
    other_hours_s = sum(
        l["seconds"]
        for l in worklogs
        if l["issuetype"] not in ("Bug", "Task", "Sub-task", "Story", "Epic")
    )

    # Daily matrix
    dates = []
    d = PERIOD_START
    while d <= PERIOD_END:
        dates.append(d.isoformat())
        d = date.fromordinal(d.toordinal() + 1)

    daily = defaultdict(lambda: {"seconds": 0, "worklogs": [], "comments": []})
    for log in worklogs:
        cell = daily[(log["author"], log["date"])]
        cell["seconds"] += log["seconds"]
        cell["worklogs"].append(log)
    for comment in comments:
        daily[(comment["author"], comment["date"])]["comments"].append(comment)

    daily_people = sorted(
        p
        for p in ({p for p, _ in daily} | {r["person"] for r in person_rows})
        if p not in EXCLUDE_PEOPLE
    )
    scrum = build_scrum(daily_people, leave_map)
    scrum_by_person = {r["person"]: r for r in scrum["people"]}
    for row in person_rows:
        rec = scrum_by_person.get(row["person"]) or {}
        row["scrum_expected"] = rec.get("expected") or 0
        row["scrum_attended"] = rec.get("attended") or 0
        row["scrum_missed"] = rec.get("missed") or 0
        row["scrum_rate"] = rec.get("rate")
        row["scrum_avg_duration"] = rec.get("avg_duration") or "—"
        row["scrum_attended_on_leave"] = rec.get("attended_on_leave") or 0

    extracted = {
        "period": {"start": PERIOD_START.isoformat(), "end": PERIOD_END.isoformat()},
        "hours_per_day": HOURS_PER_DAY,
        "notes": [
            "Actuals are Jira worklogs started 1–31 Aug 2026 (8h = 1d).",
            "Estimation accuracy uses only matching scope: ticket = August days on that Jira ticket and its subtasks ÷ sprint-plan PD; person = August days on that person's sprint-planned Jira tickets that have a numeric PD (including subtasks of those tickets) ÷ their sprint-plan PD. Jira tickets on the plan with NA/open estimates (e.g. HIEV-6941) count as sprint-planned time, not as an estimate miss or over-run. Person view of sprint-planned tickets is the August 26 sheet assignee, plus Jira subtasks of those tickets — not everyone who commented.",
            "August hours use worklog `started` when Jira returned the log. For the 9 tickets with more than 20 worklogs, missing logs are filled from issue changelog timespent deltas (date = when the log was submitted). Those fills were checked against issue timespent (HIEV-6785 changelog page misses 0.7h of pre-May history, not August).",
            "Bugs worked = distinct HIEV issuetype Bug Jira tickets with at least one August worklog or August comment. A person is credited for a unique bug Jira ticket if they logged time or commented on it in August — not the ticket assignee at create time.",
            "Fix hours = August worklogs on Bug tickets vs Task/Sub-task tickets (sprint planned and mid-sprint).",
            "Mid-sprint work = HIEV Jira tickets with August worklogs or comments that were not part of sprint planning and were added during the sprint.",
            "Expected hours = weekdays in August minus Fri 28 public holiday minus that person's planned/sick leave (8h = 1d; Deepak 12 Aug is 0.5d first-half leave).",
            "Scrum attendance = Teams call Participants sheet. Expected calls = weekdays with a recorded ~09:30 IST scrum minus PH 28 minus leave that covers the call (full-day, or Deepak 12 Aug first-half). Rate = attended expected ÷ expected. Joining on leave is recorded but not a miss.",
        ],
        "leave": [
            {
                "person": person,
                "date": iso,
                "fraction": cell["fraction"],
                "note": cell.get("note") or "",
            }
            for (person, iso), cell in sorted(leave_map.items())
        ],
        "truncated_worklogs": truncated,
        "worklog_audit": {
            "duplicate_ids_dropped": worklog_audit["duplicate_ids_dropped"],
            "payload_entries": worklog_audit["payload_entries"],
            "changelog_fill_entries": worklog_audit["changelog_fill_entries"],
            "august_seconds": worklog_audit["august_seconds"],
            "august_unique_worklogs": worklog_audit["august_unique_worklogs"],
        },
        "tickets": ticket_rows,
        "offsheet_tickets": offsheet_tickets,
        "offsheet_type_counts": dict(type_counts),
        "people": person_rows,
        "bugs": bugs,
        "bugs_by_person": dict(bugs_by_person),
        "bugs_meta": {
            "worked": len(bugs),
            "resolved": bugs_resolved,
            "open": bugs_open,
            "under_hiev_7334": bugs_under_7334,
        },
        "fix_hours": {
            "bug_seconds": bug_hours_s,
            "task_seconds": task_hours_s,
            "other_seconds": other_hours_s,
        },
        "worklogs": worklogs,
        "comments": comments,
        "scrum": {
            "call_dates": scrum["call_dates"],
            "meetings": scrum["meetings"],
            "people": scrum["people"],
            "unmatched": scrum["unmatched"],
            "team": scrum["team"],
            "rules": scrum["rules"],
            "calls_are_morning_ist": scrum["calls_are_morning_ist"],
        },
    }
    (ROOT / "data" / "extracted.json").write_text(json.dumps(extracted, indent=2))
    (ROOT / "data" / "worklog-audit.json").write_text(json.dumps(worklog_audit, indent=2))

    write_markdown(extracted, daily, daily_people, dates)
    write_html(extracted, daily, daily_people, dates)
    print(f"Wrote {ROOT / 'report' / 'index.html'}")
    print(
        f"Sprint planned: {len(ticket_rows)}  Mid-sprint: {len(offsheet_tickets)}  "
        f"People: {len(person_rows)}  Worklogs: {len(worklogs)}  Comments: {len(comments)}  "
        f"Bugs worked: {len(bugs)}  resolved/open: {bugs_resolved}/{bugs_open}  "
        f"Scrum {scrum['team']['attended']}/{scrum['team']['expected']} "
        f"({(scrum['team']['rate'] or 0) * 100:.1f}%)"
    )
    h6941 = sum(w["seconds"] for w in worklogs if w["key"] == "HIEV-6941")
    sahil = next((p for p in person_rows if p["person"] == "Sahil Siddiqui"), None)
    print(
        f"AUDIT HIEV-6941 August: {h6941/3600:.2f}h  "
        f"Sahil Siddiqui all Aug: {(sahil['actual_all_seconds'] if sahil else 0)/3600:.2f}h  "
        f"changelog fills: {worklog_audit['changelog_fill_entries']}  "
        f"dupes dropped: {worklog_audit['duplicate_ids_dropped']}"
    )
    for row in truncated:
        print(
            f"  truncated {row['key']}: payload {row['have']}/{row['total']}  "
            f"timespent {row['timespent_h']}h reconstructed {row['reconstructed_h']}h match={row['timespent_match']}"
        )


def load_person_notes() -> dict:
    if not NOTES_PATH.exists():
        return {"sprint": "August 2026", "updated": "", "people": {}}
    data = json.loads(NOTES_PATH.read_text())
    if not isinstance(data.get("people"), dict):
        data["people"] = {}
    return data


def publish_notes_files(notes: dict) -> str:
    payload = json.dumps(notes, indent=2) + "\n"
    NOTES_PATH.write_text(payload)
    for dest in (ROOT / "report" / "person-notes.json", ROOT / "docs" / "person-notes.json"):
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(payload)
    return json.dumps(notes, ensure_ascii=True).replace("<", "\\u003c")


def write_markdown(data: dict, daily, people, dates) -> None:
    lines = []
    a = lines.append
    expected_by = {p["person"]: p.get("expected_seconds") or 0 for p in data["people"]}
    a("# August 2026 sprint retrospective")
    a("")
    a("Source: `Sprint wise employe task list.xlsx` sheet **August 26** + Jira HIEV worklogs/comments/bugs for 1–31 Aug 2026.")
    a("")
    a("Assumptions: **8h = 1 person-day**. Actuals = worklogs with `started` in August (not lifetime `timespent`).")
    a("")
    a("## Formulas")
    a("")
    a("- **Hours / days:** `hours = seconds ÷ 3600`; `days = seconds ÷ 28800`.")
    a("- **Available days:** for each Mon–Fri except Fri 28 PH, add `1 − leave_fraction`. `available_hours = available_days × 8`. `leave_days = Σ leave_fraction`.")
    a("- **Logged of available:** `logged_days of available_days` (hours on the second line). Not a percentage.")
    a("- **Util:** `logged_days ÷ available_days`. Team util = `Σ logged_days ÷ Σ available_days`. Green ≥ 0.90, amber ≥ 0.75, else red.")
    a("- **Mix %:** `planned% = 100 × sprint_planned_seconds ÷ (planned + mid-sprint)`; `mid% = 100 × mid_sprint_seconds ÷ (planned + mid-sprint)`.")
    a("- **Ticket accuracy:** `August_days_on_that_jira_ticket ÷ sprint_plan_PD` (skipped if PD is NA). **Person accuracy:** `August_days_on_jira_tickets_with_numeric_PD ÷ sprint_plan_PD`. Hours on sprint-planned Jira tickets with no PD stay in sprint-planned mix, not in accuracy. Mean KPI averages ticket accuracy only where plan exists and logged > 0. 1.00 = exact. Green ≤ 1.10, amber ≤ 1.50, else red.")
    a("- **Logged bar fill:** `min(100, 100 × logged_seconds ÷ available_seconds)`.")
    a("- **Bug bar fill:** `100 × person_bug_tickets ÷ max(person_bug_tickets)`.")
    a("- **Scrum attendance %:** `100 × attended_expected ÷ expected`. Expected = recorded ~09:30 weekday calls minus PH minus leave covering the call. Missed = `expected − attended`. Avg duration = mean join time on calls joined.")
    a("- **Heatmap bands (hours that day):** (0, 2), [2, 4), [4, 6), [6, 8), ≥ 8.")
    a("")
    for note in data["notes"]:
        a(f"- {note}")
    a("")
    a("## 1. Planned vs actual days")
    a("")
    a("| Person | Planned (PD) | Leave (d) | Logged of available | Util | Sprint planned of avail | Mid-sprint of avail | Est. accuracy |")
    a("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for p in data["people"]:
        plan = "—" if p["planned_days"] is None else f"{p['planned_days']:.1f}"
        acc = "—" if p["accuracy_planned_tickets"] is None else f"{p['accuracy_planned_tickets']:.2f}"
        util = "—" if p.get("utilization") is None else f"{p['utilization']:.2f}"
        a(
            f"| {p['person']} | {plan} | {p.get('leave_days', 0):.1f} | {fmt_vs(p['actual_all_seconds'], p.get('expected_seconds') or 0)} | {util} | {fmt_vs(p['actual_planned_seconds'], p.get('expected_seconds') or 0)} | {fmt_vs(p.get('actual_offsheet_seconds') or 0, p.get('expected_seconds') or 0)} | {acc} |"
        )
    a("")
    a("### Ticket-level")
    a("")
    a("| Jira | Feature | Assignee | Plan (PD) | Logged of assignee available | Accuracy | Status |")
    a("|---|---|---|---:|---:|---:|---|")
    for t in data["tickets"]:
        if not t.get("jira"):
            continue
        plan = "—" if t["estimated_days"] is None else f"{t['estimated_days']:.0f}"
        acc = "—" if t["accuracy"] is None else f"{t['accuracy']:.2f}"
        feat = t["feature"].replace("|", "/")
        avail = expected_by.get(t["assignee"], 0)
        actual = fmt_vs(t["actual_seconds"], avail) if avail else fmt_hd(t["actual_seconds"])
        a(
            f"| [{t['jira']}](https://elocity.atlassian.net/browse/{t['jira']}) | {feat} | {t['assignee']} | {plan} | {actual} | {acc} | {t['jira_status']} |"
        )
    a("")
    off = data.get("offsheet_tickets") or []
    a("### Tasks and bugs added mid-sprint")
    a("")
    a(f"{len(off)} HIEV Jira tickets with August worklogs or comments that were not part of sprint planning (added mid-sprint). Time and comments here are included in person totals, daily hours, and the journal.")
    a("")
    a("| Jira | Type | Summary | Logged by | Logged of available | Comments | Status |")
    a("|---|---|---|---|---:|---:|---|")
    for t in off:
        who = ", ".join(t.get("logged_by") or []) or t.get("assignee") or "—"
        summ = (t.get("summary") or "").replace("|", "/")
        avail = expected_by.get(t.get("assignee") or "", 0)
        if not avail and t.get("logged_by"):
            avail = expected_by.get(t["logged_by"][0], 0)
        actual = fmt_vs(t["actual_seconds"], avail) if avail else fmt_hd(t["actual_seconds"])
        a(
            f"| [{t['key']}](https://elocity.atlassian.net/browse/{t['key']}) | {t['issuetype']} | {summ} | {who} | {actual} | {t['comment_count']} | {t['jira_status']} |"
        )
    a("")
    a("## 2. Estimation accuracy")
    a("")
    a("Same-scope only: **ticket** = August days on that Jira ticket ÷ sprint-plan PD. **Person** = August days on *sprint-planned Jira tickets that have a numeric PD* ÷ their sprint-plan PD. Time on plan Jira tickets with NA/open estimates, and mid-sprint time, is not estimation error. Values above 1.0 mean over estimate. NA / missing estimates are excluded.")
    a("")
    a("| Person | Plan (PD) | Actual on planned Jira tickets | Logged of available | Accuracy |")
    a("|---|---:|---:|---:|---:|")
    for p in data["people"]:
        if p["planned_days"] is None:
            continue
        acc = "—" if p["accuracy_planned_tickets"] is None else f"{p['accuracy_planned_tickets']:.2f}"
        a(
            f"| {p['person']} | {p['planned_days']:.1f} | {fmt_hd(p.get('actual_estimated_planned_seconds') or 0)} | {fmt_vs(p['actual_all_seconds'], p.get('expected_seconds') or 0)} | {acc} |"
        )
    a("")
    a("## 3. Bugs worked in August")
    a("")
    meta = data.get("bugs_meta") or {}
    a(
        f"Total: **{len(data['bugs'])}** distinct HIEV bugs with August worklogs or comments "
        f"({meta.get('resolved', 0)} Done/Ready for Testing, {meta.get('open', 0)} still open). "
        f"{meta.get('under_hiev_7334', 0)} of these sit under HIEV-7334. "
        "Counts are unique Jira tickets per person who logged time or commented — not assignee at create time."
    )
    a("")
    a("| Person | Unique bugs worked |")
    a("|---|---:|")
    for person, count in sorted(data["bugs_by_person"].items(), key=lambda x: -x[1]):
        a(f"| {person} | {count} |")
    a("")
    a("| Jira | Summary | Status | Worked by | August hours |")
    a("|---|---|---|---|---:|")
    for b in data["bugs"]:
        who = ", ".join(b.get("worked_by") or []) or "—"
        summ = (b.get("summary") or "").replace("|", "/")
        a(
            f"| [{b['key']}](https://elocity.atlassian.net/browse/{b['key']}) | {summ} | {b['status']} | {who} | {fmt_hd(b.get('august_seconds') or 0)} |"
        )
    a("")
    a("## 4. Fix hours invested (August worklogs)")
    a("")
    fh = data["fix_hours"]
    a(f"- Bug tickets: **{fmt_hd(fh['bug_seconds'])}**")
    a(f"- Task / Sub-task tickets: **{fmt_hd(fh['task_seconds'])}**")
    a(f"- Other types: **{fmt_hd(fh['other_seconds'])}**")
    a("")
    a("| Person | Bug time of available | Task time of available |")
    a("|---|---:|---:|")
    for p in data["people"]:
        avail = p.get("expected_seconds") or 0
        a(
            f"| {p['person']} | {fmt_vs(p['bug_fix_seconds'], avail)} | {fmt_vs(p['task_seconds'], avail)} |"
        )
    a("")
    leave_lookup = {(e["person"], e["date"]): e for e in (data.get("leave") or [])}
    a("## 5. Daily logged time")
    a("")
    header = "| Person | " + " | ".join(d[8:] for d in dates) + " | Logged of available |"
    a(header)
    a("|" + "---|" * (len(dates) + 2))
    for person in people:
        cells = []
        total = 0
        for day in dates:
            sec = daily[(person, day)]["seconds"]
            total += sec
            leave = leave_lookup.get((person, day))
            if sec:
                cells.append(f"{hours(sec):.1f}")
            elif leave:
                cells.append("½L" if leave["fraction"] < 1 else "L")
            else:
                cells.append("")
        a(f"| {person} | " + " | ".join(cells) + f" | {fmt_vs(total, expected_by.get(person, 0))} |")
    a("")
    scrum = data.get("scrum") or {}
    team_scrum = scrum.get("team") or {}
    a("## 6. Scrum call attendance")
    a("")
    rate_pct = f"{(team_scrum.get('rate') or 0) * 100:.1f}%" if team_scrum.get("rate") is not None else "—"
    a(
        f"Team rate **{team_scrum.get('attended', 0)}/{team_scrum.get('expected', 0)}** expected calls "
        f"({rate_pct}). {team_scrum.get('calls', 0)} recorded Teams scrums, all ~09:30 IST. "
        "Leave-adjusted: full-day leave is not a miss; Deepak 12 Aug first-half leave covers the morning call."
    )
    a("")
    for rule in scrum.get("rules") or []:
        a(f"- {rule}")
    a("")
    unmatched = scrum.get("unmatched") or []
    if unmatched:
        bits = [
            f"{u['name']} ({u['calls']} call{'s' if u['calls'] != 1 else ''})"
            for u in unmatched
        ]
        a("Unmatched attendees (not on the retro roster): " + "; ".join(bits) + ".")
        a("")
    a("| Person | Expected | Attended | Missed | On leave joined | Attendance | Avg duration |")
    a("|---|---:|---:|---:|---:|---:|---|")
    for row in sorted(scrum.get("people") or [], key=lambda r: (r.get("rate") is None, r.get("rate") or 0, r["person"])):
        pct = "—" if row.get("rate") is None else f"{row['rate'] * 100:.0f}%"
        a(
            f"| {row['person']} | {row['expected']} | {row['attended']} | {row['missed']} | "
            f"{row.get('attended_on_leave') or 0} | {pct} | {row.get('avg_duration') or '—'} |"
        )
    a("")
    call_dates = scrum.get("call_dates") or []
    a("Daily ticks (P = present, M = missed, L = leave, A = attended on leave):")
    a("")
    a("| Person | " + " | ".join(d[8:] for d in call_dates) + " |")
    a("|" + "---|" * (len(call_dates) + 1))
    mark = {"present": "P", "missed": "M", "leave": "L", "leave-attended": "A", "skip": ""}
    for row in scrum.get("people") or []:
        by_day = {c["date"]: c["status"] for c in row.get("days") or []}
        cells = [mark.get(by_day.get(d, "skip"), "") for d in call_dates]
        a(f"| {row['person']} | " + " | ".join(cells) + " |")
    a("")
    a("## Daily worklogs and comments")
    a("")
    for person in people:
        entries = []
        for day in dates:
            cell = daily[(person, day)]
            if cell["seconds"] or cell["comments"]:
                entries.append((day, cell))
        if not entries:
            continue
        a(f"### {person} — {fmt_vs(sum(daily[(person, d)]['seconds'] for d in dates), expected_by.get(person, 0))}")
        a("")
        for day, cell in entries:
            avail_day = day_available_seconds(person, day, leave_lookup)
            a(
                f"**{day}** — logged {fmt_hd(cell['seconds'])} of {fmt_hd(avail_day)} available, {len(cell['comments'])} comments"
            )
            a("")
            for log in cell["worklogs"]:
                note = f" — {log['comment']}" if log["comment"] else ""
                where = "planned" if log.get("on_sheet") else "mid-sprint"
                a(f"- Worklog {log['time_spent']} on [{log['key']}](https://elocity.atlassian.net/browse/{log['key']}) ({log['issuetype']}, {where}){note}")
            for c in cell["comments"]:
                a(f"- Comment on [{c['key']}](https://elocity.atlassian.net/browse/{c['key']}): {c['body']}")
            a("")
    (ROOT / "report" / "retrospective.md").write_text("\n".join(lines))


def write_html(data: dict, daily, people, dates) -> None:
    def h(text) -> str:
        return html.escape("" if text is None else str(text))

    def people_attr(*parts) -> str:
        seen: list[str] = []
        for part in parts:
            values = part if isinstance(part, (list, tuple, set)) else [part]
            for name in values:
                if name and name not in seen:
                    seen.append(str(name))
        return h("|".join(seen))

    leave_lookup = {
        (e["person"], e["date"]): e for e in (data.get("leave") or [])
    }
    expected_by = {p["person"]: p.get("expected_seconds") or 0 for p in data["people"]}
    total_expected = sum(expected_by.values())

    fh = data["fix_hours"]
    total_plan = sum(p["planned_days"] or 0 for p in data["people"])
    total_actual = sum(p["actual_all_seconds"] for p in data["people"])
    estimated_tickets = [t for t in data["tickets"] if t["accuracy"] is not None]
    worked_tickets = [t for t in estimated_tickets if t["actual_seconds"] > 0]
    avg_acc = (
        round(sum(t["accuracy"] for t in worked_tickets) / len(worked_tickets), 2)
        if worked_tickets
        else None
    )
    person_acc_rows = [p for p in data["people"] if p["accuracy_planned_tickets"] is not None]
    person_acc_trs = []
    for p in person_acc_rows:
        ratio = p["accuracy_planned_tickets"]
        band = pill(ratio)
        on_s = p["actual_planned_seconds"]
        off_s = p.get("actual_offsheet_seconds") or 0
        on_w, off_w = mix_widths(on_s, off_s)
        person_acc_trs.append(
            "<tr "
            f"data-people='{people_attr(p['person'])}'>"
            f"<td><button type='button' class='name-link' data-open-person='{h(p['person'])}'>{h(p['person'])}</button></td>"
            f"<td class='num'>{p['planned_days']:.1f}</td>"
            f"<td class='num'>{html.escape(fmt_hd(p.get('actual_estimated_planned_seconds') or 0))}</td>"
            f"<td class='num'>{html_vs(p['actual_all_seconds'], p.get('expected_seconds') or 0)}</td>"
            f"<td><div class='mix' title='Sprint planned {on_w}% · Mid-sprint {off_w}%'><span class='on' style='width:{on_w}%'></span><span class='off' style='width:{off_w}%'></span></div></td>"
            f"<td class='num'><span class='pill {html.escape(band)}'>{ratio:.2f}</span></td>"
            "</tr>"
        )

    person_opts = "".join(f'<option value="{h(p)}">{h(p)}</option>' for p in people)

    ticket_trs = []
    for t in data["tickets"]:
        if not t.get("jira"):
            continue
        plan = "—" if t["estimated_days"] is None else f"{t['estimated_days']:.0f}"
        acc = "—" if t["accuracy"] is None else f"{t['accuracy']:.2f}"
        band = t["accuracy_band"]
        avail = expected_by.get(t["assignee"], 0)
        actual_cell = html_vs(t["actual_seconds"], avail) if avail else h(fmt_hd(t["actual_seconds"]))
        names = people_attr(t["assignee"])
        jira_cell = (
            f"<a href='https://elocity.atlassian.net/browse/{h(t['jira'])}'>{h(t['jira'])}</a>"
        )
        if t.get("kind") == "subtask":
            jira_cell += " <span class='pill status'>subtask</span>"
        ticket_trs.append(
            "<tr "
            f"data-people='{names}'>"
            f"<td>{jira_cell}</td>"
            f"<td>{h(t['group'])}</td>"
            f"<td>{h(t['feature'])}</td>"
            f"<td>{h(t['assignee'])}</td>"
            f"<td class='num'>{plan}</td>"
            f"<td class='num'>{actual_cell}</td>"
            f"<td class='num'><span class='pill {h(band)}'>{acc}</span></td>"
            f"<td><span class='pill status'>{h(t['jira_status']) or '—'}</span></td>"
            "</tr>"
        )

    offsheet = data.get("offsheet_tickets") or []
    off_types = data.get("offsheet_type_counts") or {}
    off_seconds = sum(t["actual_seconds"] for t in offsheet)
    offsheet_trs = []
    for t in offsheet:
        who = ", ".join(t.get("logged_by") or []) or t.get("assignee") or "—"
        avail = expected_by.get(t.get("assignee") or "", 0)
        if not avail and t.get("logged_by"):
            avail = expected_by.get(t["logged_by"][0], 0)
        time_cell = html_vs(t["actual_seconds"], avail) if avail else h(fmt_hd(t["actual_seconds"]))
        names = people_attr(t.get("assignee"), t.get("logged_by") or [], t.get("touched_by") or [])
        offsheet_trs.append(
            "<tr "
            f"data-type='{h(t['issuetype'])}' data-people='{names}'>"
            f"<td><a href='https://elocity.atlassian.net/browse/{h(t['key'])}'>{h(t['key'])}</a></td>"
            f"<td><span class='pill type-{h(t['issuetype'])}'>{h(t['issuetype'])}</span></td>"
            f"<td>{h(t['summary'])}</td>"
            f"<td>{h(who)}</td>"
            f"<td class='num'>{time_cell}</td>"
            f"<td class='num'>{t['comment_count']}</td>"
            f"<td>{h(t['jira_status'])}</td>"
            "</tr>"
        )
    type_opts = "".join(
        f'<option value="{h(name)}">{h(name)} ({count})</option>'
        for name, count in sorted(off_types.items(), key=lambda x: -x[1])
    )

    people_trs = []
    people_mix = []
    for p in data["people"]:
        plan = "—" if p["planned_days"] is None else f"{p['planned_days']:.1f}"
        acc = p["accuracy_planned_tickets"]
        acc_label = "—" if acc is None else f"{acc:.2f}"
        acc_band = pill(acc) if acc is not None else "na"
        util = p.get("utilization")
        util_label = "—" if util is None else f"{util:.2f}"
        util_band = util_pill(util)
        on_s = p["actual_planned_seconds"]
        off_s = p.get("actual_offsheet_seconds") or 0
        on_w, off_w = mix_widths(on_s, off_s)
        leave_d = p.get("leave_days") or 0
        expected_s = p.get("expected_seconds") or 0
        people_trs.append(
            "<tr "
            f"data-people='{people_attr(p['person'])}'>"
            f"<td><button type='button' class='name-link' data-open-person='{h(p['person'])}'><strong>{h(p['person'])}</strong></button></td>"
            f"<td class='num'>{plan}</td>"
            f"<td class='num'>{leave_d:.1f}d</td>"
            f"<td class='num'>{html_vs(p['actual_all_seconds'], expected_s)}</td>"
            f"<td class='num'><span class='pill {util_band}'>{util_label}</span></td>"
            f"<td><div class='mix' title='Sprint planned {on_w}% · Mid-sprint {off_w}%'><span class='on' style='width:{on_w}%'></span><span class='off' style='width:{off_w}%'></span></div></td>"
            f"<td class='num'>{html_vs(on_s, expected_s)}</td>"
            f"<td class='num'>{html_vs(off_s, expected_s)}</td>"
            f"<td class='num'><span class='pill {acc_band}'>{acc_label}</span></td>"
            f"<td class='num'>{p['worklog_count']}</td>"
            f"<td class='num'>{p['comment_count']}</td>"
            "</tr>"
        )
        exp = expected_s or 1
        bar_w = min(100, round(100 * p["actual_all_seconds"] / exp, 1))
        people_mix.append(
            f"<div class='row' data-people='{people_attr(p['person'])}'>"
            f"<div><button type='button' class='name-link' data-open-person='{h(p['person'])}'>{h(p['person'])}</button></div>"
            f"<div class='track'><i style='width:{bar_w}%'></i></div>"
            f"<div class='n'>{html_vs(p['actual_all_seconds'], expected_s)}</div></div>"
        )

    bug_trs = []
    max_bugs = max(data["bugs_by_person"].values(), default=1) or 1
    bug_bars = []
    for person, count in sorted(data["bugs_by_person"].items(), key=lambda x: -x[1]):
        bug_trs.append(f"<tr><td>{h(person)}</td><td class='num'>{count}</td></tr>")
        bug_bars.append(
            f"<div class='row' data-people='{people_attr(person)}'>"
            f"<div><button type='button' class='name-link' data-open-person='{h(person)}'>{h(person)}</button></div>"
            f"<div class='track'><i style='width:{round(100 * count / max_bugs, 1)}%'></i></div>"
            f"<div class='n'>{count}</div></div>"
        )

    bug_detail = []
    for b in data["bugs"]:
        who = ", ".join(b.get("worked_by") or []) or "—"
        bug_detail.append(
            "<tr "
            f"data-people='{people_attr(b.get('worked_by') or [])}'>"
            f"<td><a href='https://elocity.atlassian.net/browse/{h(b['key'])}'>{h(b['key'])}</a></td>"
            f"<td>{h(b['summary'])}</td>"
            f"<td><span class='pill status'>{h(b['status']) or '—'}</span></td>"
            f"<td>{h(who)}</td>"
            f"<td class='num'>{h(fmt_hd(b.get('august_seconds') or 0))}</td>"
            "</tr>"
        )

    fix_trs = []
    for p in data["people"]:
        avail = p.get("expected_seconds") or 0
        fix_trs.append(
            "<tr "
            f"data-people='{people_attr(p['person'])}'>"
            f"<td><button type='button' class='name-link' data-open-person='{h(p['person'])}'>{h(p['person'])}</button></td>"
            f"<td class='num'>{html_vs(p['bug_fix_seconds'], avail)}</td>"
            f"<td class='num'>{html_vs(p['task_seconds'], avail)}</td>"
            "</tr>"
        )

    daily_head_cells = []
    for iso in dates:
        d = date.fromisoformat(iso)
        extra = day_col_class(d)
        title = PUBLIC_HOLIDAYS.get(d, "")
        title_attr = f" title='{h(title)}'" if title else ""
        daily_head_cells.append(
            f"<th class='dayh{extra}'{title_attr}>{d.day}<br /><span>{h(day_col_label(d))}</span></th>"
        )
    daily_head = "".join(daily_head_cells)
    daily_body = []
    for person in people:
        tds = []
        total = 0
        for iso in dates:
            d = date.fromisoformat(iso)
            sec = daily[(person, iso)]["seconds"]
            total += sec
            cls = heat_class(sec)
            extra = day_col_class(d)
            leave = leave_lookup.get((person, iso))
            if leave:
                extra += " leave"
                if leave["fraction"] < 1:
                    extra += " half"
            if sec:
                label = f"{hours(sec):.1f}"
            elif leave:
                label = "½L" if leave["fraction"] < 1 else "L"
            else:
                label = ""
            title = ""
            if leave:
                half = " first half" if leave["fraction"] < 1 else ""
                note = f" ({leave['note']})" if leave.get("note") else ""
                title = f" title='Leave{half}{note}'"
            tds.append(f"<td class='num heat {cls}{extra}'{title}>{label}</td>")
        daily_body.append(
            f"<tr data-people='{people_attr(person)}' data-person='{h(person)}'><th><button type='button' class='name-link' data-open-person='{h(person)}'>{h(person)}</button></th>{''.join(tds)}<td class='num'>{html_vs(total, expected_by.get(person, 0))}</td></tr>"
        )

    journal = []
    for person in people:
        blocks = []
        for day in dates:
            cell = daily[(person, day)]
            if not cell["seconds"] and not cell["comments"]:
                continue
            items = []
            for log in cell["worklogs"]:
                note = f" — {h(log['comment'])}" if log["comment"] else ""
                where = "planned" if log.get("on_sheet") else "mid-sprint"
                items.append(
                    f"<li><span class='meta'>worklog {h(log['time_spent'])}</span> "
                    f"<a href='https://elocity.atlassian.net/browse/{h(log['key'])}'>{h(log['key'])}</a> "
                    f"<span class='type'>{h(log['issuetype'])} · {where}</span>{note}</li>"
                )
            for c in cell["comments"]:
                where = "planned" if c.get("on_sheet") else "mid-sprint"
                items.append(
                    f"<li><span class='meta'>comment · {where}</span> "
                    f"<a href='https://elocity.atlassian.net/browse/{h(c['key'])}'>{h(c['key'])}</a> "
                    f"— {h(c['body'])}</li>"
                )
            avail_day = day_available_seconds(person, day, leave_lookup)
            blocks.append(
                f"<details><summary>{h(day)} · logged {h(fmt_hd(cell['seconds']))} of {h(fmt_hd(avail_day))} available · "
                f"{len(cell['comments'])} comments</summary><ul>{''.join(items)}</ul></details>"
            )
        if blocks:
            month_s = sum(daily[(person, d)]["seconds"] for d in dates)
            journal.append(
                f"<section class='person-day' data-person='{h(person)}' data-people='{people_attr(person)}'>"
                f"<h3>{h(person)} <span class='avail-meta'>{html_vs(month_s, expected_by.get(person, 0))}</span></h3>"
                f"{''.join(blocks)}</section>"
            )

    scrum = data.get("scrum") or {}
    team_scrum = scrum.get("team") or {}
    scrum_rate = team_scrum.get("rate")
    kpi_scrum = (
        f"{team_scrum.get('attended', 0)}/{team_scrum.get('expected', 0)}"
        f" ({scrum_rate * 100:.0f}%)"
        if scrum_rate is not None
        else "n/a"
    )
    unmatched = scrum.get("unmatched") or []
    unmatched_note = ""
    if unmatched:
        bits = [
            f"{u['name']} ({u['calls']} call{'s' if u['calls'] != 1 else ''})"
            for u in unmatched
        ]
        unmatched_note = (
            " Unmatched attendees not on this roster: " + "; ".join(bits) + "."
        )
    scrum_note = (
        f"{team_scrum.get('calls', 0)} recorded Teams scrums (weekdays 3–27 and 31 Aug, none on weekends or Fri 28 PH). "
        "Every call started ~09:30, so morning IST. Expected = those call days minus leave that covers the call "
        "(full-day, or Deepak 12 Aug first-half). Rate = attended expected ÷ expected. "
        "Joining while on leave is marked A and is not a miss."
        + unmatched_note
    )
    scrum_trs = []
    for row in sorted(
        scrum.get("people") or [],
        key=lambda r: (r.get("rate") is None, r.get("rate") if r.get("rate") is not None else 1, r["person"]),
    ):
        ratio = row.get("rate")
        pct = "—" if ratio is None else f"{ratio * 100:.0f}%"
        band = att_pill(ratio)
        scrum_trs.append(
            "<tr "
            f"data-people='{people_attr(row['person'])}'>"
            f"<td><button type='button' class='name-link' data-open-person='{h(row['person'])}'>{h(row['person'])}</button></td>"
            f"<td class='num'>{row['expected']}</td>"
            f"<td class='num'>{row['attended']}</td>"
            f"<td class='num'>{row['missed']}</td>"
            f"<td class='num'>{row.get('attended_on_leave') or 0}</td>"
            f"<td class='num'><span class='pill {band}'>{pct}</span></td>"
            f"<td class='num'>{h(row.get('avg_duration') or '—')}</td>"
            "</tr>"
        )
    call_dates = scrum.get("call_dates") or []
    scrum_tick_head_cells = []
    for iso in call_dates:
        d = date.fromisoformat(iso)
        extra = day_col_class(d)
        title = PUBLIC_HOLIDAYS.get(d, "")
        title_attr = f" title='{h(title)}'" if title else ""
        scrum_tick_head_cells.append(
            f"<th class='dayh{extra}'{title_attr}>{d.day}<br /><span>{h(day_col_label(d))}</span></th>"
        )
    tick_label = {
        "present": ("P", "present", "Present"),
        "missed": ("M", "missed", "Missed"),
        "leave": ("L", "leave", "Leave"),
        "leave-attended": ("A", "leave-attended", "Attended on leave"),
        "skip": ("", "skip", ""),
    }
    scrum_tick_body = []
    people_order = {name: i for i, name in enumerate(people)}
    for row in sorted(scrum.get("people") or [], key=lambda r: people_order.get(r["person"], 999)):
        tds = []
        by_day = {c["date"]: c for c in row.get("days") or []}
        for iso in call_dates:
            cell = by_day.get(iso) or {"status": "skip"}
            mark, cls, title = tick_label.get(cell["status"], ("", "skip", ""))
            dur = cell.get("duration") or ""
            extra_title = title
            if dur:
                extra_title = f"{title} · {dur}" if title else dur
            if cell.get("leave_note"):
                extra_title += f" ({cell['leave_note']})"
            title_attr = f" title='{h(extra_title)}'" if extra_title else ""
            tds.append(f"<td class='num heat scrum-{cls}'{title_attr}>{h(mark)}</td>")
        scrum_tick_body.append(
            f"<tr data-people='{people_attr(row['person'])}'>"
            f"<th><button type='button' class='name-link' data-open-person='{h(row['person'])}'>{h(row['person'])}</button></th>"
            f"{''.join(tds)}</tr>"
        )

    on_total = sum(p["actual_planned_seconds"] for p in data["people"])
    off_total = sum(p.get("actual_offsheet_seconds") or 0 for p in data["people"])
    on_pct, off_pct = mix_widths(on_total, off_total)
    team_util = round(days(total_actual) / days(total_expected), 2) if total_expected else None
    meta = data.get("bugs_meta") or {}
    bug_note = (
        f"{len(data['bugs'])} distinct HIEV bugs with August worklogs or comments "
        f"(unique Jira tickets per person who logged or commented — not assignee at create). "
        f"{meta.get('resolved', 0)} ended August in Done or Ready for Testing; "
        f"{meta.get('open', 0)} still open."
    )
    if meta.get("under_hiev_7334"):
        bug_note += (
            f" {meta['under_hiev_7334']} of {len(data['bugs'])} sit under HIEV-7334."
        )
    person_stats = {}
    for p in data["people"]:
        name = p["person"]
        expected_s = p.get("expected_seconds") or 0
        util = p.get("utilization")
        person_stats[name] = {
            "logged_html": html_vs(p["actual_all_seconds"], expected_s),
            "leave": f"{(p.get('leave_days') or 0):.1f}d",
            "util": "—" if util is None else f"{util:.2f}",
            "on_html": html_vs(p["actual_planned_seconds"], expected_s),
            "off_html": html_vs(p.get("actual_offsheet_seconds") or 0, expected_s),
            "plan": "—" if p["planned_days"] is None else f"{p['planned_days']:.1f} PD",
            "bugs": int(p.get("bugs_worked") or 0),
            "sheet": sum(
                1
                for t in data["tickets"]
                if t.get("jira") and canon_name(t.get("assignee")) == name
            ),
            "offsheet": sum(
                1
                for t in offsheet
                if name in (t.get("touched_by") or [])
            ),
            "bug_hours_html": html_vs(p["bug_fix_seconds"], expected_s),
            "task_hours_html": html_vs(p["task_seconds"], expected_s),
            "scrum_html": (
                f"{p.get('scrum_attended') or 0}/{p.get('scrum_expected') or 0}"
                + (
                    f" ({p['scrum_rate'] * 100:.0f}%)"
                    if p.get("scrum_rate") is not None
                    else ""
                )
            ),
            "scrum_missed": int(p.get("scrum_missed") or 0),
            "scrum_avg": p.get("scrum_avg_duration") or "—",
        }
    page = render_page(
        total_plan=total_plan,
        total_hours=hours(total_actual),
        total_days=days(total_actual),
        kpi_logged=html_vs(total_actual, total_expected),
        team_util=team_util,
        avg_acc=avg_acc,
        off_count=len(offsheet),
        off_hours_label=fmt_vs(off_seconds, total_expected),
        on_pct=on_pct,
        off_pct=off_pct,
        on_hours_label=fmt_vs(on_total, total_expected),
        off_mix_label=fmt_vs(off_total, total_expected),
        people_trs="".join(people_trs),
        people_mix="".join(people_mix),
        ticket_trs="".join(ticket_trs),
        offsheet_trs="".join(offsheet_trs),
        type_opts=type_opts,
        offsheet_count=len(offsheet),
        person_acc_trs="".join(person_acc_trs),
        bug_count=len(data["bugs"]),
        bug_note=bug_note,
        bug_bars="".join(bug_bars),
        bug_detail="".join(bug_detail),
        fh_bug=fmt_vs(fh["bug_seconds"], total_expected),
        fh_task=fmt_vs(fh["task_seconds"], total_expected),
        fh_other=fmt_vs(fh["other_seconds"], total_expected),
        fix_trs="".join(fix_trs),
        daily_head=daily_head,
        daily_body="".join(daily_body),
        kpi_scrum=kpi_scrum,
        scrum_note=scrum_note,
        scrum_trs="".join(scrum_trs),
        scrum_tick_head="".join(scrum_tick_head_cells),
        scrum_tick_body="".join(scrum_tick_body),
        person_opts=person_opts,
        person_stats_json=json.dumps(person_stats),
        person_notes_json=publish_notes_files(load_person_notes()),
        journal="".join(journal),
    )
    (ROOT / "report" / "index.html").write_text(page)
    docs = ROOT / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "report" / "index.html", docs / "index.html")
    shutil.copy(ROOT / "report" / "styles.css", docs / "styles.css")


if __name__ == "__main__":
    build()
