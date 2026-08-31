#!/usr/bin/env python3
"""Build August 2026 sprint retrospective from planned sheet + Jira dumps."""

from __future__ import annotations

import html
import json
import re
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLANNED_PATH = ROOT / "data" / "planned.json"
RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
HOURS_PER_DAY = 8.0
SEC_PER_DAY = int(HOURS_PER_DAY * 3600)
PERIOD_START = date(2026, 8, 1)
PERIOD_END = date(2026, 8, 31)

NAME_MAP = {
    "vinay chowdary chandra": "Vinay",
    "vinay": "Vinay",
    "sahil siddiqui": "Sahil Siddiqui",
    "t n shambulinga": "Shambu",
    "shambu": "Shambu",
    "dhanush k g": "Dhanush",
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
    "marish": "Marish",
    "srikant kumar sutar": "Srikant",
    "srikant": "Srikant",
    "priyanshu rajput": "Priyanshu",
    "priyanshu": "Priyanshu",
    "manjunath gowda r": "Manjunath",
    "manjunath": "Manjunath",
    "deepak bharadwaj": "Deepak",
    "deepak": "Deepak",
    "rushika sriya": "Rushika",
    "rushika": "Rushika",
    "tarun chandra": "Tarun",
    "tarun": "Tarun",
    "sudeep": "Sudeep",
    "nagaraju": "Nagaraju",
    "lavanya": "Lavanya",
}

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
            # Keep the issue with more worklogs / comments.
            def score(item: dict) -> tuple[int, int]:
                fields = item.get("fields") or {}
                wl = (fields.get("worklog") or {}).get("worklogs") or []
                comments = (fields.get("comment") or {}).get("comments") or []
                return (len(wl), len(comments))

            if score(issue) > score(existing):
                by_key[key] = issue
    return by_key


def collect_worklogs(issues: dict[str, dict]) -> list[dict]:
    rows = []
    truncated = []
    for key, issue in issues.items():
        fields = issue.get("fields") or {}
        itype = ((fields.get("issuetype") or {}).get("name")) or ""
        summary = fields.get("summary") or ""
        wl_block = fields.get("worklog") or {}
        logs = wl_block.get("worklogs") or []
        total = wl_block.get("total") or len(logs)
        if total > len(logs):
            truncated.append({"key": key, "have": len(logs), "total": total})
        for log in logs:
            started = parse_dt(log.get("started"))
            if started is None:
                continue
            day = started.date()
            if day < PERIOD_START or day > PERIOD_END:
                continue
            comment = adf_text(log.get("comment"))
            rows.append(
                {
                    "id": log.get("id"),
                    "key": key,
                    "summary": summary,
                    "issuetype": itype,
                    "author": canon_name((log.get("author") or {}).get("displayName")),
                    "raw_author": (log.get("author") or {}).get("displayName"),
                    "date": day.isoformat(),
                    "seconds": int(log.get("timeSpentSeconds") or 0),
                    "time_spent": log.get("timeSpent") or "",
                    "comment": comment,
                }
            )
    return rows, truncated


def collect_comments(issues: dict[str, dict]) -> list[dict]:
    rows = []
    for key, issue in issues.items():
        fields = issue.get("fields") or {}
        summary = fields.get("summary") or ""
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
                    "author": canon_name((comment.get("author") or {}).get("displayName")),
                    "date": day.isoformat(),
                    "body": text[:500],
                }
            )
    return rows


def hours(seconds: int) -> float:
    return round(seconds / 3600.0, 2)


def days(seconds: int) -> float:
    return round(seconds / SEC_PER_DAY, 2)


def accuracy(actual_days: float, planned_days: float | None) -> float | None:
    if planned_days is None or planned_days <= 0:
        return None
    return round(actual_days / planned_days, 2)


def fmt_h(seconds: int) -> str:
    return f"{hours(seconds):.1f}h / {days(seconds):.1f}d"


def pill(ratio: float | None) -> str:
    if ratio is None:
        return "n/a"
    if ratio <= 1.1:
        return "on-plan"
    if ratio <= 1.5:
        return "over"
    return "well-over"


