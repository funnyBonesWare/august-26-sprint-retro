# August 2026 sprint retrospective

Local report repo for the **August 26** sprint sheet (`Sprint wise employe task list.xlsx`) plus Jira HIEV actuals.

Period: **1–31 Aug 2026**. 1 person-day = **8 hours**.

## Open the report

```bash
open report/index.html
# or
python3 -m http.server 8765 --directory report
```

Markdown copy: `report/retrospective.md`

## What it answers

1. **Planned vs actual days** — sprint-planned PD vs Jira worklogs started in August
2. **Estimation accuracy** — actual days ÷ estimated PD (tickets with numeric estimates)
3. **Mid-sprint work** — tickets not in sprint planning that were added during the sprint, with August time or comments
4. **Bugs worked** — distinct HIEV `Bug` Jira tickets with August worklogs or comments, credited to who logged or commented (unique Jira tickets, not assignee)
5. **Fix hours** — August worklogs on Bug tickets vs Task/Sub-task tickets
6. **Daily log** — hours per person per day, plus worklog notes and ticket comments (sprint planned + mid-sprint)
7. **Call notes** — per-person retro comments. Type in the page during the call, then ask to commit and push so everyone sees them.

## Rebuild

Raw Jira payloads live in `data/raw/` (gitignored; emails/avatars).

```bash
python3 scripts/build_report.py
```

Writes `data/extracted.json`, `report/index.html`, `report/retrospective.md`.

## Caveats

- Actuals are **August worklogs**, not lifetime `timespent`.
- Jira returns at most 20 worklogs per issue in these dumps. **HIEV-6938, HIEV-6940, HIEV-6941** are truncated.
- QA sheet rows have no Jira tickets.
- Bugs **worked** in August are credited to people who logged time or commented on that bug, not the assignee at create time. Lavanya is excluded from person lists.
- Person estimation accuracy uses only time on that person’s **planned sheet tickets** (including subtasks of those tickets), not all August logs.
- Person view of sprint-planned tickets uses the **sheet assignee**, not everyone who logged time or commented.
