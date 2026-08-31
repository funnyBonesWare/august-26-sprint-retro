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

1. **Planned vs actual days** — sheet PD vs Jira worklogs started in August
2. **Estimation accuracy** — actual days ÷ estimated PD (tickets with numeric estimates)
3. **Bugs created** — HIEV `Bug` issues created in August, by assignee
4. **Fix hours** — August worklogs on Bug tickets vs Task/Sub-task tickets
5. **Daily log** — hours per person per day, plus worklog notes and ticket comments

## Rebuild

Raw Jira payloads live in `data/raw/` (gitignored; emails/avatars).

```bash
python3 scripts/build_report.py
```

Writes `data/extracted.json`, `report/index.html`, `report/retrospective.md`.

## Caveats

- Actuals are **August worklogs**, not lifetime `timespent`.
- Jira returns at most 20 worklogs per issue in these dumps. **HIEV-6938, HIEV-6940, HIEV-6941** are truncated.
- QA sheet rows have no Jira keys.
- Bugs are attributed to the **bug assignee**. Most August bugs are children of `HIEV-7334`.
- Person accuracy uses all August time for that user (including tickets not on the sheet), so it is often > 1.