def build():
    planned = load_json(PLANNED_PATH)
    planned_rows = planned["rows"]
    planned_keys = {r["jira"] for r in planned_rows if r.get("jira")}

    planned_issues = merge_issues([RAW_DIR / RAW_FILES["planned_issues"]])
    worklog_issues = merge_issues([RAW_DIR / name for name in RAW_FILES["worklogs"]])
    bug_issues = merge_issues([RAW_DIR / RAW_FILES["bugs_created"]])
    all_issues = {**worklog_issues, **planned_issues}

    worklogs, truncated = collect_worklogs(all_issues)
    comments = collect_comments(all_issues)

    # Ticket-level planned vs actual (August worklogs on that key)
    by_ticket_seconds: dict[str, int] = defaultdict(int)
    by_ticket_people: dict[str, set[str]] = defaultdict(set)
    for log in worklogs:
        by_ticket_seconds[log["key"]] += log["seconds"]
        by_ticket_people[log["key"]].add(log["author"])

    ticket_rows = []
    for row in planned_rows:
        key = row.get("jira") or ""
        est = parse_effort(row.get("effort"))
        actual_s = by_ticket_seconds.get(key, 0) if key else 0
        actual_d = days(actual_s)
        ratio = accuracy(actual_d, est)
        status = ((planned_issues.get(key) or {}).get("fields") or {}).get("status", {})
        ticket_rows.append(
            {
                **row,
                "estimated_days": est,
                "actual_seconds": actual_s,
                "actual_hours": hours(actual_s),
                "actual_days": actual_d,
                "accuracy": ratio,
                "accuracy_band": pill(ratio),
                "jira_status": (status or {}).get("name") or "",
                "logged_by": sorted(by_ticket_people.get(key, [])),
            }
        )

    # Person-level
    people = sorted(
        {
            canon_name(r["assignee"])
            for r in planned_rows
            if r.get("assignee")
        }
        | {log["author"] for log in worklogs}
        | {c["author"] for c in comments}
    )

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
            if l["author"] == person and l["key"] in planned_keys
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
        person_rows.append(
            {
                "person": person,
                "planned_days": round(planned_days, 1) if planned_has_estimate else None,
                "actual_all_seconds": all_s,
                "actual_planned_seconds": planned_s,
                "bug_fix_seconds": bug_s,
                "task_seconds": task_s,
                "accuracy_all": accuracy(days(all_s), est),
                "accuracy_planned_tickets": accuracy(days(planned_s), est),
                "comment_count": sum(1 for c in comments if c["author"] == person),
                "worklog_count": sum(1 for l in worklogs if l["author"] == person),
            }
        )
    person_rows.sort(key=lambda r: r["actual_all_seconds"], reverse=True)

    # Bugs created in August, by assignee (ticket owner of the bug)
    bugs = []
    bugs_by_person: dict[str, int] = defaultdict(int)
    for key, issue in bug_issues.items():
        fields = issue.get("fields") or {}
        assignee = canon_name((fields.get("assignee") or {}).get("displayName"))
        reporter = canon_name((fields.get("reporter") or {}).get("displayName"))
        parent = (fields.get("parent") or {}).get("key") or ""
        bugs.append(
            {
                "key": key,
                "summary": fields.get("summary") or "",
                "status": ((fields.get("status") or {}).get("name")) or "",
                "assignee": assignee,
                "reporter": reporter,
                "parent": parent,
                "created": (fields.get("created") or "")[:10],
                "timespent_seconds": int(fields.get("aggregatetimespent") or fields.get("timespent") or 0),
            }
        )
        bugs_by_person[assignee] += 1
    bugs.sort(key=lambda b: b["key"], reverse=True)

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

    daily_people = sorted({p for p, _ in daily} | {r["person"] for r in person_rows})

    extracted = {
        "period": {"start": PERIOD_START.isoformat(), "end": PERIOD_END.isoformat()},
        "hours_per_day": HOURS_PER_DAY,
        "notes": [
            "Actuals are Jira worklogs started 1–31 Aug 2026 (8h = 1d).",
            "Estimation accuracy = actual person-days ÷ sheet estimate (PD).",
            "HIEV-6941 / HIEV-6940 / HIEV-6938 have truncated worklog lists (Jira caps at 20 per issue payload); ticket totals may undercount daily rows.",
            "Bugs created = HIEV issuetype Bug created in August 2026, attributed to the bug assignee.",
            "Fix hours = August worklogs on Bug tickets vs Task/Sub-task tickets.",
        ],
        "truncated_worklogs": truncated,
        "tickets": ticket_rows,
        "people": person_rows,
        "bugs": bugs,
        "bugs_by_person": dict(bugs_by_person),
        "fix_hours": {
            "bug_seconds": bug_hours_s,
            "task_seconds": task_hours_s,
            "other_seconds": other_hours_s,
        },
        "worklogs": worklogs,
        "comments": comments,
    }
    (ROOT / "data" / "extracted.json").write_text(json.dumps(extracted, indent=2))

    write_markdown(extracted, daily, daily_people, dates)
    write_html(extracted, daily, daily_people, dates)
    print(f"Wrote {ROOT / 'report' / 'index.html'}")
    print(f"Tickets: {len(ticket_rows)}  People: {len(person_rows)}  Worklogs: {len(worklogs)}  Comments: {len(comments)}  Bugs: {len(bugs)}")


def write_markdown(data: dict, daily, people, dates) -> None:
    lines = []
    a = lines.append
    a("# August 2026 sprint retrospective")
    a("")
    a("Source: `Sprint wise employe task list.xlsx` sheet **August 26** + Jira HIEV worklogs/comments/bugs for 1–31 Aug 2026.")
    a("")
    a("Assumptions: 1 person-day = 8 hours. Actuals = worklogs with `started` in August (not lifetime `timespent`). Accuracy = actual days ÷ sheet estimate.")
    a("")
    for note in data["notes"]:
        a(f"- {note}")
    a("")
    a("## 1. Planned vs actual days")
    a("")
    a("| Person | Planned (PD) | Logged (all Aug) | Logged on planned tickets | Accuracy (all ÷ plan) |")
    a("|---|---:|---:|---:|---:|")
    for p in data["people"]:
        plan = "—" if p["planned_days"] is None else f"{p['planned_days']:.1f}"
        acc = "—" if p["accuracy_all"] is None else f"{p['accuracy_all']:.2f}"
        a(
            f"| {p['person']} | {plan} | {fmt_h(p['actual_all_seconds'])} | {fmt_h(p['actual_planned_seconds'])} | {acc} |"
        )
    a("")
    a("### Ticket-level")
    a("")
    a("| Jira | Feature | Assignee | Plan (PD) | Actual (Aug) | Accuracy | Status |")
    a("|---|---|---|---:|---:|---:|---|")
    for t in data["tickets"]:
        if not t.get("jira"):
            continue
        plan = "—" if t["estimated_days"] is None else f"{t['estimated_days']:.0f}"
        acc = "—" if t["accuracy"] is None else f"{t['accuracy']:.2f}"
        feat = t["feature"].replace("|", "/")
        a(
            f"| [{t['jira']}](https://elocity.atlassian.net/browse/{t['jira']}) | {feat} | {t['assignee']} | {plan} | {fmt_h(t['actual_seconds'])} | {acc} | {t['jira_status']} |"
        )
    a("")
    a("## 2. Estimation accuracy")
    a("")
    a("Values above 1.0 mean more time was logged than estimated. NA estimates are excluded.")
    a("")
    a("## 3. Bugs created (August)")
    a("")
    a(f"Total: **{len(data['bugs'])}** HIEV bugs created in August 2026.")
    a("")
    a("| Assignee | Bugs |")
    a("|---|---:|")
    for person, count in sorted(data["bugs_by_person"].items(), key=lambda x: -x[1]):
        a(f"| {person} | {count} |")
    a("")
    a("## 4. Fix hours invested (August worklogs)")
    a("")
    fh = data["fix_hours"]
    a(f"- Bug tickets: **{fmt_h(fh['bug_seconds'])}**")
    a(f"- Task / Sub-task tickets: **{fmt_h(fh['task_seconds'])}**")
    a(f"- Other types: **{fmt_h(fh['other_seconds'])}**")
    a("")
    a("| Person | Bug hours | Task hours |")
    a("|---|---:|---:|")
    for p in data["people"]:
        a(f"| {p['person']} | {fmt_h(p['bug_fix_seconds'])} | {fmt_h(p['task_seconds'])} |")
    a("")
    a("## 5. Daily logged time")
    a("")
    header = "| Person | " + " | ".join(d[8:] for d in dates) + " | Total |"
    a(header)
    a("|" + "---|" * (len(dates) + 2))
    for person in people:
        cells = []
        total = 0
        for day in dates:
            sec = daily[(person, day)]["seconds"]
            total += sec
            cells.append("" if sec == 0 else f"{hours(sec):.1f}")
        a(f"| {person} | " + " | ".join(cells) + f" | {hours(total):.1f}h |")
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
        a(f"### {person}")
        a("")
        for day, cell in entries:
            a(f"**{day}** — {fmt_h(cell['seconds'])} logged, {len(cell['comments'])} comments")
            a("")
            for log in cell["worklogs"]:
                note = f" — {log['comment']}" if log["comment"] else ""
                a(f"- Worklog {log['time_spent']} on [{log['key']}](https://elocity.atlassian.net/browse/{log['key']}) ({log['issuetype']}){note}")
            for c in cell["comments"]:
                a(f"- Comment on [{c['key']}](https://elocity.atlassian.net/browse/{c['key']}): {c['body']}")
            a("")
    (ROOT / "report" / "retrospective.md").write_text("\n".join(lines))


def write_html(data: dict, daily, people, dates) -> None:
    def h(text) -> str:
        return html.escape("" if text is None else str(text))

    fh = data["fix_hours"]
    total_plan = sum(p["planned_days"] or 0 for p in data["people"])
    total_actual = sum(p["actual_all_seconds"] for p in data["people"])
    estimated_tickets = [t for t in data["tickets"] if t["accuracy"] is not None]
    avg_acc = (
        round(sum(t["accuracy"] for t in estimated_tickets) / len(estimated_tickets), 2)
        if estimated_tickets
        else None
    )

    person_opts = "".join(f'<option value="{h(p)}">{h(p)}</option>' for p in people)

    ticket_trs = []
    for t in data["tickets"]:
        if not t.get("jira"):
            continue
        plan = "—" if t["estimated_days"] is None else f"{t['estimated_days']:.0f}"
        acc = "—" if t["accuracy"] is None else f"{t['accuracy']:.2f}"
        band = t["accuracy_band"]
        ticket_trs.append(
            "<tr>"
            f"<td><a href='https://elocity.atlassian.net/browse/{h(t['jira'])}'>{h(t['jira'])}</a></td>"
            f"<td>{h(t['group'])}</td>"
            f"<td>{h(t['feature'])}</td>"
            f"<td>{h(t['assignee'])}</td>"
            f"<td class='num'>{plan}</td>"
            f"<td class='num'>{h(fmt_h(t['actual_seconds']))}</td>"
            f"<td class='num'><span class='band {h(band)}'>{acc}</span></td>"
            f"<td>{h(t['jira_status'])}</td>"
            "</tr>"
        )

    people_trs = []
    for p in data["people"]:
        plan = "—" if p["planned_days"] is None else f"{p['planned_days']:.1f}"
        acc = "—" if p["accuracy_all"] is None else f"{p['accuracy_all']:.2f}"
        people_trs.append(
            "<tr>"
            f"<td>{h(p['person'])}</td>"
            f"<td class='num'>{plan}</td>"
            f"<td class='num'>{h(fmt_h(p['actual_all_seconds']))}</td>"
            f"<td class='num'>{h(fmt_h(p['actual_planned_seconds']))}</td>"
            f"<td class='num'>{acc}</td>"
            f"<td class='num'>{p['worklog_count']}</td>"
            f"<td class='num'>{p['comment_count']}</td>"
            "</tr>"
        )

    bug_trs = []
    for person, count in sorted(data["bugs_by_person"].items(), key=lambda x: -x[1]):
        bug_trs.append(f"<tr><td>{h(person)}</td><td class='num'>{count}</td></tr>")

    bug_detail = []
    for b in data["bugs"]:
        bug_detail.append(
            "<tr>"
            f"<td><a href='https://elocity.atlassian.net/browse/{h(b['key'])}'>{h(b['key'])}</a></td>"
            f"<td>{h(b['summary'])}</td>"
            f"<td>{h(b['assignee'])}</td>"
            f"<td>{h(b['reporter'])}</td>"
            f"<td>{h(b['status'])}</td>"
            f"<td>{h(b['created'])}</td>"
            f"<td>{h(b['parent'])}</td>"
            "</tr>"
        )

    fix_trs = []
    for p in data["people"]:
        fix_trs.append(
            "<tr>"
            f"<td>{h(p['person'])}</td>"
            f"<td class='num'>{h(fmt_h(p['bug_fix_seconds']))}</td>"
            f"<td class='num'>{h(fmt_h(p['task_seconds']))}</td>"
            "</tr>"
        )

    daily_head = "".join(f"<th>{h(d[8:])}</th>" for d in dates)
    daily_body = []
    for person in people:
        tds = []
        total = 0
        for day in dates:
            sec = daily[(person, day)]["seconds"]
            total += sec
            cls = " logged" if sec else ""
            label = "" if not sec else f"{hours(sec):.1f}"
            tds.append(f"<td class='num{cls}'>{label}</td>")
        daily_body.append(
            f"<tr><th>{h(person)}</th>{''.join(tds)}<td class='num'><strong>{hours(total):.1f}h</strong></td></tr>"
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
                items.append(
                    f"<li><span class='meta'>worklog {h(log['time_spent'])}</span> "
                    f"<a href='https://elocity.atlassian.net/browse/{h(log['key'])}'>{h(log['key'])}</a> "
                    f"<span class='type'>{h(log['issuetype'])}</span>{note}</li>"
                )
            for c in cell["comments"]:
                items.append(
                    f"<li><span class='meta'>comment</span> "
                    f"<a href='https://elocity.atlassian.net/browse/{h(c['key'])}'>{h(c['key'])}</a> "
                    f"— {h(c['body'])}</li>"
                )
            blocks.append(
                f"<details open><summary>{h(day)} · {h(fmt_h(cell['seconds']))} · "
                f"{len(cell['comments'])} comments</summary><ul>{''.join(items)}</ul></details>"
            )
        if blocks:
            journal.append(
                f"<section class='person-day' data-person='{h(person)}'><h3>{h(person)}</h3>{''.join(blocks)}</section>"
            )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>August 2026 sprint retrospective</title>
  <style>
    :root {{
      --bg: #f6f4ef;
      --ink: #1c1917;
      --muted: #57534e;
      --line: #e7e5e4;
      --card: #fff;
      --accent: #1d4e89;
      --good: #166534;
      --warn: #a16207;
      --bad: #9f1239;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font: 14px/1.45 "IBM Plex Sans", "Segoe UI", sans-serif;
      color: var(--ink);
      background: var(--bg);
    }}
    header {{
      padding: 28px 32px 16px;
      border-bottom: 1px solid var(--line);
      background: var(--card);
    }}
    h1 {{ margin: 0 0 6px; font-size: 26px; letter-spacing: -0.02em; }}
    h2 {{ margin: 28px 0 10px; font-size: 18px; }}
    h3 {{ margin: 16px 0 8px; font-size: 15px; }}
    p.lead, .note {{ color: var(--muted); max-width: 72ch; }}
    main {{ padding: 20px 32px 64px; }}
    .kpis {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin: 16px 0 8px;
    }}
    .kpi {{
      background: var(--card);
      border: 1px solid var(--line);
      padding: 14px 16px;
    }}
    .kpi strong {{ display: block; font-size: 22px; }}
    .kpi span {{ color: var(--muted); font-size: 12px; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      background: var(--card);
      border: 1px solid var(--line);
      font-size: 13px;
    }}
    th, td {{ padding: 7px 8px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
    th {{ font-weight: 600; background: #fafaf9; }}
    td.num, th.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
    .band.on-plan {{ color: var(--good); }}
    .band.over {{ color: var(--warn); }}
    .band.well-over {{ color: var(--bad); }}
    span.band.n\\/a {{ color: var(--muted); }}
    .wrap {{ overflow: auto; max-height: 520px; border: 1px solid var(--line); }}
    .heatmap td.logged {{ background: #dbeafe; }}
    .heatmap th {{ position: sticky; left: 0; background: #fafaf9; z-index: 1; }}
    .controls {{ display: flex; gap: 8px; margin: 8px 0 12px; align-items: center; }}
    select, input {{ font: inherit; padding: 6px 8px; border: 1px solid var(--line); background: #fff; }}
    a {{ color: var(--accent); }}
    ul {{ margin: 6px 0 12px 18px; }}
    .meta {{ color: var(--muted); font-size: 12px; }}
    .type {{ color: var(--muted); }}
    details summary {{ cursor: pointer; }}
    .person-day {{ margin-bottom: 18px; background: var(--card); border: 1px solid var(--line); padding: 10px 14px; }}
    footer {{ color: var(--muted); font-size: 12px; margin-top: 32px; }}
    @media print {{
      header, main {{ padding: 0; }}
      .controls {{ display: none; }}
      .wrap {{ max-height: none; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>August 2026 sprint retrospective</h1>
    <p class="lead">Planned work from the August 26 sheet versus Jira actuals (worklogs, comments, bugs) for 1–31 Aug 2026. 1d = 8h.</p>
  </header>
  <main>
    <div class="kpis">
      <div class="kpi"><strong>{total_plan:.0f} PD</strong><span>Sheet estimates (numeric only)</span></div>
      <div class="kpi"><strong>{hours(total_actual):.0f}h / {days(total_actual):.0f}d</strong><span>All August logged time</span></div>
      <div class="kpi"><strong>{avg_acc if avg_acc is not None else "n/a"}</strong><span>Mean ticket accuracy (actual ÷ plan)</span></div>
      <div class="kpi"><strong>{len(data["bugs"])}</strong><span>Bugs created in August</span></div>
    </div>
    <p class="note">Accuracy &gt; 1 means more time was logged than estimated. Daily grids use worklog <em>started</em> date. Three EVLM tickets (HIEV-6938/6940/6941) have incomplete worklog payloads (Jira cap 20).</p>

    <h2>1. Planned vs actual days</h2>
    <div class="wrap">
      <table>
        <thead><tr><th>Person</th><th class="num">Planned PD</th><th class="num">Logged (all Aug)</th><th class="num">Logged on planned tickets</th><th class="num">Accuracy</th><th class="num">Worklogs</th><th class="num">Comments</th></tr></thead>
        <tbody>
          {"".join(people_trs)}
        </tbody>
      </table>
    </div>

    <h3>Ticket-level</h3>
    <div class="wrap">
      <table>
        <thead><tr><th>Jira</th><th>Section</th><th>Feature</th><th>Assignee</th><th class="num">Plan</th><th class="num">Actual Aug</th><th class="num">Accuracy</th><th>Status</th></tr></thead>
        <tbody>
          {"".join(ticket_trs)}
        </tbody>
      </table>
    </div>

    <h2>2. Estimation accuracy</h2>
    <p class="note">Ticket accuracy = August days logged on that key ÷ sheet PD. Person accuracy = all August days logged by that person ÷ their sheet PD (people often log on tickets outside the sheet, so this runs high).</p>

    <h2>3. Bugs created</h2>
    <p class="note">{len(data["bugs"])} HIEV bugs created in August, attributed to the <em>bug assignee</em> (usually the person expected to fix it). 75 of 80 sit under parent HIEV-7334.</p>
    <div class="wrap" style="max-height:260px">
      <table>
        <thead><tr><th>Assignee</th><th class="num">Bugs</th></tr></thead>
        <tbody>{"".join(bug_trs)}</tbody>
      </table>
    </div>
    <h3>Bug list</h3>
    <div class="wrap">
      <table>
        <thead><tr><th>Key</th><th>Summary</th><th>Assignee</th><th>Reporter</th><th>Status</th><th>Created</th><th>Parent</th></tr></thead>
        <tbody>{"".join(bug_detail)}</tbody>
      </table>
    </div>

    <h2>4. Fix hours invested</h2>
    <p class="note">Bug tickets: {h(fmt_h(fh["bug_seconds"]))}. Task/Sub-task: {h(fmt_h(fh["task_seconds"]))}. Other: {h(fmt_h(fh["other_seconds"]))}.</p>
    <div class="wrap" style="max-height:360px">
      <table>
        <thead><tr><th>Person</th><th class="num">Bug hours</th><th class="num">Task hours</th></tr></thead>
        <tbody>{"".join(fix_trs)}</tbody>
      </table>
    </div>

    <h2>5. Daily logged time (hours)</h2>
    <div class="wrap heatmap">
      <table>
        <thead><tr><th>Person</th>{daily_head}<th class="num">Total</th></tr></thead>
        <tbody>{"".join(daily_body)}</tbody>
      </table>
    </div>

    <h2>Daily worklogs and comments</h2>
    <div class="controls">
      <label>Person
        <select id="personFilter">
          <option value="">All</option>
          {person_opts}
        </select>
      </label>
    </div>
    <div id="journal">
      {"".join(journal)}
    </div>

    <footer>Generated 31 Aug 2026 from SharePoint August 26 sheet + Jira HIEV. Local repo: august-26-sprint-retro.</footer>
  </main>
  <script>
    const select = document.getElementById("personFilter");
    select.addEventListener("change", () => {{
      const value = select.value;
      document.querySelectorAll(".person-day").forEach((el) => {{
        el.style.display = !value || el.dataset.person === value ? "" : "none";
      }});
    }});
  </script>
</body>
</html>
"""
    (ROOT / "report" / "index.html").write_text(page)


if __name__ == "__main__":
    build()
