# August 2026 sprint retrospective

Source: `Sprint wise employe task list.xlsx` sheet **August 26** + Jira HIEV worklogs/comments/bugs for 1–31 Aug 2026.

Assumptions: **8h = 1 person-day**. Actuals = worklogs with `started` in August (not lifetime `timespent`).

## Formulas

- **Hours / days:** `hours = seconds ÷ 3600`; `days = seconds ÷ 28800`.
- **Available days:** for each Mon–Fri except Fri 28 PH, add `1 − leave_fraction`. `available_hours = available_days × 8`. `leave_days = Σ leave_fraction`.
- **Logged of available:** `logged_days of available_days` (hours on the second line). Not a percentage.
- **Util:** `logged_days ÷ available_days`. Team util = `Σ logged_days ÷ Σ available_days`. Green ≥ 0.90, amber ≥ 0.75, else red.
- **Mix %:** `planned% = 100 × sprint_planned_seconds ÷ (planned + mid-sprint)`; `mid% = 100 × mid_sprint_seconds ÷ (planned + mid-sprint)`.
- **Ticket accuracy:** `August_days_on_that_jira_ticket ÷ sprint_plan_PD` (skipped if PD is NA). **Person accuracy:** `August_days_on_jira_tickets_with_numeric_PD ÷ sprint_plan_PD`. Hours on sprint-planned Jira tickets with no PD stay in sprint-planned mix, not in accuracy. Mean KPI averages ticket accuracy only where plan exists and logged > 0. 1.00 = exact. Green ≤ 1.10, amber ≤ 1.50, else red.
- **Logged bar fill:** `min(100, 100 × logged_seconds ÷ available_seconds)`.
- **Bug bar fill:** `100 × person_bug_tickets ÷ max(person_bug_tickets)`.
- **Scrum attendance %:** `100 × attended_expected ÷ expected`. Expected = recorded ~09:30 weekday calls minus PH minus leave covering the call. Missed = `expected − attended`. Avg duration = mean join time on calls joined.
- **Heatmap bands (hours that day):** (0, 2), [2, 4), [4, 6), [6, 8), ≥ 8.

- Actuals are Jira worklogs started 1–31 Aug 2026 (8h = 1d).
- Estimation accuracy uses only matching scope: ticket = August days on that Jira ticket and its subtasks ÷ sprint-plan PD; person = August days on that person's sprint-planned Jira tickets that have a numeric PD (including subtasks of those tickets) ÷ their sprint-plan PD. Jira tickets on the plan with NA/open estimates (e.g. HIEV-6941) count as sprint-planned time, not as an estimate miss or over-run. Person view of sprint-planned tickets is the August 26 sheet assignee, plus Jira subtasks of those tickets — not everyone who commented.
- August hours use worklog `started` when Jira returned the log. For the 9 tickets with more than 20 worklogs, missing logs are filled from issue changelog timespent deltas (date = when the log was submitted). Those fills were checked against issue timespent (HIEV-6785 changelog page misses 0.7h of pre-May history, not August).
- Bugs worked = distinct HIEV issuetype Bug Jira tickets with at least one August worklog or August comment. A person is credited for a unique bug Jira ticket if they logged time or commented on it in August — not the ticket assignee at create time.
- Fix hours = August worklogs on Bug tickets vs Task/Sub-task tickets (sprint planned and mid-sprint).
- Mid-sprint work = HIEV Jira tickets with August worklogs or comments that were not part of sprint planning and were added during the sprint.
- Expected hours = weekdays in August minus Fri 28 public holiday minus that person's planned/sick leave (8h = 1d; Deepak 12 Aug is 0.5d first-half leave).
- Scrum attendance = Teams call Participants sheet. Expected calls = weekdays with a recorded ~09:30 IST scrum minus PH 28 minus leave that covers the call (full-day, or Deepak 12 Aug first-half). Rate = attended expected ÷ expected. Joining on leave is recorded but not a miss.

## 1. Planned vs actual days

| Person | Planned (PD) | Leave (d) | Logged of available | Util | Sprint planned of avail | Mid-sprint of avail | Est. accuracy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Deepak | 15.0 | 0.5 | 20.8 of 19.5d (166h of 156h) | 1.06 | 8.0 of 19.5d (64h of 156h) | 12.8 of 19.5d (102h of 156h) | 0.02 |
| Priyanshu | 20.0 | 0.0 | 20.1 of 20.0d (161h of 160h) | 1.01 | 12.5 of 20.0d (100h of 160h) | 7.6 of 20.0d (61h of 160h) | 0.62 |
| Sahil Kumar | — | 0.0 | 20.0 of 20.0d (160h of 160h) | 1.00 | 12.2 of 20.0d (98h of 160h) | 7.8 of 20.0d (62h of 160h) | — |
| Dhanush | 7.0 | 2.0 | 18.1 of 18.0d (145h of 144h) | 1.01 | 6.0 of 18.0d (48h of 144h) | 12.1 of 18.0d (97h of 144h) | 0.43 |
| Marish | 3.0 | 1.0 | 17.9 of 19.0d (144h of 152h) | 0.94 | 2.8 of 19.0d (22h of 152h) | 15.1 of 19.0d (121h of 152h) | 0.94 |
| Tarun | 7.0 | 0.0 | 17.2 of 20.0d (138h of 160h) | 0.86 | 11.6 of 20.0d (93h of 160h) | 5.6 of 20.0d (45h of 160h) | 1.66 |
| Sudeep | 30.0 | 1.0 | 17.1 of 19.0d (137h of 152h) | 0.90 | 1.9 of 19.0d (15h of 152h) | 15.2 of 19.0d (122h of 152h) | 0.06 |
| Nagaraju | — | 1.0 | 16.8 of 19.0d (134h of 152h) | 0.88 | 0.0 of 19.0d (0h of 152h) | 16.8 of 19.0d (134h of 152h) | — |
| Sahil Siddiqui | 4.0 | 4.0 | 15.1 of 16.0d (121h of 128h) | 0.94 | 9.4 of 16.0d (75h of 128h) | 5.7 of 16.0d (45h of 128h) | 0.38 |
| Dharshini | 13.0 | 2.0 | 13.5 of 18.0d (108h of 144h) | 0.75 | 7.1 of 18.0d (56h of 144h) | 6.5 of 18.0d (52h of 144h) | 0.54 |
| Twisha | 12.0 | 2.0 | 13.3 of 18.0d (107h of 144h) | 0.74 | 6.6 of 18.0d (53h of 144h) | 6.7 of 18.0d (54h of 144h) | 0.55 |
| Shambu | 15.0 | 1.0 | 13.1 of 19.0d (105h of 152h) | 0.69 | 4.4 of 19.0d (36h of 152h) | 8.7 of 19.0d (69h of 152h) | 0.30 |
| Srikant | 19.0 | 3.0 | 11.9 of 17.0d (95h of 136h) | 0.70 | 4.1 of 17.0d (33h of 136h) | 7.8 of 17.0d (62h of 136h) | 0.21 |
| Surya | 14.0 | 0.0 | 11.4 of 20.0d (92h of 160h) | 0.57 | 7.8 of 20.0d (62h of 160h) | 3.6 of 20.0d (29h of 160h) | 0.56 |
| Manjunath | 4.0 | 4.0 | 11.1 of 16.0d (88h of 128h) | 0.69 | 10.4 of 16.0d (83h of 128h) | 0.7 of 16.0d (5h of 128h) | 0.03 |
| Rashmi | — | 5.0 | 9.2 of 15.0d (74h of 120h) | 0.61 | 0.0 of 15.0d (0h of 120h) | 9.2 of 15.0d (74h of 120h) | — |
| Rushika | 5.0 | 0.0 | 8.8 of 20.0d (70h of 160h) | 0.44 | 5.0 of 20.0d (40h of 160h) | 3.8 of 20.0d (30h of 160h) | 1.00 |
| Vinay | 5.0 | 1.0 | 6.0 of 19.0d (48h of 152h) | 0.31 | 3.8 of 19.0d (30h of 152h) | 2.2 of 19.0d (18h of 152h) | 0.05 |

### Ticket-level

| Jira | Feature | Assignee | Plan (PD) | Logged of assignee available | Accuracy | Status |
|---|---|---|---:|---:|---:|---|
| [HIEV-6372](https://elocity.atlassian.net/browse/HIEV-6372) | Abstraction of data layer (ES) | Sudeep | 30 | 1.0 of 19.0d (8h of 152h) | 0.03 | To Do |
| [HIEV-7422](https://elocity.atlassian.net/browse/HIEV-7422) | Subtask of HIEV-6372 · Abstract data layer in session-utility, analytics, payment services | Sudeep | — | 1.0 of 19.0d (8h of 152h) | — | In Progress |
| [HIEV-6945](https://elocity.atlassian.net/browse/HIEV-6945) | Plan, delegate and implement unit test cases across backend repos | Vinay | 5 | 1.2 of 19.0d (10h of 152h) | 0.24 | In Review |
| [HIEV-6988](https://elocity.atlassian.net/browse/HIEV-6988) | Subtask of HIEV-6945 · Session utility Unit test | Vinay | — | 0.2 of 19.0d (2h of 152h) | — | Done |
| [HIEV-6989](https://elocity.atlassian.net/browse/HIEV-6989) | Subtask of HIEV-6945 · Payment service unit tests | Vinay | — | 1.0 of 19.0d (8h of 152h) | — | Done |
| [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406) | Alectra Support | Vinay | — | 3.5 of 19.0d (28h of 152h) | — | In Progress |
| [HIEV-6824](https://elocity.atlassian.net/browse/HIEV-6824) | Project Based Agent Skill File Generation | Deepak | 15 | 0.0 of 19.5d (0h of 156h) | 0.00 | To Do |
| [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) | EVLM Project Activities | Deepak | — | 6.8 of 19.5d (54h of 156h) | — | In Progress |
| [HIEV-6939](https://elocity.atlassian.net/browse/HIEV-6939) | EVLM Project Activities | Sahil Kumar | — | 12.2 of 20.0d (98h of 160h) | — | To Do |
| [HIEV-7205](https://elocity.atlassian.net/browse/HIEV-7205) | Subtask of HIEV-6939 · Unit Tests + Integration Tests | Sahil Kumar | — | 0.4 of 20.0d (3h of 160h) | — | To Do |
| [HIEV-7220](https://elocity.atlassian.net/browse/HIEV-7220) | Subtask of HIEV-6939 · Sandbox for hot path testing | Sahil Kumar | — | 0.1 of 20.0d (1h of 160h) | — | Done |
| [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329) | Subtask of HIEV-6939 · Smartcar implementation in CPMS | Sahil Kumar | — | 3.0 of 20.0d (24h of 160h) | — | Done |
| [HIEV-7426](https://elocity.atlassian.net/browse/HIEV-7426) | Subtask of HIEV-6939 · CPMS integration with EVLM | Sahil Kumar | — | 1.2 of 20.0d (10h of 160h) | — | Done |
| [HIEV-7470](https://elocity.atlassian.net/browse/HIEV-7470) | Subtask of HIEV-6939 · Implement MFA step-up for privileged Ops actions (REQ-SEC-002) | Sahil Kumar | — | 0.7 of 20.0d (6h of 160h) | — | Done |
| [HIEV-7471](https://elocity.atlassian.net/browse/HIEV-7471) | Subtask of HIEV-6939 · Admin AMS proxy — roles + users CRUD (REQ-SEC-007) | Sahil Kumar | — | 0.8 of 20.0d (6h of 160h) | — | In Progress |
| [HIEV-7482](https://elocity.atlassian.net/browse/HIEV-7482) | Subtask of HIEV-6939 · Reserve SU for service account only (XX_XXX tenant, XXXX product, all-product permissions) | Sahil Kumar | — | 0.6 of 20.0d (4h of 160h) | — | In Progress |
| [HIEV-7542](https://elocity.atlassian.net/browse/HIEV-7542) | Subtask of HIEV-6939 · EVLM tenancy isolation | Sahil Kumar | — | 1.4 of 20.0d (12h of 160h) | — | Done |
| [HIEV-7545](https://elocity.atlassian.net/browse/HIEV-7545) | Subtask of HIEV-6939 · Vehicles roster: CPMS live status, SoH KPIs, and UX-parity later slice | Sahil Kumar | — | 1.4 of 20.0d (12h of 160h) | — | Done |
| [HIEV-7554](https://elocity.atlassian.net/browse/HIEV-7554) | Subtask of HIEV-6939 · Vehicles roster: EVLM-only P1 ops list + persisted display name | Sahil Kumar | — | 0.4 of 20.0d (4h of 160h) | — | Done |
| [HIEV-7581](https://elocity.atlassian.net/browse/HIEV-7581) | Subtask of HIEV-6939 · Phase 1 Ops Web manual E2E testing | Sahil Kumar | — | 0.8 of 20.0d (6h of 160h) | — | To Do |
| [HIEV-6940](https://elocity.atlassian.net/browse/HIEV-6940) | EVLM Project Activities | Manjunath | — | 0.1 of 16.0d (1h of 128h) | — | To Do |
| [HIEV-7354](https://elocity.atlassian.net/browse/HIEV-7354) | Enable submetering on Station Management advanced configuration | Manjunath | 4 | 0.1 of 16.0d (1h of 128h) | 0.03 | To Do |
| [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) | New Fleet Management web and mobile screens activity and API support | Manjunath | — | 10.2 of 16.0d (82h of 128h) | — | In Progress |
| [HIEV-7146](https://elocity.atlassian.net/browse/HIEV-7146) | Increase filter capabilities in Network API | Rushika | 1 | 0.4 of 20.0d (3h of 160h) | 0.38 | In Review |
| [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250) | Schema validation script for cross-environment consistency | Rushika | 2 | 4.1 of 20.0d (33h of 160h) | 2.06 | In Review |
| [HIEV-7191](https://elocity.atlassian.net/browse/HIEV-7191) | Customer Engagement Metrics API | Rushika | 2 | 0.5 of 20.0d (4h of 160h) | 0.25 | In Review |
| [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145) | Enhance user manual to latest version (web + mobile) | Tarun | 4 | 1.5 of 20.0d (12h of 160h) | 0.38 | Done |
| [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) | Implement OCPP charger logs validation engine | Tarun | 3 | 10.1 of 20.0d (81h of 160h) | 3.37 | In Review |
| [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347) | Implement web app API payload and data encryption | Shambu | 5 | 4.4 of 19.0d (35h of 152h) | 0.88 | To Do |
| [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350) | Add refund action for session refund (e-wallet datagrid) | Twisha | 2 | 2.0 of 18.0d (16h of 144h) | 1.00 | In Review |
| [HIEV-7360](https://elocity.atlassian.net/browse/HIEV-7360) | Auto resume on power loss (CPMS flow) | Shambu | 10 | 0.0 of 19.0d (0h of 152h) | 0.00 | To Do |
| [HIEV-7358](https://elocity.atlassian.net/browse/HIEV-7358) | Enhance Unique Drivers graph | Twisha | 3 | 1.1 of 18.0d (9h of 144h) | 0.37 | In Review |
| [HIEV-7357](https://elocity.atlassian.net/browse/HIEV-7357) | Subtask of HIEV-7358 · Enhance Unique drivers graph | Twisha | — | 0.0 of 18.0d (0h of 144h) | — | To Do |
| [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344) | New search framework for web app — phase 1 | Twisha | 7 | 3.8 of 18.0d (30h of 144h) | 0.54 | In Review |
| [HIEV-7148](https://elocity.atlassian.net/browse/HIEV-7148) | New Fleet Management web app changes | Surya | 5 | 1.0 of 20.0d (8h of 160h) | 0.20 | In Progress |
| [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362) | Alectra UI screens — SP3 web app UI | Surya | 2 | 2.6 of 20.0d (21h of 160h) | 1.31 | To Do |
| [HIEV-7355](https://elocity.atlassian.net/browse/HIEV-7355) | Enable submetering on Station Management advanced configuration | Surya | 1 | 0.0 of 20.0d (0h of 160h) | 0.00 | To Do |
| [HIEV-6944](https://elocity.atlassian.net/browse/HIEV-6944) | Abstract and standardise export buttons across web app | Surya | 1 | 1.6 of 20.0d (13h of 160h) | 1.62 | In Review |
| [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363) | Country locale based date format across tenant deployment | Surya | 4 | 2.5 of 20.0d (20h of 160h) | 0.62 | In Review |
| [HIEV-7351](https://elocity.atlassian.net/browse/HIEV-7351) | Add refund action for session refund (e-wallet datagrid) | Surya | 1 | 0.4 of 20.0d (4h of 160h) | 0.44 | In Review |
| [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) | EVLM web app frontend API integration | Sahil Siddiqui | — | 7.9 of 16.0d (63h of 128h) | — | In Progress |
| [HIEV-7348](https://elocity.atlassian.net/browse/HIEV-7348) | Implement web app API payload and data encryption | Sahil Siddiqui | 3 | 0.9 of 16.0d (7h of 128h) | 0.29 | To Do |
| [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359) | Enhance Unique Drivers graph | Sahil Siddiqui | 1 | 0.5 of 16.0d (4h of 128h) | 0.50 | To Do |
| [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364) | Export popup rework and common success/error framework for report download | Dharshini | 4 | 3.3 of 18.0d (26h of 144h) | 0.83 | Ready for Testing |
| [HIEV-7455](https://elocity.atlassian.net/browse/HIEV-7455) | Subtask of HIEV-7364 · UI/UX - Export Popup related re work and a common frameowrk to show success/error when downloading report | Dharshini | — | 0.2 of 18.0d (2h of 144h) | — | Done |
| [HIEV-7345](https://elocity.atlassian.net/browse/HIEV-7345) | New search framework for web app — phase 1 | Dharshini | 7 | 1.2 of 18.0d (10h of 144h) | 0.18 | In Progress |
| [HIEV-7150](https://elocity.atlassian.net/browse/HIEV-7150) | New Fleet Management mobile app changes | Dhanush | 2 | 0.8 of 18.0d (6h of 144h) | 0.38 | To Do |
| [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306) | Alectra UI screens | Dhanush | 5 | 1.9 of 18.0d (15h of 144h) | 0.38 | To Do |
| [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942) | EVLM mobile screens and API integration | Dhanush | — | 3.0 of 18.0d (24h of 144h) | — | To Do |
| [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) | End-to-end testing for all brands | Dharshini | 2 | 3.2 of 18.0d (26h of 144h) | 1.62 | Done |
| [HIEV-6925](https://elocity.atlassian.net/browse/HIEV-6925) | Common Dashboard | Srikant | 3 | 2.0 of 17.0d (16h of 136h) | 0.67 | In Progress |
| [HIEV-6932](https://elocity.atlassian.net/browse/HIEV-6932) | Migration plan for AWS to OCI (Canada prod) | Srikant | 2 | 0.0 of 17.0d (0h of 136h) | 0.00 | To Do |
| [HIEV-7365](https://elocity.atlassian.net/browse/HIEV-7365) | Terraform Phase 2 | Srikant | 8 | 0.0 of 17.0d (0h of 136h) | 0.00 | To Do |
| [HIEV-7366](https://elocity.atlassian.net/browse/HIEV-7366) | Developer onboarding (tech team) | Srikant | 3 | 0.0 of 17.0d (0h of 136h) | 0.00 | To Do |
| [HIEV-7367](https://elocity.atlassian.net/browse/HIEV-7367) | Infra creation and OpenSearch migration (Adani) | Srikant | 3 | 0.0 of 17.0d (0h of 136h) | 0.00 | To Do |
| [HIEV-7368](https://elocity.atlassian.net/browse/HIEV-7368) | Site-wise infra doc (Lower / Canada / Adani / Alfanar) | Priyanshu | 8 | 6.6 of 20.0d (53h of 160h) | 0.83 | Done |
| [HIEV-7392](https://elocity.atlassian.net/browse/HIEV-7392) | Subtask of HIEV-7368 · INFRA / Documentation of lower-env infra | Priyanshu | — | 2.0 of 20.0d (16h of 160h) | — | Done |
| [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393) | Subtask of HIEV-7368 · INFRA / Documentation of canada infra | Priyanshu | — | 1.9 of 20.0d (15h of 160h) | — | Done |
| [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394) | Subtask of HIEV-7368 · INFRA / Documentation of Adani-env infra | Priyanshu | — | 1.0 of 20.0d (8h of 160h) | — | Done |
| [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395) | Subtask of HIEV-7368 · INFRA / Documentation of Alfanar-env infra | Priyanshu | — | 1.0 of 20.0d (8h of 160h) | — | Done |
| [HIEV-7441](https://elocity.atlassian.net/browse/HIEV-7441) | Subtask of HIEV-7368 · Infra Doc review lower-env | Priyanshu | — | 0.5 of 20.0d (4h of 160h) | — | Done |
| [HIEV-7369](https://elocity.atlassian.net/browse/HIEV-7369) | Prod (Adani / Alfanar) security tightening | Priyanshu | 6 | 4.2 of 20.0d (34h of 160h) | 0.71 | Done |
| [HIEV-7507](https://elocity.atlassian.net/browse/HIEV-7507) | Subtask of HIEV-7369 · INFRA / Adani-Prod Security Tightening | Priyanshu | — | 1.8 of 20.0d (14h of 160h) | — | Done |
| [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508) | Subtask of HIEV-7369 · INFRA / Alfanar-Prod Security Tightening | Priyanshu | — | 2.5 of 20.0d (20h of 160h) | — | Done |
| [HIEV-6929](https://elocity.atlassian.net/browse/HIEV-6929) | No root user containers | Priyanshu | — | 0.0 of 20.0d (0h of 160h) | — | Done |
| [HIEV-7370](https://elocity.atlassian.net/browse/HIEV-7370) | Kafka lower-stage migration to self-managed | Priyanshu | 3 | 0.9 of 20.0d (7h of 160h) | 0.29 | In Progress |
| [HIEV-7371](https://elocity.atlassian.net/browse/HIEV-7371) | User onboarding to OCI via Entra ID (Azure) | Priyanshu | 3 | 2.8 of 20.0d (22h of 160h) | 0.92 | Done |
| [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372) | DevOps related activity handover KT (Dev to DevOps) | Deepak | — | 1.1 of 19.5d (9h of 156h) | — | Done |
| [HIEV-7327](https://elocity.atlassian.net/browse/HIEV-7327) | Security Profile — Alectra UI screens (SP3 web app) | Marish | 3 | 2.2 of 19.0d (18h of 152h) | 0.73 | Done |

### Tasks and bugs added mid-sprint

311 HIEV Jira tickets with August worklogs or comments that were not part of sprint planning (added mid-sprint). Time and comments here are included in person totals, daily hours, and the journal.

| Jira | Type | Summary | Logged by | Commented by | Logged of available | Comments | Status |
|---|---|---|---|---|---:|---:|---|
| [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) | Task | Enhancing session modification api with necessary session recreation | Sudeep | Sudeep | 8.5 of 19.0d (68h of 152h) | 19 | In Progress |
| [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) | Task | AdHoc assignments, Team discussions and Product maintenance  | Deepak | Deepak | 6.6 of 19.5d (53h of 156h) | 14 | In Progress |
| [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221) | Observation | EVLM Incentives Module | Marish | Marish | 5.6 of 19.0d (45h of 152h) | 6 | In Review |
| [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238) | Task | Gitlab POC | Srikant | Srikant | 5.0 of 17.0d (40h of 136h) | 9 | Done |
| [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) | Task | Adhoc Activities | Sahil Kumar | Sahil Kumar | 4.4 of 20.0d (36h of 160h) | 19 | To Do |
| [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506) | Task | Load Management – QA Testing & Validation | Nagaraju | Nagaraju | 4.0 of 19.0d (32h of 152h) | 6 | Done |
| [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557) | Task | Mobile App / Bluetooth-based charger Wi-Fi configuration (HiEV Operator) | Dhanush | Dhanush | 3.9 of 18.0d (31h of 144h) | 5 | In Progress |
| [HIEV-7497](https://elocity.atlassian.net/browse/HIEV-7497) | Observation | Alectra Mobile App Design | Marish | Marish | 3.5 of 19.0d (28h of 152h) | 4 | In Review |
| [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574) | Task | INFRA / GITLAB migration | Priyanshu | Priyanshu | 3.5 of 20.0d (28h of 160h) | 7 | In Progress |
| [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) | Epic | QA - Adhoc activities | Nagaraju | — | 3.0 of 19.0d (24h of 152h) | 0 | In Progress |
| [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445) | Task | Enhance User Manual to latest version(Mobile) | Tarun | Tarun | 2.9 of 20.0d (23h of 160h) | 7 | In Review |
| [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536) | Task | idle  time report | Rushika | Rushika | 2.8 of 20.0d (22h of 160h) | 5 | In Progress |
| [HIEV-7591](https://elocity.atlassian.net/browse/HIEV-7591) | Task | Operator-Issued e-Wallet Credits | Tarun | Tarun | 2.8 of 20.0d (22h of 160h) | 2 | In Progress |
| [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722) | Task | Audit and implement non-root users for containers | Deepak, Srikant | Deepak, Srikant | 2.6 of 17.0d (21h of 136h) | 4 | In Progress |
| [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) | Task | Support Activities | Sahil Kumar | Sahil Kumar | 2.4 of 20.0d (19h of 160h) | 9 | To Do |
| [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) | Task | AdHoc Task | Dhanush | Dhanush | 2.2 of 18.0d (18h of 144h) | 9 | In Progress |
| [HIEV-7600](https://elocity.atlassian.net/browse/HIEV-7600) | Observation | Operator-Issued e-Wallet Credits Web | Marish | Marish | 2.1 of 19.0d (17h of 152h) | 1 | In Progress |
| [HIEV-7588](https://elocity.atlassian.net/browse/HIEV-7588) | Observation | EVLM UI Enhancements | Marish | Marish | 1.9 of 19.0d (15h of 152h) | 2 | In Progress |
| [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440) | Task | Developer code Implementation flow for Customer Module | Dharshini, Sahil Siddiqui | Dharshini, Sahil Siddiqui | 1.7 of 16.0d (13h of 128h) | 5 | In Review |
| [HIEV-7566](https://elocity.atlassian.net/browse/HIEV-7566) | Observation | UIUX Design Review | Marish | Marish | 1.6 of 19.0d (13h of 152h) | 2 | In Progress |
| [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446) | Bug | Staging / HIEV Canada / Android / In-App Campaign / maxDisplayCount is not enforced for Welcome campaign | Dhanush, Nagaraju | Dhanush, Nagaraju, Sahil Siddiqui | 1.4 of 18.0d (12h of 144h) | 15 | Done |
| [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) | Task | Ad hoc work and Discussions with the Team Members on project activities  | Sahil Siddiqui | Sahil Siddiqui | 1.4 of 16.0d (11h of 128h) | 15 | To Do |
| [HIEV-6383](https://elocity.atlassian.net/browse/HIEV-6383) | Epic | Frontend / Finish Integration and Handover of New Profile Page | Rashmi | Rashmi | 1.4 of 15.0d (11h of 120h) | 2 | Testing |
| [HIEV-6384](https://elocity.atlassian.net/browse/HIEV-6384) | Epic | Frontend / Guest Charging To be brought to the Cpms Web Repo | Rashmi | Rashmi | 1.4 of 19.0d (11h of 152h) | 2 | In Review |
| [HIEV-7172](https://elocity.atlassian.net/browse/HIEV-7172) | Bug | Stage / Portal / At times, the previous or existing transaction details are sometimes not reflected in the side panel of station management  | Shambu | Shambu | 1.4 of 19.0d (11h of 152h) | 1 | To Do |
| [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378) | Task | Feature PRD writing and planing | Deepak | Deepak | 1.4 of 19.5d (11h of 156h) | 5 | Done |
| [HIEV-6914](https://elocity.atlassian.net/browse/HIEV-6914) | Epic | Adhoc Task | Rashmi | Rashmi | 1.2 of 15.0d (10h of 120h) | 2 | To Do |
| [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503) | Bug | Staging / EVSE Model / Created model is not displayed in list/search despite successful creation and duplicate-name validation | Nagaraju, Sahil Siddiqui, Twisha | Nagaraju, Sahil Siddiqui, Twisha | 1.2 of 16.0d (10h of 128h) | 8 | Done |
| [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439) | Bug | STG/ Hiev Canada/ Portal/ Location Management>>My profile>> Updated Location Not Displayed in Activity Log After Editing Tariff | Dharshini, Rashmi, Sudeep | Dharshini, Rashmi, Sudeep | 1.2 of 19.0d (10h of 152h) | 4 | Done |
| [HIEV-7152](https://elocity.atlassian.net/browse/HIEV-7152) | Task | Adhoc tasks | Dharshini | Dharshini | 1.1 of 18.0d (9h of 144h) | 2 | In Progress |
| [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458) | Bug | Staging / Mobile / New Login / Country picker shows all countries first then filters; loader flashes on country code | Dhanush, Rashmi | Dhanush, Rashmi, Sahil Siddiqui | 1.1 of 15.0d (8h of 120h) | 9 | Testing |
| [HIEV-7449](https://elocity.atlassian.net/browse/HIEV-7449) | Bug | STG/ Hiev Canada/ Portal/Tariff launch activity is not displayed in Activity Logs | Rashmi, Sudeep | Rashmi, Sudeep | 1.0 of 19.0d (8h of 152h) | 3 | Done |
| [HIEV-7442](https://elocity.atlassian.net/browse/HIEV-7442) | Task | Security reporting agent review and research | Deepak | Deepak | 1.0 of 19.5d (8h of 156h) | 3 | Done |
| [HIEV-7496](https://elocity.atlassian.net/browse/HIEV-7496) | Task | ChargeM / Production OTA blocked after 9.5.0 crash; Sunday-closed fix shipped via Play Store / App Store | Dhanush | Dhanush | 1.0 of 18.0d (8h of 144h) | 1 | Done |
| [HIEV-7537](https://elocity.atlassian.net/browse/HIEV-7537) | Task | Active Charging Report | Rushika | Rushika | 1.0 of 20.0d (8h of 160h) | 3 | To Do |
| [HIEV-7553](https://elocity.atlassian.net/browse/HIEV-7553) | Task | Product Management tasks | Deepak | Deepak | 1.0 of 19.5d (8h of 156h) | 2 | In Progress |
| [HIEV-7606](https://elocity.atlassian.net/browse/HIEV-7606) | Sub-task | gitlab Mac mini issue | Srikant | Srikant | 1.0 of 17.0d (8h of 136h) | 1 | In Progress |
| [HIEV-6607](https://elocity.atlassian.net/browse/HIEV-6607) | Bug | UAT/ Hiev India / Push Notification >> Scheduled push notification is not sent in the given time | Rashmi, Shambu | Rashmi, Shambu | 0.9 of 19.0d (7h of 152h) | 3 | Done |
| [HIEV-6649](https://elocity.atlassian.net/browse/HIEV-6649) | Task | Backend - Cost of Charging Session and electricity Report | Vinay | Sahil Kumar, Vinay | 0.9 of 19.0d (7h of 152h) | 5 | Done |
| [HIEV-7304](https://elocity.atlassian.net/browse/HIEV-7304) | Bug | Stage / Portal / ⁠My Profile>Click on ‘Export Logs’ button>Verify the report - Entity reference is ‘UNKNOWN’ with a note “value too long for type character varying(255)”>> BUT the same note later on has the entity reference 418 and entity type - location | Sudeep | Rashmi, Sudeep | 0.9 of 19.0d (7h of 152h) | 3 | Done |
| [HIEV-7352](https://elocity.atlassian.net/browse/HIEV-7352) | Bug | Stage / portal / android / HIEV canada /Refreshing the charging session couple of times during the Finishing state or after reaching max SOCresets accumulated Energy Consumed to 0, resulting in loss of previously recorded energy | Twisha | Twisha | 0.9 of 19.0d (7h of 152h) | 2 | In Review |
| [HIEV-7403](https://elocity.atlassian.net/browse/HIEV-7403) | Task | Movem sessions payment processing | Sudeep | Sudeep | 0.9 of 19.0d (7h of 152h) | 4 | Done |
| [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242) | Bug | UAT / Hiev Canada / Android / Queue / Simultaneous queue requests fail for both users with "Time slot already reserved" | Twisha, Vinay | Twisha, Vinay | 0.8 of 19.0d (7h of 152h) | 9 | Ready for Testing |
| [HIEV-7526](https://elocity.atlassian.net/browse/HIEV-7526) | Bug | Staging / Load Management / Unable to edit existing Load Group when no charging sessions are active | Nagaraju, Shambu | Nagaraju | 0.8 of 19.0d (6h of 152h) | 1 | Done |
| [HIEV-7490](https://elocity.atlassian.net/browse/HIEV-7490) | Bug | STG / Hiev Canada/ Portal/ Corporate Customer – INACTIVE RFID displays generic “Something went wrong” message. | Rashmi, Shambu | Rashmi, Shambu, Vinay | 0.8 of 19.0d (6h of 152h) | 4 | Done |
| [HIEV-7121](https://elocity.atlassian.net/browse/HIEV-7121) | Bug | Stage / Portal / Getting 500 error code after exporting a report but continuing to download other reports without viewing the downloaded reports in the export module | Nagaraju, Shambu | Nagaraju, Sahil Kumar, Shambu | 0.8 of 19.0d (6h of 152h) | 3 | Done |
| [HIEV-6393](https://elocity.atlassian.net/browse/HIEV-6393) | Epic | Backend / Firmware module Enhancement | Rashmi | Rashmi | 0.8 of 15.0d (6h of 120h) | 1 | Testing |
| [HIEV-6636](https://elocity.atlassian.net/browse/HIEV-6636) | Task | Regression Fix Verification for Login, Map, QR Scan, Reservation, and Filter Flows | Rashmi | Rashmi | 0.8 of 18.0d (6h of 144h) | 2 | Done |
| [HIEV-7031](https://elocity.atlassian.net/browse/HIEV-7031) | Task | 401 and 403 error checks and validation. in some places instead of 403 error, 401 error is being displayed which is not accurate. | Deepak, Twisha | Deepak, Twisha | 0.8 of 19.5d (6h of 156h) | 2 | Done |
| [HIEV-7340](https://elocity.atlassian.net/browse/HIEV-7340) | Task | Unit testing KT | Shambu | — | 0.8 of 19.0d (6h of 152h) | 0 | Done |
| [HIEV-7575](https://elocity.atlassian.net/browse/HIEV-7575) | Task | INFRA / lower-env runner instance storage clean | Priyanshu | Priyanshu | 0.8 of 20.0d (6h of 160h) | 2 | Done |
| [HIEV-7597](https://elocity.atlassian.net/browse/HIEV-7597) | Bug | Force delete export jobs after 7 days from completion | Shambu | Shambu | 0.8 of 19.0d (6h of 152h) | 2 | In Progress |
| [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388) | Task | Location filter support in reports | Dharshini, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.7 of 19.0d (6h of 152h) | 6 | Done |
| [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032) | Bug | Canada Prod / Prod / Alerts & Notifications > Using the alerts time filter, select “Payment Successful” option > Click on ‘Apply’ button > There are 0 corresponding search results which is incorrect as there are 77 paid session for the same time period | Rashmi, Twisha, Vinay | Rashmi, Twisha, Vinay | 0.7 of 18.0d (6h of 144h) | 8 | Done |
| [HIEV-6684](https://elocity.atlassian.net/browse/HIEV-6684) | Epic | Business related metadata/details should accept landline numbers too | Rashmi | Rashmi | 0.7 of 16.0d (6h of 128h) | 1 | Done |
| [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836) | Epic | Mobile App / In App Campaign  | Dhanush | Dhanush, Nagaraju, Sahil Siddiqui | 0.6 of 19.0d (5h of 152h) | 8 | To Do |
| [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477) | Suggestion | Provide additional entry points to initiate a reservation | Dhanush, Nagaraju, Rashmi | Dhanush, Rashmi, Sahil Siddiqui | 0.6 of 18.0d (5h of 144h) | 5 | Done |
| [HIEV-7485](https://elocity.atlassian.net/browse/HIEV-7485) | Task | Session Termination Flowchart | Sudeep | Sudeep | 0.6 of 19.0d (5h of 152h) | 2 | Done |
| [HIEV-7587](https://elocity.atlassian.net/browse/HIEV-7587) | Sub-task | gitlab pending activities  | Srikant | Srikant | 0.6 of 17.0d (5h of 136h) | 1 | Done |
| [HIEV-7414](https://elocity.atlassian.net/browse/HIEV-7414) | Sub-task | Smart car mobile app feature firebase wrapping and ios pipeline re fix again | Dhanush, Sahil Siddiqui | Dhanush, Sahil Siddiqui | 0.6 of 18.0d (4h of 144h) | 5 | Done |
| [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326) | Bug | Stage / Portal / My Profile > Activity Logs > Currently, the Changes and Notes fields often display "NA", which results in redundant information.  | Dharshini, Sahil Siddiqui, Sudeep | Dharshini, Sahil Siddiqui, Sudeep | 0.6 of 19.0d (4h of 152h) | 8 | Ready for Testing |
| [HIEV-7216](https://elocity.atlassian.net/browse/HIEV-7216) | Bug | STG/ Hiev Canada / Portal / Assets-> Diagnostic>>Diagnostic report CRON job and recovery job failed to run  | Rashmi, Shambu | Rashmi, Sahil Kumar, Shambu | 0.5 of 19.0d (4h of 152h) | 3 | Done |
| [HIEV-7416](https://elocity.atlassian.net/browse/HIEV-7416) | Bug | STG/ Hiev Canada/ Portal/ Station Remains in Maintenance Mode After Maintenance Is Removed, Blocking New Charging Sessions | Rashmi, Twisha | Twisha | 0.5 of 20.0d (4h of 160h) | 1 | In Progress |
| [HIEV-7491](https://elocity.atlassian.net/browse/HIEV-7491) | Bug | STG / Hiev Canada/ Portal/ Abnormal Event-> INACTIVE RFID of Corporate Customer – Abnormal Event displays technical error in the description. | Rashmi, Shambu | Rashmi, Shambu, Vinay | 0.5 of 19.0d (4h of 152h) | 3 | Done |
| [HIEV-6981](https://elocity.atlassian.net/browse/HIEV-6981) | Task | Adhoc | Manjunath | Manjunath | 0.5 of 16.0d (4h of 128h) | 3 | To Do |
| [HIEV-7244](https://elocity.atlassian.net/browse/HIEV-7244) | Bug | UAT / Hiev Canada / Android / Reservations / Cancelled reservations and cancelled queue's are displayed in the Upcoming tab without any status indication where customers cannot distinguish an active reservation from a cancelled one without opening it. | Nagaraju, Twisha | Nagaraju, Twisha | 0.5 of 18.0d (4h of 144h) | 3 | Done |
| [HIEV-6373](https://elocity.atlassian.net/browse/HIEV-6373) | Epic | Backend / Support & Adhoc Activities | Sahil Kumar | Sahil Kumar | 0.5 of 20.0d (4h of 160h) | 1 | To Do |
| [HIEV-7429](https://elocity.atlassian.net/browse/HIEV-7429) | Sub-task | Doc Review and MR review  | Srikant | Srikant | 0.5 of 17.0d (4h of 136h) | 1 | Done |
| [HIEV-7573](https://elocity.atlassian.net/browse/HIEV-7573) | Task | INFRA / CLOUD COST Comparison(canada VS adani) | Priyanshu | Priyanshu | 0.5 of 20.0d (4h of 160h) | 1 | Done |
| [HIEV-7589](https://elocity.atlassian.net/browse/HIEV-7589) | Task | Guest Charging - Refund Support and immediate release of cardhold when transaction id doesnt get recorded | Sudeep | Sudeep | 0.5 of 19.0d (4h of 152h) | 1 | In Progress |
| [HIEV-7564](https://elocity.atlassian.net/browse/HIEV-7564) | Bug | STG/ Portal/ Hiev Canada/ Customer -> E-wallet>> Session Refunded and Wallet Refunded are not available as separate options in the Event Type dropdown | Dharshini, Rashmi, Twisha | Dharshini, Twisha | 0.5 of 16.0d (4h of 128h) | 3 | In Review |
| [HIEV-7159](https://elocity.atlassian.net/browse/HIEV-7159) | Task | Adhoc tasks | Vinay | Vinay | 0.5 of 19.0d (4h of 152h) | 2 | Done |
| [HIEV-6441](https://elocity.atlassian.net/browse/HIEV-6441) | Task | Web App / New abnormal event added - Abnormal session termination | Rashmi | Rashmi | 0.4 of 15.0d (4h of 120h) | 1 | Testing |
| [HIEV-7472](https://elocity.atlassian.net/browse/HIEV-7472) | Task | Universal Energies / Production Release 6.4.0 (Android released / iOS In Review) — tag universal-energies-prod-2026-07-17 | Dhanush | Dhanush | 0.4 of 18.0d (4h of 144h) | 1 | Done |
| [HIEV-7541](https://elocity.atlassian.net/browse/HIEV-7541) | Task | QA Validation / Utility Tariff – Functional, Validation, Cost Calculation & Reports Testing | Nagaraju | Nagaraju | 0.4 of 19.0d (4h of 152h) | 1 | Done |
| [HIEV-7584](https://elocity.atlassian.net/browse/HIEV-7584) | Suggestion | Staging / Load Management / UI Enhancement / Add Connector Icon to Load Group Overview Connector Cards | Nagaraju, Surya | Sahil Kumar, Surya | 0.4 of 19.0d (4h of 152h) | 2 | Ready for Testing |
| [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546) | Bug | UAT/ Portal Hiev Canada/ Guest Charging >> Incorrect “Payment is being processed” Loader Message Displayed After Charging Session Starts | Dharshini, Rashmi, Sahil Siddiqui, Sudeep | Dharshini, Sahil Siddiqui, Sudeep | 0.4 of 15.0d (3h of 120h) | 9 | Ready for Testing |
| [HIEV-7475](https://elocity.atlassian.net/browse/HIEV-7475) | Bug | Staging / Android / Time is displayed in 24-hour format instead of 12-hour format with AM/PM | Dhanush, Nagaraju, Rashmi | Dhanush, Rashmi | 0.4 of 18.0d (3h of 144h) | 2 | Done |
| [HIEV-7563](https://elocity.atlassian.net/browse/HIEV-7563) | Bug | Staging / Load Management / Decommissioned station continues to be displayed in Load Group Overview | Nagaraju, Sahil Kumar | Nagaraju, Sahil Kumar | 0.4 of 20.0d (3h of 160h) | 2 | Done |
| [HIEV-7243](https://elocity.atlassian.net/browse/HIEV-7243) | Bug | UAT / Hiev Canada / Android / Reservation / Reserved time slots remain selectable and validation occurs only after reservation confirmation | Twisha, Vinay | Nagaraju, Twisha, Vinay | 0.4 of 18.0d (3h of 144h) | 5 | Done |
| [HIEV-7396](https://elocity.atlassian.net/browse/HIEV-7396) | Task | QA Validation – In-App Campaign / Campaign Display Flow | Nagaraju | Nagaraju | 0.4 of 19.0d (3h of 152h) | 3 | Done |
| [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385) | Bug | Movem Prod / Displayed Location as Closed on Location Detail screen on Sundays. | Dhanush, Nagaraju, Vinay | Dhanush, Sahil Siddiqui, Vinay | 0.4 of 18.0d (3h of 144h) | 5 | Done |
| [HIEV-7436](https://elocity.atlassian.net/browse/HIEV-7436) | Task | use last meter value timestamp or session start date for stop timestamp in force terminate logic | Sudeep | Sudeep | 0.4 of 19.0d (3h of 152h) | 1 | Done |
| [HIEV-7457](https://elocity.atlassian.net/browse/HIEV-7457) | Task | week2 cloud  cost report  | Priyanshu | Priyanshu | 0.4 of 20.0d (3h of 160h) | 1 | Done |
| [HIEV-7484](https://elocity.atlassian.net/browse/HIEV-7484) | Sub-task | OCI onboarding discussion | Srikant | Srikant | 0.4 of 17.0d (3h of 136h) | 1 | Done |
| [HIEV-7486](https://elocity.atlassian.net/browse/HIEV-7486) | Task | INFRA / DOTA Server Fix  | Priyanshu | Priyanshu | 0.4 of 20.0d (3h of 160h) | 2 | Done |
| [HIEV-7498](https://elocity.atlassian.net/browse/HIEV-7498) | Observation | Web Site Support | Marish | Marish | 0.4 of 19.0d (3h of 152h) | 1 | In Review |
| [HIEV-7522](https://elocity.atlassian.net/browse/HIEV-7522) | Task | INFRA / Weekly Cloud Cost Report (3) | Priyanshu | Priyanshu | 0.4 of 20.0d (3h of 160h) | 1 | Done |
| [HIEV-7560](https://elocity.atlassian.net/browse/HIEV-7560) | Bug | Staging / Load Management / CPMS / Load Group creation/update fails when station(s) are selected | Nagaraju, Shambu | Nagaraju, Shambu | 0.4 of 19.0d (3h of 152h) | 3 | Done |
| [HIEV-7582](https://elocity.atlassian.net/browse/HIEV-7582) | Task | INFRA / Cloud Cost Report week (3) | Priyanshu | Priyanshu | 0.4 of 20.0d (3h of 160h) | 1 | Done |
| [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390) | Bug | STG / CPMS / Bulk Operations / Get Configuration / Selected Charge Point IDs are not passed in request, resulting in HTTP 400 | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.3 of 18.0d (3h of 144h) | 7 | Done |
| [HIEV-7323](https://elocity.atlassian.net/browse/HIEV-7323) | Bug | Stage / Portal / Activity Logs > IP address and Device fields are missing from the downloaded report | Dharshini, Sudeep | Sudeep | 0.3 of 19.0d (2h of 152h) | 3 | Done |
| [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391) | Bug | STG / CPMS / Bulk Operations / Get Configuration / Perform Action button remains disabled when only Custom configuration keys are entered | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.3 of 18.0d (2h of 144h) | 7 | Done |
| [HIEV-7399](https://elocity.atlassian.net/browse/HIEV-7399) | Task | Guest Charging / Displaying Real time Charger Details in Charging Session Summary Screen | Dharshini | Dharshini, Nagaraju, Sahil Siddiqui | 0.3 of 18.0d (2h of 144h) | 4 | Done |
| [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492) | Bug | STG / CPMS / Corporate / Employees / Employee ID field accepts excessive characters without validation | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Sahil Siddiqui | 0.3 of 19.0d (2h of 152h) | 6 | Ready for Testing |
| [HIEV-7495](https://elocity.atlassian.net/browse/HIEV-7495) | Bug | STG/ Hiev Canada/ Portal/ Charging session can be started before the station’s commissioned date | Shambu | Rashmi, Shambu, Vinay | 0.3 of 19.0d (2h of 152h) | 3 | Done |
| [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539) | Bug | STG/ Portal / Hiev Canada/ Assets-> Diagnostic Job >>Job status remains In Progress even though all 2 stations are successful | Rashmi, Sahil Kumar, Shambu | Rashmi, Sahil Kumar, Shambu | 0.3 of 19.0d (2h of 152h) | 5 | Done |
| [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237) | Bug | Staging / CPMS Portal / Assets > Location Management / Invalid character limit handling results in server errors during Location creation and update | Sahil Siddiqui, Surya | Nagaraju, Sahil Siddiqui, Surya | 0.3 of 19.0d (2h of 152h) | 5 | Ready for Testing |
| [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530) | Bug | Staging / CPMS / Utility Tariff / The Design New Tariff → Utility Tariff screen has insufficient/unclear validation for the Tariff Name and TOU Price fields. | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.3 of 16.0d (2h of 128h) | 10 | In Review |
| [HIEV-7199](https://elocity.atlassian.net/browse/HIEV-7199) | Bug | The triggerPrepaidLocationPaymentJob cron job in payment service has no guard against infinite retries | Sudeep, Vinay | Sudeep, Vinay | 0.3 of 19.0d (2h of 152h) | 2 | Done |
| [HIEV-7324](https://elocity.atlassian.net/browse/HIEV-7324) | Bug | Staging / Portal / Activity Logs / Business filter displays records from other businesses after applying selected business filter | Sudeep, Twisha | Sudeep, Twisha | 0.3 of 19.0d (2h of 152h) | 2 | In Review |
| [HIEV-7379](https://elocity.atlassian.net/browse/HIEV-7379) | Bug | Stage/ CPMS / Tariff / Launch Tariff Profile fails with HTTP 500 due to missing currency_code error | Nagaraju, Twisha | Nagaraju, Twisha | 0.3 of 18.0d (2h of 144h) | 2 | Done |
| [HIEV-7401](https://elocity.atlassian.net/browse/HIEV-7401) | Sub-task | QA Validation – Export Module / Post Export Navigation Stability | Nagaraju | Nagaraju | 0.3 of 19.0d (2h of 152h) | 2 | Done |
| [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533) | Bug | Staging / CPMS / Utility Tariff / Tiered Tariff / Rate/Price field accepts excessively lengthy numeric values and exposes API validation error | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.3 of 16.0d (2h of 128h) | 10 | In Review |
| [HIEV-7301](https://elocity.atlassian.net/browse/HIEV-7301) | Bug | UAT/ Hiev Canada/ Portal/ Deleted Customer (Customer ID: 2938) is displayed in Active Customers | Rashmi, Twisha | Rashmi, Twisha | 0.3 of 18.0d (2h of 144h) | 2 | Done |
| [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291) | Bug | STG / Portal/ Hiev Canada/ Abnormal Event -> Event Type-(Start Transaction failed and Remote Start Failed) -Description message is not user friendly | Rashmi, Shambu, Vinay | Rashmi, Shambu, Vinay | 0.3 of 19.0d (2h of 152h) | 9 | Done |
| [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404) | Bug | STG / CPMS / Portal / Reservation / Save action does not trigger Create Reservation API and displays incorrect validation error | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.3 of 18.0d (2h of 144h) | 5 | Done |
| [HIEV-6752](https://elocity.atlassian.net/browse/HIEV-6752) | Task | cpms-portal: React Doctor score uplift + CI/CD gate + MR merge rule | Surya | Surya | 0.2 of 16.0d (2h of 128h) | 2 | Done |
| [HIEV-7183](https://elocity.atlassian.net/browse/HIEV-7183) | Task | New Fleet Management web Activity and API Support | Surya | — | 0.2 of 20.0d (2h of 160h) | 0 | In Progress |
| [HIEV-7295](https://elocity.atlassian.net/browse/HIEV-7295) | Bug | UAT / CPMS / Portal / Guest / Incorrect connector details displayed for selected connector on multi-connector stations | Dharshini | Dharshini, Nagaraju, Sahil Siddiqui | 0.2 of 18.0d (2h of 144h) | 4 | Done |
| [HIEV-7311](https://elocity.atlassian.net/browse/HIEV-7311) | Bug | Stage / Portal / Station Management > View the details of the station > Go to “Logs History” > Update the date range > There are 0 results are displayed which is incorrect | Twisha | Twisha | 0.2 of 18.0d (2h of 144h) | 1 | Done |
| [HIEV-7341](https://elocity.atlassian.net/browse/HIEV-7341) | Task | INFRA / Reimport TotalEnergies ssl cert | Priyanshu | Priyanshu | 0.2 of 20.0d (2h of 160h) | 1 | Done |
| [HIEV-7389](https://elocity.atlassian.net/browse/HIEV-7389) | Task | INFRA / OCI Cloud cost analysis | Priyanshu | Priyanshu | 0.2 of 20.0d (2h of 160h) | 2 | Done |
| [HIEV-7427](https://elocity.atlassian.net/browse/HIEV-7427) | Sub-task | AI Companion demo review — open questions & findings (Confluence) | Sahil Siddiqui | Sahil Siddiqui | 0.2 of 16.0d (2h of 128h) | 1 | Done |
| [HIEV-7430](https://elocity.atlassian.net/browse/HIEV-7430) | Task | mapping more defined and accurate names in the frontend for "EventType" parameter. | Dharshini, Rashmi, Sahil Siddiqui | Dharshini, Rashmi, Sahil Siddiqui | 0.2 of 15.0d (2h of 120h) | 4 | Testing |
| [HIEV-7555](https://elocity.atlassian.net/browse/HIEV-7555) | Task | INFRA / SSL CERT AUTOMATION SCRIPT | Priyanshu | Priyanshu | 0.2 of 20.0d (2h of 160h) | 1 | Done |
| [HIEV-7593](https://elocity.atlassian.net/browse/HIEV-7593) | Task | INFRA / REMOTE ACCESS | Priyanshu | Priyanshu | 0.2 of 20.0d (2h of 160h) | 2 | Done |
| [HIEV-7599](https://elocity.atlassian.net/browse/HIEV-7599) | Sub-task | Code review MR !788 — Station Management + Load Management fixes | Sahil Siddiqui | Sahil Siddiqui | 0.2 of 16.0d (2h of 128h) | 4 | Done |
| [HIEV-7614](https://elocity.atlassian.net/browse/HIEV-7614) | Bug | UAT - "request entity too large error" in email service | Shambu | Shambu | 0.2 of 19.0d (2h of 152h) | 1 | To Do |
| [HIEV-7615](https://elocity.atlassian.net/browse/HIEV-7615) | Sub-task | August 2026 sprint retrospective (Jira actuals + Teams scrum attendance) | Sahil Siddiqui | — | 0.2 of 16.0d (2h of 128h) | 0 | To Do |
| [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540) | Bug | Staging / Utility Tariff / Reports / Revenue vs Energy Cost chart loses left Y-axis labels and horizontal grid lines after zooming | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.2 of 18.0d (2h of 144h) | 7 | Done |
| [HIEV-7549](https://elocity.atlassian.net/browse/HIEV-7549) | Bug | Staging / Load management / Scheduled Charging / Add New Schedule retains validation error from edited schedule with identical From and To time | Nagaraju, Surya | Surya | 0.2 of 19.0d (2h of 152h) | 2 | Ready for Testing |
| [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558) | Bug | Staging / Utility Tariff / Reports / Revenue vs Energy Cost chart does not match design and Energy Cost disappears after zooming out | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.2 of 19.0d (2h of 152h) | 8 | Done |
| [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226) | Bug | STG/ Portal/ Hiev Canada/ Corporate >> Charging Session >> Refund button is visible even though the charging cost is displaying 0.00 | Dharshini, Rashmi, Sahil Siddiqui | Dharshini, Rashmi, Sahil Siddiqui | 0.2 of 16.0d (2h of 128h) | 4 | Done |
| [HIEV-7381](https://elocity.atlassian.net/browse/HIEV-7381) | Task | Guest Charging bug fixes | Sudeep | Sudeep | 0.2 of 19.0d (2h of 152h) | 5 | Done |
| [HIEV-7476](https://elocity.atlassian.net/browse/HIEV-7476) | Bug | Staging / Android / Reservation cards(Upcoming / Past ) do not display connector icons along with connector information | Dhanush, Nagaraju, Rashmi | Dhanush, Rashmi | 0.2 of 18.0d (2h of 144h) | 2 | Done |
| [HIEV-7488](https://elocity.atlassian.net/browse/HIEV-7488) | Bug | Staging / CPMS / Reporting / Multiple exports contain additional invalid rows irrespective of selected date range | Nagaraju, Shambu | Nagaraju, Sahil Kumar, Shambu | 0.2 of 19.0d (2h of 152h) | 3 | Done |
| [HIEV-7479](https://elocity.atlassian.net/browse/HIEV-7479) | Bug | Staging / HIEV Canada / Android / Home / Map is not rendered after fresh app installation and login | Dhanush, Nagaraju, Rashmi | Dhanush, Rashmi | 0.2 of 18.0d (2h of 144h) | 2 | Done |
| [HIEV-7501](https://elocity.atlassian.net/browse/HIEV-7501) | Bug | Staging / Load Management / Analytics tab fails to load for Load Group with active transaction | Nagaraju, Surya | Surya | 0.2 of 19.0d (2h of 152h) | 1 | Ready for Testing |
| [HIEV-7504](https://elocity.atlassian.net/browse/HIEV-7504) | Bug | Staging / Load Management / Opening Load Group Overview consistently displays “Something went wrong” after connector details load | Nagaraju, Surya | Surya | 0.2 of 20.0d (2h of 160h) | 1 | Done |
| [HIEV-7529](https://elocity.atlassian.net/browse/HIEV-7529) | Bug | Staging / Load Management / Manual Rebalance does not resolve Load Group deviation for a single connector | Nagaraju, Sahil Kumar | Nagaraju, Sahil Kumar | 0.2 of 20.0d (2h of 160h) | 4 | Done |
| [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534) | Bug | Staging / CPMS / Utility Tariff / Edit / Tiered tariff defaults to TOU instead of displaying saved Tiered configuration | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.2 of 18.0d (2h of 144h) | 8 | Done |
| [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342) | Bug | Stage / Portal / GHG reporting / "Greenhouse Gas Used" data bars is not rendered while "Cumulative" data is displayed | Dharshini, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.2 of 18.0d (2h of 144h) | 7 | Done |
| [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538) | Bug | Staging / Utility Tariff / Reports / Energy Cost chart displays inconsistent Y-axis spacing after zooming | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.2 of 18.0d (2h of 144h) | 8 | Done |
| [HIEV-7565](https://elocity.atlassian.net/browse/HIEV-7565) | Suggestion | Staging / Load Management / Hide Unstable Sessions and Variance Events columns from Load Summary and Export | Nagaraju, Surya | Surya | 0.2 of 19.0d (2h of 152h) | 1 | Ready for Testing |
| [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166) | Bug | Stage / Portal / Reservation>Successfully add a reservation for the present day>Update the date range to ‘Today’> 0 results are reflected in the data grid even though one reservation has just been added  | Dharshini, Nagaraju, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.2 of 18.0d (2h of 144h) | 5 | Done |
| [HIEV-7204](https://elocity.atlassian.net/browse/HIEV-7204) | Bug | Stage / Portal / Overall >Select ‘Today’> None of the sections reflect any data. It’s all 0 even though several sessions have been completed today > Data until yesterday is visible on Overall > Today button and calendar option to be removed | Rashmi, Sahil Siddiqui, Surya | Rashmi, Sahil Siddiqui | 0.2 of 16.0d (2h of 128h) | 2 | Done |
| [HIEV-7312](https://elocity.atlassian.net/browse/HIEV-7312) | Bug | Portal / Stage / Station Management / Maintenance slot is deleted after editing and saving without changes | Surya | Surya | 0.2 of 19.0d (2h of 152h) | 1 | Ready for Testing |
| [HIEV-7407](https://elocity.atlassian.net/browse/HIEV-7407) | Sub-task | Mobile App Pipeline Failing Fix | Sahil Siddiqui | Sahil Siddiqui | 0.2 of 16.0d (2h of 128h) | 1 | Done |
| [HIEV-7483](https://elocity.atlassian.net/browse/HIEV-7483) | Task | Movem session payment reprocessing | Sudeep | Sudeep | 0.2 of 19.0d (2h of 152h) | 1 | Done |
| [HIEV-7494](https://elocity.atlassian.net/browse/HIEV-7494) | Task | Employee ID Support – Corporate Employees | Nagaraju | Nagaraju | 0.2 of 19.0d (2h of 152h) | 1 | In Progress |
| [HIEV-7528](https://elocity.atlassian.net/browse/HIEV-7528) | Bug | Staging / Load Management / Overview / Load Usage indicator remains yellow even when load is in Safe Zone | Nagaraju, Surya | Surya | 0.2 of 19.0d (2h of 152h) | 2 | Ready for Testing |
| [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377) | Bug | Staging / Hiev Canada / Android / Reservation / Join Queue screen displays incorrect connector availability after navigating back from the queue flow | Dhanush, Nagaraju | Dhanush, Nagaraju, Sahil Siddiqui | 0.2 of 18.0d (1h of 144h) | 7 | Done |
| [HIEV-7562](https://elocity.atlassian.net/browse/HIEV-7562) | Bug | Staging / Load Management / Deleting a Load Group does not redirect user to Load Group List | Nagaraju, Surya | Surya | 0.2 of 19.0d (1h of 152h) | 1 | Ready for Testing |
| [HIEV-7376](https://elocity.atlassian.net/browse/HIEV-7376) | Bug | Android / Staging / HIEV Canada / Infinite loading displayed after selecting a connector while making a reservation | Dhanush, Nagaraju | Dhanush, Nagaraju | 0.2 of 18.0d (1h of 144h) | 3 | Done |
| [HIEV-7474](https://elocity.atlassian.net/browse/HIEV-7474) | Bug | Staging / Android / Improve readability of date and time displayed in Reservation cards | Dhanush, Nagaraju, Rashmi | Dhanush, Rashmi, Sahil Siddiqui | 0.2 of 18.0d (1h of 144h) | 4 | Done |
| [HIEV-7502](https://elocity.atlassian.net/browse/HIEV-7502) | Bug | STG/ Hiev Canada/ Portal/ Assets-> Firmware Job>>Firmware update job remains In Progress indefinitely. | Rashmi, Shambu | Rashmi, Sahil Kumar, Shambu | 0.2 of 19.0d (1h of 152h) | 5 | Done |
| [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090) | Bug | UAT/ Alfanar/ Web/ Dashboard>> Alerts and Notification -Apply button remains disabled after selecting "Last Year" filter in ALerts and Notification tab  | Rashmi, Sahil Siddiqui | Rashmi, Sahil Siddiqui | 0.1 of 16.0d (1h of 128h) | 6 | Done |
| [HIEV-7466](https://elocity.atlassian.net/browse/HIEV-7466) | Bug | STG / CPMS / Station Management / Advanced Controls collapses after saving changes | Nagaraju, Surya | Nagaraju, Surya | 0.1 of 20.0d (1h of 160h) | 2 | Done |
| [HIEV-7505](https://elocity.atlassian.net/browse/HIEV-7505) | Bug | Staging / Load Management / Clicking a Load Group tile in Grid View does not open Load Group Details | Nagaraju, Surya | Surya | 0.1 of 19.0d (1h of 152h) | 1 | Ready for Testing |
| [HIEV-7552](https://elocity.atlassian.net/browse/HIEV-7552) | Bug | STG/ Portal / Hiev Canada/ Customer->Charging Session >>Clicking Refund shows “Corresponding payment not found for the Entity ID.” | Rashmi, Twisha | Twisha | 0.1 of 15.0d (1h of 120h) | 1 | To Do |
| [HIEV-7561](https://elocity.atlassian.net/browse/HIEV-7561) | Bug | Staging / Customer / Add New Customer / Country Code dropdown shows "No options exist" and blocks customer creation | Nagaraju, Rashmi, Surya | Rashmi, Surya | 0.1 of 20.0d (1h of 160h) | 2 | Done |
| [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275) | Bug | Stage / Portal / There is a mismatch in the number of total connects as seen on the pin details in comparison to the total count of connectors in the data grid | Shambu, Vinay | Shambu, Vinay | 0.1 of 19.0d (1h of 152h) | 5 | To Do |
| [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282) | Bug | STG/ Hiev Canada/ Portal / Abnormal Event>> Event Type -(High Energy Loss between consecutive sessions)>>Inconsistent meter units displayed in High Energy Loss Between Consecutive Sessions event description | Rashmi, Shambu, Vinay | Rashmi, Shambu, Vinay | 0.1 of 19.0d (1h of 152h) | 10 | Done |
| [HIEV-7493](https://elocity.atlassian.net/browse/HIEV-7493) | Bug | Staging / CPMS / Corporate / Employees / Saving employee with excessive long Employee ID causes application to enter unrecoverable error state | Nagaraju, Sudeep, Twisha | Sudeep, Twisha | 0.1 of 19.0d (1h of 152h) | 2 | In Review |
| [HIEV-7527](https://elocity.atlassian.net/browse/HIEV-7527) | Bug | Staging / Load Management / Browser refresh redirects from Load Group details to Load Group list | Nagaraju, Surya | Nagaraju, Surya | 0.1 of 20.0d (1h of 160h) | 2 | Done |
| [HIEV-7559](https://elocity.atlassian.net/browse/HIEV-7559) | Bug | STG/ Android/ Hiev Canada/ Wallet>>Unable to add money in wallet "PaymentIntent Client Secret Mismatch" | Dhanush, Rashmi, Shambu | Dhanush, Rashmi, Shambu | 0.1 of 19.0d (1h of 152h) | 3 | Done |
| [HIEV-6885](https://elocity.atlassian.net/browse/HIEV-6885) | Bug | Canada Prod - Periodically logging out issues | Manjunath | — | 0.1 of 16.0d (1h of 128h) | 0 | To Do |
| [HIEV-7240](https://elocity.atlassian.net/browse/HIEV-7240) | Bug | UAT / Hiev Canada / Android / Queue / Unable to create a new queue reservation despite another valid time slot being available | Twisha | Dhanush, Nagaraju, Twisha | 0.1 of 18.0d (1h of 144h) | 3 | Done |
| [HIEV-7279](https://elocity.atlassian.net/browse/HIEV-7279) | Bug | Guest Charging | Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.1 of 18.0d (1h of 144h) | 5 | Done |
| [HIEV-7288](https://elocity.atlassian.net/browse/HIEV-7288) | Bug | UAT / Guest Charging / Android Chrome / Station Details / Multiple swipe gestures are required to vertically scroll the Station Details page | Dharshini, Nagaraju | Dharshini, Nagaraju | 0.1 of 19.0d (1h of 152h) | 4 | Done |
| [HIEV-7313](https://elocity.atlassian.net/browse/HIEV-7313) | Bug | Stage / Portal / My profile > Success pop-up and progress bar is missing and button label gets updated which is incorrect | Dharshini, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.1 of 18.0d (1h of 144h) | 5 | Done |
| [HIEV-7319](https://elocity.atlassian.net/browse/HIEV-7319) | Bug | Portal / Stage / Station Management / Ratio Duration field allows text input in non-editable area | Surya | Surya | 0.1 of 19.0d (1h of 152h) | 1 | Ready for Testing |
| [HIEV-7339](https://elocity.atlassian.net/browse/HIEV-7339) | Bug | Staging / Android / Hiev Canada / Empty gaps displayed between facility icons on the Location Details page | Dhanush | Dhanush, Nagaraju | 0.1 of 18.0d (1h of 144h) | 3 | Done |
| [HIEV-7384](https://elocity.atlassian.net/browse/HIEV-7384) | Sub-task | QA Validation – Reservations / Default Date Range for User Without Location Permissions | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7387](https://elocity.atlassian.net/browse/HIEV-7387) | Sub-task | QA Validation – Location Tariff Deletion Synchronization (Portal & Mobile App) | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7432](https://elocity.atlassian.net/browse/HIEV-7432) | Task | INFRA / Pipeline Build Changes  | Priyanshu | Priyanshu | 0.1 of 20.0d (1h of 160h) | 1 | Done |
| [HIEV-7473](https://elocity.atlassian.net/browse/HIEV-7473) | Sub-task | Deployment Doc and api gateway Doc | Srikant | Srikant | 0.1 of 17.0d (1h of 136h) | 1 | Done |
| [HIEV-7489](https://elocity.atlassian.net/browse/HIEV-7489) | Bug | Staging / CPMS / Portal / Reporting / Peak Hours report does not provide an Export option | Nagaraju, Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.1 of 16.0d (1h of 128h) | 2 | Done |
| [HIEV-7513](https://elocity.atlassian.net/browse/HIEV-7513) | Bug | STG/ Portal / Hiev Canada / Corporate >> Corporate Code accepts landline number despite mobile-only requirement | Sahil Siddiqui | Rashmi, Sahil Siddiqui | 0.1 of 16.0d (1h of 128h) | 2 | Done |
| [HIEV-7517](https://elocity.atlassian.net/browse/HIEV-7517) | Bug | UAT / Mobile / Guest Charging / 404 error displayed after submitting payment details while starting a charging session | Nagaraju, Sudeep | Nagaraju, Sudeep | 0.1 of 19.0d (1h of 152h) | 2 | Done |
| [HIEV-7519](https://elocity.atlassian.net/browse/HIEV-7519) | Bug | Load Usage does not reset to 0A after charging session ends | Surya | Surya | 0.1 of 19.0d (1h of 152h) | 1 | Ready for Testing |
| [HIEV-7547](https://elocity.atlassian.net/browse/HIEV-7547) | Sub-task | Load Management – Manual Rebalance Single Connector Validation | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7551](https://elocity.atlassian.net/browse/HIEV-7551) | Sub-task | Staging / Load Management / Validate Load Group Edit/Update Functionality | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7569](https://elocity.atlassian.net/browse/HIEV-7569) | Sub-task | Staging / Load Management / Validate Load Group behavior after station decommissioning | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7571](https://elocity.atlassian.net/browse/HIEV-7571) | Sub-task | Staging / Load Management / Validate Load Group Creation/Update with Station Selection | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7577](https://elocity.atlassian.net/browse/HIEV-7577) | Sub-task | QA Validation – Session Management / 401 Unauthorized Response & Logout Handling | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7586](https://elocity.atlassian.net/browse/HIEV-7586) | Task | INFRA / Adani prod ssl cert  | Priyanshu | Priyanshu | 0.1 of 20.0d (1h of 160h) | 1 | Done |
| [HIEV-7592](https://elocity.atlassian.net/browse/HIEV-7592) | Task | INFRA / S3 Static site issue | Priyanshu | Priyanshu | 0.1 of 20.0d (1h of 160h) | 1 | Done |
| [HIEV-7607](https://elocity.atlassian.net/browse/HIEV-7607) | Sub-task | Code review MR !800 — Load Management connector icon + unit test fix | Sahil Siddiqui | Sahil Siddiqui | 0.1 of 16.0d (1h of 128h) | 1 | To Do |
| [HIEV-7420](https://elocity.atlassian.net/browse/HIEV-7420) | Bug | STG/ Hiev Canada/ Portal / Maintenance Slot Displays Only Start Date Instead of Full Date Range | Rashmi, Sahil Siddiqui, Twisha | Sahil Siddiqui, Twisha | 0.1 of 15.0d (1h of 120h) | 4 | Ready for Testing |
| [HIEV-7510](https://elocity.atlassian.net/browse/HIEV-7510) | Bug | Staging / Scheduled Charging / Group Name field has no length validation and causes inconsistent API behavior | Nagaraju, Surya | Surya | 0.1 of 19.0d (1h of 152h) | 1 | Ready for Testing |
| [HIEV-7516](https://elocity.atlassian.net/browse/HIEV-7516) | Bug | UAT / Web / Location Management / Prepaid location fields and Country/Time Zone options are not loading | Nagaraju, Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.1 of 16.0d (1h of 128h) | 2 | Done |
| [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062) | Bug | Canada Prod / Portal / Business > Click on ‘Export Business’ button > Review the downloaded report  > ‘CIN’ field is present here which is incorrect  >> ‘CIN’ field has to be removed  | Dharshini, Sahil Siddiqui | Dharshini, Nagaraju, Sahil Siddiqui | 0.1 of 19.0d (1h of 152h) | 8 | Done |
| [HIEV-7234](https://elocity.atlassian.net/browse/HIEV-7234) | Bug | STG/ Hiev Canada/Portal/Assets-> Diagnostic >> Job Status dropdown displays “Dispatch” instead of “Dispatching” | Rashmi, Sahil Siddiqui | Rashmi, Sahil Siddiqui | 0.1 of 18.0d (1h of 144h) | 3 | Done |
| [HIEV-7296](https://elocity.atlassian.net/browse/HIEV-7296) | Bug | STG/ Hiev Canada/ Portal/Assets-> Firmware Management->Export button not present in Firmware Management module. | Rashmi, Sahil Siddiqui | Rashmi, Sahil Siddiqui | 0.1 of 18.0d (1h of 144h) | 3 | Done |
| [HIEV-7310](https://elocity.atlassian.net/browse/HIEV-7310) | Bug | Portal / Station Management / Active maintenance status label is not displayed during maintenance window | Surya | Surya | 0.1 of 19.0d (1h of 152h) | 1 | Ready for Testing |
| [HIEV-7316](https://elocity.atlassian.net/browse/HIEV-7316) | Bug | Portal / Stage / Station Management / Connector Type dropdown text overlaps for actions requiring connector type selection | Surya | Surya | 0.1 of 19.0d (1h of 152h) | 1 | Ready for Testing |
| [HIEV-7331](https://elocity.atlassian.net/browse/HIEV-7331) | Task | Guest Charging / Guest charging Dropdown filter in Charging session grid | Surya | Nagaraju, Surya | 0.1 of 20.0d (1h of 160h) | 2 | Done |
| [HIEV-7383](https://elocity.atlassian.net/browse/HIEV-7383) | Sub-task | Task Name: QA Validation – Customer Details / E-Wallet / Default API Response Sorting | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7386](https://elocity.atlassian.net/browse/HIEV-7386) | Sub-task | QA Validation – Tariff Profile Launch (currency_code HTTP 500 Fix) | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7397](https://elocity.atlassian.net/browse/HIEV-7397) | Sub-task | QA Validation – Reservation / Join Queue Connector Availability Timeline | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7398](https://elocity.atlassian.net/browse/HIEV-7398) | Sub-task | QA Validation – Reservation / Connector Selection Infinite Loading | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7405](https://elocity.atlassian.net/browse/HIEV-7405) | Task | QA Analysis – Load Management PRD Review | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7413](https://elocity.atlassian.net/browse/HIEV-7413) | Bug | STG/ Portal/ Hiev Canada/ Station Management-> Maintenance - Maintenance Slot Remove (-) Icon is Misaligned in Custom Slots Section | Rashmi, Surya | Surya | 0.1 of 15.0d (1h of 120h) | 1 | Testing |
| [HIEV-7419](https://elocity.atlassian.net/browse/HIEV-7419) | Sub-task | QA Validation – Guest Charging / Connector State Validation | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7423](https://elocity.atlassian.net/browse/HIEV-7423) | Bug | STG / Portal / Business / Export Business button becomes non-functional in reduced viewport | Nagaraju, Surya | Surya | 0.1 of 19.0d (1h of 152h) | 1 | Ready for Testing |
| [HIEV-7435](https://elocity.atlassian.net/browse/HIEV-7435) | Sub-task | QA Validation – Guest Charging / Offline/Unavailable Charger Validation | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7437](https://elocity.atlassian.net/browse/HIEV-7437) | Sub-task | QA Validation – Guest Charging / Empty Response After Simulator Disconnect | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7454](https://elocity.atlassian.net/browse/HIEV-7454) | Sub-task | QA Validation – Guest Charging / Multi-Connector Mapping | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7478](https://elocity.atlassian.net/browse/HIEV-7478) | Sub-task | QA Validation – In-App Campaign / maxDisplayCount Enforcement | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7499](https://elocity.atlassian.net/browse/HIEV-7499) | Bug | STG/ Portal / Hiev Canada/ Job Status is displayed as InProgress while the station status is Pending | Rashmi, Shambu | Rashmi, Sahil Kumar, Shambu | 0.1 of 19.0d (1h of 152h) | 5 | Done |
| [HIEV-7524](https://elocity.atlassian.net/browse/HIEV-7524) | Sub-task | QA Validation – Guest Charging / Non-Available Connector States | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7543](https://elocity.atlassian.net/browse/HIEV-7543) | Sub-task | Validate Reporting Export Data | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7570](https://elocity.atlassian.net/browse/HIEV-7570) | Sub-task | QA Validation – Reservation / Reserved Time Slot Availability | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7572](https://elocity.atlassian.net/browse/HIEV-7572) | Sub-task | QA Validation – EVSE Models / Model Creation & Search | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7578](https://elocity.atlassian.net/browse/HIEV-7578) | Observation | Staging / Load Management / Previously selected stations are cleared when adding another location while editing Load Group | Nagaraju, Surya | Sahil Siddiqui, Surya | 0.1 of 19.5d (1h of 156h) | 2 | To Do |
| [HIEV-7583](https://elocity.atlassian.net/browse/HIEV-7583) | Sub-task | QA Validation – Queue Reservation / Multiple Available Time Slots | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7585](https://elocity.atlassian.net/browse/HIEV-7585) | Bug | Staging  / Load Management / Round Robin / Extremely large pasted Time Interval is saved as null | Nagaraju, Surya | Surya | 0.1 of 19.0d (1h of 152h) | 1 | Ready for Testing |
| [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133) | Bug | Stage / Portal / Low Priority issues - 4 | Rashmi, Sahil Siddiqui, Surya | Rashmi, Sahil Siddiqui, Surya | 0.1 of 20.0d (1h of 160h) | 5 | Done |
| [HIEV-7303](https://elocity.atlassian.net/browse/HIEV-7303) | Bug | Stage / Portal / My Profile > Verify that only one business is reflected in the ‘Business’ filter > Click on ‘Export Logs’ button > Download is successfully completed >Time stamp is in UTC format while the data grid shows the local time (IST) | Twisha | Twisha | 0.1 of 19.0d (1h of 152h) | 1 | To Do |
| [HIEV-7382](https://elocity.atlassian.net/browse/HIEV-7382) | Sub-task | QA Validation - Reset Password Email Validity Time Zone Fix | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7402](https://elocity.atlassian.net/browse/HIEV-7402) | Sub-task | QA Validation – Business Export / CIN Column Removal | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 2 | Done |
| [HIEV-7408](https://elocity.atlassian.net/browse/HIEV-7408) | Sub-task | QA Validation – GHG Reporting / Y-Axis Alignment After Zoom | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7415](https://elocity.atlassian.net/browse/HIEV-7415) | Sub-task | QA Validation – Guest Charging / Charging Duration Time Format | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7438](https://elocity.atlassian.net/browse/HIEV-7438) | Sub-task | QA Validation – Guest Charging / Real-Time Charging Session Updates | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7443](https://elocity.atlassian.net/browse/HIEV-7443) | Sub-task | QA Validation – Reporting / Location Filter & Selected CPID Count | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7465](https://elocity.atlassian.net/browse/HIEV-7465) | Sub-task | QA Validation – Station Details / Advanced Controls UI Issues | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7518](https://elocity.atlassian.net/browse/HIEV-7518) | Bug | Staging / Portal / Load Management / Grammar and capitalisation issue in EVSE duplicate assignment error message | Nagaraju, Surya | Surya | 0.1 of 19.0d (1h of 152h) | 1 | In Progress |
| [HIEV-7568](https://elocity.atlassian.net/browse/HIEV-7568) | Sub-task | QA Validation – Session Management / Invalidated Session Handling | Nagaraju | Nagaraju | 0.1 of 19.0d (1h of 152h) | 1 | Done |
| [HIEV-7299](https://elocity.atlassian.net/browse/HIEV-7299) | Bug | STG/ Portal/ HIev Canada/ Dashboard-> Abnormal Event>>Description error message is not details for Connector not found | Rashmi, Vinay | Rashmi, Vinay | 0.1 of 19.0d (1h of 152h) | 3 | Done |
| [HIEV-7550](https://elocity.atlassian.net/browse/HIEV-7550) | Bug | UAT / Portal/ Hiev Canada / Guest Charging >>After the scanning the QR code  Error message is not user Friendly when a charging session is already active. | Dharshini, Rashmi | Dharshini, Rashmi | 0.1 of 18.0d (1h of 144h) | 2 | Done |
| [HIEV-7018](https://elocity.atlassian.net/browse/HIEV-7018) | Bug | Canada Prod/Portal/⁠Station Overview > Using the "Charger" filter, select ONE charger>Corresponding results are reflected BUT the map does not reflect the location pin and continues to show all the pins that were present before the filter was applied | Surya | Nagaraju, Surya | 0.1 of 20.0d (0h of 160h) | 2 | Done |
| [HIEV-7202](https://elocity.atlassian.net/browse/HIEV-7202) | Bug | STG/ Hiev Canada/ Web/ Station Management-> Incorrect confirmation message displayed when changing Installation State from Commission to Decommission for a blocked station | Rashmi, Sahil Siddiqui | Rashmi, Sahil Siddiqui | 0.1 of 16.0d (0h of 128h) | 3 | Done |
| [HIEV-7314](https://elocity.atlassian.net/browse/HIEV-7314) | Bug | Portal / Stage / Station Management / 'Please add at least one slot' validation is displayed immediately after selecting Custom Slots | Surya | Surya | 0.1 of 19.0d (0h of 152h) | 1 | Ready for Testing |
| [HIEV-7315](https://elocity.atlassian.net/browse/HIEV-7315) | Bug | Stage / Portal / Refresh action is incorrect and is resetting filters applied instead | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.1 of 18.0d (0h of 144h) | 4 | Done |
| [HIEV-7317](https://elocity.atlassian.net/browse/HIEV-7317) | Bug | Stage / Portal / On updating and saving the user email address, user gets logged out successfully >>Email address should not editable  | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.1 of 18.0d (0h of 144h) | 4 | Done |
| [HIEV-7320](https://elocity.atlassian.net/browse/HIEV-7320) | Bug | Stage / Portal / My Profile > Low priority issues  | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.1 of 18.0d (0h of 144h) | 4 | Done |
| [HIEV-7321](https://elocity.atlassian.net/browse/HIEV-7321) | Bug | UAT / Portal / Station Management / Minimum Balance field lacks input length validation and allows excessive numeric input | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.1 of 20.0d (0h of 160h) | 5 | Done |
| [HIEV-7328](https://elocity.atlassian.net/browse/HIEV-7328) | Bug | Stage / Portal / Report Subscription>Create a new email alert > Click on 'X’ icon on the top right corner of the pop-up> Instead of closing the pop-up, the screen reverts back to the create a new email alert or to review the existing alert details screen | Rashmi, Sahil Siddiqui | Rashmi, Sahil Siddiqui | 0.1 of 16.0d (0h of 128h) | 2 | Done |
| [HIEV-7400](https://elocity.atlassian.net/browse/HIEV-7400) | Sub-task | QA Validation – Location Details / Facilities Grid Layout | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7409](https://elocity.atlassian.net/browse/HIEV-7409) | Sub-task | QA Validation – GHG Reporting / Y-Axis Synchronisation After Zoom In | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7410](https://elocity.atlassian.net/browse/HIEV-7410) | Sub-task | QA Validation – GHG Reporting / Greenhouse Gas Used Data Bars Rendering | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7412](https://elocity.atlassian.net/browse/HIEV-7412) | Sub-task | QA Validation – GHG Reporting / Y-Axis Interval and Grid Line Spacing After Zoom In | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7417](https://elocity.atlassian.net/browse/HIEV-7417) | Sub-task | QA Validation – Guest Charging / Duplicate Error Message Presentation | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7418](https://elocity.atlassian.net/browse/HIEV-7418) | Sub-task | QA Validation – Guest Charging / Payment Processing Loader UI | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7431](https://elocity.atlassian.net/browse/HIEV-7431) | Sub-task | QA Validation – My Profile / Low Priority UI Improvements | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7433](https://elocity.atlassian.net/browse/HIEV-7433) | Sub-task | QA Validation – Guest Charging / Charging Session Loading Indicator UI | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7434](https://elocity.atlassian.net/browse/HIEV-7434) | Sub-task | QA Validation – Guest Charging / Session Summary Loading Indicator | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7444](https://elocity.atlassian.net/browse/HIEV-7444) | Sub-task | QA Validation – Location Management / Timing Navigation Button Visibility | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7452](https://elocity.atlassian.net/browse/HIEV-7452) | Sub-task | QA Validation – Station Management / Station Name Character Limit & UI Display | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7456](https://elocity.atlassian.net/browse/HIEV-7456) | Bug | Staging / HIEV Canada / Android / In-App Campaign / Eligible campaigns are not displayed after login | Nagaraju | — | 0.1 of 18.0d (0h of 144h) | 0 | To Do |
| [HIEV-7459](https://elocity.atlassian.net/browse/HIEV-7459) | Sub-task | QA Validation – Reservations / New Reservation Save Flow | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7461](https://elocity.atlassian.net/browse/HIEV-7461) | Sub-task | QA Validation – My Profile / Refresh Filter Persistence | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7462](https://elocity.atlassian.net/browse/HIEV-7462) | Sub-task | QA Validation – My Profile / Export Logs UI & Download Feedback | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7463](https://elocity.atlassian.net/browse/HIEV-7463) | Sub-task | QA Validation – EVSE Models / Validation Message Alignment | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7468](https://elocity.atlassian.net/browse/HIEV-7468) | Bug | Staging / Load Management / Load Group Creation / Save button triggers infinite loading with no API request | Sahil Siddiqui | Nagaraju, Sahil Kumar, Sahil Siddiqui | 0.1 of 16.0d (0h of 128h) | 5 | Done |
| [HIEV-7469](https://elocity.atlassian.net/browse/HIEV-7469) | Sub-task | QA Validation – Reservations / Today Date Range & Future Reservation Visibility | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7480](https://elocity.atlassian.net/browse/HIEV-7480) | Sub-task | QA Validation – Bulk Operations / Get Configuration Custom Keys | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7481](https://elocity.atlassian.net/browse/HIEV-7481) | Sub-task | QA Validation – Bulk Operations / Get Configuration CPID Payload | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7487](https://elocity.atlassian.net/browse/HIEV-7487) | Bug | STG/ Hiev Canada/ Portal/ Abnormal Event-> When the station is under maintenance >> Maintenance message displays a non user friendly timestamp.  | Shambu | Rashmi, Shambu | 0.1 of 19.0d (0h of 152h) | 2 | In Progress |
| [HIEV-7509](https://elocity.atlassian.net/browse/HIEV-7509) | Bug | Staging / CPMS / Scheduled Charging / Cancel and Save buttons have inconsistent dimensions | Nagaraju, Surya | Surya | 0.1 of 19.0d (0h of 152h) | 1 | Ready for Testing |
| [HIEV-7512](https://elocity.atlassian.net/browse/HIEV-7512) | Bug | Staging / Charging Sessions / Guest Charging filter width is inconsistent with other filters | Nagaraju, Surya | Surya | 0.1 of 19.0d (0h of 152h) | 1 | Ready for Testing |
| [HIEV-7520](https://elocity.atlassian.net/browse/HIEV-7520) | Sub-task | Staging / Load Management / Validate Create Load Group Save Flow Fix | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7521](https://elocity.atlassian.net/browse/HIEV-7521) | Sub-task | QA Validation / Guest Charging / Stop Charging Retry Handling and Button Text | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7523](https://elocity.atlassian.net/browse/HIEV-7523) | Sub-task | QA Validation – Guest Charging / 404 Error After Payment Submission | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7525](https://elocity.atlassian.net/browse/HIEV-7525) | Sub-task | UAT / QA Validation / Re-test Location and Station Configuration Issues | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7567](https://elocity.atlassian.net/browse/HIEV-7567) | Sub-task | QA Validation – Guest Charging / Charging Session Grid Filter | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7590](https://elocity.atlassian.net/browse/HIEV-7590) | Bug | Wrong currency shown for Oshawa Power (business_id 1256) | Shambu | Shambu | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7596](https://elocity.atlassian.net/browse/HIEV-7596) | Sub-task | Utility Tariff – Validate Revenue vs Energy Cost Chart Zoom & Rendering | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7598](https://elocity.atlassian.net/browse/HIEV-7598) | Sub-task | Utility Tariff – Validate Revenue vs Energy Cost Chart Design & Zoom-Out Behavior | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7447](https://elocity.atlassian.net/browse/HIEV-7447) | Sub-task | QA Validation – Location Management / Character Limit Validation | Nagaraju | Nagaraju | 0.1 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7514](https://elocity.atlassian.net/browse/HIEV-7514) | Bug | STG/ Portal / Hiev Canada/ Location Management>> Add Location >>Landline number is accepted in the Location Contact Number field | Rashmi, Sahil Siddiqui | Rashmi, Sahil Siddiqui | 0.1 of 16.0d (0h of 128h) | 2 | Done |
| [HIEV-7515](https://elocity.atlassian.net/browse/HIEV-7515) | Bug | STG/ Portal / Hiev Canada /Administration -> User Management>> Landline number is accepted  in Add New User Contact field  | Rashmi, Sahil Siddiqui | Rashmi, Sahil Siddiqui | 0.1 of 16.0d (0h of 128h) | 2 | Done |
| [HIEV-7165](https://elocity.atlassian.net/browse/HIEV-7165) | Bug | Stage / Portal /Reservation> User is unable to make a reservation for a customer that has previously made two reservation in the last 6 months > Getting the error - User has already reached max reservation limit | Nagaraju | Nagaraju, Twisha | 0.0 of 18.0d (0h of 144h) | 2 | Done |
| [HIEV-7411](https://elocity.atlassian.net/browse/HIEV-7411) | Sub-task | QA Validation – Reporting / Greenhouse Gas Report Title Update | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7421](https://elocity.atlassian.net/browse/HIEV-7421) | Sub-task | QA Validation – Guest Charging / Multiple Connector Horizontal Scrolling | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7448](https://elocity.atlassian.net/browse/HIEV-7448) | Sub-task | QA Validation – User Management / User Details Action Button Styling | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7451](https://elocity.atlassian.net/browse/HIEV-7451) | Sub-task | QA Validation – Tariff Management / Validation Message Clearance | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7453](https://elocity.atlassian.net/browse/HIEV-7453) | Sub-task | QA Validation – Station Management / Minimum Balance Input Validation | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7460](https://elocity.atlassian.net/browse/HIEV-7460) | Sub-task | QA Validation – My Profile / Email Address Edit Restriction | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7464](https://elocity.atlassian.net/browse/HIEV-7464) | Bug | Staging / CPMS Portal / Station Management / Long station name causes table layout overflow after navigating between management screens | Nagaraju | — | 0.0 of 20.0d (0h of 160h) | 0 | To Do |
| [HIEV-7467](https://elocity.atlassian.net/browse/HIEV-7467) | Sub-task | QA Validation – Station Overview Charger Filter Map Pin | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7594](https://elocity.atlassian.net/browse/HIEV-7594) | Sub-task | Utility Tariff – Tiered Tariff Edit/View Validation | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7595](https://elocity.atlassian.net/browse/HIEV-7595) | Sub-task | Utility Tariff – Validate Energy Cost Chart Zoom & Y-Axis Spacing | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | To Do |
| [HIEV-6380](https://elocity.atlassian.net/browse/HIEV-6380) | Epic | Mobile App / App store rating  after session - Check New Flows | Nagaraju | Nagaraju | 0.0 of 18.0d (0h of 144h) | 1 | Done |
| [HIEV-6446](https://elocity.atlassian.net/browse/HIEV-6446) | Bug | Stage / Portal / Station Management - Low Priority Issues 1 | Surya | Nagaraju, Surya | 0.0 of 20.0d (0h of 160h) | 3 | Done |
| [HIEV-6875](https://elocity.atlassian.net/browse/HIEV-6875) | Bug | UAT/ Hiev Canada / Android/Prepaid Location >> Parking charges is not applied in tariff > Green Strip is showing with message “Your Ev was charged successfully”  >>After clicking on arrow >> Navigate to Energised to GO! Screen. | Rashmi | Rashmi | 0.0 of 18.0d (0h of 144h) | 1 | Done |
| [HIEV-6894](https://elocity.atlassian.net/browse/HIEV-6894) | Bug | MOVEM / Prod/ Add new location > Search for a location > Select an option > all the mandatory fields gets auto-populated except for 'City' field | Rashmi | Rashmi | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7077](https://elocity.atlassian.net/browse/HIEV-7077) | Bug | UAT/ Alfanar/ Android/ Parking Charges Applied to Session but Not Reflected in Session Details and Invoices | Rashmi | Rashmi | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7094](https://elocity.atlassian.net/browse/HIEV-7094) | Bug | Canada Prod / Portal / ⁠Customer Groups>Go to Customers tab>Click on ‘View RFID'>Side panel with the RFID details is visible>Click on Delete>Pop-up to confirm the delete action is visible>Click on either Cancel or Delete, msg on pop-up shows ‘Undefined’ | Sahil Siddiqui | Rashmi, Sahil Siddiqui | 0.0 of 16.0d (0h of 128h) | 3 | Done |
| [HIEV-7143](https://elocity.atlassian.net/browse/HIEV-7143) | Bug | UAT/ Hiev Canada / Android/Location details>> Reservation >> Reservation Details screen briefly displays “No Location Found” message while data is loading | Rashmi | Rashmi | 0.0 of 18.0d (0h of 144h) | 1 | Done |
| [HIEV-7163](https://elocity.atlassian.net/browse/HIEV-7163) | Bug | UAT/ Hiev Canada / Android/ Reservation>> Filter >>Filter icon not showing red dot after applying filter | Rashmi | Rashmi | 0.0 of 18.0d (0h of 144h) | 1 | Done |
| [HIEV-7207](https://elocity.atlassian.net/browse/HIEV-7207) | Bug | Staging / Portal / Menu > Assets > Add New Location > Timing / Back and Next buttons are cropped when "Customized" timing is selected at 100% browser zoom | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.0 of 20.0d (0h of 160h) | 2 | Done |
| [HIEV-7214](https://elocity.atlassian.net/browse/HIEV-7214) | Bug | Staging / Portal / Session Management / Previous browser gets stuck in "Something went wrong" refresh loop instead of redirecting to Login after session is invalidated | Surya | Nagaraju, Surya | 0.0 of 20.0d (0h of 160h) | 2 | Done |
| [HIEV-7215](https://elocity.atlassian.net/browse/HIEV-7215) | Bug | Staging / Portal / Reservations / "No options exist" dropdown remains visible after losing focus in All Chargers filter | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.0 of 20.0d (0h of 160h) | 2 | Done |
| [HIEV-7218](https://elocity.atlassian.net/browse/HIEV-7218) | Bug | Staging / Portal / Tariff Management > Design New Tariff / Validation message persists after disabling tariff section | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.0 of 20.0d (0h of 160h) | 2 | Done |
| [HIEV-7235](https://elocity.atlassian.net/browse/HIEV-7235) | Bug | Staging / CPMS Portal / Assets > Station Management / Long station names cause UI overflow in the details page and incorrect character limit handling | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.0 of 20.0d (0h of 160h) | 2 | Done |
| [HIEV-7236](https://elocity.atlassian.net/browse/HIEV-7236) | Bug | Staging / CPMS Portal / User Management / Inconsistent styling of action buttons on User Details page | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.0 of 20.0d (0h of 160h) | 2 | Done |
| [HIEV-7269](https://elocity.atlassian.net/browse/HIEV-7269) | Bug | UAT / Guest Charging / Android Chrome / QR Scan / Error page reloads after displaying "Guest charging is not allowed at this location" for Planned stations | Nagaraju | Nagaraju, Sahil Siddiqui | 0.0 of 18.0d (0h of 144h) | 2 | Done |
| [HIEV-7297](https://elocity.atlassian.net/browse/HIEV-7297) | Bug | STG/ Portal / Hiev Canada/ Dashboard-> Abnormal Event>> Description error message is not detials if Customer not found it is showing only "Customer not found"  | Rashmi | Rashmi, Vinay | 0.0 of 19.0d (0h of 152h) | 2 | Done |
| [HIEV-7302](https://elocity.atlassian.net/browse/HIEV-7302) | Bug | Stage / Portal / My Profile>Click on ‘Export Logs’ button > Download is successfully completed > the downloaded file’s name is “ActivityLogs_tenant_2026-07-27T11_31_59.038Z” >> the downloaded file’s name is to be updated | Rashmi | Rashmi, Sudeep | 0.0 of 19.0d (0h of 152h) | 3 | Done |
| [HIEV-7309](https://elocity.atlassian.net/browse/HIEV-7309) | Bug | STG / Android / Hiev Canada / Tapping clustered station markers on the map does not zoom into the selected area | Nagaraju | Dhanush, Nagaraju | 0.0 of 18.0d (0h of 144h) | 2 | Done |
| [HIEV-7356](https://elocity.atlassian.net/browse/HIEV-7356) | Bug | Stage / Android / HIEV canada / Customer is redirected to "Awaiting Connection" screen instead of Session Summary after completing a charging session initiated via QR code  | Nagaraju | Nagaraju | 0.0 of 18.0d (0h of 144h) | 1 | Done |
| [HIEV-7450](https://elocity.atlassian.net/browse/HIEV-7450) | Sub-task | QA Validation – Reservations / All Chargers Dropdown Focus Behavior | Nagaraju | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7500](https://elocity.atlassian.net/browse/HIEV-7500) | Bug | STG/ Hiev Canada/ Portal/ Assets-> Firmware Management>> File Name Autosuggestion Dropdown Overlaps the Cancel Button | Rashmi | Nagaraju | 0.0 of 15.0d (0h of 120h) | 1 | Done |
| [HIEV-7511](https://elocity.atlassian.net/browse/HIEV-7511) | Bug | Staging / Load Management / Load Group Name does not provide inline validation for 50-character limit | Surya | Surya | 0.0 of 19.0d (0h of 152h) | 1 | Ready for Testing |
| [HIEV-7531](https://elocity.atlassian.net/browse/HIEV-7531) | Bug | STG/ Portal/ Hiev Canada/ Reservation >>Reservation within the maximum duration limit is incorrectly rejected | Rashmi | Rashmi, Twisha | 0.0 of 18.0d (0h of 144h) | 2 | Done |
| [HIEV-7535](https://elocity.atlassian.net/browse/HIEV-7535) | Bug | UAT/ Portal / Hiev Canada / Guest Charging >> Guest Charger QR Code Shows “Invalid QR” Error | Rashmi | Nagaraju | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7544](https://elocity.atlassian.net/browse/HIEV-7544) | Bug | UAT/ Portal/ Hiev Canada/ Guest Charging>> Incorrect charging session data is displayed in charging summary screen . | Rashmi | Dharshini, Sudeep | 0.0 of 19.0d (0h of 152h) | 2 | To Do |
| [HIEV-6315](https://elocity.atlassian.net/browse/HIEV-6315) | Bug | Stage / Portal / User Management > “Resend Activation Link” continues to be present even though  account status is “Active” | Rashmi | Rashmi | 0.0 of 19.0d (0h of 152h) | 1 | Done |
| [HIEV-7095](https://elocity.atlassian.net/browse/HIEV-7095) | Bug | Alfanar UAT / Click on ‘Add New Location’ > Search for an address in the ‘Address Line 1’> Select any option from the drop down >“State/Province” and “TimeZone” field does not get auto-populated > City and Zip code gets populated most of the times | Rashmi | Rashmi, Sudeep | 0.0 of 19.0d (0h of 152h) | 3 | Done |
| [HIEV-7156](https://elocity.atlassian.net/browse/HIEV-7156) | Bug | UAT/ Hiev Canada/ Android/ Reservation>> Click on Join Queue arrow -> Reservation details screen are unavailable | Rashmi | — | 0.0 of 18.0d (0h of 144h) | 0 | Done |
| [HIEV-7209](https://elocity.atlassian.net/browse/HIEV-7209) | Bug | Staging / Portal / Menu > Assets > Location Management > Asset Settings > EVSE Models > Add New EVSE Model / Validation error messages are inconsistently aligned across form fields | Surya | Nagaraju, Surya | 0.0 of 20.0d (0h of 160h) | 2 | Done |
| [HIEV-7232](https://elocity.atlassian.net/browse/HIEV-7232) | Suggestion | Staging / Hiev India / Android / Improve Reservation screen UI/UX for better readability and accessibility | Dhanush | Dhanush, Nagaraju | 0.0 of 19.0d (0h of 152h) | 2 | Done |
| [HIEV-7264](https://elocity.atlassian.net/browse/HIEV-7264) | Bug | Stage / Portal / On occasion, after extended idle periods, we get a pop-up ‘Something Went Wrong.” pop-up. By clicking on 'Refresh Page’ button, the page gets refreshed but the pop-up continues to be present.  User unable to logout either and is stuck.  | Surya | Nagaraju, Surya | 0.0 of 20.0d (0h of 160h) | 2 | Done |
| [HIEV-7576](https://elocity.atlassian.net/browse/HIEV-7576) | Bug | STG/ Android/ Alfanar/ Unable to Log In with Phone Number OTP Login fails due to missing app check token | Rashmi | — | 0.0 of 18.0d (0h of 144h) | 0 | To Do |
| [HIEV-7333](https://elocity.atlassian.net/browse/HIEV-7333) | Bug | CPMS / Stage / Incorrect report title displayed as "Greenhouse Gas Used" in Reporting dashboard | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.0 of 18.0d (0h of 144h) | 4 | Done |
| [HIEV-7335](https://elocity.atlassian.net/browse/HIEV-7335) | Bug | Stage / Portal / GHG reporting / Inconsistent Y-axis intervals and grid line spacing after first zoom in Greenhouse Gas report fullscreen view | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.0 of 18.0d (0h of 144h) | 4 | Done |
| [HIEV-7336](https://elocity.atlassian.net/browse/HIEV-7336) | Bug | Stage / Portal / GHG reporting / Right Y-axis displays fewer values than the left Y-axis, after zooming in Greenhouse Gas report | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.0 of 18.0d (0h of 144h) | 4 | Done |
| [HIEV-7337](https://elocity.atlassian.net/browse/HIEV-7337) | Bug | Stage / Portal / GHG reporting / Top horizontal grid line is missing a corresponding right Y-axis value after zooming out in Greenhouse Gas report fullscreen view | Sahil Siddiqui | Nagaraju, Sahil Siddiqui | 0.0 of 18.0d (0h of 144h) | 4 | Done |

## 2. Estimation accuracy

Same-scope only: **ticket** = August days on that Jira ticket ÷ sprint-plan PD. **Person** = August days on *sprint-planned Jira tickets that have a numeric PD* ÷ their sprint-plan PD. Time on plan Jira tickets with NA/open estimates, and mid-sprint time, is not estimation error. Values above 1.0 mean over estimate. NA / missing estimates are excluded.

| Person | Plan (PD) | Actual on planned Jira tickets | Logged of available | Accuracy |
|---|---:|---:|---:|---:|
| Deepak | 15.0 | 0.2d (2h) | 20.8 of 19.5d (166h of 156h) | 0.02 |
| Priyanshu | 20.0 | 12.5d (100h) | 20.1 of 20.0d (161h of 160h) | 0.62 |
| Dhanush | 7.0 | 3.0d (24h) | 18.1 of 18.0d (145h of 144h) | 0.43 |
| Marish | 3.0 | 2.8d (22h) | 17.9 of 19.0d (144h of 152h) | 0.94 |
| Tarun | 7.0 | 11.6d (93h) | 17.2 of 20.0d (138h of 160h) | 1.66 |
| Sudeep | 30.0 | 1.9d (15h) | 17.1 of 19.0d (137h of 152h) | 0.06 |
| Sahil Siddiqui | 4.0 | 1.5d (12h) | 15.1 of 16.0d (121h of 128h) | 0.38 |
| Dharshini | 13.0 | 7.1d (56h) | 13.5 of 18.0d (108h of 144h) | 0.54 |
| Twisha | 12.0 | 6.6d (53h) | 13.3 of 18.0d (107h of 144h) | 0.55 |
| Shambu | 15.0 | 4.4d (36h) | 13.1 of 19.0d (105h of 152h) | 0.30 |
| Srikant | 19.0 | 4.0d (32h) | 11.9 of 17.0d (95h of 136h) | 0.21 |
| Surya | 14.0 | 7.8d (62h) | 11.4 of 20.0d (92h of 160h) | 0.56 |
| Manjunath | 4.0 | 0.1d (1h) | 11.1 of 16.0d (88h of 128h) | 0.03 |
| Rushika | 5.0 | 5.0d (40h) | 8.8 of 20.0d (70h of 160h) | 1.00 |
| Vinay | 5.0 | 0.2d (2h) | 6.0 of 19.0d (48h of 152h) | 0.05 |

## 3. Bugs worked in August

Total: **156** distinct HIEV bugs with August worklogs or comments (134 Done/Ready for Testing, 22 still open). 72 of these sit under HIEV-7334. Counts are unique Jira tickets per person who logged time or commented — not assignee at create time.

| Person | Unique bugs worked |
|---|---:|
| Nagaraju | 84 |
| Rashmi | 58 |
| Sahil Siddiqui | 55 |
| Surya | 31 |
| Dharshini | 25 |
| Shambu | 21 |
| Twisha | 19 |
| Vinay | 13 |
| Sudeep | 13 |
| Dhanush | 13 |
| Sahil Kumar | 9 |
| Manjunath | 1 |

| Jira | Summary | Status | Worked by | August hours |
|---|---|---|---|---:|
| [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446) | Staging / HIEV Canada / Android / In-App Campaign / maxDisplayCount is not enforced for Welcome campaign | Done | Dhanush, Nagaraju, Sahil Siddiqui | 1.4d (12h) |
| [HIEV-7172](https://elocity.atlassian.net/browse/HIEV-7172) | Stage / Portal / At times, the previous or existing transaction details are sometimes not reflected in the side panel of station management  | To Do | Shambu | 1.4d (11h) |
| [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503) | Staging / EVSE Model / Created model is not displayed in list/search despite successful creation and duplicate-name validation | Done | Nagaraju, Sahil Siddiqui, Twisha | 1.2d (10h) |
| [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439) | STG/ Hiev Canada/ Portal/ Location Management>>My profile>> Updated Location Not Displayed in Activity Log After Editing Tariff | Done | Dharshini, Rashmi, Sudeep | 1.2d (10h) |
| [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458) | Staging / Mobile / New Login / Country picker shows all countries first then filters; loader flashes on country code | Testing | Dhanush, Rashmi, Sahil Siddiqui | 1.1d (8h) |
| [HIEV-7449](https://elocity.atlassian.net/browse/HIEV-7449) | STG/ Hiev Canada/ Portal/Tariff launch activity is not displayed in Activity Logs | Done | Rashmi, Sudeep | 1.0d (8h) |
| [HIEV-6607](https://elocity.atlassian.net/browse/HIEV-6607) | UAT/ Hiev India / Push Notification >> Scheduled push notification is not sent in the given time | Done | Rashmi, Shambu | 0.9d (7h) |
| [HIEV-7304](https://elocity.atlassian.net/browse/HIEV-7304) | Stage / Portal / ⁠My Profile>Click on ‘Export Logs’ button>Verify the report - Entity reference is ‘UNKNOWN’ with a note “value too long for type character varying(255)”>> BUT the same note later on has the entity reference 418 and entity type - location | Done | Rashmi, Sudeep | 0.9d (7h) |
| [HIEV-7352](https://elocity.atlassian.net/browse/HIEV-7352) | Stage / portal / android / HIEV canada /Refreshing the charging session couple of times during the Finishing state or after reaching max SOCresets accumulated Energy Consumed to 0, resulting in loss of previously recorded energy | In Review | Twisha | 0.9d (7h) |
| [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242) | UAT / Hiev Canada / Android / Queue / Simultaneous queue requests fail for both users with "Time slot already reserved" | Ready for Testing | Twisha, Vinay | 0.8d (7h) |
| [HIEV-7526](https://elocity.atlassian.net/browse/HIEV-7526) | Staging / Load Management / Unable to edit existing Load Group when no charging sessions are active | Done | Nagaraju, Shambu | 0.8d (6h) |
| [HIEV-7490](https://elocity.atlassian.net/browse/HIEV-7490) | STG / Hiev Canada/ Portal/ Corporate Customer – INACTIVE RFID displays generic “Something went wrong” message. | Done | Rashmi, Shambu, Vinay | 0.8d (6h) |
| [HIEV-7121](https://elocity.atlassian.net/browse/HIEV-7121) | Stage / Portal / Getting 500 error code after exporting a report but continuing to download other reports without viewing the downloaded reports in the export module | Done | Nagaraju, Sahil Kumar, Shambu | 0.8d (6h) |
| [HIEV-7597](https://elocity.atlassian.net/browse/HIEV-7597) | Force delete export jobs after 7 days from completion | In Progress | Shambu | 0.8d (6h) |
| [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032) | Canada Prod / Prod / Alerts & Notifications > Using the alerts time filter, select “Payment Successful” option > Click on ‘Apply’ button > There are 0 corresponding search results which is incorrect as there are 77 paid session for the same time period | Done | Rashmi, Twisha, Vinay | 0.7d (6h) |
| [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326) | Stage / Portal / My Profile > Activity Logs > Currently, the Changes and Notes fields often display "NA", which results in redundant information.  | Ready for Testing | Dharshini, Sahil Siddiqui, Sudeep | 0.6d (4h) |
| [HIEV-7216](https://elocity.atlassian.net/browse/HIEV-7216) | STG/ Hiev Canada / Portal / Assets-> Diagnostic>>Diagnostic report CRON job and recovery job failed to run  | Done | Rashmi, Sahil Kumar, Shambu | 0.5d (4h) |
| [HIEV-7416](https://elocity.atlassian.net/browse/HIEV-7416) | STG/ Hiev Canada/ Portal/ Station Remains in Maintenance Mode After Maintenance Is Removed, Blocking New Charging Sessions | In Progress | Rashmi, Twisha | 0.5d (4h) |
| [HIEV-7491](https://elocity.atlassian.net/browse/HIEV-7491) | STG / Hiev Canada/ Portal/ Abnormal Event-> INACTIVE RFID of Corporate Customer – Abnormal Event displays technical error in the description. | Done | Rashmi, Shambu, Vinay | 0.5d (4h) |
| [HIEV-7244](https://elocity.atlassian.net/browse/HIEV-7244) | UAT / Hiev Canada / Android / Reservations / Cancelled reservations and cancelled queue's are displayed in the Upcoming tab without any status indication where customers cannot distinguish an active reservation from a cancelled one without opening it. | Done | Nagaraju, Twisha | 0.5d (4h) |
| [HIEV-7564](https://elocity.atlassian.net/browse/HIEV-7564) | STG/ Portal/ Hiev Canada/ Customer -> E-wallet>> Session Refunded and Wallet Refunded are not available as separate options in the Event Type dropdown | In Review | Dharshini, Rashmi, Twisha | 0.5d (4h) |
| [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546) | UAT/ Portal Hiev Canada/ Guest Charging >> Incorrect “Payment is being processed” Loader Message Displayed After Charging Session Starts | Ready for Testing | Dharshini, Rashmi, Sahil Siddiqui, Sudeep | 0.4d (3h) |
| [HIEV-7475](https://elocity.atlassian.net/browse/HIEV-7475) | Staging / Android / Time is displayed in 24-hour format instead of 12-hour format with AM/PM | Done | Dhanush, Nagaraju, Rashmi | 0.4d (3h) |
| [HIEV-7563](https://elocity.atlassian.net/browse/HIEV-7563) | Staging / Load Management / Decommissioned station continues to be displayed in Load Group Overview | Done | Nagaraju, Sahil Kumar | 0.4d (3h) |
| [HIEV-7243](https://elocity.atlassian.net/browse/HIEV-7243) | UAT / Hiev Canada / Android / Reservation / Reserved time slots remain selectable and validation occurs only after reservation confirmation | Done | Nagaraju, Twisha, Vinay | 0.4d (3h) |
| [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385) | Movem Prod / Displayed Location as Closed on Location Detail screen on Sundays. | Done | Dhanush, Nagaraju, Sahil Siddiqui, Vinay | 0.4d (3h) |
| [HIEV-7560](https://elocity.atlassian.net/browse/HIEV-7560) | Staging / Load Management / CPMS / Load Group creation/update fails when station(s) are selected | Done | Nagaraju, Shambu | 0.4d (3h) |
| [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390) | STG / CPMS / Bulk Operations / Get Configuration / Selected Charge Point IDs are not passed in request, resulting in HTTP 400 | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.3d (3h) |
| [HIEV-7323](https://elocity.atlassian.net/browse/HIEV-7323) | Stage / Portal / Activity Logs > IP address and Device fields are missing from the downloaded report | Done | Dharshini, Sudeep | 0.3d (2h) |
| [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391) | STG / CPMS / Bulk Operations / Get Configuration / Perform Action button remains disabled when only Custom configuration keys are entered | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.3d (2h) |
| [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492) | STG / CPMS / Corporate / Employees / Employee ID field accepts excessive characters without validation | Ready for Testing | Dharshini, Nagaraju, Sahil Siddiqui | 0.3d (2h) |
| [HIEV-7495](https://elocity.atlassian.net/browse/HIEV-7495) | STG/ Hiev Canada/ Portal/ Charging session can be started before the station’s commissioned date | Done | Rashmi, Shambu, Vinay | 0.3d (2h) |
| [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539) | STG/ Portal / Hiev Canada/ Assets-> Diagnostic Job >>Job status remains In Progress even though all 2 stations are successful | Done | Rashmi, Sahil Kumar, Shambu | 0.3d (2h) |
| [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237) | Staging / CPMS Portal / Assets > Location Management / Invalid character limit handling results in server errors during Location creation and update | Ready for Testing | Nagaraju, Sahil Siddiqui, Surya | 0.3d (2h) |
| [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530) | Staging / CPMS / Utility Tariff / The Design New Tariff → Utility Tariff screen has insufficient/unclear validation for the Tariff Name and TOU Price fields. | In Review | Dharshini, Nagaraju, Sahil Siddiqui | 0.3d (2h) |
| [HIEV-7199](https://elocity.atlassian.net/browse/HIEV-7199) | The triggerPrepaidLocationPaymentJob cron job in payment service has no guard against infinite retries | Done | Sudeep, Vinay | 0.3d (2h) |
| [HIEV-7324](https://elocity.atlassian.net/browse/HIEV-7324) | Staging / Portal / Activity Logs / Business filter displays records from other businesses after applying selected business filter | In Review | Sudeep, Twisha | 0.3d (2h) |
| [HIEV-7379](https://elocity.atlassian.net/browse/HIEV-7379) | Stage/ CPMS / Tariff / Launch Tariff Profile fails with HTTP 500 due to missing currency_code error | Done | Nagaraju, Twisha | 0.3d (2h) |
| [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533) | Staging / CPMS / Utility Tariff / Tiered Tariff / Rate/Price field accepts excessively lengthy numeric values and exposes API validation error | In Review | Dharshini, Nagaraju, Sahil Siddiqui | 0.3d (2h) |
| [HIEV-7301](https://elocity.atlassian.net/browse/HIEV-7301) | UAT/ Hiev Canada/ Portal/ Deleted Customer (Customer ID: 2938) is displayed in Active Customers | Done | Rashmi, Twisha | 0.3d (2h) |
| [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291) | STG / Portal/ Hiev Canada/ Abnormal Event -> Event Type-(Start Transaction failed and Remote Start Failed) -Description message is not user friendly | Done | Rashmi, Shambu, Vinay | 0.3d (2h) |
| [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404) | STG / CPMS / Portal / Reservation / Save action does not trigger Create Reservation API and displays incorrect validation error | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.3d (2h) |
| [HIEV-7295](https://elocity.atlassian.net/browse/HIEV-7295) | UAT / CPMS / Portal / Guest / Incorrect connector details displayed for selected connector on multi-connector stations | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.2d (2h) |
| [HIEV-7311](https://elocity.atlassian.net/browse/HIEV-7311) | Stage / Portal / Station Management > View the details of the station > Go to “Logs History” > Update the date range > There are 0 results are displayed which is incorrect | Done | Twisha | 0.2d (2h) |
| [HIEV-7614](https://elocity.atlassian.net/browse/HIEV-7614) | UAT - "request entity too large error" in email service | To Do | Shambu | 0.2d (2h) |
| [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540) | Staging / Utility Tariff / Reports / Revenue vs Energy Cost chart loses left Y-axis labels and horizontal grid lines after zooming | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.2d (2h) |
| [HIEV-7549](https://elocity.atlassian.net/browse/HIEV-7549) | Staging / Load management / Scheduled Charging / Add New Schedule retains validation error from edited schedule with identical From and To time | Ready for Testing | Nagaraju, Surya | 0.2d (2h) |
| [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558) | Staging / Utility Tariff / Reports / Revenue vs Energy Cost chart does not match design and Energy Cost disappears after zooming out | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.2d (2h) |
| [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226) | STG/ Portal/ Hiev Canada/ Corporate >> Charging Session >> Refund button is visible even though the charging cost is displaying 0.00 | Done | Dharshini, Rashmi, Sahil Siddiqui | 0.2d (2h) |
| [HIEV-7476](https://elocity.atlassian.net/browse/HIEV-7476) | Staging / Android / Reservation cards(Upcoming / Past ) do not display connector icons along with connector information | Done | Dhanush, Nagaraju, Rashmi | 0.2d (2h) |
| [HIEV-7488](https://elocity.atlassian.net/browse/HIEV-7488) | Staging / CPMS / Reporting / Multiple exports contain additional invalid rows irrespective of selected date range | Done | Nagaraju, Sahil Kumar, Shambu | 0.2d (2h) |
| [HIEV-7479](https://elocity.atlassian.net/browse/HIEV-7479) | Staging / HIEV Canada / Android / Home / Map is not rendered after fresh app installation and login | Done | Dhanush, Nagaraju, Rashmi | 0.2d (2h) |
| [HIEV-7501](https://elocity.atlassian.net/browse/HIEV-7501) | Staging / Load Management / Analytics tab fails to load for Load Group with active transaction | Ready for Testing | Nagaraju, Surya | 0.2d (2h) |
| [HIEV-7504](https://elocity.atlassian.net/browse/HIEV-7504) | Staging / Load Management / Opening Load Group Overview consistently displays “Something went wrong” after connector details load | Done | Nagaraju, Surya | 0.2d (2h) |
| [HIEV-7529](https://elocity.atlassian.net/browse/HIEV-7529) | Staging / Load Management / Manual Rebalance does not resolve Load Group deviation for a single connector | Done | Nagaraju, Sahil Kumar | 0.2d (2h) |
| [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534) | Staging / CPMS / Utility Tariff / Edit / Tiered tariff defaults to TOU instead of displaying saved Tiered configuration | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.2d (2h) |
| [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342) | Stage / Portal / GHG reporting / "Greenhouse Gas Used" data bars is not rendered while "Cumulative" data is displayed | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.2d (2h) |
| [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538) | Staging / Utility Tariff / Reports / Energy Cost chart displays inconsistent Y-axis spacing after zooming | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.2d (2h) |
| [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166) | Stage / Portal / Reservation>Successfully add a reservation for the present day>Update the date range to ‘Today’> 0 results are reflected in the data grid even though one reservation has just been added  | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.2d (2h) |
| [HIEV-7204](https://elocity.atlassian.net/browse/HIEV-7204) | Stage / Portal / Overall >Select ‘Today’> None of the sections reflect any data. It’s all 0 even though several sessions have been completed today > Data until yesterday is visible on Overall > Today button and calendar option to be removed | Done | Rashmi, Sahil Siddiqui, Surya | 0.2d (2h) |
| [HIEV-7312](https://elocity.atlassian.net/browse/HIEV-7312) | Portal / Stage / Station Management / Maintenance slot is deleted after editing and saving without changes | Ready for Testing | Surya | 0.2d (2h) |
| [HIEV-7528](https://elocity.atlassian.net/browse/HIEV-7528) | Staging / Load Management / Overview / Load Usage indicator remains yellow even when load is in Safe Zone | Ready for Testing | Nagaraju, Surya | 0.2d (2h) |
| [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377) | Staging / Hiev Canada / Android / Reservation / Join Queue screen displays incorrect connector availability after navigating back from the queue flow | Done | Dhanush, Nagaraju, Sahil Siddiqui | 0.2d (1h) |
| [HIEV-7562](https://elocity.atlassian.net/browse/HIEV-7562) | Staging / Load Management / Deleting a Load Group does not redirect user to Load Group List | Ready for Testing | Nagaraju, Surya | 0.2d (1h) |
| [HIEV-7376](https://elocity.atlassian.net/browse/HIEV-7376) | Android / Staging / HIEV Canada / Infinite loading displayed after selecting a connector while making a reservation | Done | Dhanush, Nagaraju | 0.2d (1h) |
| [HIEV-7474](https://elocity.atlassian.net/browse/HIEV-7474) | Staging / Android / Improve readability of date and time displayed in Reservation cards | Done | Dhanush, Nagaraju, Rashmi, Sahil Siddiqui | 0.2d (1h) |
| [HIEV-7502](https://elocity.atlassian.net/browse/HIEV-7502) | STG/ Hiev Canada/ Portal/ Assets-> Firmware Job>>Firmware update job remains In Progress indefinitely. | Done | Rashmi, Sahil Kumar, Shambu | 0.2d (1h) |
| [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090) | UAT/ Alfanar/ Web/ Dashboard>> Alerts and Notification -Apply button remains disabled after selecting "Last Year" filter in ALerts and Notification tab  | Done | Rashmi, Sahil Siddiqui | 0.1d (1h) |
| [HIEV-7466](https://elocity.atlassian.net/browse/HIEV-7466) | STG / CPMS / Station Management / Advanced Controls collapses after saving changes | Done | Nagaraju, Surya | 0.1d (1h) |
| [HIEV-7505](https://elocity.atlassian.net/browse/HIEV-7505) | Staging / Load Management / Clicking a Load Group tile in Grid View does not open Load Group Details | Ready for Testing | Nagaraju, Surya | 0.1d (1h) |
| [HIEV-7552](https://elocity.atlassian.net/browse/HIEV-7552) | STG/ Portal / Hiev Canada/ Customer->Charging Session >>Clicking Refund shows “Corresponding payment not found for the Entity ID.” | To Do | Rashmi, Twisha | 0.1d (1h) |
| [HIEV-7561](https://elocity.atlassian.net/browse/HIEV-7561) | Staging / Customer / Add New Customer / Country Code dropdown shows "No options exist" and blocks customer creation | Done | Nagaraju, Rashmi, Surya | 0.1d (1h) |
| [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275) | Stage / Portal / There is a mismatch in the number of total connects as seen on the pin details in comparison to the total count of connectors in the data grid | To Do | Shambu, Vinay | 0.1d (1h) |
| [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282) | STG/ Hiev Canada/ Portal / Abnormal Event>> Event Type -(High Energy Loss between consecutive sessions)>>Inconsistent meter units displayed in High Energy Loss Between Consecutive Sessions event description | Done | Rashmi, Shambu, Vinay | 0.1d (1h) |
| [HIEV-7493](https://elocity.atlassian.net/browse/HIEV-7493) | Staging / CPMS / Corporate / Employees / Saving employee with excessive long Employee ID causes application to enter unrecoverable error state | In Review | Nagaraju, Sudeep, Twisha | 0.1d (1h) |
| [HIEV-7527](https://elocity.atlassian.net/browse/HIEV-7527) | Staging / Load Management / Browser refresh redirects from Load Group details to Load Group list | Done | Nagaraju, Surya | 0.1d (1h) |
| [HIEV-7559](https://elocity.atlassian.net/browse/HIEV-7559) | STG/ Android/ Hiev Canada/ Wallet>>Unable to add money in wallet "PaymentIntent Client Secret Mismatch" | Done | Dhanush, Rashmi, Shambu | 0.1d (1h) |
| [HIEV-6885](https://elocity.atlassian.net/browse/HIEV-6885) | Canada Prod - Periodically logging out issues | To Do | Manjunath | 0.1d (1h) |
| [HIEV-7240](https://elocity.atlassian.net/browse/HIEV-7240) | UAT / Hiev Canada / Android / Queue / Unable to create a new queue reservation despite another valid time slot being available | Done | Dhanush, Nagaraju, Twisha | 0.1d (1h) |
| [HIEV-7279](https://elocity.atlassian.net/browse/HIEV-7279) | Guest Charging | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.1d (1h) |
| [HIEV-7288](https://elocity.atlassian.net/browse/HIEV-7288) | UAT / Guest Charging / Android Chrome / Station Details / Multiple swipe gestures are required to vertically scroll the Station Details page | Done | Dharshini, Nagaraju | 0.1d (1h) |
| [HIEV-7313](https://elocity.atlassian.net/browse/HIEV-7313) | Stage / Portal / My profile > Success pop-up and progress bar is missing and button label gets updated which is incorrect | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.1d (1h) |
| [HIEV-7319](https://elocity.atlassian.net/browse/HIEV-7319) | Portal / Stage / Station Management / Ratio Duration field allows text input in non-editable area | Ready for Testing | Surya | 0.1d (1h) |
| [HIEV-7339](https://elocity.atlassian.net/browse/HIEV-7339) | Staging / Android / Hiev Canada / Empty gaps displayed between facility icons on the Location Details page | Done | Dhanush, Nagaraju | 0.1d (1h) |
| [HIEV-7489](https://elocity.atlassian.net/browse/HIEV-7489) | Staging / CPMS / Portal / Reporting / Peak Hours report does not provide an Export option | Done | Nagaraju, Sahil Siddiqui | 0.1d (1h) |
| [HIEV-7513](https://elocity.atlassian.net/browse/HIEV-7513) | STG/ Portal / Hiev Canada / Corporate >> Corporate Code accepts landline number despite mobile-only requirement | Done | Rashmi, Sahil Siddiqui | 0.1d (1h) |
| [HIEV-7517](https://elocity.atlassian.net/browse/HIEV-7517) | UAT / Mobile / Guest Charging / 404 error displayed after submitting payment details while starting a charging session | Done | Nagaraju, Sudeep | 0.1d (1h) |
| [HIEV-7519](https://elocity.atlassian.net/browse/HIEV-7519) | Load Usage does not reset to 0A after charging session ends | Ready for Testing | Surya | 0.1d (1h) |
| [HIEV-7420](https://elocity.atlassian.net/browse/HIEV-7420) | STG/ Hiev Canada/ Portal / Maintenance Slot Displays Only Start Date Instead of Full Date Range | Ready for Testing | Rashmi, Sahil Siddiqui, Twisha | 0.1d (1h) |
| [HIEV-7510](https://elocity.atlassian.net/browse/HIEV-7510) | Staging / Scheduled Charging / Group Name field has no length validation and causes inconsistent API behavior | Ready for Testing | Nagaraju, Surya | 0.1d (1h) |
| [HIEV-7516](https://elocity.atlassian.net/browse/HIEV-7516) | UAT / Web / Location Management / Prepaid location fields and Country/Time Zone options are not loading | Done | Nagaraju, Sahil Siddiqui | 0.1d (1h) |
| [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062) | Canada Prod / Portal / Business > Click on ‘Export Business’ button > Review the downloaded report  > ‘CIN’ field is present here which is incorrect  >> ‘CIN’ field has to be removed  | Done | Dharshini, Nagaraju, Sahil Siddiqui | 0.1d (1h) |
| [HIEV-7234](https://elocity.atlassian.net/browse/HIEV-7234) | STG/ Hiev Canada/Portal/Assets-> Diagnostic >> Job Status dropdown displays “Dispatch” instead of “Dispatching” | Done | Rashmi, Sahil Siddiqui | 0.1d (1h) |
| [HIEV-7296](https://elocity.atlassian.net/browse/HIEV-7296) | STG/ Hiev Canada/ Portal/Assets-> Firmware Management->Export button not present in Firmware Management module. | Done | Rashmi, Sahil Siddiqui | 0.1d (1h) |
| [HIEV-7310](https://elocity.atlassian.net/browse/HIEV-7310) | Portal / Station Management / Active maintenance status label is not displayed during maintenance window | Ready for Testing | Surya | 0.1d (1h) |
| [HIEV-7316](https://elocity.atlassian.net/browse/HIEV-7316) | Portal / Stage / Station Management / Connector Type dropdown text overlaps for actions requiring connector type selection | Ready for Testing | Surya | 0.1d (1h) |
| [HIEV-7413](https://elocity.atlassian.net/browse/HIEV-7413) | STG/ Portal/ Hiev Canada/ Station Management-> Maintenance - Maintenance Slot Remove (-) Icon is Misaligned in Custom Slots Section | Testing | Rashmi, Surya | 0.1d (1h) |
| [HIEV-7423](https://elocity.atlassian.net/browse/HIEV-7423) | STG / Portal / Business / Export Business button becomes non-functional in reduced viewport | Ready for Testing | Nagaraju, Surya | 0.1d (1h) |
| [HIEV-7499](https://elocity.atlassian.net/browse/HIEV-7499) | STG/ Portal / Hiev Canada/ Job Status is displayed as InProgress while the station status is Pending | Done | Rashmi, Sahil Kumar, Shambu | 0.1d (1h) |
| [HIEV-7585](https://elocity.atlassian.net/browse/HIEV-7585) | Staging  / Load Management / Round Robin / Extremely large pasted Time Interval is saved as null | Ready for Testing | Nagaraju, Surya | 0.1d (1h) |
| [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133) | Stage / Portal / Low Priority issues - 4 | Done | Rashmi, Sahil Siddiqui, Surya | 0.1d (1h) |
| [HIEV-7303](https://elocity.atlassian.net/browse/HIEV-7303) | Stage / Portal / My Profile > Verify that only one business is reflected in the ‘Business’ filter > Click on ‘Export Logs’ button > Download is successfully completed >Time stamp is in UTC format while the data grid shows the local time (IST) | To Do | Twisha | 0.1d (1h) |
| [HIEV-7518](https://elocity.atlassian.net/browse/HIEV-7518) | Staging / Portal / Load Management / Grammar and capitalisation issue in EVSE duplicate assignment error message | In Progress | Nagaraju, Surya | 0.1d (1h) |
| [HIEV-7299](https://elocity.atlassian.net/browse/HIEV-7299) | STG/ Portal/ HIev Canada/ Dashboard-> Abnormal Event>>Description error message is not details for Connector not found | Done | Rashmi, Vinay | 0.1d (1h) |
| [HIEV-7550](https://elocity.atlassian.net/browse/HIEV-7550) | UAT / Portal/ Hiev Canada / Guest Charging >>After the scanning the QR code  Error message is not user Friendly when a charging session is already active. | Done | Dharshini, Rashmi | 0.1d (1h) |
| [HIEV-7018](https://elocity.atlassian.net/browse/HIEV-7018) | Canada Prod/Portal/⁠Station Overview > Using the "Charger" filter, select ONE charger>Corresponding results are reflected BUT the map does not reflect the location pin and continues to show all the pins that were present before the filter was applied | Done | Nagaraju, Surya | 0.1d (0h) |
| [HIEV-7202](https://elocity.atlassian.net/browse/HIEV-7202) | STG/ Hiev Canada/ Web/ Station Management-> Incorrect confirmation message displayed when changing Installation State from Commission to Decommission for a blocked station | Done | Rashmi, Sahil Siddiqui | 0.1d (0h) |
| [HIEV-7314](https://elocity.atlassian.net/browse/HIEV-7314) | Portal / Stage / Station Management / 'Please add at least one slot' validation is displayed immediately after selecting Custom Slots | Ready for Testing | Surya | 0.1d (0h) |
| [HIEV-7315](https://elocity.atlassian.net/browse/HIEV-7315) | Stage / Portal / Refresh action is incorrect and is resetting filters applied instead | Done | Nagaraju, Sahil Siddiqui | 0.1d (0h) |
| [HIEV-7317](https://elocity.atlassian.net/browse/HIEV-7317) | Stage / Portal / On updating and saving the user email address, user gets logged out successfully >>Email address should not editable  | Done | Nagaraju, Sahil Siddiqui | 0.1d (0h) |
| [HIEV-7320](https://elocity.atlassian.net/browse/HIEV-7320) | Stage / Portal / My Profile > Low priority issues  | Done | Nagaraju, Sahil Siddiqui | 0.1d (0h) |
| [HIEV-7321](https://elocity.atlassian.net/browse/HIEV-7321) | UAT / Portal / Station Management / Minimum Balance field lacks input length validation and allows excessive numeric input | Done | Nagaraju, Sahil Siddiqui | 0.1d (0h) |
| [HIEV-7328](https://elocity.atlassian.net/browse/HIEV-7328) | Stage / Portal / Report Subscription>Create a new email alert > Click on 'X’ icon on the top right corner of the pop-up> Instead of closing the pop-up, the screen reverts back to the create a new email alert or to review the existing alert details screen | Done | Rashmi, Sahil Siddiqui | 0.1d (0h) |
| [HIEV-7456](https://elocity.atlassian.net/browse/HIEV-7456) | Staging / HIEV Canada / Android / In-App Campaign / Eligible campaigns are not displayed after login | To Do | Nagaraju | 0.1d (0h) |
| [HIEV-7468](https://elocity.atlassian.net/browse/HIEV-7468) | Staging / Load Management / Load Group Creation / Save button triggers infinite loading with no API request | Done | Nagaraju, Sahil Kumar, Sahil Siddiqui | 0.1d (0h) |
| [HIEV-7487](https://elocity.atlassian.net/browse/HIEV-7487) | STG/ Hiev Canada/ Portal/ Abnormal Event-> When the station is under maintenance >> Maintenance message displays a non user friendly timestamp.  | In Progress | Rashmi, Shambu | 0.1d (0h) |
| [HIEV-7509](https://elocity.atlassian.net/browse/HIEV-7509) | Staging / CPMS / Scheduled Charging / Cancel and Save buttons have inconsistent dimensions | Ready for Testing | Nagaraju, Surya | 0.1d (0h) |
| [HIEV-7512](https://elocity.atlassian.net/browse/HIEV-7512) | Staging / Charging Sessions / Guest Charging filter width is inconsistent with other filters | Ready for Testing | Nagaraju, Surya | 0.1d (0h) |
| [HIEV-7590](https://elocity.atlassian.net/browse/HIEV-7590) | Wrong currency shown for Oshawa Power (business_id 1256) | Done | Shambu | 0.1d (0h) |
| [HIEV-7514](https://elocity.atlassian.net/browse/HIEV-7514) | STG/ Portal / Hiev Canada/ Location Management>> Add Location >>Landline number is accepted in the Location Contact Number field | Done | Rashmi, Sahil Siddiqui | 0.1d (0h) |
| [HIEV-7515](https://elocity.atlassian.net/browse/HIEV-7515) | STG/ Portal / Hiev Canada /Administration -> User Management>> Landline number is accepted  in Add New User Contact field  | Done | Rashmi, Sahil Siddiqui | 0.1d (0h) |
| [HIEV-7165](https://elocity.atlassian.net/browse/HIEV-7165) | Stage / Portal /Reservation> User is unable to make a reservation for a customer that has previously made two reservation in the last 6 months > Getting the error - User has already reached max reservation limit | Done | Nagaraju, Twisha | 0.0d (0h) |
| [HIEV-7464](https://elocity.atlassian.net/browse/HIEV-7464) | Staging / CPMS Portal / Station Management / Long station name causes table layout overflow after navigating between management screens | To Do | Nagaraju | 0.0d (0h) |
| [HIEV-6446](https://elocity.atlassian.net/browse/HIEV-6446) | Stage / Portal / Station Management - Low Priority Issues 1 | Done | Nagaraju, Surya | 0.0d (0h) |
| [HIEV-6875](https://elocity.atlassian.net/browse/HIEV-6875) | UAT/ Hiev Canada / Android/Prepaid Location >> Parking charges is not applied in tariff > Green Strip is showing with message “Your Ev was charged successfully”  >>After clicking on arrow >> Navigate to Energised to GO! Screen. | Done | Rashmi | 0.0d (0h) |
| [HIEV-6894](https://elocity.atlassian.net/browse/HIEV-6894) | MOVEM / Prod/ Add new location > Search for a location > Select an option > all the mandatory fields gets auto-populated except for 'City' field | Done | Rashmi | 0.0d (0h) |
| [HIEV-7077](https://elocity.atlassian.net/browse/HIEV-7077) | UAT/ Alfanar/ Android/ Parking Charges Applied to Session but Not Reflected in Session Details and Invoices | Done | Rashmi | 0.0d (0h) |
| [HIEV-7094](https://elocity.atlassian.net/browse/HIEV-7094) | Canada Prod / Portal / ⁠Customer Groups>Go to Customers tab>Click on ‘View RFID'>Side panel with the RFID details is visible>Click on Delete>Pop-up to confirm the delete action is visible>Click on either Cancel or Delete, msg on pop-up shows ‘Undefined’ | Done | Rashmi, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7143](https://elocity.atlassian.net/browse/HIEV-7143) | UAT/ Hiev Canada / Android/Location details>> Reservation >> Reservation Details screen briefly displays “No Location Found” message while data is loading | Done | Rashmi | 0.0d (0h) |
| [HIEV-7163](https://elocity.atlassian.net/browse/HIEV-7163) | UAT/ Hiev Canada / Android/ Reservation>> Filter >>Filter icon not showing red dot after applying filter | Done | Rashmi | 0.0d (0h) |
| [HIEV-7207](https://elocity.atlassian.net/browse/HIEV-7207) | Staging / Portal / Menu > Assets > Add New Location > Timing / Back and Next buttons are cropped when "Customized" timing is selected at 100% browser zoom | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7214](https://elocity.atlassian.net/browse/HIEV-7214) | Staging / Portal / Session Management / Previous browser gets stuck in "Something went wrong" refresh loop instead of redirecting to Login after session is invalidated | Done | Nagaraju, Surya | 0.0d (0h) |
| [HIEV-7215](https://elocity.atlassian.net/browse/HIEV-7215) | Staging / Portal / Reservations / "No options exist" dropdown remains visible after losing focus in All Chargers filter | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7218](https://elocity.atlassian.net/browse/HIEV-7218) | Staging / Portal / Tariff Management > Design New Tariff / Validation message persists after disabling tariff section | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7235](https://elocity.atlassian.net/browse/HIEV-7235) | Staging / CPMS Portal / Assets > Station Management / Long station names cause UI overflow in the details page and incorrect character limit handling | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7236](https://elocity.atlassian.net/browse/HIEV-7236) | Staging / CPMS Portal / User Management / Inconsistent styling of action buttons on User Details page | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7269](https://elocity.atlassian.net/browse/HIEV-7269) | UAT / Guest Charging / Android Chrome / QR Scan / Error page reloads after displaying "Guest charging is not allowed at this location" for Planned stations | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7297](https://elocity.atlassian.net/browse/HIEV-7297) | STG/ Portal / Hiev Canada/ Dashboard-> Abnormal Event>> Description error message is not detials if Customer not found it is showing only "Customer not found"  | Done | Rashmi, Vinay | 0.0d (0h) |
| [HIEV-7302](https://elocity.atlassian.net/browse/HIEV-7302) | Stage / Portal / My Profile>Click on ‘Export Logs’ button > Download is successfully completed > the downloaded file’s name is “ActivityLogs_tenant_2026-07-27T11_31_59.038Z” >> the downloaded file’s name is to be updated | Done | Rashmi, Sudeep | 0.0d (0h) |
| [HIEV-7309](https://elocity.atlassian.net/browse/HIEV-7309) | STG / Android / Hiev Canada / Tapping clustered station markers on the map does not zoom into the selected area | Done | Dhanush, Nagaraju | 0.0d (0h) |
| [HIEV-7356](https://elocity.atlassian.net/browse/HIEV-7356) | Stage / Android / HIEV canada / Customer is redirected to "Awaiting Connection" screen instead of Session Summary after completing a charging session initiated via QR code  | Done | Nagaraju | 0.0d (0h) |
| [HIEV-7500](https://elocity.atlassian.net/browse/HIEV-7500) | STG/ Hiev Canada/ Portal/ Assets-> Firmware Management>> File Name Autosuggestion Dropdown Overlaps the Cancel Button | Done | Nagaraju, Rashmi | 0.0d (0h) |
| [HIEV-7511](https://elocity.atlassian.net/browse/HIEV-7511) | Staging / Load Management / Load Group Name does not provide inline validation for 50-character limit | Ready for Testing | Surya | 0.0d (0h) |
| [HIEV-7531](https://elocity.atlassian.net/browse/HIEV-7531) | STG/ Portal/ Hiev Canada/ Reservation >>Reservation within the maximum duration limit is incorrectly rejected | Done | Rashmi, Twisha | 0.0d (0h) |
| [HIEV-7535](https://elocity.atlassian.net/browse/HIEV-7535) | UAT/ Portal / Hiev Canada / Guest Charging >> Guest Charger QR Code Shows “Invalid QR” Error | Done | Nagaraju, Rashmi | 0.0d (0h) |
| [HIEV-7544](https://elocity.atlassian.net/browse/HIEV-7544) | UAT/ Portal/ Hiev Canada/ Guest Charging>> Incorrect charging session data is displayed in charging summary screen . | To Do | Dharshini, Rashmi, Sudeep | 0.0d (0h) |
| [HIEV-6315](https://elocity.atlassian.net/browse/HIEV-6315) | Stage / Portal / User Management > “Resend Activation Link” continues to be present even though  account status is “Active” | Done | Rashmi | 0.0d (0h) |
| [HIEV-7095](https://elocity.atlassian.net/browse/HIEV-7095) | Alfanar UAT / Click on ‘Add New Location’ > Search for an address in the ‘Address Line 1’> Select any option from the drop down >“State/Province” and “TimeZone” field does not get auto-populated > City and Zip code gets populated most of the times | Done | Rashmi, Sudeep | 0.0d (0h) |
| [HIEV-7156](https://elocity.atlassian.net/browse/HIEV-7156) | UAT/ Hiev Canada/ Android/ Reservation>> Click on Join Queue arrow -> Reservation details screen are unavailable | Done | Rashmi | 0.0d (0h) |
| [HIEV-7209](https://elocity.atlassian.net/browse/HIEV-7209) | Staging / Portal / Menu > Assets > Location Management > Asset Settings > EVSE Models > Add New EVSE Model / Validation error messages are inconsistently aligned across form fields | Done | Nagaraju, Surya | 0.0d (0h) |
| [HIEV-7264](https://elocity.atlassian.net/browse/HIEV-7264) | Stage / Portal / On occasion, after extended idle periods, we get a pop-up ‘Something Went Wrong.” pop-up. By clicking on 'Refresh Page’ button, the page gets refreshed but the pop-up continues to be present.  User unable to logout either and is stuck.  | Done | Nagaraju, Surya | 0.0d (0h) |
| [HIEV-7576](https://elocity.atlassian.net/browse/HIEV-7576) | STG/ Android/ Alfanar/ Unable to Log In with Phone Number OTP Login fails due to missing app check token | To Do | Rashmi | 0.0d (0h) |
| [HIEV-7333](https://elocity.atlassian.net/browse/HIEV-7333) | CPMS / Stage / Incorrect report title displayed as "Greenhouse Gas Used" in Reporting dashboard | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7335](https://elocity.atlassian.net/browse/HIEV-7335) | Stage / Portal / GHG reporting / Inconsistent Y-axis intervals and grid line spacing after first zoom in Greenhouse Gas report fullscreen view | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7336](https://elocity.atlassian.net/browse/HIEV-7336) | Stage / Portal / GHG reporting / Right Y-axis displays fewer values than the left Y-axis, after zooming in Greenhouse Gas report | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |
| [HIEV-7337](https://elocity.atlassian.net/browse/HIEV-7337) | Stage / Portal / GHG reporting / Top horizontal grid line is missing a corresponding right Y-axis value after zooming out in Greenhouse Gas report fullscreen view | Done | Nagaraju, Sahil Siddiqui | 0.0d (0h) |

## 4. Fix hours invested (August worklogs)

- Bug tickets: **36.1d (289h)**
- Task / Sub-task tickets: **208.8d (1671h)**
- Other types: **16.5d (132h)**

| Person | Bug time of available | Task time of available |
|---|---:|---:|
| Deepak | 0.0 of 19.5d (0h of 156h) | 20.8 of 19.5d (166h of 156h) |
| Priyanshu | 0.0 of 20.0d (0h of 160h) | 20.1 of 20.0d (161h of 160h) |
| Sahil Kumar | 0.5 of 20.0d (4h of 160h) | 19.6 of 20.0d (156h of 160h) |
| Dhanush | 3.1 of 18.0d (25h of 144h) | 14.4 of 18.0d (116h of 144h) |
| Marish | 0.0 of 19.0d (0h of 152h) | 2.8 of 19.0d (22h of 152h) |
| Tarun | 0.0 of 20.0d (0h of 160h) | 17.2 of 20.0d (138h of 160h) |
| Sudeep | 3.9 of 19.0d (31h of 152h) | 13.2 of 19.0d (105h of 152h) |
| Nagaraju | 3.2 of 19.0d (26h of 152h) | 13.3 of 19.0d (107h of 152h) |
| Sahil Siddiqui | 2.5 of 16.0d (20h of 128h) | 12.6 of 16.0d (101h of 128h) |
| Dharshini | 2.9 of 18.0d (23h of 144h) | 10.7 of 18.0d (85h of 144h) |
| Twisha | 6.2 of 18.0d (50h of 144h) | 7.1 of 18.0d (57h of 144h) |
| Shambu | 7.9 of 19.0d (63h of 152h) | 5.2 of 19.0d (42h of 152h) |
| Srikant | 0.0 of 17.0d (0h of 136h) | 11.9 of 17.0d (95h of 136h) |
| Surya | 2.5 of 20.0d (20h of 160h) | 8.4 of 20.0d (67h of 160h) |
| Manjunath | 0.1 of 16.0d (1h of 128h) | 10.9 of 16.0d (88h of 128h) |
| Rashmi | 2.4 of 15.0d (19h of 120h) | 6.8 of 15.0d (54h of 120h) |
| Rushika | 0.0 of 20.0d (0h of 160h) | 8.8 of 20.0d (70h of 160h) |
| Vinay | 0.8 of 19.0d (7h of 152h) | 5.1 of 19.0d (41h of 152h) |

## 5. Daily logged time

| Person | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | Logged of available |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Deepak |  |  | 8.0 | 10.0 | 8.0 | 9.0 |  |  |  | 17.0 | 8.0 | 4.0 | 8.0 | 8.0 |  |  | 8.0 | 16.0 | 8.0 | 8.0 |  |  |  | 12.0 | 10.0 | 8.0 |  |  |  |  | 16.0 | 20.8 of 19.5d (166h of 156h) |
| Dhanush |  |  | 8.0 |  | 7.5 |  | 2.0 |  | 5.7 | 8.0 | 10.5 | 12.5 | 15.0 | 7.5 |  |  | 12.0 | 7.0 | L | 9.2 | 4.0 |  |  | 12.0 | 8.0 | 8.0 | 8.0 |  |  |  |  | 18.1 of 18.0d (145h of 144h) |
| Dharshini | 13.5 | 8.0 | L | 5.0 | 4.8 | 3.2 | 1.2 |  | 7.0 | 5.0 | 3.0 | 3.0 | 3.0 |  | 2.0 |  | 6.0 | 7.0 | 10.0 | 2.2 | L |  |  | 3.8 | 5.5 | 3.7 |  |  |  | 6.0 | 5.2 | 13.5 of 18.0d (108h of 144h) |
| Manjunath |  |  | 7.5 | 7.0 | 6.5 | 6.0 | L |  |  | L |  | 7.3 | 7.0 | 7.0 |  |  | 7.0 | 7.0 | 6.5 | 6.0 |  |  |  |  | L | 6.7 | 7.0 |  |  |  | L | 11.1 of 16.0d (88h of 128h) |
| Marish |  |  | 8.5 | 9.0 | 7.0 | 6.0 | 7.0 |  |  | 9.0 | 9.0 | 9.0 | 8.0 | 8.0 |  |  | 6.0 | 9.0 | L | 8.0 |  |  |  | 8.0 | 7.0 |  | 16.0 |  |  |  | 9.0 | 17.9 of 19.0d (144h of 152h) |
| Nagaraju |  |  | 11.2 | 7.2 | 5.0 | 6.8 | 4.9 |  |  | 6.2 | 5.4 | 6.7 | 7.3 | 8.8 |  |  | 9.8 | 5.2 | 7.3 | 7.9 | 8.4 |  |  | 2.0 | 13.8 | 8.0 | 2.3 |  |  |  | L | 16.8 of 19.0d (134h of 152h) |
| Priyanshu |  |  | 2.0 | 8.0 | 8.0 | 8.0 | 1.0 |  | 12.0 | 7.0 | 8.0 | 12.0 | 8.0 |  |  | 8.0 | 9.0 | 10.0 | 6.0 | 6.0 |  |  | 12.0 | 7.0 | 12.0 | 7.0 |  |  |  |  | 10.0 | 20.1 of 20.0d (161h of 160h) |
| Rashmi | 5.0 |  | L | L | L | 6.8 | 5.8 |  |  | 6.7 | L | L | 1.6 | 0.2 |  | 6.0 | 7.2 | 8.1 | 6.7 | 3.4 | 0.8 |  | 1.5 | 3.2 | 3.2 | 3.8 | 0.5 |  |  | 3.5 |  | 9.2 of 15.0d (74h of 120h) |
| Rushika |  |  |  |  | 6.0 | 6.0 |  |  |  | 6.0 | 5.0 |  | 6.0 | 8.0 |  |  | 3.0 |  | 5.0 | 6.0 | 7.0 |  |  | 6.0 |  | 6.0 |  |  |  |  |  | 8.8 of 20.0d (70h of 160h) |
| Sahil Kumar |  |  | 9.0 | 7.0 | 7.0 | 8.0 | 6.0 |  |  | 5.5 | 9.5 | 8.5 | 8.0 | 8.0 |  |  | 8.5 | 8.0 | 8.0 | 12.2 | 8.5 |  |  | 10.0 | 5.5 | 8.5 | 8.5 |  |  |  | 6.0 | 20.0 of 20.0d (160h of 160h) |
| Sahil Siddiqui |  |  | L | 7.8 | 7.2 | 6.0 |  |  | 5.0 | 9.5 | 7.0 | 9.5 | 8.1 | 4.0 |  |  | 7.5 | 10.0 | L | L | 8.5 |  |  | 2.5 | 5.7 | L | 11.1 |  |  |  | 11.7 | 15.1 of 16.0d (121h of 128h) |
| Shambu |  | 6.0 | 7.0 | 6.5 | 7.5 | 10.0 | 3.0 |  |  | 8.0 | 8.0 | 1.0 | 5.0 |  |  |  | 8.8 | 2.5 | 7.5 | 0.5 | 2.0 |  |  | L | 8.0 | 5.5 |  |  |  |  | 8.0 | 13.1 of 19.0d (105h of 152h) |
| Srikant |  |  | 6.0 | 6.0 | 6.0 | 8.0 | 10.0 |  |  | 6.0 | 5.5 | 6.0 | L | L |  |  | 4.0 |  |  | 8.0 | 10.0 |  |  | 5.0 | 5.0 | 5.0 | L |  |  |  | 4.5 | 11.9 of 17.0d (95h of 136h) |
| Sudeep |  |  | 6.0 | 15.5 | 8.1 | 6.7 | 4.0 |  | 7.0 | 8.0 | 8.0 | 1.5 | 17.0 |  |  |  | 8.2 | 4.0 |  | 8.0 |  |  |  | L |  | 26.8 |  |  |  |  | 8.1 | 17.1 of 19.0d (137h of 152h) |
| Surya |  |  |  |  |  | 5.5 | 7.5 |  |  | 8.8 | 6.5 | 7.4 | 7.0 | 7.5 | 3.0 |  | 10.5 | 7.2 |  | 4.0 |  |  |  | 7.7 |  | 5.0 |  | 3.0 | 1.0 |  |  | 11.4 of 20.0d (92h of 160h) |
| Tarun |  |  | 13.0 |  | 16.0 | 1.0 |  |  | 3.0 | 7.5 | 8.0 | 8.0 | 8.0 |  |  | 8.0 | 8.0 | 7.0 | 6.0 | 7.0 |  |  | 7.0 | 8.0 | 0.5 | 8.0 |  |  |  | 7.0 | 7.0 | 17.2 of 20.0d (138h of 160h) |
| Twisha |  | 18.0 | 2.0 | 4.0 | 3.0 | 13.2 | 5.0 |  |  | 6.0 | 1.0 | 9.0 | 4.0 | 2.0 |  |  | 6.0 | L | L | 0.2 | 8.0 |  |  |  | 8.0 | 11.3 |  |  |  |  | 6.0 | 13.3 of 18.0d (107h of 144h) |
| Vinay |  |  | 3.8 | 4.8 | 4.2 |  |  |  |  | 8.0 |  | 6.0 |  |  |  | 10.0 | 5.9 |  |  |  | L |  |  |  |  |  |  |  |  |  | 5.0 | 6.0 of 19.0d (48h of 152h) |

## 6. Scrum call attendance

Team rate **258/332** expected calls (77.7%). 20 recorded Teams scrums, all ~09:30 IST. Leave-adjusted: full-day leave is not a miss; Deepak 12 Aug first-half leave covers the morning call.

- Source: Teams Meeting Summary + Participants sheets (unique person per call).
- Expected call days = weekdays in Aug 2026 with a recorded scrum, excluding Fri 28 public holiday and that person's leave covering the call.
- No weekend calls in the export; weekends are not expected.
- All 20 recorded calls started ~09:30 (morning IST), so Deepak's 12 Aug first-half leave covers the call: not expected, not a miss.
- Full-day leave is never counted as a miss. Joining on a leave day is 'attended on leave' and does not change the rate.
- Rate = attended expected calls ÷ expected calls (leave-adjusted).

Unmatched attendees (not on the retro roster): Dinesh Chandra (13 calls); Saravana Kumar (1 call).

| Person | Expected | Attended | Missed | On leave joined | Attendance | Avg duration |
|---|---:|---:|---:|---:|---:|---|
| Surya | 20 | 0 | 20 | 0 | 0% | — |
| Twisha | 18 | 10 | 8 | 0 | 56% | 15m 39s |
| Manjunath | 16 | 9 | 7 | 0 | 56% | 17m 6s |
| Marish | 19 | 13 | 6 | 0 | 68% | 18m 1s |
| Dharshini | 18 | 13 | 5 | 0 | 72% | 18m 24s |
| Rushika | 20 | 15 | 5 | 0 | 75% | 16m 10s |
| Sudeep | 19 | 15 | 4 | 0 | 79% | 16m 9s |
| Rashmi | 15 | 12 | 3 | 0 | 80% | 13m 51s |
| Dhanush | 18 | 15 | 3 | 0 | 83% | 15m 59s |
| Shambu | 19 | 16 | 3 | 0 | 84% | 18m 8s |
| Srikant | 17 | 15 | 2 | 0 | 88% | 18m 25s |
| Vinay | 19 | 17 | 2 | 0 | 89% | 14m 39s |
| Priyanshu | 20 | 18 | 2 | 0 | 90% | 17m 27s |
| Sahil Siddiqui | 16 | 15 | 1 | 0 | 94% | 19m 9s |
| Deepak | 19 | 18 | 1 | 0 | 95% | 17m 36s |
| Sahil Kumar | 20 | 19 | 1 | 0 | 95% | 17m 20s |
| Tarun | 20 | 19 | 1 | 0 | 95% | 17m 30s |
| Nagaraju | 19 | 19 | 0 | 0 | 100% | 18m 22s |

Daily ticks (P = present, M = missed, L = leave, A = attended on leave):

| Person | 03 | 04 | 05 | 06 | 07 | 10 | 11 | 12 | 13 | 14 | 17 | 18 | 19 | 20 | 21 | 24 | 25 | 26 | 27 | 31 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Deepak | P | P | P | P | P | P | P | L | P | P | P | M | P | P | P | P | P | P | P | P |
| Dhanush | P | M | M | M | P | P | P | P | P | P | P | P | L | P | L | P | P | P | P | P |
| Dharshini | L | M | P | P | M | P | P | P | M | P | P | P | P | P | L | M | P | P | P | M |
| Manjunath | M | P | P | M | L | L | P | M | P | P | M | P | P | P | M | M | L | M | P | L |
| Marish | P | P | P | M | P | P | M | P | P | P | M | P | L | M | P | M | P | M | P | P |
| Nagaraju | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | L |
| Priyanshu | P | P | P | P | M | P | P | P | P | P | M | P | P | P | P | P | P | P | P | P |
| Rashmi | L | L | L | M | M | M | L | L | P | P | P | P | P | P | P | P | P | P | P | P |
| Rushika | P | P | M | P | P | M | P | P | M | P | P | P | P | M | P | P | P | P | P | M |
| Sahil Kumar | P | P | P | P | P | P | P | P | P | P | P | M | P | P | P | P | P | P | P | P |
| Sahil Siddiqui | L | P | P | P | P | P | P | P | P | P | P | P | L | L | M | P | P | L | P | P |
| Shambu | P | P | P | P | P | P | P | P | P | M | P | P | P | P | M | L | M | P | P | P |
| Srikant | P | P | P | P | P | P | P | P | L | L | P | P | M | M | P | P | P | P | L | P |
| Sudeep | P | P | P | P | M | P | P | P | P | P | M | P | M | P | P | L | P | P | M | P |
| Surya | M | M | M | M | M | M | M | M | M | M | M | M | M | M | M | M | M | M | M | M |
| Tarun | P | P | P | P | P | P | M | P | P | P | P | P | P | P | P | P | P | P | P | P |
| Twisha | M | P | P | P | M | P | M | P | P | P | M | L | L | M | M | M | P | P | P | M |
| Vinay | M | P | P | P | P | P | P | P | P | P | P | P | P | P | L | P | P | M | P | P |

## Daily worklogs and comments

### Deepak — 20.8 of 19.5d (166h of 156h)

**2026-08-03** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378) (Task, mid-sprint)
- Worklog 4.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378): AUG sprint feature planning and writing PRD documents
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): docs release related discussions , code review, MR merge and deployments

**2026-08-04** — logged 1.2d (10h) of 1.0d (8h) available, 3 comments

- Worklog 4h on [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378) (Task, mid-sprint)
- Worklog 2h on [HIEV-7031](https://elocity.atlassian.net/browse/HIEV-7031) (Task, mid-sprint)
- Worklog 4h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Comment on [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378): wrote PRDs for sprint features.. All PRDs are under this folder:
- Comment on [HIEV-7031](https://elocity.atlassian.net/browse/HIEV-7031): closing the ticket as this was a self reported task and no testing needed..
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): Security points fixes and notfication channels development.

**2026-08-05** — logged 1.0d (8h) of 1.0d (8h) available, 3 comments

- Worklog 6h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Worklog 2.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-7354](https://elocity.atlassian.net/browse/HIEV-7354): requirement documentation changed a bit and hence updated the estimate as well to 4d as the testing for this to be done by developer only and QA wont be able to test here.. Dinesh has updated requiremnt in same link. https://elocity.atlassian.net/wiki/x/AQBmgQ
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): UX discussion, tenant related discussions with colleagues and incentives related testings.
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): discussion on wallet refund, staging downtime jobs, movem related issue, QA concerns etc..

**2026-08-06** — logged 1.1d (9h) of 1.0d (8h) available, 3 comments

- Worklog 1h on [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378) (Task, mid-sprint)
- Worklog 4h on [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372) (Task, planned)
- Worklog 4h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Comment on [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378): Started reviewing Search framework PRD:
- Comment on [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372): Started listing out the regular activities.
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): incentives ledger UX discussions and requirement writing

**2026-08-10** — logged 2.1d (17h) of 1.0d (8h) available, 8 comments

- Worklog 2h on [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378) (Task, mid-sprint)
- Worklog 2h on [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372) (Task, planned)
- Worklog 2h on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350) (Task, planned)
- Worklog 2h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Worklog 3.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Worklog 6.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378): Reviewd Search framework PRD and need to discuss the same with twisha today
- Comment on [HIEV-7378](https://elocity.atlassian.net/browse/HIEV-7378): This is done as all features in sprint have now PRD written.
- Comment on [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372): continued working on this a bit
- Comment on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350): Reviewd the code and keeping it active as integration has to happen yet.. Once done, will check once and forward to QA
- Comment on [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145): This is done and can be closed.
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): evlm customer transformer apis create to map manually
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): Adani payment gateway call, sprint related leads discussions and syncup with team members on tasks
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): implementation document review on Unique driver schema validator report review ams long token for eipre allen ocpp charger log validator implementation plan. review

**2026-08-11** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 2h on [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372) (Task, planned)
- Worklog 6.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372): sending this ticket to you for review.
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): change log creation by manual commits check for multiple teams discussion on feature implementation with developers

**2026-08-12** — logged 0.5d (4h) of 0.5d (4h) available, 2 comments

- Worklog 2h on [HIEV-7442](https://elocity.atlassian.net/browse/HIEV-7442) (Task, mid-sprint)
- Worklog 2.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-7442](https://elocity.atlassian.net/browse/HIEV-7442): read and compared few security tools for our use case.
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): sprint tasks discussinos with couple of developers and QA and report review

**2026-08-13** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Worklog 4.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): incentive ledger API for mobile creation based on existing designs
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): search filter task implementation doc review and discussion with QA and others plus MR reviews

**2026-08-14** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-7442](https://elocity.atlassian.net/browse/HIEV-7442) (Task, mid-sprint)
- Worklog 4.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-7442](https://elocity.atlassian.net/browse/HIEV-7442): have done a report on this.. will do a last round of checks and attach here.
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): review and planning on search filter and call with sahil to discuss on the same and review of schema validation report and ocpp validotor log implementation plan reveiw and sprint related leads discussion

**2026-08-17** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 4.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Worklog 4h on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722) (Task, mid-sprint)
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): started going through the new features in the backlog and written FRDs to plan ahead discussion with team members on their tasks and review of MRs
- Comment on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722): understanding the root user access and other access for containers and checking the business/technical impact on changing it.

**2026-08-18** — logged 2.0d (16h) of 1.0d (8h) available, 2 comments

- Worklog 4.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Worklog 4h on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722) (Task, mid-sprint)
- Worklog 4h on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722) (Task, mid-sprint)
- Worklog 4h on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722) (Task, mid-sprint)
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): went through backlog feature FRDs and planning.. discussion with team members on sprint related things
- Comment on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722): completed the analysis and testing.. will apply for all services..

**2026-08-19** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-7553](https://elocity.atlassian.net/browse/HIEV-7553) (Task, mid-sprint)
- Worklog 4.00h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Comment on [HIEV-7553](https://elocity.atlassian.net/browse/HIEV-7553): Create 2 FRDs for 2 reports: Idle time report: Log in with Atlassian account Active charging report: Log in with Atlassian account
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): Creating of dashboard and report/export APIs and framework..

**2026-08-20** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 8.00h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): tested and deployed dashboard and report modules for evlm

**2026-08-24** — logged 1.5d (12h) of 1.0d (8h) available, 2 comments

- Worklog 2.00h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Worklog 6.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Worklog 4h on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722) (Task, mid-sprint)
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): git new setup and endpoint changes in backend repos
- Comment on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722): applied to all services…. once the uat releast is done tommorw, this should be completed from application side.. sending it for review after tomorows UAT release.

**2026-08-25** — logged 1.2d (10h) of 1.0d (8h) available, 2 comments

- Worklog 6.00h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Worklog 4.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): customer onabording issue and gitlab endpoint change corrections
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): implementation docs review and task delegation and PRD for one feature and discussions

**2026-08-26** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 6.00h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Worklog 2.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): created mobile insigth and other smaller apis for more section and test of customer onboaring module completion
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): MR reviews and discussions

**2026-08-31** — logged 2.0d (16h) of 1.0d (8h) available, 5 comments

- Worklog 4h on [HIEV-7553](https://elocity.atlassian.net/browse/HIEV-7553) (Task, mid-sprint)
- Worklog 2h on [HIEV-7442](https://elocity.atlassian.net/browse/HIEV-7442) (Task, mid-sprint)
- Worklog 4.00h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Worklog 2.00h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Worklog 2.00h on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938) (Task, planned)
- Worklog 2.00h on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748) (Task, mid-sprint)
- Comment on [HIEV-7553](https://elocity.atlassian.net/browse/HIEV-7553): September sprint planning and sprint excel updation based plus estimation started
- Comment on [HIEV-7442](https://elocity.atlassian.net/browse/HIEV-7442): this report is sticked data of multiple different resources and research. but since the reviews and details about security agents are mostly media based which can be biased, only withs hands on experience we can be sure about the quality and usefulness.
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): on thursday, aug 27th, continued testing app and asked for few changes/fixes….
- Comment on [HIEV-6938](https://elocity.atlassian.net/browse/HIEV-6938): cpms api call from evlm has some strange issue which is taking lot of time to find issue.. still checking
- Comment on [HIEV-6748](https://elocity.atlassian.net/browse/HIEV-6748): MR reviews and merging

### Dhanush — 18.1 of 18.0d (145h of 144h)

**2026-08-03** — logged 1.0d (8h) of 1.0d (8h) available, 8 comments

- Worklog 1h on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377) (Bug, mid-sprint) — Fixed Join Queue back-navigation timeline (settings→slots order, refetch on return) on Station List.
- Worklog 1h on [HIEV-7376](https://elocity.atlassian.net/browse/HIEV-7376) (Bug, mid-sprint) — Fixed infinite loading after connector filter selection on reservation Station List (slots refetch loop); covered with related settings/slots ordering work.
- Worklog 1h on [HIEV-7339](https://elocity.atlassian.net/browse/HIEV-7339) (Bug, mid-sprint) — Investigation and fix for Facilities empty gaps on Location Details (compact 3-column grid layout).
- Worklog 5h on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306) (Task, planned) — AIONEV TestFlight setup – iOS signing, Fastlane, local + CI upload, GitLab CERT_PASSWORD, docs. End-to-end verified.
- Comment on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377): Fix completed for incorrect connector availability after returning from Join Queue (and related Station List slots ordering issues). Root causes addressed: 1) Station List was calling slots before reservation settings finished, so customSlotDuration was not driven by settings.minPeriodMinute. 2) Join Queue with a longer duration (e.g. 60/90 mins) overwrote Redux slots; coming back painted false red half-hour gaps because the list did not refetch with settings duration. 3) Selecting a connector f
- Comment on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377): Update: The related merge request is closed. The fix is available for QA on branch react-doctor-score-improvements (merged). Please test against a build from react-doctor-score-improvements. GitLab branch: https://gitlab.com/elocity1/frontend/mobile/CPMS-MobileApp/-/tree/react-doctor-score-improvements
- Comment on [HIEV-7376](https://elocity.atlassian.net/browse/HIEV-7376): Fix completed for infinite loading after selecting a connector during reservation (HIEV Canada Android). Root cause: on Station List, selecting a connector filter dispatched slots, the reducer cleared slots on REQUEST, and connectorSequence bounced between the selected value and undefined. That re-triggered slots in a tight loop and left the screen stuck in loading. Related issues in the same flow (also fixed on the same branch): settings vs slots call order, and incorrect red timeline gaps afte
- Comment on [HIEV-7376](https://elocity.atlassian.net/browse/HIEV-7376): Update: The related merge request is closed. The fix is available for QA on branch react-doctor-score-improvements (merged). Please test against a build from react-doctor-score-improvements. GitLab branch: https://gitlab.com/elocity1/frontend/mobile/CPMS-MobileApp/-/tree/react-doctor-score-improvements
- Comment on [HIEV-7339](https://elocity.atlassian.net/browse/HIEV-7339): Fix completed for the Facilities empty-gap layout on Location Details (HIEV Canada Android). Root cause: the facilities grid was not packing items into available columns before wrapping, which left unused cells and uneven rows when a station had multiple facilities. Change: updated the facilities section to a compact sequential 3-column layout so available grid positions are filled before starting a new row. Verification: open Location Details for a station with multiple facilities and confirm t
- Comment on [HIEV-7339](https://elocity.atlassian.net/browse/HIEV-7339): Update: The related merge request is closed. The fix is available for QA on branch react-doctor-score-improvements (merged). Please test against a build from react-doctor-score-improvements. GitLab branch: https://gitlab.com/elocity1/frontend/mobile/CPMS-MobileApp/-/tree/react-doctor-score-improvements
- Comment on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306): Progress – 3 Aug AIONEV Android + iOS store / CI path is done and tested end to end (Play Internal + TestFlight). Android / Play Release keystore wired in (elocityAionevKeyRelease) and Play service account JSON committed Fastlane Android lanes: build AAB + upload to Play Internal (draft); fixed repo-root / JSON path issues Local AAB built and uploaded to Play Internal successfully GitLab jobs: build_android_aab + deploy_android_internal; Mac Mini runners assigned to aionev so jobs actually pick 
- Comment on [HIEV-7240](https://elocity.atlassian.net/browse/HIEV-7240): which environment is it present ?

**2026-08-05** — logged 0.9d (8h) of 1.0d (8h) available, 4 comments

- Worklog 2h on [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385) (Bug, mid-sprint) — HIEV-7385: investigated Sunday Closed mismatch (JS getDay vs OCPI ISO weekday); fixed CardHeader/Map/ChargingLocation with getISODay; updated unit tests; branched from chargem-prod-2026-07-20 and cherry-picked to react-doctor-score-improvements and feature/evlm-enrollment; pushed branches for QA / upcoming Movem DOTA.
- Worklog 3h on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306) (Task, planned) — Rev2 design review vs AIONEV, theme token + copy polish, iOS sim verify, push + Play Internal / TestFlight pipeline for 1.0.0 (3).
- Worklog 2h 30m on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) (Task, mid-sprint) — CI Android reanimated pollution + worklets prefabReleasePackage fix
- Comment on [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385): Update — fix ready for QA / DOTA Root cause: Location Details / cards used JS getDay() (Sunday=0) against API/OCPI regularHours.weekday (Monday=1 … Sunday=7), so Sundays falsely showed Closed . Fix agreed / implemented getISODay() in CardHeader (Location Detail open status), MapComponent (closed markers), and ChargingLocation for consistency. Mon–Sat card behavior unchanged (1–6 already matched ISO); Sunday now correctly uses 7. Unit tests updated + HIEV-7385 Sunday regression coverage. Branches
- Comment on [HIEV-7309](https://elocity.atlassian.net/browse/HIEV-7309): Since its working as expected i have moved it to done status
- Comment on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306): Progress – 5 Aug Went through the new EV Driver Rev2 design flow against AIONEV. Primary theming was already in place; finished the remaining token/copy gaps and shipped a new internal build. UI / design alignment Compared Rev2 standalone design screen-by-screen (onboarding → Home/Reports/Rewards/Support/Profile + Wi-Fi/fault flows) — coverage already matched Added missing Rev2 accent tokens (infoCyanBg/Dark, infoBody, warningDeep, tipBorder, onPrimary) to brandData Replaced leftover hardcoded c
- Comment on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073): CI: Android assemble release failures (reanimated + worklets prefab) Problem 1 — reanimated Hiev Canada UAT assemblehievCanadaRelease failed: AnimatedSensorModule.h / leftover NativeReanimatedModule.* from polluted shared-runner node_modules (CMake GLOB_RECURSE). Fix: scripts/ci-clean-stale-native-modules.sh — reanimated_tree_polluted() detects stale NativeReanimatedModule / missing ReanimatedModuleProxy; refuse stamp + wipe. GitLab cache key bumped to v7 . Commits: e3e0690e6 on react-doctor-sco

**2026-08-07** — logged 0.2d (2h) of 1.0d (8h) available, 1 comments

- Worklog 2h on [HIEV-7414](https://elocity.atlassian.net/browse/HIEV-7414) (Sub-task, mid-sprint) — Smartcar RTDB override for all brands/envs; enableConnectMyCar RTDB+appConfig fallback; commits pushed to react-doctor-score-improvements and feature/evlm-enrollment.
- Comment on [HIEV-7414](https://elocity.atlassian.net/browse/HIEV-7414): Follow-up work completed for Smartcar Firebase RTDB config override (all brands / all envs): Pulled latest react-doctor-score-improvements and feature/evlm-enrollment. Brought Smartcar RTDB override from feature/evlm-enrollment onto react-doctor-score-improvements. Extended resolveSmartcarConfig so non-empty RTDB values override .env/apiConfig for development, staging, UAT, and production (all flavors). enableConnectMyCar: RTDB true enables Connect My Car; bundled appConfig remains fallback (set

**2026-08-09** — logged 0.7d (6h) of 0.0d (0h) available, 4 comments

- Worklog 10m on [HIEV-7232](https://elocity.atlassian.net/browse/HIEV-7232) (Suggestion, mid-sprint) — Reviewed ticket and noted Product + UX approval gate before Mobile pickup.
- Worklog 30m on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) (Task, mid-sprint) — Prepared Smartcar Connect My Car API contract doc and shared with Sahil (battery/charge/odometer/location/controls live vs mocked).
- Worklog 5h on [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836) (Epic, mid-sprint) — HIEV-5836: campaign cold-start fix, Firebase path, overlay sequencing (tour → biometric → campaign), modal UX polish, tests.
- Comment on [HIEV-7232](https://elocity.atlassian.net/browse/HIEV-7232): All changes for this ticket need to go through the Product team and UX for review/approval first. Only after Product + UX sign-off can Mobile pick this up for development.
- Comment on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073): Smartcar / Connect My Car — API contract shared with Sahil Prepared and shared the Smartcar (Connect My Car) mobile API contract document with Sahil for backend/QA alignment. Document path: docs/smartcar-connect-my-car-api-contract.md Covers: Always-live endpoints (auth code exchange, list vehicles, rename) Vehicle data/control endpoints currently mocked by default: battery, charge (plugged-in/state), odometer, location, start/stop charge, lock/unlock Expected request/response shapes, OAuth scop
- Comment on [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836): Ready for Testing — HIEV-5836 In-App Campaign Branches updated: • react-doctor-score-improvements (c4d349f18) • feature/evlm-enrollment (cherry-pick 1c57db630) What was fixed / delivered: 1. Campaign modal not showing for logged-in users (cold start) - Root cause: gate used auth.access_token, which TokenSanitizer strips from Redux - Fix: gate on isLoggedIn && !isLoggingOut 2. Firebase campaigns path - App now reads env-aware path: /environments/{env}/config/campaigns (staging/UAT) or /config/cam
- Comment on [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836): Assigned to Nagaraju for QA retest (Ready for Testing). Please follow the test plan in the previous comment. Branches: react-doctor-score-improvements @ c4d349f18 and feature/evlm-enrollment @ 1c57db630.

**2026-08-10** — logged 1.0d (8h) of 1.0d (8h) available, 3 comments

- Worklog 2h on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446) (Bug, mid-sprint) — HIEV-7446: investigate maxDisplayCount bypass (count-on-close), fix count-on-show, tests, cherry-pick to feature/evlm-enrollment.
- Worklog 3h on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446) (Bug, mid-sprint) — HIEV-7446: re-investigate every-launch bypass, harden normalize/max enforcement/race/single listener, tests, cherry-pick.
- Worklog 3h on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446) (Bug, mid-sprint) — HIEV-7446: re-investigate every-launch bypass, harden normalize/max enforcement/race/single listener, tests, cherry-pick.
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Ready for Testing — HIEV-7446 maxDisplayCount not enforced Work logged: 2h Branches / commits: • react-doctor-score-improvements → f0226af15 • feature/evlm-enrollment → ec2b92b23 (cherry-pick) Root cause: Campaign displayCount in AsyncStorage was incremented only when the user closed the modal (X / Got it). If the user force-quit the app, navigated away, or otherwise dismissed without hitting close, the impression was never recorded. On the next cold start, campaignsShownInSession reset (not per
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Ready for Testing (retest) — HIEV-7446 maxDisplayCount still not enforced Work logged: 3h (deep re-investigation + harden fix) Branches / commits: • react-doctor-score-improvements → f9ee5e63a • feature/evlm-enrollment → cherry-pick of f9ee5e63a Why the previous fix was not enough: Counting on modal open fixed force-quit without close, but QA still saw Welcome on every launch. Root causes found on re-investigation: 1. Fail-open max check — if displayRules.maxDisplayCount was missing/mis-nested/u
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Ready for Testing (retest) — HIEV-7446 maxDisplayCount still not enforced Work logged: 3h (deep re-investigation + harden fix) Branches / commits: • react-doctor-score-improvements → f9ee5e63a • feature/evlm-enrollment → cherry-pick of f9ee5e63a Why the previous fix was not enough: Counting on modal open fixed force-quit without close, but QA still saw Welcome on every launch. Root causes found on re-investigation: 1. Fail-open max check — if displayRules.maxDisplayCount was missing/mis-nested/u

**2026-08-11** — logged 1.3d (10h) of 1.0d (8h) available, 4 comments

- Worklog 3h 30m on [HIEV-7472](https://elocity.atlassian.net/browse/HIEV-7472) (Task, mid-sprint) — Universal Energies production release work: tag universal-energies-prod-2026-07-17 baseline, Android 6.4.0 release, iOS App Store submission (In Review). Extra time for Apple Distribution certificate issues (expired/signing setup) and pod installation during the iOS archive/build path.
- Worklog 2h on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458) (Bug, mid-sprint) — Investigated New Login country picker loader + all-countries flash. Root cause: empty [] metadata treated as loaded + LoaderIcon while METADATA_REQUEST loading. Implemented resolveCountryCodesFromMetadata fallback, removed country-box loader, remount picker on codes change, and added/updated unit tests.
- Worklog 2h on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446) (Bug, mid-sprint) — HIEV-7446: multi-campaign maxDisplayCount/cooldown/onlyOnce enforcement, RTDB casing fix, race fixes, tests, push to react-doctor-score-improvements + feature/evlm-enrollment.
- Worklog 1h on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) (Task, planned) — Investigated Firebase App Check debug-token setup for Adani Razorpay E2E (iOS simulator vs real device). Confirmed Adani-CMS tokens already registered; documented rebuild + append-app-check-env steps and posted runbook comment on ticket.
- Worklog 2h on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942) (Task, planned) — Smartcar Connect My Car backend contract integration (get-smartcar-info, actions, disconnect, mock flag, tests) on feature/evlm-enrollment.
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Fix verified and pushed for retest (HIEV-7446 — multi-campaign display rules). Root cause 1) Welcome campaign in Canada staging RTDB used typo key maxdisplayCount (lowercase d) instead of maxDisplayCount, so the app treated max as missing and either dropped welcome from the multi-campaign carousel or previously allowed unlimited shows. 2) Show-path races could mark the session as shown without presenting the modal (tour/biometric enabled flicker). 3) Impression counting / persistence needed hard
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): App Check debug tokens — Adani iOS E2E (simulator vs real device) Confirmed: Adani-CMS Firebase already has the shared tokens registered ( cpms-local-dev , cpms-qa-sideload , cpms-ci-emulator ). No need to add new tokens in the console unless the build is generating a different UUID. Important: App Check is required for OTP login (v6). Razorpay itself does not send App Check headers — failures usually happen at login OTP before reaching wallet/Razorpay. A) iOS Simulator (recommended for Maestro)
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): Original estimate increased by +1d (2d → 3d). Initial setup/understanding of the ticket and first-time App Check / device / Maestro environment setup for Dharshini hit multiple blockers, so the estimate was adjusted to reflect that ramp-up time.
- Comment on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942): Smartcar Connect My Car — backend API contract integration Aligned mobile Connect My Car with the backend Smartcar contract on feature/evlm-enrollment and pushed. Vehicle Details reads via GET /mobile/v1/smart-car/get-smartcar-info Actions via POST /vehicle/{action}/{vehicleId} (start/stop charge, lock/unlock, disconnect) Null telemetry blocks handled as empty; SMARTCAR_USE_MOCK_DATA mocks get-smartcar-info only Commit: feat(HIEV-6942): align Smartcar Connect My Car with backend API contract Tim

**2026-08-12** — logged 1.6d (12h) of 1.0d (8h) available, 13 comments

- Worklog 1h on [HIEV-7479](https://elocity.atlassian.net/browse/HIEV-7479) (Bug, mid-sprint) — Verified map render on HIEV Canada Android staging build from GitLab job 15854547329 after related react-doctor / map fixes. Map and app usable; marking Ready for Testing.
- Worklog 50m on [HIEV-7476](https://elocity.atlassian.net/browse/HIEV-7476) (Bug, mid-sprint) — Connector icons on Upcoming/Past reservation cards with fallback + tests. Cherry-pick to feature/evlm-enrollment.
- Worklog 2h 30m on [HIEV-7475](https://elocity.atlassian.net/browse/HIEV-7475) (Bug, mid-sprint) — 12-hour AM/PM formatting across reservations, notifications, home charging, reports, and shared helpers/tests. Cherry-pick to feature/evlm-enrollment.
- Worklog 40m on [HIEV-7474](https://elocity.atlassian.net/browse/HIEV-7474) (Bug, mid-sprint) — Reservation card schedule readability (middle-dot date/time). Implementation, tests, and cherry-pick to feature/evlm-enrollment.
- Worklog 2h on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458) (Bug, mid-sprint) — Cold-start BootSplash (GIF / AppLogo), remove LoaderIcon from Entrypoint + profile gate, unit tests, MR !488 merge follow-up, cherry-pick to feature/evlm-enrollment.
- Worklog 1h on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446) (Bug, mid-sprint) — HIEV-7446: root-cause + fix for multi-campaign impression counting — count per viewed page so closing campaign-001 does not exhaust campaign-002; tests + push to react-doctor-score-improvements and feature/evlm-enrollment.
- Worklog 1h on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) (Task, mid-sprint) — Investigated GitLab Jest CI failures; fixed 3 unit tests (formatDuration NaN, Reports helpers spy, CustomCalendarModal onApply); pushed to react-doctor-score-improvements and feature/evlm-enrollment.
- Worklog 1h on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) (Task, mid-sprint) — Fixed CI Jest log overflow (4MB) and async timer leaks: FilterBar/SmartcarAuth/CustomPayment cleanup, jest.setupAfterEnv console mute, Firebase Perf mock; verified full suite (558/7742); pushed to react-doctor-score-improvements and feature/evlm-enrollment.
- Worklog 1h 30m on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) (Task, mid-sprint) — CI: disable broken SAST/DS yellow jobs; Pods cache symlink noise; React Doctor score gate (79→81+); unit_test coverage gate (EVLM/Fleet shell exclusions). Planned later: EVLM + Fleet orchestration unit tests.
- Worklog 1h on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) (Task, mid-sprint) — Attended Alectra meeting (1h).
- Comment on [HIEV-7479](https://elocity.atlassian.net/browse/HIEV-7479): — Moving this to Ready for Testing. Update: This issue is resolved and working as expected. It was addressed as part of the related fixes (the earlier react-doctor-score work was half-done when a build was taken, which likely surfaced this blank-map behavior). Verified on: Brand/Platform: HIEV Canada — Android (staging) GitLab job (build used for testing): https://gitlab.com/elocity1/frontend/mobile/CPMS-MobileApp/-/jobs/15854547329 Result: Map rendered correctly after fresh install/login; appli
- Comment on [HIEV-7476](https://elocity.atlassian.net/browse/HIEV-7476): Implementation update — In Progress Added connector icons on Upcoming/Past reservation cards alongside connector information, with a safe fallback icon when a type-specific asset is unavailable. Also adjusted list card layout/styles for icon + text alignment. Unit tests updated for the new reservation list behavior. Commits: 3bfba8cb4 on react-doctor-score-improvements; cherry-picked as d4fde752a on feature/evlm-enrollment. Next: device QA on Upcoming/Past cards for multiple connector types, the
- Comment on [HIEV-7475](https://elocity.atlassian.net/browse/HIEV-7475): Implementation update — In Progress Standardized user-facing times to 12-hour format with AM/PM across the app (not only reservation booking slots). Scope includes reservations, notifications, home charging schedules/time picker, reports hour labels, maintenance/location/transcript surfaces, plus shared formatClockTime helper and tests. Commits: 3bfba8cb4 on react-doctor-score-improvements; cherry-picked as d4fde752a on feature/evlm-enrollment. Next: device QA across the listed surfaces, then mo
- Comment on [HIEV-7474](https://elocity.atlassian.net/browse/HIEV-7474): Implementation update — In Progress Updated reservation card schedule formatting for readability using a middle-dot separator, e.g. “Aug 12 2026 · 11:45 AM - 12:45 PM”. Changes cover new reservation list/details and related date-time formatting helpers. Unit tests updated. Commits: 3bfba8cb4 on react-doctor-score-improvements; cherry-picked as d4fde752a on feature/evlm-enrollment. Next: device QA on Upcoming/Past reservation cards, then move to Ready for Testing once estimates/worklog are confir
- Comment on [HIEV-7472](https://elocity.atlassian.net/browse/HIEV-7472): Worklog updated from 2h 30m → 3h 30m (+1h). Additional time spent on Apple Distribution certificate issues (expired/signing setup) and pod installation during the Universal Energies iOS archive/build path for the 6.4.0 production release.
- Comment on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458): Ready for QA. Merged: https://gitlab.com/elocity1/frontend/mobile/CPMS-MobileApp/-/merge_requests/488 → react-doctor-score-improvements Cherry-picked onto feature/evlm-enrollment (cf0956dc3). Covered: (1) country-code loader flash + first-open all-countries filter, (2) cold-start branded BootSplash instead of LoaderIcon. Please verify on STAGE Android/iOS per acceptance criteria in the description. Assigning to reporter for testing.
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Update — multi-campaign maxDisplayCount (QA feedback) Root cause In a multi-campaign carousel, every open recorded an impression for all eligible campaigns at once (not only the page the user was looking at). So if campaign-001 and campaign-002 were both in the modal and the tester closed while on campaign-001 five times, campaign-002’s maxDisplayCount was also incremented each time. After campaign-001 hit its max, campaign-002 looked exhausted too and never appeared alone — even when it still h
- Comment on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306): blocked from backend side so moving to TO DO
- Comment on [HIEV-7150](https://elocity.atlassian.net/browse/HIEV-7150): Blocked from backend side so moving to to do.
- Comment on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073): CI: Jest unit test failures (formatDuration / Reports / CustomCalendarModal) GitLab unit-test job on react-doctor-score-improvements failed with 3 assertion failures (other suites only had console noise, which does not fail Jest). Fixes helpers.formatDuration(NaN): updated unit test to expect empty string — matches helper JSDoc (invalid inputs blank for charts). Reports screen test: removed jest.spyOn(helpers, 'formatDuration') — Reports uses a local formatDuration; helpers is auto-mocked via Pr
- Comment on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073): CI: Jest console noise / async timer cleanup (GitLab 4MB log limit) Follow-up after the assertion fixes: the GitLab unit-test job log hit the 4MB cap (mostly Analytics console.log + act()/Cannot log after tests spam). Leaked FilterBar setTimeouts also crashed later suites (e.g. BuildDetails via Platform.OS after teardown). Fixes Timer cleanup on unmount: FilterBar scroll retries, SmartcarAuth WebView timeouts, CustomPayment fetchBalances delay. jest.setupAfterEnv.js: mute expected Analytics/act/
- Comment on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073): AdHoc CI follow-up on feature/evlm-enrollment (and mirrored on react-doctor-score-improvements where applicable): Cleared yellow GitLab security jobs (semgrep / gemnasium / gemnasium-maven): Docker-only analyzers were failing on Mac shell (/analyzer missing) or unauthorized security-products image pulls — disabled until infra has a working Docker runner + registry access. yarn lint:security still runs. Stopped caching ios/Pods to remove symlink "file exists" noise on Mac runners. React Doctor sc
- Comment on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073): Attended Alectra meeting Joined the Alectra meeting for discussion/alignment. Logged 1h against AdHoc.

**2026-08-13** — logged 1.9d (15h) of 1.0d (8h) available, 4 comments

- Worklog 1d on [HIEV-7496](https://elocity.atlassian.net/browse/HIEV-7496) (Task, mid-sprint) — ChargeM OTA investigation and HIEV-7385 Sunday-fix delivery: staging 10.0.0 rehearsal (Android S20 FE + iOS simulator), Production 9.5.0 publish, immediate Production disable after crash, and Play Store / App Store native release path due to business case.
- Worklog 3h on [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477) (Suggestion, mid-sprint) — Implemented extra reservation entry points (+ on Reservation list and Reserve on Location List cards), shared navigation helpers, i18n, and unit tests.
- Worklog 4h on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306) (Task, planned) — EMS OpenAPI review, client/adapters, screen wiring (Home, Diagnostics, Session, Reports, New ticket), tests, push, and internal store pipeline.
- Comment on [HIEV-7496](https://elocity.atlassian.net/browse/HIEV-7496): Work log — 13 Aug 2026 Full sequence of what we did on ChargeM DOTA, and why we ended on a normal store release. 1. Context HIEV-7385 Sunday-closed JS fix on branch fix/HIEV-7385-sunday-iso-weekday . Same-day HIEV America Production OTA crashed on store 1.4.0 with installTurboModule (JS vs native mismatch). America Production left Disabled. That failure is the same class as ChargeM Production later. ChargeM store version at the time: 9.5.0 . Tag used: chargem-prod-2026-07-20 . 2. Staging rehears
- Comment on [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477): Worked on this on branch react-doctor-score-improvements . Additional reservation entry points are in place without changing booking logic. 1. Reservation tab Added a + action in the top-right of the Upcoming/Past reservation screens. Tapping it opens Location List so the user can pick a station and continue into the existing charger/time reservation flow. 2. Location List Reserve button Reserve now appears next to Directions on reservable location cards. The list payload uses isReservable, but 
- Comment on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306): Progress – 13 Aug Picked up the EMS OpenAPI spec from Vinay (status, diagnostics, session curtailment, reports summary/buckets). Contract is ~70–80% locked so the client is adapter-based. Mapped onto AIONEV screens: Home → GET /mobile/v1/ems/status (charging / curtailed / FALLBACK fault + measured kW) Status & Diagnostics → GET /diagnostics (links + faults; live path when mock is off) Session detail → GET /sessions/{id}/curtailment (timeline + curtailed duration) Reports → summary + buckets for 
- Comment on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942): Still blocked hence moving to TO-DO

**2026-08-14** — logged 0.9d (8h) of 1.0d (8h) available, 1 comments

- Worklog 1h on [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477) (Suggestion, mid-sprint) — Manual verification of HIEV-7477 reservation entry points on HIEV Canada staging release 20.0.0 (1): S20 FE emulator and physical Samsung device. Moved ticket to Ready for Testing.
- Worklog 6h 30m on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) (Task, mid-sprint) — iOS CI on Xcode 26: provisioning decode without security cms, Podfile.lock/PODS_ROOT, CocoaPods --project-directory equals form, System.keychain/SHA codesign, Library/Keychains + login-keychain archive signing. Pushed to react-doctor-score-improvements and cherry-picked to feature/evlm-enrollment.
- Comment on [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477): Moved to Ready for Testing and assigned to the reporter for QA. Implementation was verified on HIEV Canada staging (20.0.0 / 1) on Samsung S20 FE emulator and a physical Samsung device. Booking logic is unchanged; this only adds reservation entry points. Please cover: Reservation tab: + in the top-right opens Location List, then selecting a reservable location continues into the existing charger/time flow. Location List: Reserve is shown next to Directions on reservable stations and starts the s

**2026-08-17** — logged 1.5d (12h) of 1.0d (8h) available, 4 comments

- Worklog 4h on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557) (Task, mid-sprint) — Proposal, firmware contract, BLE framing/crypto/session, and in-app charger emulator.
- Worklog 2h on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) (Task, planned) — Code review of MR !489 (Maestro E2E wallet/card payment coverage). No Critical or High findings; Approve with nits. MR merged to react-doctor-score-improvements and cherry-picked to feature/evlm-enrollment.
- Worklog 6h on [HIEV-7150](https://elocity.atlassian.net/browse/HIEV-7150) (Task, planned) — Fleet mobile API contract integration on feature/evlm-enrollment: stations/start/stop, reused detail + history dates, own live session poll, zero tariff, 403 hide-tab, and contract-gap fixes from review.
- Comment on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306): Whatever integrations are done its completed and its blocked till backend provides more contracts sending to TO-DO
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): Code review complete — no Critical / High findings Code review for MR !489 (Maestro E2E: brand payment flows) is done. Cursor Agent deep review on the MR reported Critical: None and High: None . Verdict was Approve with nits only (Medium/Nits are non-blocking). Merge Merged into react-doctor-score-improvements (merge commit f7bfd2083). Cherry-picked onto feature/evlm-enrollment as 237966f73. Logging 2h for the review. Moving this ticket to Done.
- Comment on [HIEV-7150](https://elocity.atlassian.net/browse/HIEV-7150): Picked this up again after the mobile fleet API contract. Work is on feature/evlm-enrollment (commits 0c3380fa, 2ff5089b, 9b33d46e). Done Fleet Stations: GET /fleet/mobile/stations (JWT, no businessId). Search and group chips still filter client-side after one list fetch. Station Detail: reuses GET /mobile/v2/evse-connectors plus list cache. Start/stop use POST /fleet/mobile/stations/:evseUid/connectors/:connectorId/start|stop with empty body. Zero tariff: fleet connectors hide price and skip pr
- Comment on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073): iOS CI / Xcode 26 archive signing (14 Aug) Unblocked Mac Mini iOS archive jobs failing on Xcode 26 / macOS 26. Fixes applied on react-doctor-score-improvements and cherry-picked to feature/evlm-enrollment once the pipeline was green. What was fixed Decode iOS provisioning profiles without security cms (macOS 26 incompatibility). Keep Podfile.lock and pin PODS_ROOT so archive pod install is stable. Pass CocoaPods --project-directory as equals form (CLI parsing on newer CocoaPods). Keep System.key

**2026-08-18** — logged 0.9d (7h) of 1.0d (8h) available, 0 comments

- Worklog 5h on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557) (Task, mid-sprint) — Device stabilisation: PRNG crash, session/chunk bugs, physical walkthrough of first-time setup and change-Wi-Fi (rollback + success), 152 tests.
- Worklog 2h on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) (Task, mid-sprint) — HiEV Canada production release AAB (3.0.1 / 54) — cherry-pick HIEV-7271 from July tag, production config, assemble.

**2026-08-20** — logged 1.1d (9h) of 1.0d (8h) available, 8 comments

- Worklog 10m on [HIEV-7559](https://elocity.atlassian.net/browse/HIEV-7559) (Bug, mid-sprint) — Updated HiEV Canada staging Stripe publishable key and pushed to react-doctor-score-improvements and feature/evlm-enrollment.
- Worklog 2h on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557) (Task, mid-sprint) — Full-app UI restyle, team email draft, GitLab ticket, and release APK rebuild (HIEVConfigurator-demo.apk).
- Worklog 4h on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557) (Task, mid-sprint) — Standalone proposal/flows/GATT package, ARM64 demo zip under the mail size limit, and review email sent to Dinesh Chandra.
- Worklog 3h on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306) (Task, planned) — Alectra login/register Figma redesign, Lexend Deca app-wide, and internal TestFlight + Play Internal 1.0.0 (5).
- Comment on [HIEV-7559](https://elocity.atlassian.net/browse/HIEV-7559): Updated HiEV Canada staging Stripe publishable key to resolve the PaymentIntent client secret mismatch seen when adding money to the wallet on Android staging. Root cause: the mobile app staging publishable key did not belong to the same Stripe account that created the backend PaymentIntent. Changes pushed: react-doctor-score-improvements — commit 87a564d64 feature/evlm-enrollment — commit 9262970cc app/hiev-canada/config/apiConfig.ts (staging stripe_key only) QA verification (HiEV Canada stagin
- Comment on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557): Work log — 17–18 Aug Proposal + firmware contract + BLE stack. Mapped Lovejeet’s four objectives to app vs firmware. Built framing/chunking, GATT transport, session state machine, crypto handshake (cert + transcript), Wi-Fi validation taxonomy, rollback, lockout, audit (no passwords in logs). In-app emulator so development and demo do not wait on hardware. Docs: proposal, end-to-end flows, GATT spec.
- Comment on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557): Work log — 18 Aug (device) Stabilised the demo on a physical Android phone. Launch crash (PRNG / tweetnacl) fixed; honeycomb logo; Android 15 safe area. Session bugs: overlapping connect attempts and out-of-order BLE chunks — both would have shown up on real firmware too; added as firmware non-negotiables. Walked first-time setup and “change Wi-Fi on a charger already set up” (wrong password → rollback; correct password → success, encrypted audit line). 152 tests passing. Demo password on emulat
- Comment on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557): Work log — 20 Aug (UI + email + APK) Restyled remaining screens to match provisioning: sign-in, forgot password, map, dashboard, device/customer lists, profile, menu, location/charger details. Shared Input / Dropdown / Button / hamburger menu updated so AMS login and the rest of the operator app look like one product. Email draft for Lovejeet/Jayant (paste-ready, no git links). Firmware needs are listed; no “decisions for Monday” section. Release APK rebuild for demo. Due: 31 Aug 2026. App side 
- Comment on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557): Work log — 20 Aug (package shared with Dinesh) Review package sent to Dinesh Chandra for confirmation before it goes to the wider group. Attached: PROPOSAL.md — BLE provisioning proposal (standalone; no personal ask-language). FLOWS.md — end-to-end diagrams for the Operator BLE path. FIRMWARE-GATT-SPEC.md — GATT / protocol contract for firmware. HIEVConfigurator-demo.zip — ARM64 demo APK, zipped to 19 MB so it can be mailed (under the 34 MB limit). Email asks Dinesh whether the package is fine a
- Comment on [HIEV-7306](https://elocity.atlassian.net/browse/HIEV-7306): Progress – 20 Aug Redid the Alectra login / register flow against the Figma (Alectra Login & register). New path is phone login → 4-digit OTP → Setting up your account → Complete registration (terms checkbox) → Register charger → success, then the existing Wi-Fi onboarding. Legal pages now use the same header chrome. Also switched the app to Lexend Deca globally (iOS + Android + Paper), not just the auth screens. Pushed to master: 81f15e2 . Internal builds kicked off for 1.0.0 (5) — Play Interna
- Comment on [HIEV-7150](https://elocity.atlassian.net/browse/HIEV-7150): Blocked as of now so moving the ticket to TO-DO status.
- Comment on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073): HiEV Canada production release APK / AAB (18 Aug) Prepared and built the HiEV Canada production Android release from tag hiev-canada-prod-2026-07-17 (hotfix branch hotfix/hiev-canada-HIEV-7271-location-deny ). Cherry-picked HIEV-7271 — stop map re-render loop when location access is denied. Generated production config and bumped Android to 3.0.1 (versionCode 54) . Assembled HiEV Canada production app-hievCanada-release.aab . Logged 2h against AdHoc.

**2026-08-21** — logged 0.5d (4h) of 0.0d (0h) available, 0 comments

- Worklog 4h on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557) (Task, mid-sprint) — Lovejeet feedback that the first draft was not joint/implementation-ready; questionnaire to Jayant on GATT, advertise window, security, and fallback.

**2026-08-24** — logged 1.5d (12h) of 1.0d (8h) available, 0 comments

- Worklog 4h on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557) (Task, mid-sprint) — Firmware answers from Jayant (FFF0/FFF1/FFF2, RFID window, BLE/Wi-Fi exclusive, reboot, PIN, no OCPP over BLE); align the app contract.
- Worklog 1d on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942) (Task, planned) — Elocity Grid+ brand + store setup: new white-label app (com.elocity.gridplus.app), Firebase/Play/iOS signing wired, pushed on feature/evlm-enrollment (cfe2fc863).

**2026-08-25** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 1d on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942) (Task, planned) — Elocity Grid+: CA_THY tenant, CodePush keys, Play Fastlane SA on elocity-grid (fastlane-elocitygrid), CI parity. Commit 45957a997 on feature/evlm-enrollment.
- Comment on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942): Elocity Grid+ white-label app — native brand scaffold and store identity (24 Aug) Created the Elocity Grid+ mobile brand for EVLM on feature/evlm-enrollment, reusing HiEV Canada logos as placeholders until brand assets are confirmed. Build / identity Android flavor elocityGridPlus and iOS scheme elocityGridPlusMobileApp Bundle/package ID set to com.elocity.gridplus.app after Apple rejected com.elocity.gridplus; notification extension nested under that ID Wired Canada tenant CA_ELO with Stripe, S

**2026-08-26** — logged 1.0d (8h) of 1.0d (8h) available, 3 comments

- Worklog 2.00h on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073) (Task, mid-sprint)
- Worklog 6h on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942) (Task, planned) — EVLM enrollment resume + post-enrollment API wiring on feature/evlm-enrollment (9c44abb92, 6596ac442). Compared against EVLM backend master; leftover Demand Response disabled.
- Comment on [HIEV-7073](https://elocity.atlassian.net/browse/HIEV-7073): CI: HiEV Canada staging Android APK (26 Aug) Unblocked assemblehievCanadaRelease on Mac Mini shell runner 4DyBoSaQl for feature/evlm-enrollment (HiEV Canada staging). Same fixes mirrored to react-doctor-score-improvements . Ignored log noise: yarn cache miss / peer deps, SDK XML, AGP package= in manifests, Kotlin deprecations, worklets-core -Wexceptions, babel isModuleDeclaration, Fastlane 2.238.0 notice. Issues found and fixed 1. otp-verify compile — Auth.GOOGLE_SIGN_IN_API App JS only uses RNO
- Comment on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942): Elocity Grid+ — Play Fastlane account, tenant, CodePush, App Check prep (25 Aug) Continued EVLM mobile brand setup on feature/evlm-enrollment. Switched API tenant from CA_ELO to CA_THY; Stripe still used for Grid+ payments Wired Android/iOS CodePush staging and production keys CI builds use committed Play JSON + keystore (same as Alfanar/HiEV America) — no extra GitLab secret Imported Play Fastlane service account fastlane-elocitygrid@elocity-grid.iam.gserviceaccount.com (Firebase project elocit
- Comment on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942): EVLM mobile API integration — enrollment + post-enrollment (26 Aug) Continued HIEV-6942 on feature/evlm-enrollment. Wired live EVLM customer APIs against backend master, then fixed onboarding resume so in-progress customers are not treated as new enrollments. Shipped on feature/evlm-enrollment 9c44abb92 — feat(evlm): wire post-enrollment APIs and stop leftover Demand Response 6596ac442 — fix(evlm): resume onboarding from status instead of Enroll Now Enrollment Home gates on GET /evlm/v1/customer

**2026-08-27** — logged 1.0d (8h) of 1.0d (8h) available, 0 comments

- Worklog 1d on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557) (Task, mid-sprint) — Implement ESP32 firmware BLE v1 on feature/esp32-firmware-ble-v1, rewrite proposal/flows/GATT pack, rebuild demo APK, push 15e34c5.

**2026-08-31** — logged 0.0d (0h) of 1.0d (8h) available, 1 comments

- Comment on [HIEV-7557](https://elocity.atlassian.net/browse/HIEV-7557): Work log — 21–27 Aug (firmware v1) Lovejeet’s 21 Aug feedback: the first draft was not joint / implementation-ready (app-invented GATT e10c, framing/CRC, X25519, charger Wi-Fi scan, live join phases, OCPP over BLE, physical button). Questionnaire went to Jayant. Firmware answers (24 Aug) are now the contract. App and docs were rewritten to match. What changed on the app New firmware path: src/provisioning/firmware/ — BLE FFF0/FFF1/FFF2, raw JSON, reboot semantics, honest success (Credentials sto

### Dharshini — 13.5 of 18.0d (108h of 144h)

**2026-08-01** — logged 1.7d (14h) of 0.0d (0h) available, 5 comments

- Worklog 1h on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7295](https://elocity.atlassian.net/browse/HIEV-7295) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166) (Bug, mid-sprint)
- Worklog 1d on [HIEV-7152](https://elocity.atlassian.net/browse/HIEV-7152) (Task, mid-sprint)
- Worklog 30m on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062) (Bug, mid-sprint)
- Comment on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342): MR:
- Comment on [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226): MR:
- Comment on [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166): MR:
- Comment on [HIEV-7152](https://elocity.atlassian.net/browse/HIEV-7152): Worked on Guest Charging Review comments and tested it by performing charging sessions with different scenarios.
- Comment on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062): MR:

**2026-08-02** — logged 1.0d (8h) of 0.0d (0h) available, 0 comments

- Worklog 1d on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) (Task, planned)

**2026-08-03** — logged 0.0d (0h) of 0.0d (0h) available, 1 comments

- Comment on [HIEV-7295](https://elocity.atlassian.net/browse/HIEV-7295): MR:

**2026-08-04** — logged 0.6d (5h) of 1.0d (8h) available, 3 comments

- Worklog 3h on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388) (Task, mid-sprint)
- Worklog 30m on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7313](https://elocity.atlassian.net/browse/HIEV-7313) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) (Task, planned)
- Comment on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342): Resolved MR review comments.
- Comment on [HIEV-7313](https://elocity.atlassian.net/browse/HIEV-7313): Resolved MR Review Comments.
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): There is a problem with the Xcode application, which does not accept a build. Therefore, I have to run the test scripts on the physical mobile device. However, I am unable to do so despite trying all the steps. I will seek further guidance from Dhanush.

**2026-08-05** — logged 0.6d (5h) of 1.0d (8h) available, 10 comments

- Worklog 2h 30m on [HIEV-7399](https://elocity.atlassian.net/browse/HIEV-7399) (Task, mid-sprint)
- Worklog 1h on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388) (Task, mid-sprint)
- Worklog 45m on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388) (Task, mid-sprint)
- Worklog 30m on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364) (Task, planned)
- Comment on [HIEV-7399](https://elocity.atlassian.net/browse/HIEV-7399): MR:
- Comment on [HIEV-7399](https://elocity.atlassian.net/browse/HIEV-7399): Mapped the ChargerDetails in Charging Session Summary Screen with real time API response and tested by staring charging session.
- Comment on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388): MR:
- Comment on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388): The UI has been completed, and an MR has been raised.
- Comment on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388): Review Comments has been resolved
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): Discussed about the task and approach to be implemented with Marish.
- Comment on [HIEV-7295](https://elocity.atlassian.net/browse/HIEV-7295): Review Comments are fixed
- Comment on [HIEV-7279](https://elocity.atlassian.net/browse/HIEV-7279): Review Comments are fixed
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): Because of some blocked will be moving this ticket to To do.
- Comment on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062): Can you Clear cache and check once again.

**2026-08-06** — logged 0.4d (3h) of 1.0d (8h) available, 7 comments

- Worklog 1h on [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390) (Bug, mid-sprint)
- Comment on [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404): Added a local storage fallback for reservation settings and rounded start/end times to exact minutes for accurate validation.
- Comment on [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404): MR: https://gitlab.com/elocity1/frontend/web/cpms-portal/-/merge_requests/785
- Comment on [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404): Fixed the alignment issue in Export File name popup.
- Comment on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391): Updated GetConfiguration to evaluate typed custom key inputs dynamically, enabling the Perform Action button and passing the key in the API payload. Note : Make sure the selected CPID is active
- Comment on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391): MR:
- Comment on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390): Get Configuration in Bulk Operations sent an empty consumer ID in the API payload, resulting in a 400 Bad Request error. Updated it to parse the selected CPID from station network state and pass it as the consumer in the request body. Note :Make sure the selected CPID is online.
- Comment on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390): MR:

**2026-08-07** — logged 0.2d (1h) of 1.0d (8h) available, 4 comments

- Worklog 30m on [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7430](https://elocity.atlassian.net/browse/HIEV-7430) (Task, mid-sprint)
- Comment on [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439): This is backend issue , so will forward this ticket to
- Comment on [HIEV-7430](https://elocity.atlassian.net/browse/HIEV-7430): MR:
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): This task is currently blocked as the required UI/UX flow and design have not yet been provided by the UI/UX team. Development will continue once the requirements are shared.
- Comment on [HIEV-7345](https://elocity.atlassian.net/browse/HIEV-7345): This task needs backend support first. Will pick once the backend is available.

**2026-08-09** — logged 0.9d (7h) of 0.0d (0h) available, 0 comments

- Worklog 7h on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440) (Task, mid-sprint)

**2026-08-10** — logged 0.6d (5h) of 1.0d (8h) available, 2 comments

- Worklog 5h on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) (Task, planned)
- Comment on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440): Completed documentation , need to re-verify once again.
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): Fixed and parametrised Canada Stripe wallet flow , created Indian RazorPay wallet top-up flow.

**2026-08-11** — logged 0.4d (3h) of 1.0d (8h) available, 3 comments

- Worklog 30m on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) (Task, planned)
- Comment on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391): Resolved MR review comments
- Comment on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390): Resolved MR review comments
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): worked on razorypay test flow but then faced some blockers while running the test scripts.

**2026-08-12** — logged 0.4d (3h) of 1.0d (8h) available, 2 comments

- Worklog 1h on [HIEV-7152](https://elocity.atlassian.net/browse/HIEV-7152) (Task, mid-sprint)
- Worklog 2h on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) (Task, planned)
- Comment on [HIEV-7152](https://elocity.atlassian.net/browse/HIEV-7152): There was some issue in razorpay in adani , was working on that with sudeep.
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): Completed maya payment test flow.

**2026-08-13** — logged 0.4d (3h) of 1.0d (8h) available, 1 comments

- Worklog 3h on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) (Task, planned)
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): Created PayWay payment for total energies and enabled stripe for Universal Energies.

**2026-08-15** — logged 0.2d (2h) of 0.0d (0h) available, 2 comments

- Worklog 2h on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151) (Task, planned)
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): All P0 and P1 payment flows are fully completed, tested, and green (including the Canada Stripe fix, India Razorpay, Movem Maya, and Total Energies ABA PayWay). The Maestro suite is now successfully wired with flavor-specific skip lists in run_tests.sh and all necessary testID s have been added to the UI!
- Comment on [HIEV-7151](https://elocity.atlassian.net/browse/HIEV-7151): MR:

**2026-08-17** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364) (Task, planned)
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): Added progress bar for both synchronous and asynchronous download flows and started implementation on the new export popup.

**2026-08-18** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364) (Task, planned)
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): Completed the implementation of the new download popup. I have tested the download success scenarios, but I still need to verify the download failure scenarios.

**2026-08-19** — logged 1.2d (10h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440) (Task, mid-sprint)
- Worklog 6h on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364) (Task, planned)
- Comment on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440): The document has been updated with the requested changes.
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/790

**2026-08-20** — logged 0.3d (2h) of 1.0d (8h) available, 3 comments

- Worklog 15m on [HIEV-7550](https://elocity.atlassian.net/browse/HIEV-7550) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7323](https://elocity.atlassian.net/browse/HIEV-7323) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7288](https://elocity.atlassian.net/browse/HIEV-7288) (Bug, mid-sprint)
- Comment on [HIEV-7550](https://elocity.atlassian.net/browse/HIEV-7550): If the session is already active and the user try to do guest charging again for the same location , an error popup will be displayed as shown in below image.
- Comment on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546): The backend first needs to return min wallet balance parameter in response.
- Comment on [HIEV-7288](https://elocity.atlassian.net/browse/HIEV-7288): Following further testing, we found that the scrolling issue during the Disconnected / Unavailable state is device and browser-engine specific. As this behaviour is isolated to specific mobile viewports/OS types and does not impact normal charging flows, we propose closing this ticket at this time. We will re-evaluate and prioritise this in a future update if needed.

**2026-08-24** — logged 0.5d (4h) of 1.0d (8h) available, 7 comments

- Worklog 45m on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530) (Bug, mid-sprint)
- Comment on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/796
- Comment on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/796
- Comment on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/796
- Comment on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/796
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/796
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/796
- Comment on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/795

**2026-08-25** — logged 0.7d (6h) of 1.0d (8h) available, 7 comments

- Worklog 15m on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530) (Bug, mid-sprint)
- Worklog 3h on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364) (Task, planned)
- Comment on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558): Verified full-screen modal zoom ( enableZoom: openRevenueVsCost ) with horizontal scale mode ( scaleMode: "x" ). Both Revenue and Energy Cost series remain clearly visible and properly aligned after zooming in and out.
- Comment on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540): Made Y-axis bounds ( ticksCount ) an optional parameter in DoubleBarChartOptions . Standard Dashboard dual-axis charts ( RevenueSessions , RevenueDiscounts , RevenueChargingDuration ) do not pass ticksCount , keeping standard dynamic auto-scaling intact.
- Comment on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538): Updated BarChartOptions and DoubleBarChartOptions so that Y-axis overrides ( beginAtZero , suggestedMax , ticks.count ) run only when ticksCount is explicitly provided.
- Comment on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534): Added unit test suite in vitest/pages/Tariff/RevenueShare/UtilityShare/TariffDesigner/utils.test.ts covering getUtilityTariffActiveTab and normalizeActiveType .
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): Restored shared validatePositiveNumberIncludeZero without any global length limit ( maxLength = undefined ) to safeguard all non-utility components. Created and applied positive_include_zero_max_5 (kWh Min/Max) and positive_include_zero_max_10 (Price) strictly to Utility Tariff fields.Added missing validation keys across all 8 locale files.
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): As soon as text exceeds 30 characters, the red error callout tooltip ( "Tariff Name cannot exceed 30 characters" ) appears immediately right after typing on keystroke.
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): The review comments have been resolved. I need to verify a few design-related things with Marish. Once that’s done, I’ll send it for review.

**2026-08-26** — logged 0.5d (4h) of 1.0d (8h) available, 8 comments

- Worklog 40m on [HIEV-7564](https://elocity.atlassian.net/browse/HIEV-7564) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364) (Task, planned)
- Worklog 30m on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326) (Bug, mid-sprint)
- Comment on [HIEV-7564](https://elocity.atlassian.net/browse/HIEV-7564): This requires backend support too , so assigning this to
- Comment on [HIEV-7564](https://elocity.atlassian.net/browse/HIEV-7564): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/801
- Comment on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/797
- Comment on [HIEV-7544](https://elocity.atlassian.net/browse/HIEV-7544): This is backend issue, assigning ticket to .
- Comment on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492): Resolved MR Review Comments.
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): Sending MR for re-review.
- Comment on [HIEV-7345](https://elocity.atlassian.net/browse/HIEV-7345): I haven’t received any API contract yet.Will pick this up once i receive it and backend is completed.
- Comment on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/798

**2026-08-30** — logged 0.8d (6h) of 0.0d (0h) available, 1 comments

- Worklog 6h on [HIEV-7345](https://elocity.atlassian.net/browse/HIEV-7345) (Task, planned)
- Comment on [HIEV-7345](https://elocity.atlassian.net/browse/HIEV-7345): Recieved the api contract ,gone through the requirements and flow.

**2026-08-31** — logged 0.7d (5h) of 1.0d (8h) available, 7 comments

- Worklog 15m on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440) (Task, mid-sprint)
- Worklog 4h on [HIEV-7345](https://elocity.atlassian.net/browse/HIEV-7345) (Task, planned)
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): Blocked saving on price validation error and show instant error when it reach character limitation.
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/802
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): Blocked saving on price validation error and show instant error when it reach character limitation.
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): MR: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/802
- Comment on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440): The document has been updated with the re-reviewed changes.
- Comment on [HIEV-7345](https://elocity.atlassian.net/browse/HIEV-7345): Started the implementation.
- Comment on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326): The MR includes changes for HIEV-7326 and HIEV-7564 in a single MR. I have updated title and added detailed description addressing both the tickets in the MR.

### Manjunath — 11.1 of 16.0d (88h of 128h)

**2026-08-03** — logged 0.9d (8h) of 1.0d (8h) available, 0 comments

- Worklog 6h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned) — Unified customer and user system and looked into ways to distinguish normal customer and fleet customer. And have noted the challenges for unified customer and user implementation.
- Worklog 0.50h on [HIEV-6940](https://elocity.atlassian.net/browse/HIEV-6940) (Task, planned)
- Worklog 1h on [HIEV-6885](https://elocity.atlassian.net/browse/HIEV-6885) (Bug, mid-sprint) — Pushing all the previous changes to canada prod, so event thread will be free to take new requests.

**2026-08-04** — logged 0.9d (7h) of 1.0d (8h) available, 0 comments

- Worklog 7h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned) — Completed with the data models, implementation docs and prd, want to get it reviewd to start the implementation

**2026-08-05** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 1h on [HIEV-7354](https://elocity.atlassian.net/browse/HIEV-7354) (Task, planned) — Looked into existing submetering related implementation in the CPMS.
- Worklog 5h 30m on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned) — Enhancement of the Implementation doc and prd for the feature design.
- Comment on [HIEV-7354](https://elocity.atlassian.net/browse/HIEV-7354): Below are the existing implementations for the evse submetering: CRUD API : SubmeteringController exposes GET , POST , POST /verify , PUT :id , and DELETE :id endpoints under /submetering/endpoints , restricted to tenant admins with RESTRICTED_INTERNAL_ACCESS permission. Verify Endpoint : The POST /verify endpoint checks if any of the submitted chargePointIds are already mapped to another submetering endpoint, preventing duplicate EVSE assignments. Upsert Logic : SubmeteringService handles creat
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Implementation decisions. Fleet Operators (web users) manage groups, stations, and managers. Fleet Managers are existing customers (mobile users) who charge vehicles. When we add a manager, we create both a web user + mobile customer and link them — profile changes sync both ways automatically. Stations get created the normal way, then designated to a fleet group. One charger = one group. Access mode: "Fleet Exclusive" means only the assigned managers can charge there. "Shared" means public can 

**2026-08-06** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned) — Resolving the review blockers of the fleet feature prd and technical implementation doc.
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Got review for the implementation doc, Resolving the review blockers and requirement mismatch for the fleet feature prd and technical implementation doc.

**2026-08-12** — logged 0.9d (7h) of 1.0d (8h) available, 2 comments

- Worklog 7h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned) — Resolved all review feedback — 3 blockers, 9 mismatches, and 8 open questions across PRD, tech doc, and backlog. Finalized the session ES fleet field injection approach — session-utility queries CPMS for fleet context, same pattern as corporate/guest charging enrichment. Updated PRD v1.3 §3.6 with the fleet context population mechanism and kept technical details deferred for later discussion. Reviewed the full feature in a live discussion — walked through the design end-to-end, all decisions validated, ready for development. Started the implementation part with correcting the naming mismatch between new and old fleet management feature. Renaming old fleet management to vehicle telematics.
- Worklog 0.33h on [HIEV-6940](https://elocity.atlassian.net/browse/HIEV-6940) (Task, planned)
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Resolved all review feedback — 3 blockers, 9 mismatches, and 8 open questions across PRD, tech doc, and backlog. Finalized the session ES fleet field injection approach — session-utility queries CPMS for fleet context, same pattern as corporate/guest charging enrichment. Updated PRD v1.3 §3.6 with the fleet context population mechanism and kept technical details deferred for later discussion. Reviewed the full feature in a live discussion — walked through the design end-to-end, all decisions val
- Comment on [HIEV-6940](https://elocity.atlassian.net/browse/HIEV-6940): Discussion with Sahil about the roles and permission framework for the EVLM feature. Ams should support product specific permission. CPMS-Hiev will have its own roles and permissions and EVLM will have its own roles and permissions.

**2026-08-13** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned) — Renaming old fleet to telematics and started working on the fleet manager creation flow
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Completed renaming old fleet management module to the telematics module. APIs, services, dtos etc Created database entities for the fleet related tables Started working on the fleet manager creation API

**2026-08-14** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned) — continued with the implementation of the onboarding of fleet manager and profile sync when updating customer or user data.
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): continued with the implementation of the onboarding of fleet manager and profile sync when updating customer or user data.

**2026-08-17** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned)
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Created API contracts documents and have shared with respective frontend developers. Continued to work on the profile sync and fleet group creation

**2026-08-18** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned)
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Worked on the Fleet Group CRUD APIs. Working on API to dedicate stations to a group. Worked on adding manager to fleet groups.

**2026-08-19** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned)
- Worklog 2h 30m on [HIEV-6981](https://elocity.atlassian.net/browse/HIEV-6981) (Task, mid-sprint) — Support for the ocpp integration for the charger.
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Dedicating chargers to stations and adding managers to the fleet groups.
- Comment on [HIEV-6981](https://elocity.atlassian.net/browse/HIEV-6981): Support for the ocpp integration for the charger.

**2026-08-20** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned)
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Started to work on the fleet specific transaction, adding fleet transaction related details to session index. Rebasing and conflict resolution for the renaming of old fleetmanagement to vehicle telematics

**2026-08-26** — logged 0.8d (7h) of 1.0d (8h) available, 2 comments

- Worklog 6h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned)
- Worklog 40m on [HIEV-6981](https://elocity.atlassian.net/browse/HIEV-6981) (Task, mid-sprint) — Add CA_THY tenant to the stg environment
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Continued to work on fleet transactions and supporting multiple transactions for the fleet manager.
- Comment on [HIEV-6981](https://elocity.atlassian.net/browse/HIEV-6981): Added CA_THY tenant to the stg environment

**2026-08-27** — logged 0.9d (7h) of 1.0d (8h) available, 2 comments

- Worklog 6h on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147) (Task, planned) — Added all the permission related details for the APIs, then started with the mobile API. List the managers stattion mobile API completed.
- Worklog 1h on [HIEV-6981](https://elocity.atlassian.net/browse/HIEV-6981) (Task, mid-sprint) — Gateway Preauth, gitlab ci issue fixes, as publish build job was not starting.
- Comment on [HIEV-7147](https://elocity.atlassian.net/browse/HIEV-7147): Added all the permission related details for the APIs, then started with the mobile API. Working on the List the managers station mobile API.
- Comment on [HIEV-6981](https://elocity.atlassian.net/browse/HIEV-6981): Gateway Preauth, gitlab ci issue fixes, as publish build job was not starting. https://gitlab.evnet.xyz/elocity1/backend/gateway-preauth/-/commit/0ccaa0ea08eccaa2283e44f1902d1ff6b04d2e40

### Marish — 17.9 of 19.0d (144h of 152h)

**2026-08-03** — logged 1.1d (8h) of 1.0d (8h) available, 1 comments

- Worklog 1d 30m on [HIEV-7327](https://elocity.atlassian.net/browse/HIEV-7327) (Task, planned)
- Comment on [HIEV-7327](https://elocity.atlassian.net/browse/HIEV-7327): Settings Page, Charger Detailed screen design Completed

**2026-08-04** — logged 1.1d (9h) of 1.0d (8h) available, 0 comments

- Worklog 1d 1h on [HIEV-7327](https://elocity.atlassian.net/browse/HIEV-7327) (Task, planned)

**2026-08-05** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221) (Observation, mid-sprint)
- Comment on [HIEV-7327](https://elocity.atlassian.net/browse/HIEV-7327): History and security events page design and prototypes

**2026-08-06** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221) (Observation, mid-sprint)
- Comment on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221): I completed the changes which we discussed during the yesterday’s call. I'm continue working on the Ledger and History sections.

**2026-08-07** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221) (Observation, mid-sprint)
- Comment on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221): Incentive Ledger List Design Completed.

**2026-08-10** — logged 1.1d (9h) of 1.0d (8h) available, 1 comments

- Worklog 2h on [HIEV-7455](https://elocity.atlassian.net/browse/HIEV-7455) (Sub-task, planned)
- Worklog 7h on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221) (Observation, mid-sprint)
- Comment on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221): Completed Approve, reject , hold entry dialog screen design

**2026-08-11** — logged 1.1d (9h) of 1.0d (8h) available, 2 comments

- Worklog 1d 1h on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221) (Observation, mid-sprint)
- Comment on [HIEV-7455](https://elocity.atlassian.net/browse/HIEV-7455): Discussed this with Dharshini and recommended adding two types of toast notifications—Success and Error states.
- Comment on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221): Completed Ledger details view screen flow design

**2026-08-12** — logged 1.1d (9h) of 1.0d (8h) available, 1 comments

- Worklog 1d 1h on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221) (Observation, mid-sprint)
- Comment on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221): Completed Payout Batches list screen & Payout Batch detailed view screen with the all conformation dialog with MFA designs Design Link:

**2026-08-13** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 3h on [HIEV-7498](https://elocity.atlassian.net/browse/HIEV-7498) (Observation, mid-sprint)
- Worklog 5h on [HIEV-7497](https://elocity.atlassian.net/browse/HIEV-7497) (Observation, mid-sprint)
- Comment on [HIEV-7221](https://elocity.atlassian.net/browse/HIEV-7221): Completed Batch flow design

**2026-08-14** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 1d on [HIEV-7497](https://elocity.atlassian.net/browse/HIEV-7497) (Observation, mid-sprint)
- Comment on [HIEV-7498](https://elocity.atlassian.net/browse/HIEV-7498): Banner Slider Issue Support
- Comment on [HIEV-7497](https://elocity.atlassian.net/browse/HIEV-7497): Completed Screen Analysis & Continue working on the screen design

**2026-08-17** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7497](https://elocity.atlassian.net/browse/HIEV-7497) (Observation, mid-sprint)
- Comment on [HIEV-7497](https://elocity.atlassian.net/browse/HIEV-7497): Base screen design structure completed.

**2026-08-18** — logged 1.1d (9h) of 1.0d (8h) available, 2 comments

- Worklog 1d 1h on [HIEV-7497](https://elocity.atlassian.net/browse/HIEV-7497) (Observation, mid-sprint)
- Comment on [HIEV-7497](https://elocity.atlassian.net/browse/HIEV-7497): Register flow design - Continue on working.
- Comment on [HIEV-7497](https://elocity.atlassian.net/browse/HIEV-7497): Register Flow Design - Completed

**2026-08-20** — logged 1.0d (8h) of 1.0d (8h) available, 0 comments

- Worklog 5h on [HIEV-7566](https://elocity.atlassian.net/browse/HIEV-7566) (Observation, mid-sprint)
- Worklog 3h on [HIEV-6944](https://elocity.atlassian.net/browse/HIEV-6944) (Task, planned)

**2026-08-21** — logged 0.0d (0h) of 1.0d (8h) available, 2 comments

- Comment on [HIEV-7566](https://elocity.atlassian.net/browse/HIEV-7566): Export module enhancements - Completed
- Comment on [HIEV-6944](https://elocity.atlassian.net/browse/HIEV-6944): Fixed

**2026-08-24** — logged 1.0d (8h) of 1.0d (8h) available, 0 comments

- Worklog 1d on [HIEV-7566](https://elocity.atlassian.net/browse/HIEV-7566) (Observation, mid-sprint)

**2026-08-25** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7588](https://elocity.atlassian.net/browse/HIEV-7588) (Observation, mid-sprint)
- Comment on [HIEV-7566](https://elocity.atlassian.net/browse/HIEV-7566): Login - Microsoft - Done Profile Page Logs - Done Diagnostic Module - Done Utility Tariff - Done Guest Charging -Done

**2026-08-26** — logged 0.0d (0h) of 1.0d (8h) available, 1 comments

- Comment on [HIEV-7588](https://elocity.atlassian.net/browse/HIEV-7588): Notification Dropdown - Completed FAQ Design - Completed

**2026-08-27** — logged 2.0d (16h) of 1.0d (8h) available, 1 comments

- Worklog 1d on [HIEV-7600](https://elocity.atlassian.net/browse/HIEV-7600) (Observation, mid-sprint)
- Worklog 1d on [HIEV-7588](https://elocity.atlassian.net/browse/HIEV-7588) (Observation, mid-sprint)
- Comment on [HIEV-7588](https://elocity.atlassian.net/browse/HIEV-7588): Profile Page Design - Completed User Management screen - completed Login Page - completed

**2026-08-28** — logged 0.0d (0h) of 0.0d (0h) available, 1 comments

- Comment on [HIEV-7600](https://elocity.atlassian.net/browse/HIEV-7600): Analyzed and designed the Operator-Issued Wallet Credits screen, covering the complete credit issuance workflow with validation and audit-focused UX.

**2026-08-31** — logged 1.1d (9h) of 1.0d (8h) available, 0 comments

- Worklog 1d 1h on [HIEV-7600](https://elocity.atlassian.net/browse/HIEV-7600) (Observation, mid-sprint)

### Nagaraju — 16.8 of 19.0d (134h of 152h)

**2026-08-03** — logged 1.4d (11h) of 1.0d (8h) available, 4 comments

- Worklog 15m on [HIEV-7379](https://elocity.atlassian.net/browse/HIEV-7379) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7376](https://elocity.atlassian.net/browse/HIEV-7376) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7356](https://elocity.atlassian.net/browse/HIEV-7356) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7309](https://elocity.atlassian.net/browse/HIEV-7309) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7244](https://elocity.atlassian.net/browse/HIEV-7244) (Bug, mid-sprint)
- Worklog 1.00h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 1.00h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 0.75h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 1.00h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 1.50h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 1.00h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 2.50h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 0.75h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 15m on [HIEV-6380](https://elocity.atlassian.net/browse/HIEV-6380) (Epic, mid-sprint)
- Comment on [HIEV-7356](https://elocity.atlassian.net/browse/HIEV-7356): Working as expected
- Comment on [HIEV-7309](https://elocity.atlassian.net/browse/HIEV-7309): Working as expected
- Comment on [HIEV-7244](https://elocity.atlassian.net/browse/HIEV-7244): Working as expected, label has been implemented
- Comment on [HIEV-6380](https://elocity.atlassian.net/browse/HIEV-6380): Verified the app rating feature in the debug build. The implementation is working as expected as per the acceptance criteria.

**2026-08-04** — logged 0.9d (7h) of 1.0d (8h) available, 6 comments

- Worklog 15m on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7387](https://elocity.atlassian.net/browse/HIEV-7387) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7386](https://elocity.atlassian.net/browse/HIEV-7386) (Sub-task, mid-sprint)
- Worklog 1h on [HIEV-7384](https://elocity.atlassian.net/browse/HIEV-7384) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7383](https://elocity.atlassian.net/browse/HIEV-7383) (Sub-task, mid-sprint)
- Worklog 40m on [HIEV-7382](https://elocity.atlassian.net/browse/HIEV-7382) (Sub-task, mid-sprint)
- Worklog 2.50h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Comment on [HIEV-7387](https://elocity.atlassian.net/browse/HIEV-7387): Validated the tariff deletion functionality from the Location Details page. Verification performed: Opened a location with an assigned tariff. Deleted the tariff and confirmed the delete action. Verified the delete request was triggered and the portal refreshed automatically. Confirmed the tariff was removed from the location details. Scanned the location QR code in the mobile application. Verified the deleted tariff was no longer displayed in the app. Observation: The current implementation per
- Comment on [HIEV-7386](https://elocity.atlassian.net/browse/HIEV-7386): Validated the Tariff Profile launch functionality. Verification performed: Selected an existing tariff profile and initiated the launch process. Completed all mandatory launch details. Verified the Launch Tariff API executed successfully. Confirmed no HTTP 500 Internal Server Error was returned. Verified no currency_code database constraint violation was observed. Confirmed the tariff profile was successfully launched and displayed under the Launched tab with Active status. Refreshed the page an
- Comment on [HIEV-7384](https://elocity.atlassian.net/browse/HIEV-7384): Validated the Reservations module using a user with no Location module permissions. Verification performed: Logged in with a user having no Location permissions. Verified the Reservations page loaded successfully. Confirmed the default date range was displayed correctly. Verified the Reservations API request included the correct from and to date parameters. Confirmed only reservation records within the selected date range were displayed. Changed the date range and verified the API request update
- Comment on [HIEV-7383](https://elocity.atlassian.net/browse/HIEV-7383): Validated the E-Wallet transaction listing in the Customer Details screen. Verified the default API request sends columns[]=insertedAt and columnOrders[]=DESC . Confirmed the API response returns the latest transactions first (descending order). Verified clicking the Date column changes the request to columnOrders[]=ASC and the transaction order updates accordingly. Verified clicking the Date column again changes the request back to columnOrders[]=DESC . Confirmed the UI transaction order matche
- Comment on [HIEV-7382](https://elocity.atlassian.net/browse/HIEV-7382): Verified: Password reset email displays the validity period in IST for Indian locations. Password reset email displays the validity period in the appropriate Canada time zone for Canadian locations. Confirmed the fix works as expected on the STG environment.
- Comment on [HIEV-7379](https://elocity.atlassian.net/browse/HIEV-7379): Working as expected

**2026-08-05** — logged 0.6d (5h) of 1.0d (8h) available, 13 comments

- Worklog 30m on [HIEV-7402](https://elocity.atlassian.net/browse/HIEV-7402) (Sub-task, mid-sprint)
- Worklog 10m on [HIEV-7402](https://elocity.atlassian.net/browse/HIEV-7402) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7401](https://elocity.atlassian.net/browse/HIEV-7401) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7400](https://elocity.atlassian.net/browse/HIEV-7400) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7398](https://elocity.atlassian.net/browse/HIEV-7398) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7397](https://elocity.atlassian.net/browse/HIEV-7397) (Sub-task, mid-sprint)
- Worklog 1h on [HIEV-7396](https://elocity.atlassian.net/browse/HIEV-7396) (Task, mid-sprint)
- Worklog 15m on [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7121](https://elocity.atlassian.net/browse/HIEV-7121) (Bug, mid-sprint)
- Comment on [HIEV-7402](https://elocity.atlassian.net/browse/HIEV-7402): Validated the Business Export report to verify removal of the CIN column. The issue is still reproducible as the exported report continues to include the CIN column. The ticket has been returned for further investigation.
- Comment on [HIEV-7401](https://elocity.atlassian.net/browse/HIEV-7401): Validated the export workflow and post-export navigation behavior. Verification performed: Generated export reports for multiple modules. Verified the export confirmation popup was displayed successfully. Clicked Back without opening the Exports module. Navigated to Station Management and verified the page loaded successfully without any refresh or HTTP 500 errors. Verified the Decommissioned tab loaded successfully. Generated multiple exports consecutively and confirmed portal stability across 
- Comment on [HIEV-7400](https://elocity.atlassian.net/browse/HIEV-7400): Validated the Facilities grid layout on the Location Details page. Verification performed: Opened the Location Details page for a charging station with multiple facilities. Verified the Facilities section displays icons in a compact sequential 3-column grid. Confirmed there are no unnecessary empty gaps or placeholder cells between facility icons. Verified the layout remains visually balanced and consistent across multiple rows. Confirmed all facility icons are displayed correctly without affect
- Comment on [HIEV-7398](https://elocity.atlassian.net/browse/HIEV-7398): Validated the connector selection flow in the Reservation module. Verification performed: Selected an available location and navigated to the Reservation screen. Verified selecting a connector loaded the reservation timeline successfully without entering an infinite loading state. Confirmed the loading indicator disappeared after the reservation details were loaded. Tested multiple connectors and verified the timeline updated correctly for each selection. Switched between connectors multiple tim
- Comment on [HIEV-7397](https://elocity.atlassian.net/browse/HIEV-7397): Validated the Join Queue connector availability timeline after navigating back from the queue flow. Verification performed: Verified the connector availability timeline before and after navigating back from the Join Queue screen. Confirmed the timeline remained consistent and no alternate time slots were incorrectly marked unavailable. Verified no visual inconsistencies were observed after returning to the Reservation screen. Confirmed reopening the Join Queue screen did not alter the connector 
- Comment on [HIEV-7396](https://elocity.atlassian.net/browse/HIEV-7396): Activities performed: Logged into the elocity-ca-cms Firebase project. Updated the campaign configuration under the staging environment: Set isActive = true . Configured startDate and endDate to cover the current date. Configured the campaign title , message , priority , and displayRules . Built and installed the latest staging APK. Logged into the app using a registered (non-guest) user. Navigated to the Map/Home screen and waited for the campaign modal to appear. Observed that the campaign mod
- Comment on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377): Working as expected
- Comment on [HIEV-7376](https://elocity.atlassian.net/browse/HIEV-7376): Working as expected
- Comment on [HIEV-7339](https://elocity.atlassian.net/browse/HIEV-7339): Working as expected
- Comment on [HIEV-7121](https://elocity.atlassian.net/browse/HIEV-7121): Working as expected
- Comment on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062): Validated the Business Export report to verify removal of the CIN column. The issue is still reproducible as the exported report continues to include the CIN column. The ticket has been returned for further investigation, FYI checked on prod and stg
- Comment on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062): The issue is still reproducible as the exported report continues to include the CIN column.
- Comment on [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836): Not working as per requirement , Configured the Firebase campaign with valid settings and tested on the latest STG build. The campaign modal is still not displayed for a logged-in user. Reassigning back for investigation as discussed.

**2026-08-06** — logged 0.8d (7h) of 1.0d (8h) available, 19 comments

- Worklog 15m on [HIEV-7423](https://elocity.atlassian.net/browse/HIEV-7423) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7421](https://elocity.atlassian.net/browse/HIEV-7421) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7419](https://elocity.atlassian.net/browse/HIEV-7419) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7418](https://elocity.atlassian.net/browse/HIEV-7418) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7417](https://elocity.atlassian.net/browse/HIEV-7417) (Sub-task, mid-sprint)
- Worklog 40m on [HIEV-7415](https://elocity.atlassian.net/browse/HIEV-7415) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7412](https://elocity.atlassian.net/browse/HIEV-7412) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7411](https://elocity.atlassian.net/browse/HIEV-7411) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7410](https://elocity.atlassian.net/browse/HIEV-7410) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7409](https://elocity.atlassian.net/browse/HIEV-7409) (Sub-task, mid-sprint)
- Worklog 40m on [HIEV-7408](https://elocity.atlassian.net/browse/HIEV-7408) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7405](https://elocity.atlassian.net/browse/HIEV-7405) (Task, mid-sprint)
- Worklog 20m on [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166) (Bug, mid-sprint)
- Comment on [HIEV-7421](https://elocity.atlassian.net/browse/HIEV-7421): Validated the connector selection behavior for Guest Charging with multiple connectors. Verification performed: Scanned the Guest Charging QR code for a station configured with multiple connectors. Navigated to the Location Details page. Verified the connector list supported horizontal scrolling. Confirmed all available connectors could be viewed by swiping horizontally. Verified connectors beyond the initially visible area were fully accessible and selectable. Confirmed no UI or scrolling issue
- Comment on [HIEV-7419](https://elocity.atlassian.net/browse/HIEV-7419): Validated the Guest Charging flow for unsupported connector states. Verification performed: Configured connectors with unsupported states. Verified the behavior for Reserved, Faulted, SuspendedEV, SuspendedEVSE, and Unknown connector states. Confirmed connectors in these states were not selectable on the Location Details page after scanning the Guest Charging QR code. Verified users were prevented from proceeding to the payment flow for unsupported connector states. Confirmed no unexpected navig
- Comment on [HIEV-7418](https://elocity.atlassian.net/browse/HIEV-7418): Validated the payment processing loading screen in the Guest Charging flow. Verification performed: Scanned a valid Guest Charging QR code. Selected a connector and initiated the charging flow. Verified the payment processing loading indicator was displayed correctly. Confirmed the loading indicator did not overlap the Station Details content. Verified the loading screen was displayed consistently throughout the payment processing state. Confirmed no UI alignment or visual presentation issues we
- Comment on [HIEV-7417](https://elocity.atlassian.net/browse/HIEV-7417): Validated the Guest Charging error presentation for the "Failed to generate add card link" scenario. Verification performed: Triggered the error scenario during the Guest Charging flow (minimum balance configured as 0). Verified the error was displayed only as a modal dialog. Confirmed no duplicate toast notification was displayed along with the modal. Verified the Retry and Cancel actions were displayed correctly in the modal. Repeated the validation multiple times to ensure consistent behavior
- Comment on [HIEV-7415](https://elocity.atlassian.net/browse/HIEV-7415): Validated the charging duration display in the Guest Charging flow. Verification performed: Completed a Guest Charging session successfully. Verified the charging duration displayed on the Payment Processing screen. Verified the charging duration displayed on the Session Details screen. Verified the charging duration displayed on the Session Summary screen. Confirmed the charging duration is displayed in a user-friendly format without milliseconds across all applicable screens. Verified consiste
- Comment on [HIEV-7412](https://elocity.atlassian.net/browse/HIEV-7412): Validated the Greenhouse Gas reporting chart after the initial Zoom In operation. Verification performed: Opened the Greenhouse Gas report and launched it in fullscreen mode. Performed the initial Zoom In operation and verified the Y-axis intervals. Confirmed the horizontal grid lines remained evenly spaced throughout the chart. Navigated away from the report, reopened it, and repeated the verification to validate the first-load behavior. Performed additional zoom interactions to ensure chart re
- Comment on [HIEV-7411](https://elocity.atlassian.net/browse/HIEV-7411): Validated the Greenhouse Gas report title update in the Reporting module. Verification performed: Navigated to Dashboard → Reporting. Opened the Greenhouse Gas report. Verified the report title in the left navigation panel. Verified the report title in the report header. Confirmed the title is displayed as "Greenhouse Gas Reduction" consistently across the Reporting module. Verified no inconsistencies or incorrect references to the previous title were observed. Result: Fix verified successfully.
- Comment on [HIEV-7410](https://elocity.atlassian.net/browse/HIEV-7410): Validated the Greenhouse Gas Used reporting chart. Verification performed: Opened the Greenhouse Gas Used report with charging session data. Verified the chart rendered successfully for the selected date range. Confirmed the Greenhouse Gas Used data series was displayed as bars. Verified the Cumulative data series was displayed as a line. Confirmed both data series matched the chart legend and were rendered correctly. Verified no missing bars or visualization inconsistencies were observed. Resul
- Comment on [HIEV-7409](https://elocity.atlassian.net/browse/HIEV-7409): Validated the Greenhouse Gas reporting chart after zooming in. Verification performed: Opened the Greenhouse Gas report and verified chart rendering in fullscreen mode. Performed multiple Zoom In operations and verified both left and right Y-axes remained synchronized. Confirmed each horizontal grid line had a corresponding value on both Y-axes. Verified the number of Y-axis labels remained consistent after zooming. Performed additional zoom in/out operations to ensure chart alignment and spacin
- Comment on [HIEV-7408](https://elocity.atlassian.net/browse/HIEV-7408): Validated the Greenhouse Gas report chart behavior after zoom operations. Verification performed: Opened the Greenhouse Gas report with available data. Verified the chart in fullscreen mode. Performed multiple Zoom Out operations and confirmed both left and right Y-axes remained synchronized. Verified every horizontal grid line had a corresponding value on both Y-axes, including the topmost grid line. Performed Zoom In operations and confirmed axis alignment remained consistent. Verified no miss
- Comment on [HIEV-7405](https://elocity.atlassian.net/browse/HIEV-7405): Reviewed the Load Management PRD to understand the feature and its business workflow. Activities performed: Studied the functional requirements and expected system behavior. Understood the Load Management workflow and key concepts. Identified the major modules, user actions, and business rules. Reviewed the feature from a QA perspective to determine the testing scope and potential validation scenarios. Result: PRD analysis completed and feature understanding established for QA validation.
- Comment on [HIEV-7402](https://elocity.atlassian.net/browse/HIEV-7402): Validated the Business Export report. Verification performed: Generated the Business export report from the Business module. Downloaded and reviewed the exported report. Verified the 'CIN' column has been removed from the export. Confirmed the remaining columns are displayed correctly with proper data alignment. Verified the report downloads successfully without any formatting or export issues. Result: Fix verified successfully. The 'CIN' column is no longer present in the exported report.
- Comment on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342): Issue has been fixed and is working as expected
- Comment on [HIEV-7337](https://elocity.atlassian.net/browse/HIEV-7337): Verified on the latest STG build. Tested the Greenhouse Gas report in fullscreen mode with multiple zoom in/out operations. Both Y-axes remained synchronized, and every horizontal grid line displayed the corresponding Y-axis values. Issue has been fixed .
- Comment on [HIEV-7336](https://elocity.atlassian.net/browse/HIEV-7336): Working as expected
- Comment on [HIEV-7335](https://elocity.atlassian.net/browse/HIEV-7335): Verified on the latest STG build. After the initial Zoom In operation, the Y-axis intervals remained uniform and the horizontal grid lines were evenly spaced. The issue has been resolved.
- Comment on [HIEV-7333](https://elocity.atlassian.net/browse/HIEV-7333): Verified on the latest STG build. The report title has been updated from "Greenhouse Gas Used" to "Greenhouse Gas Reduction" in both the navigation panel and the report header. Issue has been fixed.
- Comment on [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166): Blocked by 7404
- Comment on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062): Working as expected

**2026-08-07** — logged 0.6d (5h) of 1.0d (8h) available, 9 comments

- Worklog 40m on [HIEV-7438](https://elocity.atlassian.net/browse/HIEV-7438) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7437](https://elocity.atlassian.net/browse/HIEV-7437) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7435](https://elocity.atlassian.net/browse/HIEV-7435) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7434](https://elocity.atlassian.net/browse/HIEV-7434) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7433](https://elocity.atlassian.net/browse/HIEV-7433) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7431](https://elocity.atlassian.net/browse/HIEV-7431) (Sub-task, mid-sprint)
- Worklog 1.25h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Comment on [HIEV-7438](https://elocity.atlassian.net/browse/HIEV-7438): Validated the real-time Charging Session updates in the Guest Charging flow. Verification performed: Initiated a Guest Charging session. Monitored the Charging Session screen during an active charging session. Verified that the charging session details were updated automatically in real time without requiring a manual refresh. Observed the session information refreshing approximately every 10–15 seconds. Confirmed the charging session remained active and the displayed information stayed synchron
- Comment on [HIEV-7437](https://elocity.atlassian.net/browse/HIEV-7437): Validated the Guest Charging session behavior after disconnecting the simulator. Verification performed: Scanned the Guest Charging QR code. Selected a connector and initiated the charging flow. Entered valid card details. Disconnected the simulator before completing the payment flow. Copied the Charging Session URL from the mobile browser and opened it in the desktop browser. Refreshed the page and inspected the network response. Verified the API returned an empty response and no unexpected err
- Comment on [HIEV-7435](https://elocity.atlassian.net/browse/HIEV-7435): Validated the Guest Charging flow for Offline/Unknown and Unavailable charger states. Verification performed: Configured the charger in Offline/Unknown and Unavailable states. Scanned the Guest Charging QR code and navigated to the Location Details page. Verified the "Swipe to Start Charging" action was disabled. Confirmed the message "Charging station is currently unavailable for guest charging" was displayed. Verified users were prevented from proceeding to the payment flow. Confirmed the prev
- Comment on [HIEV-7434](https://elocity.atlassian.net/browse/HIEV-7434): Validated the Session Summary loading behavior in the Guest Charging flow. Verification performed: Scanned a valid Guest Charging QR code. Started and completed a Guest Charging session. Navigated to the Session Summary page after stopping the charging session. Verified the loading behavior while the Session Summary page was loading. Confirmed only a single loading indicator was displayed during the loading state. Verified the additional circular loading spinner was no longer displayed. Performe
- Comment on [HIEV-7433](https://elocity.atlassian.net/browse/HIEV-7433): Validated the Charging Session loading behavior in the Guest Charging flow. Verification performed: Scanned a valid Guest Charging QR code. Initiated a charging session by swiping "Swipe to Start Charging". Verified the Charging Session screen during the loading state. Confirmed the "Loading station details..." indicator was displayed correctly without overlapping the session information cards. Verified the Charging Session layout remained stable while session details were loading. Performed a r
- Comment on [HIEV-7431](https://elocity.atlassian.net/browse/HIEV-7431): Validated the low-priority UI improvements in the My Profile module. Verification performed: Verified the Submit button is displayed with the updated button styling consistent with the application. Confirmed the Cancel button is available in the Edit Profile side panel and functions correctly. Verified consistent terminology is used for the logout flow. Confirmed the filter label has been updated from "Select Name" to "User Name". Performed a regression check on the My Profile functionality to e
- Comment on [HIEV-7399](https://elocity.atlassian.net/browse/HIEV-7399): Working as expected
- Comment on [HIEV-7320](https://elocity.atlassian.net/browse/HIEV-7320): Verified on the latest Staging build. All reported issues in the My Profile module have been validated, including button styling, Cancel action, logout terminology, and filter label updates. The issues have been resolved.
- Comment on [HIEV-7279](https://elocity.atlassian.net/browse/HIEV-7279): Working as expected

**2026-08-10** — logged 0.8d (6h) of 1.0d (8h) available, 21 comments

- Worklog 30m on [HIEV-7456](https://elocity.atlassian.net/browse/HIEV-7456) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7454](https://elocity.atlassian.net/browse/HIEV-7454) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7453](https://elocity.atlassian.net/browse/HIEV-7453) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7452](https://elocity.atlassian.net/browse/HIEV-7452) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7451](https://elocity.atlassian.net/browse/HIEV-7451) (Sub-task, mid-sprint)
- Worklog 15m on [HIEV-7450](https://elocity.atlassian.net/browse/HIEV-7450) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7448](https://elocity.atlassian.net/browse/HIEV-7448) (Sub-task, mid-sprint)
- Worklog 25m on [HIEV-7447](https://elocity.atlassian.net/browse/HIEV-7447) (Sub-task, mid-sprint)
- Worklog 15m on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446) (Bug, mid-sprint) — Retesting the fix
- Worklog 30m on [HIEV-7444](https://elocity.atlassian.net/browse/HIEV-7444) (Sub-task, mid-sprint)
- Worklog 40m on [HIEV-7443](https://elocity.atlassian.net/browse/HIEV-7443) (Sub-task, mid-sprint)
- Worklog 1h 10m on [HIEV-7396](https://elocity.atlassian.net/browse/HIEV-7396) (Task, mid-sprint)
- Comment on [HIEV-7454](https://elocity.atlassian.net/browse/HIEV-7454): Validated connector mapping for multi-connector stations in the Guest Charging flow. Verification performed: Scanned the Guest Charging QR code for a station with multiple connectors. Selected different connectors and initiated charging sessions. Verified the connector details displayed on the Charging Session screen matched the selected connector. Verified the connector information displayed throughout the Guest Charging flow remained consistent. Validated the connector recorded in CPMS → Custo
- Comment on [HIEV-7453](https://elocity.atlassian.net/browse/HIEV-7453): Validated the Minimum Balance field in the Station Management module. Verification performed: Navigated to Menu → Assets → Station Management → Info → Advanced Controls. Opened the station in Edit mode. Verified the Minimum Balance field accepted only numeric input. Attempted to enter values exceeding the supported maximum input length. Confirmed the field restricted input to a maximum of 9 digits and prevented additional characters from being entered. Verified the entered value was saved succes
- Comment on [HIEV-7452](https://elocity.atlassian.net/browse/HIEV-7452): Validated the Station Name field and Station Details page. Verification performed: Navigated to Menu → Assets → Station Management. Created/edited a station and entered the maximum allowed number of characters in the Station Name field. Attempted to enter additional characters after reaching the maximum limit. Verified the character limit was enforced correctly without modifying the existing text unexpectedly. Saved the station and opened the Station Details page. Verified long station names wer
- Comment on [HIEV-7451](https://elocity.atlassian.net/browse/HIEV-7451): Validated the validation behavior for optional tariff sections in the New Tariff form. Verification performed: Navigated to Menu → Tariff Management → New Tariff. Enabled optional tariff sections (Time Limit, Time Penalty, and Energy Limit). Triggered field validation by leaving required fields empty or entering invalid values. Verified validation messages were displayed appropriately. Disabled each tariff section by unchecking its corresponding checkbox. Confirmed all validation messages were c
- Comment on [HIEV-7450](https://elocity.atlassian.net/browse/HIEV-7450): Validated the All Chargers filter dropdown behavior in the Reservations module. Verification performed: Navigated to Menu → Reservations. Opened the All Chargers filter dropdown. Triggered the "No options exist" state by searching for an invalid charger. Clicked outside the dropdown and on other filters/input fields. Verified the dropdown closed automatically when it lost focus. Performed a regression check to ensure the dropdown behavior remained consistent during repeated interactions. Result:
- Comment on [HIEV-7448](https://elocity.atlassian.net/browse/HIEV-7448): Validated the User Details page in the User Management module. Verification performed: Navigated to Menu → Administration → User Management. Opened the User Details page for an existing user. Verified the styling of the Edit, Delete, and Resend Activation Link buttons. Confirmed the action buttons have consistent height, padding, border radius, and alignment. Performed a visual regression check to ensure the button styling remained consistent across the page. Result: Fix verified successfully. T
- Comment on [HIEV-7447](https://elocity.atlassian.net/browse/HIEV-7447): Validated character limit handling for Location Name and Address Line 1. Verification performed: Verified the Location Name field with input exceeding the supported character limit during Add New Location and Edit Location flows. Confirmed the Location Name scenario is functioning as expected. Verified the Address Line 1 field by typing and pasting long input. Observed that when the input exceeds approximately 200 characters, the application still displays the generic error: "Something went wron
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Retested on the latest Staging build. maxDisplayCount is still not enforced. The campaign continues to appear on every app launch despite being configured with maxDisplayCount = 5 in Firebase. Reopening the ticket.
- Comment on [HIEV-7444](https://elocity.atlassian.net/browse/HIEV-7444): Validated the Timing section in the Add New Location workflow. Verification performed: Navigated to Menu → Assets → Location Management. Created a new location and proceeded to the Timing step. Selected the "Customized" timing option. Verified the Back and Next buttons were fully visible and accessible at 100% browser zoom. Tested multiple browser zoom levels to ensure the buttons remained visible and were not cropped. Confirmed the layout remained responsive and no scrolling or UI alignment iss
- Comment on [HIEV-7443](https://elocity.atlassian.net/browse/HIEV-7443): Validated the Location filter functionality in the Reporting module. Verification performed: Opened Dashboard → Reporting. Selected one or more locations using the Location filter. Applied the selected filter. Verified the selected location PK(s)(CPID is primary key) were passed in the API request as per the expected contract. Confirmed the report data was filtered correctly based on the selected locations. Verified the selected CPID count was updated correctly (e.g., "23 Selected") after applyi
- Comment on [HIEV-7396](https://elocity.atlassian.net/browse/HIEV-7396): Validated the In-App Campaign feature based on the provided test plan and additional functional scenarios. Verification performed: Verified campaign display for a fresh login with tour and biometric flow. Verified campaign display for returning users with completed tour and enabled biometrics. Verified biometric flow before campaign display for returning users with pending biometric setup. Verified campaign retrieval after a cold start of a previously logged-in session. Confirmed the campaign di
- Comment on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388): Verified on the latest STG build. The Location filter is functioning as expected. Selected location PK(s) are correctly passed in the API request, the report data is filtered correctly, and the selected CPID count (e.g., "23 Selected" ) is displayed accurately.
- Comment on [HIEV-7321](https://elocity.atlassian.net/browse/HIEV-7321): Verified on the latest Staging build. The Minimum Balance field now restricts input to a maximum of 9 digits and prevents users from entering additional numeric characters. The validation behaves as expected, and the issue has been resolved.
- Comment on [HIEV-7295](https://elocity.atlassian.net/browse/HIEV-7295): Verified on the latest UAT build. The selected connector is displayed correctly throughout the Guest Charging flow, and the same connector is accurately recorded in CPMS → Customer → Charging Sessions . The issue has been resolved.
- Comment on [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237): Verified the fix on the latest STG build. Location Name: Character limit validation is working as expected. Address Line 1: The issue is still reproducible. When typing or pasting input exceeding Exactly 200 characters , the application immediately displays the generic error: "Something went wrong! We hit a temporary glitch. Please refresh the page." The Address Line 1 scenario is not yet resolved. Reopening the ticket please investigate.
- Comment on [HIEV-7236](https://elocity.atlassian.net/browse/HIEV-7236): Working as expected
- Comment on [HIEV-7235](https://elocity.atlassian.net/browse/HIEV-7235): Working as expected
- Comment on [HIEV-7218](https://elocity.atlassian.net/browse/HIEV-7218): Working as expected
- Comment on [HIEV-7215](https://elocity.atlassian.net/browse/HIEV-7215): Working as expected
- Comment on [HIEV-7207](https://elocity.atlassian.net/browse/HIEV-7207): Verified on the latest staging. The Back and Next buttons remain fully visible and accessible after selecting Customised timing. Validated at 100% browser zoom and across multiple zoom levels. No button cropping or layout issues were observed. The issue has been resolved.
- Comment on [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836): During regression testing while verifying the maxDisplayCount fix, it was observed that eligible campaigns are no longer displayed after login. The campaign was previously displayed as expected during earlier validation. Raising this as a regression issue for further investigation.

**2026-08-11** — logged 0.7d (5h) of 1.0d (8h) available, 17 comments

- Worklog 30m on [HIEV-7469](https://elocity.atlassian.net/browse/HIEV-7469) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7467](https://elocity.atlassian.net/browse/HIEV-7467) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7466](https://elocity.atlassian.net/browse/HIEV-7466) (Bug, mid-sprint)
- Worklog 40m on [HIEV-7465](https://elocity.atlassian.net/browse/HIEV-7465) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7464](https://elocity.atlassian.net/browse/HIEV-7464) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7463](https://elocity.atlassian.net/browse/HIEV-7463) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7462](https://elocity.atlassian.net/browse/HIEV-7462) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7461](https://elocity.atlassian.net/browse/HIEV-7461) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7460](https://elocity.atlassian.net/browse/HIEV-7460) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7459](https://elocity.atlassian.net/browse/HIEV-7459) (Sub-task, mid-sprint)
- Worklog 0.67h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 0.25h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Comment on [HIEV-7469](https://elocity.atlassian.net/browse/HIEV-7469): Validated the Reservation date range filtering behavior. Created a reservation for the current day with a future start time. Applied the Today date range and verified the newly created reservation is displayed. Applied the This Year date range and verified the newly created reservation is included along with existing reservations. Confirmed reservations with a future start time are correctly reflected in the data grid. Verified the results remain consistent when switching between date ranges. Re
- Comment on [HIEV-7467](https://elocity.atlassian.net/browse/HIEV-7467): Validated the Station Overview Charger filter. Selected a single charger from the Charger filter. Applied the filter and verified the corresponding results in the data grid. Verified that the map now displays only the pin for the selected charger's location. Confirmed that previously displayed location pins are removed after applying the filter. Result: Fix verified successfully. The issue has been resolved.
- Comment on [HIEV-7465](https://elocity.atlassian.net/browse/HIEV-7465): Validated the reported Advanced Controls issues in Station Details. Verified the checkbox alignment for Ratio Duration, Auto Stop on Low Wallet Balance, and Dedicated Customer . Verified the Advanced Controls section behavior after clicking Cancel . Confirmed the Change option for Dedicated Customer follows the expected application styling. Validated the above scenarios and confirmed the reported issues are no longer reproducible. Issue 3 was not validated as requested. Result: Issues 1, 2, and 
- Comment on [HIEV-7463](https://elocity.atlassian.net/browse/HIEV-7463): Validated the Add New EVSE Model form under Asset Settings. Triggered field-level validation by leaving mandatory fields empty and moving focus to the next field. Repeated the validation flow across the mandatory fields. Verified the floating labels/placeholders remain consistently aligned after validation. Confirmed the validation state does not cause any visual misalignment. Performed a regression check to ensure the form layout remains consistent. Result: Fix verified successfully. The issue 
- Comment on [HIEV-7462](https://elocity.atlassian.net/browse/HIEV-7462): Validated the Export Logs functionality in My Profile. Clicked Export Logs and verified the success pop-up is displayed after the export completes. Verified the Export Logs button is disabled during the export while retaining the “Export Logs” label. Verified the download progress bar is displayed at the bottom of the screen during the export. Validated the complete export flow across the reported scenarios. Verified the downloaded report content Result: Fix verified successfully. All reported i
- Comment on [HIEV-7461](https://elocity.atlassian.net/browse/HIEV-7461): Validated the Refresh action in My Profile . Applied the Name filter by selecting one or more names. Clicked Apply and verified the filtered results. Clicked the Refresh icon. Confirmed the applied filter selection is retained after refresh. Verified the filtered results remain consistent. Confirmed the Reset button remains enabled while the filter is applied. Result: Fix verified successfully. The issue has been resolved.
- Comment on [HIEV-7460](https://elocity.atlassian.net/browse/HIEV-7460): Validated the My Profile email address edit restriction. Navigated to My Profile → Edit . Verified the Email Address field is non-editable. Confirmed the user cannot modify the registered email address. Verified the edit functionality for the remaining profile fields is unaffected. Confirmed the previous issue of users being logged out after changing their email address cannot occur. Result: Fix verified successfully. The issue has been resolved.
- Comment on [HIEV-7459](https://elocity.atlassian.net/browse/HIEV-7459): Validate the fix for the New Reservation Save flow in the CPMS Portal. Verification scope: Verify that all mandatory reservation details can be entered successfully. Verify reservation creation with the default reservation duration. Modify the Start Date/Time and End Date/Time using valid reservation durations. Click Save and verify that the Create Reservation API is triggered. Verify that the reservation is created successfully. Verify that the incorrect "Maximum Reservation duration: Minutes" 
- Comment on [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404): Verified on the staging. Tested the New Reservation flow with modified start/end times using valid reservation durations. The Create Reservation API is triggered successfully , the reservation is created as expected, and the incorrect "Maximum Reservation duration: Minutes" error is no longer displayed. Fix verified successfully
- Comment on [HIEV-7317](https://elocity.atlassian.net/browse/HIEV-7317): Email id is not editable , working as expected
- Comment on [HIEV-7315](https://elocity.atlassian.net/browse/HIEV-7315): Verified on Staging. Applied filters are retained after clicking Refresh, and the filtered results remain unchanged. Working as expected.
- Comment on [HIEV-7313](https://elocity.atlassian.net/browse/HIEV-7313): Verified on staging. The Export Logs success pop-up, progress bar, and correct button behavior are now working as expected.
- Comment on [HIEV-7209](https://elocity.atlassian.net/browse/HIEV-7209): Verified on the latest Staging. Floating labels/placeholders remain consistently aligned after triggering field-level validation across the mandatory fields.Working as expected .
- Comment on [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166): Verified on the latest STG build. Newly created reservations with a future start time are now correctly displayed under both Today and This Year date ranges. Fix verified successfully.
- Comment on [HIEV-7018](https://elocity.atlassian.net/browse/HIEV-7018): Verified on Staging. After selecting and applying a single Charger filter, the map now displays only the corresponding location pin, while pins from other locations are removed. Fix verified successfully.
- Comment on [HIEV-6446](https://elocity.atlassian.net/browse/HIEV-6446): Issue 1 and 2 have been fixed working as expected
- Comment on [HIEV-6446](https://elocity.atlassian.net/browse/HIEV-6446): Issue 4 : The “Change” option can remain blue, as the color clearly indicates that it is an actionable link and improves discoverability.

**2026-08-12** — logged 0.8d (7h) of 1.0d (8h) available, 10 comments

- Worklog 30m on [HIEV-7481](https://elocity.atlassian.net/browse/HIEV-7481) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7480](https://elocity.atlassian.net/browse/HIEV-7480) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7479](https://elocity.atlassian.net/browse/HIEV-7479) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7478](https://elocity.atlassian.net/browse/HIEV-7478) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477) (Suggestion, mid-sprint)
- Worklog 40m on [HIEV-7476](https://elocity.atlassian.net/browse/HIEV-7476) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7475](https://elocity.atlassian.net/browse/HIEV-7475) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7474](https://elocity.atlassian.net/browse/HIEV-7474) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7466](https://elocity.atlassian.net/browse/HIEV-7466) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7396](https://elocity.atlassian.net/browse/HIEV-7396) (Task, mid-sprint)
- Worklog 0.50h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 20m on [HIEV-7165](https://elocity.atlassian.net/browse/HIEV-7165) (Bug, mid-sprint)
- Comment on [HIEV-7481](https://elocity.atlassian.net/browse/HIEV-7481): Validated the Bulk Operations → OCPP Action Center → Get Configuration flow. Selected one or more CPIDs. Selected Get Configuration . Selected predefined configuration keys. Verified the Perform Action button is enabled. Inspected the Network request for the get-configuration API. Confirmed the selected CPID is correctly passed in the request payload. Verified the configuration request is processed successfully without the previous HTTP 400 Bad Request error. Result: Fix verified successfully. T
- Comment on [HIEV-7480](https://elocity.atlassian.net/browse/HIEV-7480): Validated the Bulk Operations → OCPP Action Center → Get Configuration flow. Selected Charge Point ID(s) and Get Configuration action. Enabled the Custom option. Entered valid custom configuration keys. Confirmed the Perform Action button becomes enabled. Verified the action can be performed successfully using the entered custom keys. Result: Fix verified successfully. The issue has been resolved.
- Comment on [HIEV-7478](https://elocity.atlassian.net/browse/HIEV-7478): Validated the In-App Campaign maxDisplayCount functionality Configured campaign-welcome-001 with maxDisplayCount = 5 . Verified the campaign display count is tracked correctly across multiple app launches. Confirmed the campaign stops displaying after reaching its configured maximum display count. Tested multiple active campaigns with different display limits, such as campaign-welcome-001 = 5 and campaign-welcome-002 = 3 . Verified that each campaign follows its own configured maxDisplayCount in
- Comment on [HIEV-7466](https://elocity.atlassian.net/browse/HIEV-7466): Thanks for the clarification. Understood that the accordion state is intentionally reset to the default state after a successful update/page re-render, and maintaining the expanded/collapsed state is not currently required. I also understand that the accordion containing validation errors will be automatically expanded to allow the user to address the issue. Based on the clarification and expected behavior, closing this issue as no further action is required.
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Verified on the latest STG build. The Welcome campaign now respects the configured maxDisplayCount = 5 and stops displaying after the maximum display count is reached. Fix verified successfully.
- Comment on [HIEV-7396](https://elocity.atlassian.net/browse/HIEV-7396): Validated the In-App Campaign feature based on the provided test plan and additional functional scenarios. Verification performed: Verified campaign display for a fresh login with tour and biometric flow. Verified campaign display for returning users with completed tour and enabled biometrics. Verified biometric flow before campaign display for returning users with pending biometric setup. Verified campaign retrieval after a cold start of a previously logged-in session. Confirmed the campaign di
- Comment on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391): Working as expected
- Comment on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390): Working as expected
- Comment on [HIEV-7288](https://elocity.atlassian.net/browse/HIEV-7288): The issue is consistently reproducible when there is a single connector in the station , issue doesn't occur when there are multiple connectors , reopening the ticket
- Comment on [HIEV-7232](https://elocity.atlassian.net/browse/HIEV-7232): Update: The items from this suggestion have now been split for better tracking. The date/time readability and connector icon issues have been raised as separate bugs, while the + icon in the Reservation tab and Reserve action in the Location List are being tracked as UX enhancements. Closing this ticket.

**2026-08-13** — logged 0.9d (7h) of 1.0d (8h) available, 4 comments

- Worklog 1h 30m on [HIEV-7494](https://elocity.atlassian.net/browse/HIEV-7494) (Task, mid-sprint)
- Worklog 40m on [HIEV-7493](https://elocity.atlassian.net/browse/HIEV-7493) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7489](https://elocity.atlassian.net/browse/HIEV-7489) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7489](https://elocity.atlassian.net/browse/HIEV-7489) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7488](https://elocity.atlassian.net/browse/HIEV-7488) (Bug, mid-sprint)
- Worklog 1h 30m on [HIEV-7401](https://elocity.atlassian.net/browse/HIEV-7401) (Sub-task, mid-sprint)
- Worklog 0.50h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 0.75h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 0.25h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Comment on [HIEV-7494](https://elocity.atlassian.net/browse/HIEV-7494): Validated Employee ID support for Corporate Employees. Verified Employee ID field is available while adding a Corporate Employee. Verified Employee ID can be entered and saved with the employee details. Verified Employee ID is retained after saving and reopening the employee. Verified Employee ID is displayed correctly in the employee details. Verified Employee ID mapping to the corresponding charging session. Validated Employee ID behavior across applicable employee/session scenarios. Documente
- Comment on [HIEV-7489](https://elocity.atlassian.net/browse/HIEV-7489): Discussed this with Vinay regarding the missing Export/Download option for the Peak Hours report. Confirmed that the Download/Export option is intentionally hidden due to the high backend load associated with generating the Peak Hours report export . This is an existing product/technical decision and is also documented in HIEV-2238 – Hide Report Download button for the Peak Hours Report . Hence, the absence of the Export option is expected behavior and no change is required at this time. Closing
- Comment on [HIEV-7401](https://elocity.atlassian.net/browse/HIEV-7401): Validated the Export Module Enhancement and Optimization functionality. Reviewed the export requirements and identified the applicable reporting modules. Verified Export/Download functionality for the supported reports. Validated export behavior across different date ranges and report data. Verified the downloaded/exported data against the data displayed in the UI. Checked API requests and export responses through the Network tab. Verified loading/progress behavior during export operations. Vali
- Comment on [HIEV-7165](https://elocity.atlassian.net/browse/HIEV-7165): Confirmed from my end as well. I’m currently unable to reproduce the issue in STG.closing the ticket. I’ll review/retest it again if the issue is reported or reproduced in the future.

**2026-08-14** — logged 1.1d (9h) of 1.0d (8h) available, 1 comments

- Worklog 15m on [HIEV-7512](https://elocity.atlassian.net/browse/HIEV-7512) (Bug, mid-sprint)
- Worklog 40m on [HIEV-7510](https://elocity.atlassian.net/browse/HIEV-7510) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7509](https://elocity.atlassian.net/browse/HIEV-7509) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506) (Task, mid-sprint)
- Worklog 40m on [HIEV-7505](https://elocity.atlassian.net/browse/HIEV-7505) (Bug, mid-sprint)
- Worklog 40m on [HIEV-7504](https://elocity.atlassian.net/browse/HIEV-7504) (Bug, mid-sprint)
- Worklog 40m on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503) (Bug, mid-sprint)
- Worklog 40m on [HIEV-7501](https://elocity.atlassian.net/browse/HIEV-7501) (Bug, mid-sprint)
- Worklog 0.50h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 0.50h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Comment on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506): 14/07/2026 - Load Management QA Validated Load Group creation with EVSE make restrictions : Confirmed that Load Groups can be created only with Elocity Make EVSEs . Verified that attempting to create a Load Group with non-Elocity chargers is rejected with the message: “One or more chargers are not of Elocity make.” Validated charger online precondition for Load Group creation: Confirmed that the respective charger must be Online to create a Load Group. Verified that attempting to create a Load G

**2026-08-17** — logged 1.2d (10h) of 1.0d (8h) available, 11 comments

- Worklog 40m on [HIEV-7529](https://elocity.atlassian.net/browse/HIEV-7529) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7528](https://elocity.atlassian.net/browse/HIEV-7528) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7527](https://elocity.atlassian.net/browse/HIEV-7527) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7526](https://elocity.atlassian.net/browse/HIEV-7526) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7525](https://elocity.atlassian.net/browse/HIEV-7525) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7524](https://elocity.atlassian.net/browse/HIEV-7524) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7523](https://elocity.atlassian.net/browse/HIEV-7523) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7521](https://elocity.atlassian.net/browse/HIEV-7521) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7520](https://elocity.atlassian.net/browse/HIEV-7520) (Sub-task, mid-sprint)
- Worklog 15m on [HIEV-7518](https://elocity.atlassian.net/browse/HIEV-7518) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7517](https://elocity.atlassian.net/browse/HIEV-7517) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7516](https://elocity.atlassian.net/browse/HIEV-7516) (Bug, mid-sprint)
- Worklog 2h 30m on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506) (Task, mid-sprint)
- Worklog 30m on [HIEV-7288](https://elocity.atlassian.net/browse/HIEV-7288) (Bug, mid-sprint) — Re-tested Station Details scrolling across different station states and identified that the issue occurs specifically when the station is Disconnected/Unavailable. Updated the Jira with the additional observation
- Worklog 15m on [HIEV-7269](https://elocity.atlassian.net/browse/HIEV-7269) (Bug, mid-sprint)
- Comment on [HIEV-7525](https://elocity.atlassian.net/browse/HIEV-7525): Validation Scope: Verify Payment Type = Prepaid displays the required configuration fields such as: Minimum Balance Auto Stop Other applicable prepaid fields Verify Country dropdown loads available options. Verify Time Zone dropdown loads available options. Verify existing locations display previously configured Minimum Balance and related fields in View mode. Verify existing locations display the same configuration correctly in Edit mode. Verify existing stations display Advanced Controls corre
- Comment on [HIEV-7524](https://elocity.atlassian.net/browse/HIEV-7524): Validated the Guest Charging flow for the following connector states: Charging SuspendedEV SuspendedEVSE Finishing Faulted For each state: Scanned the Guest Charging QR code. Selected the affected connector. Verified the Location Details page behavior. Confirmed the Start Charging action is not available/enabled. Verified the message "Charging station is currently unavailable for guest charging" is displayed. Confirmed the user is prevented from proceeding to the Add Card/Payment flow. Verified 
- Comment on [HIEV-7523](https://elocity.atlassian.net/browse/HIEV-7523): Validated the Guest Charging payment flow on UAT. Scanned the Guest Charging QR code for an available station. Selected an available connector. Swiped Start Charging . Verified the Payment Details page is displayed when Minimum Balance is greater than 0. Entered valid payment/card details and submitted the payment. Verified payment/pre-authorisation is processed successfully. Confirmed the user is redirected to the Session Details screen instead of a 404 page. Verified the charging session is in
- Comment on [HIEV-7521](https://elocity.atlassian.net/browse/HIEV-7521): QA Validation Performed: Verified the Guest Charging flow on UAT / Android Chrome . Verified the behavior when no active charging session exists. Confirmed the "No active charging session found" handling. Tested the Retry action and confirmed the previous repeated retry-loop behavior is no longer occurring. Tested Cancel and confirmed the expected navigation behavior. Verified the Stop Charging action text has been corrected to "Swipe to Stop Charging" . Confirmed the reported issue is resolved 
- Comment on [HIEV-7520](https://elocity.atlassian.net/browse/HIEV-7520): Validation Performed Created a Load Group with valid configuration details. Selected the required location/station/EVSE. Clicked Save . Verified that the Save action completes successfully. Verified that the Load Group creation API is triggered. Verified that the Load Group is created successfully. Verified that the Save button does not remain in an indefinite loading state. Verified that no unexpected frontend error occurs. Verified the flow with stations selected, which was the scenario affect
- Comment on [HIEV-7517](https://elocity.atlassian.net/browse/HIEV-7517): Working as expected
- Comment on [HIEV-7516](https://elocity.atlassian.net/browse/HIEV-7516): Hi , thanks for checking this. I retested the reported scenarios on UAT now using the same flow, and I can confirm that the previously observed issues are no longer reproducible. Prepaid-related fields, Country/Time Zone options, and Make/Model options are loading as expected , and I am also able to view/edit the existing configuration. Since the issue is currently not reproducible, we can close this ticket. I’ll keep an eye on these scenarios during further UAT testing and raise a new ticket if
- Comment on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506): 17/07/2026 - Load Management QA Continued functional testing of Load Management / Load Group Overview . Validated Load Group configuration and EVSE/connector load behavior during charging and meter value updates. Tested Manual Rebalance behavior for a single-connector Load Group in a deviation/overload state; observed that the expected load correction was not occurring. Identified and documented an issue where Load Usage remains yellow (Near Limit) even at very low loads such as 1A/2A , despite 
- Comment on [HIEV-7468](https://elocity.atlassian.net/browse/HIEV-7468): Working as expected closing the ticket
- Comment on [HIEV-7288](https://elocity.atlassian.net/browse/HIEV-7288): Reopening the ticket based on additional observations during further validation. The scrolling issue is not observed in all scenarios. I found that it occurs when the station is in Disconnected/Unavailable state, while the Station Details page scrolls smoothly when the station is in other tested states. This suggests the issue may be related to the UI/content rendered for the Disconnected/Unavailable state. I have updated the ticket with the additional observation for further investigation.
- Comment on [HIEV-7269](https://elocity.atlassian.net/browse/HIEV-7269): Acknowledged. As confirmed by the developer , the twice-loading behavior is expected due to the Firebase configuration loading after the initial page load. This behavior is also present in other Guest Charging flows and is a known/accepted limitation by the business.Closing the ticket

**2026-08-18** — logged 0.7d (5h) of 1.0d (8h) available, 2 comments

- Worklog 3h 30m on [HIEV-7541](https://elocity.atlassian.net/browse/HIEV-7541) (Task, mid-sprint)
- Worklog 20m on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530) (Bug, mid-sprint)
- Comment on [HIEV-7541](https://elocity.atlassian.net/browse/HIEV-7541): Scope / Activities Tested Utility Tariff Design Validated creation of Utility Tariffs. Validated tariff name field and character-length behaviour. Tested TOU (Time-of-Use) tariff creation. Tested Tiered tariff creation. Validated switching between TOU and Tiered configurations. Validated adding/removing TOU intervals. Validated adding/removing Tier bands. TOU Validation Time intervals must not overlap. At least one day must be selected. Price must be a positive number. To time cannot be the same
- Comment on [HIEV-7535](https://elocity.atlassian.net/browse/HIEV-7535): Not an issue , Closing this bug

**2026-08-19** — logged 0.9d (7h) of 1.0d (8h) available, 8 comments

- Worklog 1h on [HIEV-7551](https://elocity.atlassian.net/browse/HIEV-7551) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7549](https://elocity.atlassian.net/browse/HIEV-7549) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7547](https://elocity.atlassian.net/browse/HIEV-7547) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7543](https://elocity.atlassian.net/browse/HIEV-7543) (Sub-task, mid-sprint)
- Worklog 15m on [HIEV-7527](https://elocity.atlassian.net/browse/HIEV-7527) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506) (Task, mid-sprint)
- Comment on [HIEV-7551](https://elocity.atlassian.net/browse/HIEV-7551): QA Validation Completed Validated Load Group edit/update functionality in Staging: Edited existing Load Groups with no active charging sessions . Modified editable Load Group configuration values and saved the changes. Validated the flow with an online connector . Validated the flow with an offline connector . Confirmed that updates are saved successfully when there are no ongoing charging sessions. Verified that the previous generic "Something went wrong!" error is no longer displayed incorrect
- Comment on [HIEV-7547](https://elocity.atlassian.net/browse/HIEV-7547): Testing / Validation Points Tested a Load Group with a single Elocity connector . Started a charging transaction using the OCPP simulator . Started MeterValues and reported a load above the allocated limit to simulate a Deviation condition. Verified that the Load Group/connector entered Deviation . Triggered Manual Rebalance while the connector was in Deviation. Verified the Manual Rebalance API response returned a Request ID with status: accepted . Verified that the simulator received SetChargi
- Comment on [HIEV-7543](https://elocity.atlassian.net/browse/HIEV-7543): Scope: Energy Used Station Availability Connector Faults Station Outages Connector Fault Duration Outage Duration Utilisation Validation: Verify all CPIDs are included as expected. Verify records and values correspond to the selected date range. Verify no genuinely invalid or unexpected data is present. Validate across different date ranges such as Yesterday, Last Week, Last Month, and This Year.
- Comment on [HIEV-7529](https://elocity.atlassian.net/browse/HIEV-7529): Retested on STG after the fix was deployed. Validated the single-connector Load Group Deviation scenario using the OCPP simulator. Manual Rebalance now triggers the expected corrective flow — status: accepted response was received, SetChargingProfile was sent to the connector, and the expected RemoteStopTransaction flow was observed for the simulated Deviation condition. As clarified by the developer, the simulator can report meter values above the applied charging profile, whereas real Elocity 
- Comment on [HIEV-7527](https://elocity.atlassian.net/browse/HIEV-7527): Closing this as expected behavior. As clarified by the developer, there is currently no dedicated GET API to fetch Load Group-specific details on page refresh. The Load Group details page is populated using data fetched from the Load Group grid and passed when navigating into the specific Load Group. Therefore, on browser refresh, the user is redirected to the Load Group list so the required data can be fetched again.
- Comment on [HIEV-7526](https://elocity.atlassian.net/browse/HIEV-7526): Working as expected
- Comment on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506): 19/07/2026 - Load Management QA Completed QA validation of Load Management functionality in Staging, covering: Load Group Edit/Update: Verified existing Load Groups can be edited and updated successfully when there are no ongoing charging sessions. Validated Load Group update with both online and offline connectors . Confirmed the previous EVSE_GROUP_UPDATE_ONGOING_SESSIONS / HTTP 500 error is no longer incorrectly triggered when no active charging session exists. Verified updated Load Group con
- Comment on [HIEV-7488](https://elocity.atlassian.net/browse/HIEV-7488): As clarified, all CPIDs are expected to be included in the export. Additional rows are not present with Charge Point IDs such as 0 , 1 , 2 , 3 , etc. Working as expected closing the ticket

**2026-08-20** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 20m on [HIEV-7565](https://elocity.atlassian.net/browse/HIEV-7565) (Suggestion, mid-sprint)
- Worklog 45m on [HIEV-7563](https://elocity.atlassian.net/browse/HIEV-7563) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7562](https://elocity.atlassian.net/browse/HIEV-7562) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7561](https://elocity.atlassian.net/browse/HIEV-7561) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7560](https://elocity.atlassian.net/browse/HIEV-7560) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558) (Bug, mid-sprint)
- Worklog 4h 30m on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506) (Task, mid-sprint)
- Comment on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506): 20/Aug/2026 - QA Validation Load Management Continued Load Management testing in Staging, covering: Validated Load Group configuration boundaries with Max Load, Curtailment Limit and Minimum Current. Tested Max Load = Curtailment Limit = Minimum Current (6A) and verified the configuration and charging behavior. Started a single-connector charging session and verified the expected allocated load / real-time load behavior. Verified SetChargingProfile was sent correctly with the allocated limit and
- Comment on [HIEV-7500](https://elocity.atlassian.net/browse/HIEV-7500): QA Observation: The reported suggestion dropdown is generated by the browser's native autofill/history functionality and is not part of the CPMS application UI. The application does not control the rendering, positioning, or behavior of these browser-generated suggestions. The overlap with the Cancel/Save buttons is therefore caused by browser-native behavior and is not reproducible as an application-level UI defect. Closing as: Browser-specific behavior.

**2026-08-21** — logged 1.1d (8h) of 1.0d (8h) available, 14 comments

- Worklog 45m on [HIEV-7572](https://elocity.atlassian.net/browse/HIEV-7572) (Sub-task, mid-sprint)
- Worklog 1h on [HIEV-7571](https://elocity.atlassian.net/browse/HIEV-7571) (Sub-task, mid-sprint)
- Worklog 45m on [HIEV-7570](https://elocity.atlassian.net/browse/HIEV-7570) (Sub-task, mid-sprint)
- Worklog 1h on [HIEV-7569](https://elocity.atlassian.net/browse/HIEV-7569) (Sub-task, mid-sprint)
- Worklog 40m on [HIEV-7568](https://elocity.atlassian.net/browse/HIEV-7568) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7567](https://elocity.atlassian.net/browse/HIEV-7567) (Sub-task, mid-sprint)
- Worklog 15m on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7288](https://elocity.atlassian.net/browse/HIEV-7288) (Bug, mid-sprint)
- Worklog 0.75h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Worklog 2.50h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Comment on [HIEV-7572](https://elocity.atlassian.net/browse/HIEV-7572): Validated the EVSE Model creation and search flow on STG. Created EVSE Models with different connector configurations, including 2 connectors and 3 connectors . Verified the model creation flow with all mandatory details. Initial validation showed the reported issue; the created model was not immediately visible in the list/search. Retested the flow after the fix was available. Confirmed newly created EVSE Models are now displayed correctly in the list. Verified the created models can be found u
- Comment on [HIEV-7571](https://elocity.atlassian.net/browse/HIEV-7571): QA Validation Completed Retested Load Group creation and update scenarios involving station selection. Created a new Load Group with a station selected and verified the configuration is now created successfully. Edited an existing Load Group and added/selected a station, then verified the changes are saved successfully. Verified the previous 60–90 second continuous loading behavior is no longer observed. Verified the previous "Failed to enable load management config on one or more Elocity charge
- Comment on [HIEV-7570](https://elocity.atlassian.net/browse/HIEV-7570): Validated the Reservation flow on HIEV Canada Android UAT. Created a reservation for a connector with a specific time slot. Returned to the same connector's reservation flow. Verified the previously reserved time slot is displayed in red and is not selectable. Verified other available time slots remain selectable. Verified the Join Queue chart also displays the booked timeline in red. Confirmed users cannot select or proceed with an already reserved time slot. Verified the reservation availabili
- Comment on [HIEV-7569](https://elocity.atlassian.net/browse/HIEV-7569): QA Validation Completed Validated Load Group behavior when assigned connectors/stations are decommissioned. When a Load Group has multiple connectors , decommissioning one connector removes the decommissioned connector while the Load Group remains available with the remaining connector(s). When a Load Group has only one connector , decommissioning that connector results in the Load Group no longer being displayed in the Load Group list. Discussed the single-connector behavior with the developer 
- Comment on [HIEV-7568](https://elocity.atlassian.net/browse/HIEV-7568): Validated the Session Management flow across multiple browsers on STG. Logged in to the Portal using the first browser. Logged in using the same account from a second browser and selected Logout Existing Session . Returned to the first browser and performed actions/refresh. Confirmed the previously active session is invalidated and the user is logged out. Verified the user is not stuck in the "Something went wrong" refresh loop. Confirmed no repeated error pop-ups or refresh loops are observed. 
- Comment on [HIEV-7567](https://elocity.atlassian.net/browse/HIEV-7567): Validated the Guest Charging dropdown filter in the Charging Session grid on UAT. Verified the Guest Charging filter is available in the grid. Verified the filter options can be selected successfully. Applied the Guest Charging filter and verified the corresponding charging session records. Verified the results are filtered correctly based on the selected option. Verified the filter can be changed/reset and the grid updates accordingly. Result: Fix verified successfully. The Guest Charging dropd
- Comment on [HIEV-7563](https://elocity.atlassian.net/browse/HIEV-7563): QA Validation: Retested the Load Group behavior after station/connector decommissioning. With multiple connectors , decommissioning one connector removes the decommissioned connector while the Load Group remains available with the remaining connector(s). With a single connector , decommissioning that connector results in the Load Group being removed from the Load Group list. Discussed the single-connector behavior with the developer and confirmed that the current behavior is accepted for this re
- Comment on [HIEV-7560](https://elocity.atlassian.net/browse/HIEV-7560): Working as expected closing the bug
- Comment on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503): Retested in Staging. Issue is still reproducible with an additional observation. On clicking Save , the page remains in a loading state for around 30–40 seconds . After the loading completes, “Failed to fetch EVSE model” is observed in the background. “Something went wrong” is displayed on the UI with an option to refresh the page. Clicking Refresh Page results in a CORS error in the Network tab. The application then enters an error/refresh loop and remains unusable. Clearing site data is requir
- Comment on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503): Retested in staging , Issue has been fixed , working as expected , closing the ticket
- Comment on [HIEV-7331](https://elocity.atlassian.net/browse/HIEV-7331): Validated in UAT , working as expected
- Comment on [HIEV-7288](https://elocity.atlassian.net/browse/HIEV-7288): Validated the observation. The scrolling issue is reproducible in specific device/browser combinations. As discussed, Closing the ticket for now; we can re-evaluate it in a future iteration if required.
- Comment on [HIEV-7243](https://elocity.atlassian.net/browse/HIEV-7243): Verified on Staging. Previously reserved time slots are now displayed in red and are not selectable in the reservation flow. The booked timeline is also correctly displayed in red in the Join Queue chart. Fix verified successfully.
- Comment on [HIEV-7214](https://elocity.atlassian.net/browse/HIEV-7214): Verified on STG using multiple browsers with the same user account. After invalidating the first browser session, performing an action or refresh now logs the user out without triggering the previous "Something went wrong" refresh loop. Fix verified successfully.

**2026-08-24** — logged 0.2d (2h) of 1.0d (8h) available, 2 comments

- Worklog 45m on [HIEV-7583](https://elocity.atlassian.net/browse/HIEV-7583) (Sub-task, mid-sprint)
- Worklog 15m on [HIEV-7578](https://elocity.atlassian.net/browse/HIEV-7578) (Observation, mid-sprint)
- Worklog 1h on [HIEV-7577](https://elocity.atlassian.net/browse/HIEV-7577) (Sub-task, mid-sprint)
- Comment on [HIEV-7577](https://elocity.atlassian.net/browse/HIEV-7577): Validated the 401 Unauthorized session handling on STG. Kept the CPMS Portal idle for an extended period and performed an action after the session became invalid. Verified the API returns a 401 Unauthorized response. Confirmed the 401 response headers are received by the frontend. Verified the frontend triggers the logout sequence when the unauthorized response is received. Confirmed the user is not stuck on the "Something Went Wrong" popup or an infinite refresh loop. Verified the user can retu
- Comment on [HIEV-7264](https://elocity.atlassian.net/browse/HIEV-7264): Verified on STG. After session invalidation, the API returns 401 Unauthorized with the expected response headers, and the frontend correctly triggers the logout sequence. The user is no longer stuck in the "Something Went Wrong" refresh loop. Fix verified successfully.

**2026-08-25** — logged 1.7d (14h) of 1.0d (8h) available, 3 comments

- Worklog 15m on [HIEV-7585](https://elocity.atlassian.net/browse/HIEV-7585) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7584](https://elocity.atlassian.net/browse/HIEV-7584) (Suggestion, mid-sprint)
- Worklog 1d 1h on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506) (Task, mid-sprint)
- Worklog 4.00h on [HIEV-7193](https://elocity.atlassian.net/browse/HIEV-7193) (Epic, mid-sprint)
- Comment on [HIEV-7583](https://elocity.atlassian.net/browse/HIEV-7583): Validated the Queue Reservation flow on HIEV Canada Android UAT. Joined the queue with a 1-hour charging duration . Verified the first queue reservation is created successfully with an assigned start time. Attempted to create another queue reservation while another valid consecutive time slot was available. Verified the application correctly identifies and allocates the next available time slot. Confirmed the second queue reservation is created successfully without displaying an incorrect "Time 
- Comment on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506): 25/Aug/2026 - Load Management QA Validation – Balanced & FIFO Continued end-to-end validation of Load Management using multiple stations/connectors with Balanced and First In First Out (FIFO) management modes. Balanced Mode Validation Configured a Load Group with multiple connectors/stations using: Max Load Limit: 30A Curtailment Limit: 24A Minimum Current: 6A Input Voltage: 230V Management Mode: Balanced Verified allocation with multiple active charging sessions: 2 active sessions: 12A + 12A = 
- Comment on [HIEV-7240](https://elocity.atlassian.net/browse/HIEV-7240): Working as expected closing the bug

**2026-08-26** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 1d on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506) (Task, mid-sprint)
- Comment on [HIEV-7506](https://elocity.atlassian.net/browse/HIEV-7506): 26/Aug/2026 - Continued Load Management validation – Round Robin mode: Configured Round Robin management mode with a 1-minute time interval and validated configuration/save behavior. Identified a validation gap in the Time Interval field: UI allows values beyond the backend-supported limit, while the API rejects values greater than 10,000,000 . Confirmed 10,000,001 is rejected by the backend and raised this as a separate validation issue. Investigated offline load reservation behavior and confir

**2026-08-27** — logged 0.3d (2h) of 1.0d (8h) available, 10 comments

- Worklog 30m on [HIEV-7598](https://elocity.atlassian.net/browse/HIEV-7598) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7596](https://elocity.atlassian.net/browse/HIEV-7596) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7595](https://elocity.atlassian.net/browse/HIEV-7595) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7594](https://elocity.atlassian.net/browse/HIEV-7594) (Sub-task, mid-sprint)
- Worklog 20m on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530) (Bug, mid-sprint)
- Comment on [HIEV-7598](https://elocity.atlassian.net/browse/HIEV-7598): Validation covered: Navigated to Menu → Revenue Share → Utility Tariff → Reports . Verified the chart against the approved design. Verified Revenue and Energy Cost are displayed correctly. Opened the chart in Fullscreen . Tested Zoom Out (-) multiple times. Verified both Revenue and Energy Cost data remain visible after zooming. Verified the chart does not lose either dataset or its corresponding axis. Verified Reset Zoom restores the expected chart view.
- Comment on [HIEV-7596](https://elocity.atlassian.net/browse/HIEV-7596): Validation covered: Navigated to Menu → Revenue Share → Utility Tariff → Reports . Verified the Revenue vs Energy Cost chart displays correctly. Opened the chart in Fullscreen . Verified both Revenue and Energy Cost data are displayed. Tested Zoom In (+) functionality. Verified the left Y-axis (Revenue) labels remain visible after zooming. Verified the right Y-axis (Energy Cost) labels remain visible. Verified horizontal grid lines remain displayed and correctly aligned. Verified the chart data 
- Comment on [HIEV-7595](https://elocity.atlassian.net/browse/HIEV-7595): Validation covered: Opened Menu → Revenue Share → Utility Tariff → Reports . Opened the Energy Cost chart in fullscreen. Verified the chart after clicking Zoom In (+) . Performed multiple zoom-in actions, including up to 5–6 consecutive zooms . Verified Y-axis tick values remain consistently and proportionally spaced. Verified horizontal grid lines remain properly aligned with the corresponding Y-axis values. Verified the chart remains usable and readable at different zoom levels.
- Comment on [HIEV-7594](https://elocity.atlassian.net/browse/HIEV-7594): Validation covered: Created a Utility Tariff with Tiered configuration. Verified the saved Tiered tariff appears correctly under Designed Utility Tariff . Opened the tariff in View/Edit mode. Verified Tiered is selected by default. Verified the previously saved Tiered configuration is displayed immediately. Verified there is no need to manually switch between TOU and Tiered to view the saved configuration. Verified the behavior for the relevant tariff configuration.
- Comment on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558): Working as expected ,Closing the ticket
- Comment on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540): Working as expected ,Closing the ticket
- Comment on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538): Working as expected ,Closing the ticket
- Comment on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534): Working as expected
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): Retest – Failed Field-level validation is now displayed for the invalid values. However, when clicking Save , the form still submits and an error modal is displayed with raw backend/API validation messages: document.tierBands.0.minKwh must not be less than 0 document.tierBands.0.minKwh must be a number conforming to the specified constraints document.tierBands.0.rate must not be less than 0 document.tierBands.0.rate must be a number conforming to the specified constraints These technical API val
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): Retest Update – Failed Tariff Name: PASS The 30-character limit is now enforced. When more than 30 characters are entered, the validation message "Tariff Name is too lengthy!" is displayed and the tariff cannot be saved. No further functional issue observed. TOU Price: FAIL The Price field still allows excessively large numeric values to be entered. Although a validation message is displayed, clicking Save still successfully creates the tariff. When the created tariff is opened for viewing, the 

### Priyanshu — 20.1 of 20.0d (161h of 160h)

**2026-08-03** — logged 0.2d (2h) of 1.0d (8h) available, 1 comments

- Worklog 2h on [HIEV-7341](https://elocity.atlassian.net/browse/HIEV-7341) (Task, mid-sprint)
- Comment on [HIEV-7341](https://elocity.atlassian.net/browse/HIEV-7341): import new cert for TE, with RSA 2048, changed and validate as well now it will work till

**2026-08-04** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 2h on [HIEV-7392](https://elocity.atlassian.net/browse/HIEV-7392) (Sub-task, planned)
- Worklog 2h on [HIEV-7392](https://elocity.atlassian.net/browse/HIEV-7392) (Sub-task, planned)
- Worklog 2h on [HIEV-7389](https://elocity.atlassian.net/browse/HIEV-7389) (Task, mid-sprint)
- Worklog 2h on [HIEV-7368](https://elocity.atlassian.net/browse/HIEV-7368) (Task, planned)
- Comment on [HIEV-7389](https://elocity.atlassian.net/browse/HIEV-7389): analysis and created the report regarding the invoice generated by oracle cloud
- Comment on [HIEV-7368](https://elocity.atlassian.net/browse/HIEV-7368): started working on the detailed documentation of existing infrastructure.

**2026-08-05** — logged 1.0d (8h) of 1.0d (8h) available, 3 comments

- Worklog 1d on [HIEV-7392](https://elocity.atlassian.net/browse/HIEV-7392) (Sub-task, planned)
- Comment on [HIEV-7392](https://elocity.atlassian.net/browse/HIEV-7392): started working on the detailed documentation of existing infrastructure.
- Comment on [HIEV-7392](https://elocity.atlassian.net/browse/HIEV-7392): link :- Changes completed: Refreshed lower-env inventory for OCI Toronto region and AWS us-east-1. Added deeper OCI resource coverage including block volumes, boot volumes, object storage buckets, certificates, vaults, and OKE resources. Added AWS coverage for Lambda, ECR, CloudFormation, launch templates, Route53, ACM, S3, and related resources. Added OCI OpenSearch cluster details after validating from OCI console and targeted CLI lookup. OCI OpenSearch clusters added.
- Comment on [HIEV-7389](https://elocity.atlassian.net/browse/HIEV-7389): OCI CLOUD COST july-2026 = $3,311.22 (USD) june-2026 = $3,251.57 (USD) may-2026 = $3,782.64 (USD) apr-2026 = $4,836.54 (USD) march- 2026 = $5,059.50 (USD) feb-2026 = $3,541.87 (USD)

**2026-08-06** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 4h on [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393) (Sub-task, planned)
- Worklog 4h on [HIEV-7392](https://elocity.atlassian.net/browse/HIEV-7392) (Sub-task, planned)
- Comment on [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393): • Updated the canada-prod AWS cloud inventory documentation. Changes completed: Created/refreshed canada-prod inventory for AWS ca-central-1. Added structured Confluence-ready sections by service. Covered VPCs, subnets, route tables, internet/NAT gateways, security groups, Elastic IPs, EC2, EBS, load balancers, target groups, RDS, MSK, EKS, Auto Scaling groups, launch templates, SNS, ACM, Route53, and S3. Added OpenSearch coverage and documented the active OpenSearch domain.

**2026-08-07** — logged 0.1d (1h) of 1.0d (8h) available, 1 comments

- Worklog 1h on [HIEV-7432](https://elocity.atlassian.net/browse/HIEV-7432) (Task, mid-sprint)
- Comment on [HIEV-7432](https://elocity.atlassian.net/browse/HIEV-7432): now build stage can run by any branch and only deployment stage will run by main branch

**2026-08-09** — logged 1.5d (12h) of 0.0d (0h) available, 0 comments

- Worklog 2h on [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395) (Sub-task, planned)
- Worklog 2h on [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394) (Sub-task, planned)
- Worklog 1d on [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393) (Sub-task, planned)

**2026-08-10** — logged 0.9d (7h) of 1.0d (8h) available, 5 comments

- Worklog 3h on [HIEV-7457](https://elocity.atlassian.net/browse/HIEV-7457) (Task, mid-sprint)
- Worklog 2h on [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395) (Sub-task, planned)
- Worklog 2h on [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394) (Sub-task, planned)
- Comment on [HIEV-7457](https://elocity.atlassian.net/browse/HIEV-7457): adani aws - 157.3 adani oci - 118.2 alfanar oci - 214.6 india aws - 3.13 india oci - 0.07 canada aws - 540.61 lower-env oci - 322.61 lower -env aws - 53.48 prod compartment - 13.31
- Comment on [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395): Alfanar prod: OCI-only inventory updated OCI region: me-jeddah-1 OCI compartment: alfanar Route table, security list, and NSG rule details included Latest report generated and updated
- Comment on [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394): Adani prod: Combined AWS + OCI inventory created AWS region: ap-south-1 OCI region: ap-mumbai-1 OCI compartment: adani Route table, security list, NSG, AWS route, and AWS security group rule details included Latest report generated and updated
- Comment on [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393): Canada prod: AWS-only inventory for ca-central-1 Service Summary links added Plain Markdown links only, no visible HTML anchors Latest report generated and updated
- Comment on [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393): link - https://elocity.atlassian.net/wiki/spaces/DevOps/pages/2175336449/canada-prod+AWS+Cloud+Resource+Inventory

**2026-08-11** — logged 1.0d (8h) of 1.0d (8h) available, 0 comments

- Worklog 2h on [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395) (Sub-task, planned)
- Worklog 2h on [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394) (Sub-task, planned)
- Worklog 4h on [HIEV-7371](https://elocity.atlassian.net/browse/HIEV-7371) (Task, planned)

**2026-08-12** — logged 1.5d (12h) of 1.0d (8h) available, 4 comments

- Worklog 1d 4h on [HIEV-7371](https://elocity.atlassian.net/browse/HIEV-7371) (Task, planned)
- Comment on [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395): Document Link:-
- Comment on [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394): Document Link:-
- Comment on [HIEV-7371](https://elocity.atlassian.net/browse/HIEV-7371): Completed so far: Confirmed OCI tenancy is using IAM Identity Domain flow. Identified correct OCI navigation for SAML IdP setup: Identity & Security → Domains → Default → Federation → Identity providers Confirmed SAML IdP creation is available from: Identity providers → Actions → Add SAML IdP Defined target access model: Entra ID users/groups → SCIM provisioning → OCI Identity Domain users/groups → OCI IAM policies Created step-by-step runbook: OCI_EntraID_SSO_SCIM_Runbook.md Updated runbook wit
- Comment on [HIEV-7371](https://elocity.atlassian.net/browse/HIEV-7371): Completed OCI and Microsoft Entra ID SSO/SCIM integration work. Summary: Configured Microsoft Entra ID SAML SSO for OCI Console. Activated OCI SAML Identity Provider: Microsoft Entra ID(OCI_access). Updated OCI Default Identity Provider Policy to allow Entra SSO while keeping Username-Password enabled for fallback. Assigned OCI Console app to the IdP policy. Validated Entra SSO login flow successfully. Configured SCIM provisioning from Entra ID to OCI Identity Domain. Created/configured OCI conf

**2026-08-13** — logged 1.0d (8h) of 1.0d (8h) available, 3 comments

- Worklog 1h on [HIEV-7486](https://elocity.atlassian.net/browse/HIEV-7486) (Task, mid-sprint)
- Worklog 1h on [HIEV-7486](https://elocity.atlassian.net/browse/HIEV-7486) (Task, mid-sprint)
- Worklog 1h on [HIEV-7486](https://elocity.atlassian.net/browse/HIEV-7486) (Task, mid-sprint)
- Worklog 5h on [HIEV-7371](https://elocity.atlassian.net/browse/HIEV-7371) (Task, planned)
- Comment on [HIEV-7486](https://elocity.atlassian.net/browse/HIEV-7486): Fixed the DOTA/CodePush outage. The application services were running, but the VM firewall was rejecting inbound HTTP/HTTPS traffic, so api.evnet.xyz:443 was unreachable publicly. Added and persisted iptables allow rules for ports 80 and 443, then renewed the expired Let’s Encrypt certificate and reloaded nginx. Verified: https://api.evnet.xyz/ returns 200 OK https://dashboard.evnet.xyz/ redirects to /dashboard TLS certificate is valid until 2026-11-11
- Comment on [HIEV-7486](https://elocity.atlassian.net/browse/HIEV-7486): The DOTA API auth middleware was treating every Bearer token as a Google ID token unless it had the old cli- prefix. I changed it so Bearer auth now checks the stored Token List / access key first, then falls back to Google ID token auth for dashboard login. Verified on https://api.evnet.xyz using the existing CLI Access key: GET /authenticated -> 200 GET /account -> 200 GET /apps -> 200 I rebuilt and restarted dota-api.service; nginx, mysql, redis, and the API service are all active.
- Comment on [HIEV-7371](https://elocity.atlassian.net/browse/HIEV-7371): Continued OCI Entra ID SSO rollout validation. Verified Default Identity Provider Policy is active. Configured/confirmed IdP rules for Admin local fallback and Standard Entra SSO. Confirmed Entra SSO remains available for standard OCI groups. Reviewed OCI Console sign-on/security policy behavior. Identified that hiding/blocking username-password requires changes to Security Policy for OCI Console, not only IdP policy. Decided not to apply deny sign-on rules now due to lockout risk. Left current 

**2026-08-16** — logged 1.0d (8h) of 0.0d (0h) available, 0 comments

- Worklog 4h on [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508) (Sub-task, planned)
- Worklog 4h on [HIEV-7507](https://elocity.atlassian.net/browse/HIEV-7507) (Sub-task, planned)

**2026-08-17** — logged 1.1d (9h) of 1.0d (8h) available, 4 comments

- Worklog 3h on [HIEV-7522](https://elocity.atlassian.net/browse/HIEV-7522) (Task, mid-sprint)
- Worklog 6h on [HIEV-7507](https://elocity.atlassian.net/browse/HIEV-7507) (Sub-task, planned)
- Comment on [HIEV-7522](https://elocity.atlassian.net/browse/HIEV-7522): adani(aws) - 199.52 adani(oci) - 130.29 alfanar(oci) - 227.8 india(aws) - 5.15 india(oci) - 0.07 canada(aws) - 542.79 lower-env(aws) - 55.98 lower-env(oci) - 335.05 prod_compartment - 15.63
- Comment on [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508): Reviewed alfanra prod OCI jeddah security posture and updated the security tightening runbook with detailed service-wise review steps and proposed tightening sequence. No OCI changes were applied; this was documentation and planning only.
- Comment on [HIEV-7507](https://elocity.atlassian.net/browse/HIEV-7507): Reviewed Adani prod OCI Mumbai security posture and updated the security tightening runbook with detailed service-wise review steps, AWS connectivity observations from OCI side, and proposed tightening sequence. No OCI changes were applied; this was documentation and planning only.
- Comment on [HIEV-7507](https://elocity.atlassian.net/browse/HIEV-7507): Completed today’s Adani prod OCI Mumbai zero-downtime security tightening and validation. Work completed: Took before-state backups before each change. Restricted SSH 22 from public access to 10.100.0.0/16. Restricted OKE API 6443 from public access to 10.100.0.0/16. Restricted Kafka 9092 from public access to 10.100.0.0/16. Removed public access to ingress-nginx metrics/status port 10254. Removed public access to Istio status port 15021. Validated Kubernetes access through VPN/private context. 

**2026-08-18** — logged 1.2d (10h) of 1.0d (8h) available, 1 comments

- Worklog 1d on [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508) (Sub-task, planned)
- Worklog 2h on [HIEV-7507](https://elocity.atlassian.net/browse/HIEV-7507) (Sub-task, planned)
- Comment on [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508): Work completed: Enabled VCN flow logs for alfanar-prod-private-subnet. Created capture filter for accepted/rejected private subnet traffic. Confirmed flow logs are ingesting records successfully. Verified initial private subnet traffic records are visible in OCI Logging. Documented flow log OCIDs, retention, and observation plan in the security status report. Reviewed remaining SFTP/FTP exposure and identified that source client IPs must be confirmed before narrowing rules. Flow log details: Reg

**2026-08-19** — logged 0.8d (6h) of 1.0d (8h) available, 0 comments

- Worklog 2h on [HIEV-7555](https://elocity.atlassian.net/browse/HIEV-7555) (Task, mid-sprint)
- Worklog 4h on [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508) (Sub-task, planned)

**2026-08-20** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 2h on [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508) (Sub-task, planned)
- Worklog 4h on [HIEV-7370](https://elocity.atlassian.net/browse/HIEV-7370) (Task, planned)
- Comment on [HIEV-7555](https://elocity.atlassian.net/browse/HIEV-7555): Implemented automated Let’s Encrypt wildcard certificate renewal for lower/dev *.evnet.xyz and integrated it with OCI Certificate Service. Summary: Configured renewal on dev VPN instance elocity-development-vpn-instance ( 10.50.33.29 ). Installed and configured certbot with Cloudflare DNS-01 validation. Created scoped Cloudflare API token for evnet.xyz with: Zone:DNS:Edit Zone:Zone:Read Client IP restricted to 192.18.159.179 Installed OCI CLI in isolated root venv at /opt/oci-cli-venv/bin/oci . 
- Comment on [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508): Reviewed 24+ hours of VCN flow logs for alfanar-prod-private-subnet. Findings: No 10.104.* or 10.0.* traffic observed. No rejected traffic observed. Kafka 9092 traffic is only from internal 10.102.0.0/16 sources, mainly OKE worker nodes. Public-looking sources in logs appear to be return traffic from outbound connections, not required inbound exposure. Recommendation: Safe to remove the private security-list rule 0.0.0.0/0 -> all marked “Kafka broker access”. Keep 10.102.0.0/16 -> all unchanged 

**2026-08-21** — logged 0.0d (0h) of 1.0d (8h) available, 2 comments

- Comment on [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508): Removed the private security-list ingress rule: 0.0.0.0/0 -> all description: Kafka broker access Validation completed: OCI security list now has 9 ingress rules; the broad Kafka rule is gone. Private API 10.102.36.143:6443 reachable. alfanar-prod nodes all Ready. No pods in non-Running/non-Succeeded state. Kafka namespace pods are Running. Services list is accessible. Public LB 141.147.129.183:80 and :443 reachable. Private Istio LB 10.102.31.166:15021 reachable.
- Comment on [HIEV-7370](https://elocity.atlassian.net/browse/HIEV-7370): Discussed this with srikant and it will be same as the dev as well stg the repor is ready need to validate the load before deploying into the cluster step for oci-stg: deploy the same Strimzi operator chart using kafka/oci-stg into the kafka-stg namespace on lower-env. Config is already aligned with oci-dev; new one points to kafka-stg.

**2026-08-23** — logged 1.5d (12h) of 0.0d (0h) available, 0 comments

- Worklog 4h on [HIEV-7575](https://elocity.atlassian.net/browse/HIEV-7575) (Task, mid-sprint)
- Worklog 4h on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574) (Task, mid-sprint)
- Worklog 2h on [HIEV-7573](https://elocity.atlassian.net/browse/HIEV-7573) (Task, mid-sprint)
- Worklog 2h on [HIEV-7573](https://elocity.atlassian.net/browse/HIEV-7573) (Task, mid-sprint)

**2026-08-24** — logged 0.9d (7h) of 1.0d (8h) available, 3 comments

- Worklog 3h on [HIEV-7582](https://elocity.atlassian.net/browse/HIEV-7582) (Task, mid-sprint)
- Worklog 4h on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574) (Task, mid-sprint)
- Comment on [HIEV-7575](https://elocity.atlassian.net/browse/HIEV-7575): Actions completed: Cleaned old Docker runner cache volumes. Removed unused GitLab runner cache volumes via docker volume rm . Reset Docker data root during maintenance window after confirming no active runner jobs. Preserved old Docker data as rollback backup: /var/lib/docker.bak.2026-08-21-073301 Recreated fresh /var/lib/docker . Restarted and validated Docker and GitLab Runner services. Added automated cleanup script with 7-day retention.
- Comment on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574): Added GitLab self-managed registry support in lower-env. Created/updated gitlab-self-registry-secret in all namespaces where gitlab-registry-secret already exists. Details: Cluster/context: lower-env Secret name: gitlab-self-registry-secret Secret type: kubernetes.io/dockerconfigjson Registry server: gitlab.evnet.xyz:5050 Namespaces updated: 57 Existing gitlab-registry-secret was not modified and remains available. Also configured Argo CD repository access for: https://gitlab.evnet.xyz/elocity1/
- Comment on [HIEV-7573](https://elocity.atlassian.net/browse/HIEV-7573): Completed July 2026 cost comparison for Canada prod vs Adani prod. Summary: Canada prod before tax: $2,397.58 Canada prod after 13% tax: $2,709.27 Adani prod before tax: ~$1,456.64 Adani prod billed/after-tax view: ~$1,635.92 Canada is higher by ~$1,073/month after tax.

**2026-08-25** — logged 1.5d (12h) of 1.0d (8h) available, 4 comments

- Worklog 1h on [HIEV-7586](https://elocity.atlassian.net/browse/HIEV-7586) (Task, mid-sprint)
- Worklog 2h on [HIEV-7575](https://elocity.atlassian.net/browse/HIEV-7575) (Task, mid-sprint)
- Worklog 2h on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574) (Task, mid-sprint)
- Worklog 4h on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574) (Task, mid-sprint)
- Worklog 3h on [HIEV-7370](https://elocity.atlassian.net/browse/HIEV-7370) (Task, planned)
- Comment on [HIEV-7582](https://elocity.atlassian.net/browse/HIEV-7582): $162.85 adani (aws) $3.39 india (aws) $619.46 canada(aws) $55.45 lower-env(aws) $130.0 adani(oci) $228 alfanar(oci) $335.43 lower-env(oci) $15.83 prod(oci_compartment) $.07india(oci)
- Comment on [HIEV-7575](https://elocity.atlassian.net/browse/HIEV-7575): removed Preserved old Docker data as it is no longer needed
- Comment on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574): Completed GitLab self-managed registry secret setup for Adani prod and Alfanar prod. Adani prod: Context used: adani-prod-private API endpoint: https://10.104.13.198:6443 Created/updated gitlab-self-registry-secret in all namespaces where gitlab-registry-secret already exists. Registry endpoint configured: gitlab.evnet.xyz:5050 Existing gitlab-registry-secret was not modified. Adani validation: gitlab-self-registry-secret count: 17 gitlab-registry-secret count: 17 Sample docker-server verified a
- Comment on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574): created fresh runners from scratch in mac-mini

**2026-08-26** — logged 0.9d (7h) of 1.0d (8h) available, 3 comments

- Worklog 2h on [HIEV-7593](https://elocity.atlassian.net/browse/HIEV-7593) (Task, mid-sprint)
- Worklog 1h on [HIEV-7592](https://elocity.atlassian.net/browse/HIEV-7592) (Task, mid-sprint)
- Worklog 4h on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574) (Task, mid-sprint)
- Comment on [HIEV-7586](https://elocity.atlassian.net/browse/HIEV-7586): Generated private key and CSR for SSL pinning cert. CSR covers *.ad.hiev.network, *.hiev.network, and *.internal-ad.hiev.network. Also extracted current SPKI pin for ams.ad.hiev.network: sha256/qMsfeQhQDRlcYTO6UVAOl8+KGvb9B6a+OYad5btmVR0=. CSR still needs CA signing before importing into ACM
- Comment on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574): create new mac mini runner with tags Removed old Docker backup from runner instance. Disk usage improved from 83% to 52%. Docker and GitLab Runner services validated as active. All runners are configured with Docker executor. Cleanup automation is in place with 7-day retention and runs daily at 02:00 IST. Cleanup safely removes only inactive GitLab runner cache volumes and uses Docker-native prune for images/build cache.
- Comment on [HIEV-7370](https://elocity.atlassian.net/browse/HIEV-7370): Kafka-stg deployment is blocked by OCI infrastructure API timeout, not Kafka/Strimzi config. One PVC provisioned successfully, but remaining PVCs are pending because OCI CSI is timing out while calling iaas.ca-toronto-1.oraclecloud.com:443 . Same timeout is also seen on OCI Load Balancer sync, so impact is broader than Kafka PVC provisioning. Need OCI/OKE API connectivity issue checked from OCI side.

**2026-08-27** — logged 0.0d (0h) of 1.0d (8h) available, 4 comments

- Comment on [HIEV-7593](https://elocity.atlassian.net/browse/HIEV-7593): Configured runbook steps for connecting the Mac mini to the Headscale server via Tailscale. Includes auth key creation on headscale- control, Mac mini registration using the Headscale login server, SSH enablement, optional screen sharing setup, and validation commands.
- Comment on [HIEV-7593](https://elocity.atlassian.net/browse/HIEV-7593): implement anydesk mac mini access
- Comment on [HIEV-7592](https://elocity.atlassian.net/browse/HIEV-7592): S3 static website hosting is configured correctly for evlm-stg.evnet.xyz bucket. Public read policy and public access settings are in place, and the direct S3 website endpoint returns 200 OK: Custom domain evlm-stg.evnet.xyz is currently resolving via Cloudflare and returning 404, so DNS/Cloudflare routing needs to be updated separately.
- Comment on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574): Registered and validated two new backend GitLab runners (Instance-Backend-Runner-1 and Instance-Backend-Runner-2) on the OCI VPN runner instance. Increased runner concurrency from 2 to 4, cleaned unused Docker storage, and updated Docker cleanup retention from 7 days to 2 days, improving available disk space from ~21GB to ~56GB.

**2026-08-31** — logged 1.2d (10h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574) (Task, mid-sprint)
- Worklog 6h on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574) (Task, mid-sprint)
- Comment on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574): Investigated the Mac Mini GitLab Runner issue. The failure is caused by the outdated docker:stable client and docker:18.09.7-dind service conflicting with the mounted Docker socket. Recommended using a current Docker CLI image with the host socket and removing DinD. Cleanup may slow the first build but will not affect build correctness.
- Comment on [HIEV-7574](https://elocity.atlassian.net/browse/HIEV-7574): Cloned backend repositories under local backend workspace. Updated GitLab CI Docker build/publish jobs for Mac mini runner compatibility. Replaced old Docker image usage with docker:27-cli. Removed Docker-in-Docker from build/publish jobs where applicable. Added mac-mini-backend runner tag to route jobs correctly. Added linux/amd64 platform configuration for Docker builds. Created branch ci/mac-mini-docker-build across backend repos. Committed and pushed changes to GitLab. Created merge requests

### Rashmi — 9.2 of 15.0d (74h of 120h)

**2026-08-01** — logged 0.6d (5h) of 0.0d (0h) available, 1 comments

- Worklog 5.00h on [HIEV-6914](https://elocity.atlassian.net/browse/HIEV-6914) (Epic, mid-sprint)
- Comment on [HIEV-6914](https://elocity.atlassian.net/browse/HIEV-6914): Tested Maintenance feature on uat env (CA_ELO) and executing charging session scenario

**2026-08-06** — logged 0.8d (7h) of 1.0d (8h) available, 5 comments

- Worklog 15m on [HIEV-7420](https://elocity.atlassian.net/browse/HIEV-7420) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7416](https://elocity.atlassian.net/browse/HIEV-7416) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7413](https://elocity.atlassian.net/browse/HIEV-7413) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7296](https://elocity.atlassian.net/browse/HIEV-7296) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7095](https://elocity.atlassian.net/browse/HIEV-7095) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090) (Bug, mid-sprint)
- Worklog 5.00h on [HIEV-6914](https://elocity.atlassian.net/browse/HIEV-6914) (Epic, mid-sprint)
- Worklog 20m on [HIEV-6607](https://elocity.atlassian.net/browse/HIEV-6607) (Bug, mid-sprint)
- Comment on [HIEV-7296](https://elocity.atlassian.net/browse/HIEV-7296): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7095](https://elocity.atlassian.net/browse/HIEV-7095): Retested on uat env Alfanar , issue still exists - TimeZone field does not get autopupulated
- Comment on [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090): Retested on uat env CA_ELO, the issue has been fixed
- Comment on [HIEV-6914](https://elocity.atlassian.net/browse/HIEV-6914): Tested Maintenance feature on stg env CA_ELO on mobile and web app and completed the testing for the Maintenance feature under Station Management module.
- Comment on [HIEV-6607](https://elocity.atlassian.net/browse/HIEV-6607): Retested on uat env CA_ELO, the issue has been fixed, it is working as expected

**2026-08-07** — logged 0.7d (6h) of 1.0d (8h) available, 4 comments

- Worklog 15m on [HIEV-7234](https://elocity.atlassian.net/browse/HIEV-7234) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7163](https://elocity.atlassian.net/browse/HIEV-7163) (Bug, mid-sprint)
- Worklog 5h on [HIEV-6383](https://elocity.atlassian.net/browse/HIEV-6383) (Epic, mid-sprint)
- Comment on [HIEV-7234](https://elocity.atlassian.net/browse/HIEV-7234): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226): Retested on stg env CA_ELO, the issue has been fixed . Refund button disabled for charging cost 0.00.
- Comment on [HIEV-7163](https://elocity.atlassian.net/browse/HIEV-7163): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-6383](https://elocity.atlassian.net/browse/HIEV-6383): Tested activity log on stg env CA_ELO for Location , Station.

**2026-08-10** — logged 0.8d (7h) of 1.0d (8h) available, 4 comments

- Worklog 15m on [HIEV-7328](https://elocity.atlassian.net/browse/HIEV-7328) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7204](https://elocity.atlassian.net/browse/HIEV-7204) (Bug, mid-sprint)
- Worklog 6h on [HIEV-6383](https://elocity.atlassian.net/browse/HIEV-6383) (Epic, mid-sprint)
- Worklog 10m on [HIEV-6315](https://elocity.atlassian.net/browse/HIEV-6315) (Bug, mid-sprint)
- Comment on [HIEV-7328](https://elocity.atlassian.net/browse/HIEV-7328): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7204](https://elocity.atlassian.net/browse/HIEV-7204): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-6383](https://elocity.atlassian.net/browse/HIEV-6383): Tested Activity log on Customer, Business, EVSE Model, Tariff , Location Tariff Module on stg env
- Comment on [HIEV-6315](https://elocity.atlassian.net/browse/HIEV-6315): Retested on the STG environment for CA_ELO. The issue is verified as fixed. After logging in with the system-generated password and manually changing the password, the account is considered fully activated and verified, and the “Resend Activation Link” button is no longer displayed.

**2026-08-13** — logged 0.2d (2h) of 1.0d (8h) available, 5 comments

- Worklog 15m on [HIEV-7299](https://elocity.atlassian.net/browse/HIEV-7299) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7299](https://elocity.atlassian.net/browse/HIEV-7299) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226) (Bug, mid-sprint)
- Comment on [HIEV-7299](https://elocity.atlassian.net/browse/HIEV-7299): Retesting on stg env CA_ELO, the issue still exists.
- Comment on [HIEV-7299](https://elocity.atlassian.net/browse/HIEV-7299): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291): Issue 1 : Retested on stg env CA_ELO, the issue still exists. Description error message not user friendly . Issue 2 : Retested on stg env CA_ELO, the issue still exists.Units is missing . Issue 3 : Retested on stg env CA_ELO, the issue still exists.
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): Retested on stg env CA_ELO, the issue still exists.
- Comment on [HIEV-7094](https://elocity.atlassian.net/browse/HIEV-7094): Retested on stg env CA_ELO, the issue has been fixed. It is working as expected.

**2026-08-14** — logged 0.0d (0h) of 1.0d (8h) available, 1 comments

- Worklog 15m on [HIEV-7202](https://elocity.atlassian.net/browse/HIEV-7202) (Bug, mid-sprint)
- Comment on [HIEV-7202](https://elocity.atlassian.net/browse/HIEV-7202): Retested on stg env CA_ELO, the issue has been fixed.

**2026-08-16** — logged 0.8d (6h) of 0.0d (0h) available, 1 comments

- Worklog 6h on [HIEV-6393](https://elocity.atlassian.net/browse/HIEV-6393) (Epic, mid-sprint)
- Comment on [HIEV-6393](https://elocity.atlassian.net/browse/HIEV-6393): Tested on stg env CA_ELO, verify that export is present for job level and retry option present for job level and failed at task level and Verify that the user is able to upload new firmware after entering valid details, verify that user is able to able to schedule firmware update.

**2026-08-17** — logged 0.9d (7h) of 1.0d (8h) available, 6 comments

- Worklog 15m on [HIEV-7515](https://elocity.atlassian.net/browse/HIEV-7515) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7514](https://elocity.atlassian.net/browse/HIEV-7514) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7156](https://elocity.atlassian.net/browse/HIEV-7156) (Bug, mid-sprint)
- Worklog 5h 30m on [HIEV-6684](https://elocity.atlassian.net/browse/HIEV-6684) (Epic, mid-sprint)
- Comment on [HIEV-7515](https://elocity.atlassian.net/browse/HIEV-7515): As confirmed by , it is working as expected .So closing the ticket.
- Comment on [HIEV-7514](https://elocity.atlassian.net/browse/HIEV-7514): As confirmed by , it is working as expected . So closing the ticket.
- Comment on [HIEV-7513](https://elocity.atlassian.net/browse/HIEV-7513): As confirmed by , it is working as expected . So closing the ticket.
- Comment on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291): Issue 1 : Retested on stg env CA_ELO , the issue still exists. Issue 2 : Rested on stg env CA_ELO, the issue still exists Issue 3 : Retested on stg env CA_ELO, the issue still exists.
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): Retested on stg env CA_ELO, the issue still exists.
- Comment on [HIEV-6684](https://elocity.atlassian.net/browse/HIEV-6684): Tested on STG environment – CA_ELO. Performed regression testing for all modules having contact field .Tested Location Management and User Management, Corporate , Customer including checking that the Contact Number field accepts only valid mobile numbers.

**2026-08-18** — logged 1.0d (8h) of 1.0d (8h) available, 8 comments

- Worklog 15m on [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7535](https://elocity.atlassian.net/browse/HIEV-7535) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7531](https://elocity.atlassian.net/browse/HIEV-7531) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7297](https://elocity.atlassian.net/browse/HIEV-7297) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7216](https://elocity.atlassian.net/browse/HIEV-7216) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7143](https://elocity.atlassian.net/browse/HIEV-7143) (Bug, mid-sprint)
- Worklog 15m on [HIEV-6894](https://elocity.atlassian.net/browse/HIEV-6894) (Bug, mid-sprint)
- Worklog 6h on [HIEV-6384](https://elocity.atlassian.net/browse/HIEV-6384) (Epic, mid-sprint)
- Comment on [HIEV-7297](https://elocity.atlassian.net/browse/HIEV-7297): Retested on stg env CA_ELO, the issue has been fixed. Description for customer not found display a details error message including RFID tag.
- Comment on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291): Issue 1 : Retesting cannot be performed because the reservation cannot be created. Retesting will be carried out once the reservation-related issue is fixed. Issue 1 : Reservation related issue resolved, Rested on stg env CA_ELO, the issues has been fixed. Issue 2 : Retested on stg env CA_ELO, the issue has been fixed. Issue 3 : Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): Retested on stg env CA_ELO, the issue has been fixed -It is correctly showing all meter value in same unit.
- Comment on [HIEV-7216](https://elocity.atlassian.net/browse/HIEV-7216): Retested on stg env CA_ELO, the issue has been fixed.Diagnostic job successfully run
- Comment on [HIEV-7143](https://elocity.atlassian.net/browse/HIEV-7143): Retested on uat env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133): Issue 1 : Retested on stg env CA_ELO, the issue has been fixed. Issue 2 : Retested on stg env CA_ELO, the issue has been fixed. Issue 3 : Retested on stg env CA_ELO, the issue still exists.
- Comment on [HIEV-6894](https://elocity.atlassian.net/browse/HIEV-6894): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-6384](https://elocity.atlassian.net/browse/HIEV-6384): Performed regression testing for the Guest Charging functionality in the UAT environment (CA_ELO) to validate the existing functionality.During testing, the major Guest Charging flows were executed, including the charging initiation and validation scenarios. Blocker-level issues were identified, which are impacting the core Guest Charging functionality and preventing the complete regression cycle from being successfully completed.

**2026-08-19** — logged 0.8d (7h) of 1.0d (8h) available, 5 comments

- Worklog 10m on [HIEV-7552](https://elocity.atlassian.net/browse/HIEV-7552) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7550](https://elocity.atlassian.net/browse/HIEV-7550) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7544](https://elocity.atlassian.net/browse/HIEV-7544) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7301](https://elocity.atlassian.net/browse/HIEV-7301) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032) (Bug, mid-sprint)
- Worklog 5h on [HIEV-6384](https://elocity.atlassian.net/browse/HIEV-6384) (Epic, mid-sprint)
- Comment on [HIEV-7301](https://elocity.atlassian.net/browse/HIEV-7301): Retested on uat env CA_ELO, the issue has been fixed .It is working as expected.
- Comment on [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133): Issue 3 : As confirmed by , it is expected workflow, so closing the ticket.
- Comment on [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133): Issue 3 : As confirmed by , it is expected workflow, so closing the ticket.
- Comment on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-6384](https://elocity.atlassian.net/browse/HIEV-6384): Tested in the UAT environment (CA_ELO) by executing the charging session scenario with tarifff, without tariff, minimum wallet balance and also validating ui and validation message as a Guest charger.

**2026-08-20** — logged 0.4d (3h) of 1.0d (8h) available, 10 comments

- Worklog 15m on [HIEV-7564](https://elocity.atlassian.net/browse/HIEV-7564) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7559](https://elocity.atlassian.net/browse/HIEV-7559) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7559](https://elocity.atlassian.net/browse/HIEV-7559) (Bug, mid-sprint)
- Worklog 5m on [HIEV-7550](https://elocity.atlassian.net/browse/HIEV-7550) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7500](https://elocity.atlassian.net/browse/HIEV-7500) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7479](https://elocity.atlassian.net/browse/HIEV-7479) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477) (Suggestion, mid-sprint)
- Worklog 15m on [HIEV-7476](https://elocity.atlassian.net/browse/HIEV-7476) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7475](https://elocity.atlassian.net/browse/HIEV-7475) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7474](https://elocity.atlassian.net/browse/HIEV-7474) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7430](https://elocity.atlassian.net/browse/HIEV-7430) (Task, mid-sprint)
- Worklog 15m on [HIEV-6875](https://elocity.atlassian.net/browse/HIEV-6875) (Bug, mid-sprint)
- Comment on [HIEV-7559](https://elocity.atlassian.net/browse/HIEV-7559): Retested on stg env CA_ELO Android(20.3.0)(10), the issue has been fixed.
- Comment on [HIEV-7550](https://elocity.atlassian.net/browse/HIEV-7550): Retested on uat env CA_ELO, it is working as expected.
- Comment on [HIEV-7531](https://elocity.atlassian.net/browse/HIEV-7531): As confirmed , it is working as expected so closing the ticket.
- Comment on [HIEV-7479](https://elocity.atlassian.net/browse/HIEV-7479): Retested on stg env CA_ELO Android(20.3.0)(6), the issue has been fixed. It is working as expected.
- Comment on [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477): Retested on stg env CA_ELO, the issue has been fixed .Both “+ “ icon and “Reserve button “ are added .
- Comment on [HIEV-7476](https://elocity.atlassian.net/browse/HIEV-7476): Retested on stg env CA_ELO Android(20.3.0)(6), the issue has been fixed . It is showing Connector icon with connector information
- Comment on [HIEV-7475](https://elocity.atlassian.net/browse/HIEV-7475): Retested on stg env CA_ELO Android(20.3.0) (6) , the issue has been fixed .
- Comment on [HIEV-7474](https://elocity.atlassian.net/browse/HIEV-7474): Retested on Android (20.3.0) (6) in stg env CA_ELO, the issue has been fixed .
- Comment on [HIEV-7430](https://elocity.atlassian.net/browse/HIEV-7430): Executed the respective scenarios on STG env CA_ELO and verified that the event types are displayed as per the requirement: SessionMoneyRefundedEvent → Session refund — Unable to execute the scenario because the refund was not initiated. Hence, the event type could not be verified. CreditWalletMoneyRefundedEvent → Wallet refund — Verified successfully. WalletMoneyDebitedEvent → Session debit — Verified successfully. WalletMoneyCreditedEvent → Wallet credit — Verified successfully. All executable
- Comment on [HIEV-6875](https://elocity.atlassian.net/browse/HIEV-6875): Retested on uat env CA_ELO, it is working as expected.

**2026-08-21** — logged 0.1d (1h) of 1.0d (8h) available, 5 comments

- Worklog 15m on [HIEV-7502](https://elocity.atlassian.net/browse/HIEV-7502) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7499](https://elocity.atlassian.net/browse/HIEV-7499) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7077](https://elocity.atlassian.net/browse/HIEV-7077) (Bug, mid-sprint)
- Comment on [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539): Retested on stg env CA_ELO, the issue still exists.
- Comment on [HIEV-7502](https://elocity.atlassian.net/browse/HIEV-7502): Retested on stg env CA_ELO, the issue still exists.
- Comment on [HIEV-7502](https://elocity.atlassian.net/browse/HIEV-7502): As confirmed by , in lower env status remains in progress, it is working expected , so closing the ticket.
- Comment on [HIEV-7499](https://elocity.atlassian.net/browse/HIEV-7499): Retested on stg env CA_ELO, the issue still exists. When the Job Status is displayed as Success for a Job ID -55, the Successful Station Count is still showing 0 stations . Similarly, when the Job Status is in Pending state, the Pending Station count/column is not getting updated showing 0 stations.
- Comment on [HIEV-7077](https://elocity.atlassian.net/browse/HIEV-7077): Retested on uat env on Alfanar , it is working as expected . Correctly showing parking charges

**2026-08-23** — logged 0.2d (2h) of 0.0d (0h) available, 1 comments

- Worklog 1h 30m on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458) (Bug, mid-sprint)
- Comment on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458): Tested on stg env CA_ELO verify that Cold start HIEV Canada (or other non-GIF brand): AppLogo, no spinner, then first screen. New Login country box: no loader flash; flag/+code always visible. First country picker open: major countries only (not full world list); updates when metadata arrives. Logged-in new-login flow: BootSplash while profile loads (no spinner).

**2026-08-24** — logged 0.4d (3h) of 1.0d (8h) available, 1 comments

- Worklog 10m on [HIEV-7576](https://elocity.atlassian.net/browse/HIEV-7576) (Bug, mid-sprint)
- Worklog 3h on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458) (Bug, mid-sprint)
- Comment on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458): Tested on stg env Total energies, Alfanar, Hiev America, verify that Cold start HIEV Canada (or other non-GIF brand): AppLogo, no spinner, then first screen. New Login country box: no loader flash; flag/+code always visible. First country picker open: major countries only (not full world list); updates when metadata arrives. Logged-in new-login flow: BootSplash while profile loads (no spinner).

**2026-08-25** — logged 0.4d (3h) of 1.0d (8h) available, 4 comments

- Worklog 10m on [HIEV-7561](https://elocity.atlassian.net/browse/HIEV-7561) (Bug, mid-sprint)
- Worklog 3h on [HIEV-6636](https://elocity.atlassian.net/browse/HIEV-6636) (Task, mid-sprint)
- Comment on [HIEV-7561](https://elocity.atlassian.net/browse/HIEV-7561): Issue has been retested in stg env CA_ELO. It is working as expected and country code is displayed correctly.
- Comment on [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539): As confirmed by , in lower env working as expected , so closing the ticket.
- Comment on [HIEV-7499](https://elocity.atlassian.net/browse/HIEV-7499): As confirmed by , working as expected, so closing the ticket.
- Comment on [HIEV-6636](https://elocity.atlassian.net/browse/HIEV-6636): Tested on uat env CA_ELO, and Verified the legal links on the login screen no longer overlap with the keyboard and the screen remains usable. Verified the OTP screen back label/text behavior is displayed correctly. Verified the map quick action overlay hides appropriately when the keyboard is visible. Confirmed the map UI remains properly aligned and is not covered by the keyboard. Verified the redesigned location filter loading spinner does not get stuck indefinitely. Confirmed filter content l

**2026-08-26** — logged 0.5d (4h) of 1.0d (8h) available, 5 comments

- Worklog 15m on [HIEV-7449](https://elocity.atlassian.net/browse/HIEV-7449) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7302](https://elocity.atlassian.net/browse/HIEV-7302) (Bug, mid-sprint)
- Worklog 3h on [HIEV-6636](https://elocity.atlassian.net/browse/HIEV-6636) (Task, mid-sprint)
- Comment on [HIEV-7449](https://elocity.atlassian.net/browse/HIEV-7449): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7304](https://elocity.atlassian.net/browse/HIEV-7304): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7302](https://elocity.atlassian.net/browse/HIEV-7302): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-6636](https://elocity.atlassian.net/browse/HIEV-6636): Tested on uat env CA_ELO, Verified that Reservation list loads successfully without repeated API calls or infinite loading. “No Reservations” empty state is displayed correctly when there is no reservation data. “Upcoming” and “Past” empty-state text is centered and properly aligned. QR scanner opens correctly on first-time use. Camera permission is requested and works as expected. After granting permission, the camera preview loads immediately. QR scanning works without needing to go back and r

**2026-08-27** — logged 0.1d (0h) of 1.0d (8h) available, 3 comments

- Worklog 15m on [HIEV-7491](https://elocity.atlassian.net/browse/HIEV-7491) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7490](https://elocity.atlassian.net/browse/HIEV-7490) (Bug, mid-sprint)
- Comment on [HIEV-7491](https://elocity.atlassian.net/browse/HIEV-7491): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7490](https://elocity.atlassian.net/browse/HIEV-7490): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7487](https://elocity.atlassian.net/browse/HIEV-7487): Retested on stg env CA_ELO , the issue has not been fixed. Actual Result -Station is under maintenance and cannot be used until August 28, 2026 at 06:00 . Expected Result - Station is under maintenance and cannot be used until August 28, 2026 at 6:00 AM.Displaying the time in 12-hour format with AM/PM (e.g., 6:00 AM) to make the maintenance timing clearer and more user-friendly.

**2026-08-30** — logged 0.4d (4h) of 0.0d (0h) available, 1 comments

- Worklog 3h 30m on [HIEV-6441](https://elocity.atlassian.net/browse/HIEV-6441) (Task, mid-sprint)
- Comment on [HIEV-6441](https://elocity.atlassian.net/browse/HIEV-6441): Tested on uat env CA_ELO, verify that the scenario was executed successfully. The charging session was terminated abnormally, and the corresponding abnormal event was generated with the expected session termination details. No unexpected errors were observed.

**2026-08-31** — logged 0.0d (0h) of 1.0d (8h) available, 2 comments

- Comment on [HIEV-7495](https://elocity.atlassian.net/browse/HIEV-7495): Retested on stg env CA_ELO, the issue has been fixed.
- Comment on [HIEV-7095](https://elocity.atlassian.net/browse/HIEV-7095): As confirmed by , it is expected behaviour.

### Rushika — 8.8 of 20.0d (70h of 160h)

**2026-08-04** — logged 0.0d (0h) of 1.0d (8h) available, 1 comments

- Comment on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250): prepared the implementation document and got it approved by deepak. started working on the database schema comparison part.

**2026-08-05** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250) (Task, planned)
- Comment on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250): Implemented Database schema validation and elastic search validation part as well. Tested for dev, stg, UAT environments.

**2026-08-06** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250) (Task, planned)
- Comment on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250): schema validation script - development completed. sent the report format for review to deepak. elastic search validation didn’t work properly. need to fix elastic search validation part of the script. need to cross check the report data with manual verification.

**2026-08-10** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250) (Task, planned)
- Comment on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250): Submitted Validation report to deepak for review. report format changes required.

**2026-08-11** — logged 0.6d (5h) of 1.0d (8h) available, 1 comments

- Worklog 5h on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250) (Task, planned)
- Comment on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250): Report Format changes.

**2026-08-13** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250) (Task, planned)
- Worklog 2h on [HIEV-7191](https://elocity.atlassian.net/browse/HIEV-7191) (Task, planned)
- Comment on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250): Fixed issue with production validation part of the script. Changes the report format. Script generates the report with all the differences between the dev, stg, UAT, canada prod, adani prod and alafanar prod database schemas and elastic search index mapppings.
- Comment on [HIEV-7191](https://elocity.atlassian.net/browse/HIEV-7191): Working on the review comments. separated the features (customer engagemet score metrics and network enhancement filters API changes) mixed up in the same MR. Need to remove the changes in health controller. Need to remove the mock data response.

**2026-08-14** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 6h on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250) (Task, planned)
- Worklog 2h on [HIEV-7191](https://elocity.atlassian.net/browse/HIEV-7191) (Task, planned)
- Comment on [HIEV-7250](https://elocity.atlassian.net/browse/HIEV-7250): Manually cross verified the report data randomnly across all environments in both PG and ES. Areas covered : Related to PG : pg_tables, pg_columns, pg_datatypes, pg_default values, pg_indexes, pg_constraints. Related to ES : es_indices, es_mappings, es_datatypes, es_settings. Submitted report to Deepak for review.
- Comment on [HIEV-7191](https://elocity.atlassian.net/browse/HIEV-7191): Changed code according to the review comments. Need to submit for review to deepak.

**2026-08-17** — logged 0.4d (3h) of 1.0d (8h) available, 1 comments

- Worklog 3h on [HIEV-7146](https://elocity.atlassian.net/browse/HIEV-7146) (Task, planned)
- Comment on [HIEV-7146](https://elocity.atlassian.net/browse/HIEV-7146): Received Review comments related to the MR raised for the network api filter enhancements. Changes : removed the defined enum values for make and used manufacturer table instead. payment type enum is not defined. defined payment type in constants and used those values. Status - Done Review - To be done.

**2026-08-19** — logged 0.6d (5h) of 1.0d (8h) available, 2 comments

- Worklog 2h on [HIEV-7537](https://elocity.atlassian.net/browse/HIEV-7537) (Task, mid-sprint)
- Worklog 3h on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536) (Task, mid-sprint)
- Comment on [HIEV-7537](https://elocity.atlassian.net/browse/HIEV-7537): Understanding the codebase related to anakytics service. Analyzing the FRD for active charging report - InProgress.
- Comment on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536): Understanding the codebase related to anakytics service. Analyzing the FRD for Idle time report - InProgress.

**2026-08-20** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 3h on [HIEV-7537](https://elocity.atlassian.net/browse/HIEV-7537) (Task, mid-sprint)
- Worklog 3h on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536) (Task, mid-sprint)
- Comment on [HIEV-7537](https://elocity.atlassian.net/browse/HIEV-7537): Preparing Implementation Document
- Comment on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536): preparing Implementation Document.

**2026-08-21** — logged 0.9d (7h) of 1.0d (8h) available, 2 comments

- Worklog 3h on [HIEV-7537](https://elocity.atlassian.net/browse/HIEV-7537) (Task, mid-sprint)
- Worklog 4h on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536) (Task, mid-sprint)
- Comment on [HIEV-7537](https://elocity.atlassian.net/browse/HIEV-7537): Implementation document - Done. https://elocity.atlassian.net/wiki/x/CYAggw
- Comment on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536): Implementation Document - Done.

**2026-08-24** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536) (Task, mid-sprint)
- Comment on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536): Implementation started according to the requirements.

**2026-08-26** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536) (Task, mid-sprint)
- Comment on [HIEV-7536](https://elocity.atlassian.net/browse/HIEV-7536): Revising implementation documents.

### Sahil Kumar — 20.0 of 20.0d (160h of 160h)

**2026-08-03** — logged 1.1d (9h) of 1.0d (8h) available, 1 comments

- Worklog 5h on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329) (Sub-task, planned) — Completed the implementation
- Worklog 2h on [HIEV-6939](https://elocity.atlassian.net/browse/HIEV-6939) (Task, planned) — Creation of tracking report for EVLM
- Worklog 2.00h on [HIEV-6373](https://elocity.atlassian.net/browse/HIEV-6373) (Epic, mid-sprint)
- Comment on [HIEV-7216](https://elocity.atlassian.net/browse/HIEV-7216): The changes are merged and deployed in stg right now.

**2026-08-04** — logged 0.9d (7h) of 1.0d (8h) available, 3 comments

- Worklog 5h on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329) (Sub-task, planned)
- Worklog 2.00h on [HIEV-6373](https://elocity.atlassian.net/browse/HIEV-6373) (Epic, mid-sprint)
- Comment on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329): Started with the testing and completed few flows in local testing. Spent most of the time in initial integration setup and integration issues. Local testing is completed and I need to do end to end testing with the mobile app but I was unable to build the app due to build failure.
- Comment on [HIEV-7121](https://elocity.atlassian.net/browse/HIEV-7121): The changes are reviewed and deployed to stg for testing. attach the MR here itself from next time for easier access.
- Comment on [HIEV-6373](https://elocity.atlassian.net/browse/HIEV-6373): Fleet Management Implementation Doc Review Technical discussions, doubt clarifications and small maintenance works

**2026-08-05** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329) (Sub-task, planned)
- Comment on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329): Worked on following: 1. Smartcar webhook MR ( !1019 ) — Simplified feature/smartcar-webhook-vehicle-state-ingestion vs apr26-release , ran multi-agent review, fixed usedFallback correctness, added regression tests 2. Smartcar Connect config — Env-gated auto webhook subscribe/unsubscribe; fixed 401 subscribe auth (legacy vs API client); consolidated env into JSON configs; then moved config to tenant AWS Secrets Manager + Redis cache ( .env Smartcar values removed) Debugging / clarifications Simul

**2026-08-06** — logged 1.0d (8h) of 1.0d (8h) available, 4 comments

- Worklog 1h on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint)
- Worklog 4h on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint)
- Worklog 3h on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329) (Sub-task, planned)
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Gitlab CE self managed discussion Discussed GitLab SaaS → self-managed cutover risks for our repos. Socket issue MR review and discussion Reviewed and discussed the socket-related MR / issue (findings + next steps aligned with Shambu )
- Comment on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424): Multi-repo review of CPO utility tariff train — all REQUEST CHANGES : data-migration !271 — DDL appended to shipped upgrade_v17 (already-migrated envs never get tables); uniqueness/RLS gaps analytics !133 — money-path bugs ( search_after non-unique, fail-open tier seed, swallowed bucket errors) cpms !1013 — needs rebase; live crons vs commented tariff jobs; no tests; dead shouldAutoRenew ; missing TOU/tier validation Suggested merge order after fixes: data-migration → cpms → analytics. Also upda
- Comment on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329): Smartcar app build and integration setup Mobile app rebuild/setup for Smartcar Connect ( SMARTCAR_CLIENT_ID is build-time, not Firebase). Local Connect + webhook path exercised; clarified Connect vehicles ≠ dashboard simulator vehicles (must select the same sim vehicle during Connect). Config moved to tenant AWS Secrets Manager (JSON blobs) with env-gated webhookAutoSubscribe . Battery capacity “incapable” on connect is handled (75 kWh fallback) — does not block save. Smartcar remaining flows te
- Comment on [HIEV-6649](https://elocity.atlassian.net/browse/HIEV-6649): Added review comments on all 3 MRs. Please fix and send back.

**2026-08-07** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 1h on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint)
- Worklog 3h on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint)
- Worklog 2h on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint)
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Leads Sync Up Calls Discussions
- Comment on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424): EIPRE Code Walkthrough EVLM Architecture and Low Level Documentations add to the EVLM Tracker

**2026-08-10** — logged 0.7d (6h) of 1.0d (8h) available, 4 comments

- Worklog 2h 30m on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint)
- Worklog 1h on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint)
- Worklog 2h on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329) (Sub-task, planned)
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): MR review notes on CPMS !1025 : Reset location–tariff mapping after session creation (remove recreation-only mapping). Add a field on single + terminated session ES docs to mark manual recreation. Discuss: tariff ±15m cleanup → later zero cost; backup may miss refunded ES fields if taken before refund update. .keyword mapping differs by env — follow up with Vinay for long-term fix. Republish Accepted SetChargingProfile via cpms_external_setchargingprofile_1 + ocpp_external_chargingprofileset_1 (
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Implementation Doc Review Use https://gitlab.com/elocity1/backend/gateway-preauth/ repository for exposing the APIs and pre-auth-check API to decrypt the token rather than another envoy.
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Minor technical discussions with team
- Comment on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329): Update — Smartcar Connect session lifecycle & API contract ( !1019 , 9cb71183e ) Added mobile API contract doc ( docs/Smartcar-Connect-Mobile-API-Contract.md ) Extracted smartcarSessionLifecycle.service ; simplified Smartcar DTOs/controller/client Removed unused fleetJob.service + batch request DTO Hardened vehicle-state ingest/writer paths; added unit tests for Smartcar + session lifecycle

**2026-08-11** — logged 1.2d (10h) of 1.0d (8h) available, 5 comments

- Worklog 3h on [HIEV-7426](https://elocity.atlassian.net/browse/HIEV-7426) (Sub-task, planned) — EVLM ↔ CPMS telematics/EVSE API parity
- Worklog 3h on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Adhoc: activeQueue, addressLine2, gateway-preauth review, Fleet Management Review
- Worklog 2h on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329) (Sub-task, planned) — Smartcar webhook fleet alignment + vehicle status API
- Worklog 1h 30m on [HIEV-6939](https://elocity.atlassian.net/browse/HIEV-6939) (Task, planned) — EVLM handover docs + SEC subtasks
- Comment on [HIEV-7468](https://elocity.atlassian.net/browse/HIEV-7468): Its a frontend issue. assigned it to you.
- Comment on [HIEV-7426](https://elocity.atlassian.net/browse/HIEV-7426): Hardened EVLM CPMS client for telematics/EVSE parity ( getIsCharging soft-verify, AMS customer id parse fail-closed) Treated Smartcar Pending as accepted-into-pipeline; success only on terminal Accepted Wired EVSE listing via /evses/v2 DROPDOWN for integration paths Branch: feat/cpms-telematics-evse-api-parity (EVLM); CPMS side on feature/smartcar-webhook-vehicle-state-ingestion
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Investigated EVSE group activeQueue ghost sessions vs hasOngoingSessions gating; reviewed proposed gate + prune approach Fixed composed addresses to omit null/blank addressLine2 (CPMS 37410cc14 on master) Started review of gateway-preauth MR !2 against Encrypted Bearer JWT + Edge Decrypt guide (HIEV-6699): https://gitlab.com/elocity1/backend/gateway-preauth/-/merge_requests/2 Reviewed Fleet Management implementation doc with Manjunath.
- Comment on [HIEV-7329](https://elocity.atlassian.net/browse/HIEV-7329): Aligned fleet start/stop with webhook-owned vehicle state ( isOnline , freshness timestamps, needsReauth / offline preflight) Added GET /fleet/vehicle/:id/status (SOC, online/plugged/charging/connection) Fixed start/stop charge writes to stop relying on old cache/ lastUpdatedAt fields MR: https://gitlab.com/elocity1/backend/cpms/-/merge_requests/1019
- Comment on [HIEV-6939](https://elocity.atlassian.net/browse/HIEV-6939): Ran EVLM handover sync with Manjunath; captured decisions and ownership moves Updated evlm/docs + evlm-tracker (traceability, risks, MVP scope, UAT/security notes) Created Phase 1 code subtasks: HIEV-7470 (MFA step-up SEC-002), HIEV-7471 (Admin AMS proxy SEC-007)

**2026-08-12** — logged 1.1d (8h) of 1.0d (8h) available, 5 comments

- Worklog 3h 30m on [HIEV-7471](https://elocity.atlassian.net/browse/HIEV-7471) (Sub-task, planned) — AMS product RBAC + EVLM admin roles/users proxy
- Worklog 2h on [HIEV-7426](https://elocity.atlassian.net/browse/HIEV-7426) (Sub-task, planned) — CPMS live sandbox Mode A/B testing design
- Worklog 2h on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Edge-decrypt gateway-preauth / helm MR review
- Worklog 1h on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint) — EVLM Backend Confluence docs + bi-weekly refresh skill
- Comment on [HIEV-7471](https://elocity.atlassian.net/browse/HIEV-7471): Follow-on to product-aware RBAC: SU reserved for service_account in XX_XXX only.
- Comment on [HIEV-7471](https://elocity.atlassian.net/browse/HIEV-7471): Designed and implemented product-scoped RBAC across AMS / EVLM / data-migration: product on roles & permissions, unique (product, code, tenantId) , product filter on list APIs, login role selection via product header (default CPMS) Built EVLM admin AMS proxy for roles + users CRUD under Administration, with FE API handoff doc; multi-agent review of working-tree changes against the product RBAC plan Clarified SU reservation for service-account-only use in XX_XXX (related HIEV-7482): no human SU a
- Comment on [HIEV-7426](https://elocity.atlassian.net/browse/HIEV-7426): Set up worktree for feat/cpms-telematics-evse-api-parity and walked through enabling live CPMS for sandbox UI testing (vs faker) Defined Mode A (existing) vs Mode B (live) selection/mapping needs: live transformer, enrolled customer, optional dedicated CPID, real vehicles Identified remaining live inputs for telematics path (AMS customer id, enrollment type, transformer, vehicle status/SOC checks for stop/soft-verify)
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Multi-agent reviewed encrypted Bearer JWT edge-decrypt work against Encrypted Bearer JWT Edge Decrypt Implementation Guide (HIEV-6699) Posted review notes on gateway-preauth !2 and k8s-helm-charts !198 : KID_UNKNOWN alignment, kid UUID validation / pending-claim order, maintainability + crypto unit tests, Secret optional behavior
- Comment on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424): Stood up EVLM Backend Confluence structure aligned with Frontend docs under the EVLM space hub Added Documentation Maintenance / bi-weekly refresh page and evlm-confluence-refresh skill (tracker update → commit/push → Confluence page refresh)

**2026-08-13** — logged 1.0d (8h) of 1.0d (8h) available, 4 comments

- Worklog 3h 30m on [HIEV-7482](https://elocity.atlassian.net/browse/HIEV-7482) (Sub-task, planned) — Reserve SU for M2M service account
- Worklog 2h 30m on [HIEV-7471](https://elocity.atlassian.net/browse/HIEV-7471) (Sub-task, planned) — Product RBAC review leftovers and MRs
- Worklog 1h 30m on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Sudeep assist, Kafka ES mapping, technical discussions
- Worklog 30m on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint) — EVLM bi-weekly Confluence/tracker refresh
- Comment on [HIEV-7482](https://elocity.atlassian.net/browse/HIEV-7482): Implemented SU reservation for the AMS M2M service account only: XX_XXX tenant, catch-all product XXXX , union of all-product permissions on service_account@elocity.com AMS HTTP APIs fail closed on role SU ( 400 SU_RESERVED_FOR_SERVICE_ACCOUNT ); login/refresh fail-closed except that exact service-account identity; Azure login rejects if any mapped group is SU Edited v18 in place (remap human SU→AD, RIA strip, Azure INNER JOIN, XX_XXX user_role); CSV bulk keeps HTTP 201 with per-row remarks Mult
- Comment on [HIEV-7471](https://elocity.atlassian.net/browse/HIEV-7471): Closed remaining RBAC review items: attached TenantBusinessHeaderInterceptor on AMS roles APIs (same tenant remap as users), bound permission codes to request product, fail-closed downgrade_v18 for EVLM-only users Kept FE admin roles/users handoff consistent with SU as XXXX + all-product permissions (follow-on HIEV-7482) Opened stacked MRs (land data-migration before AMS): data-migration !274 , ams !387 , evlm !26
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Helped Sudeep on recreate charging session (transaction ID / OCPP–CPMS lookup) and one customer email Diagnosed ES mapping miss on charging-profile Kafka: CPMS_External_SetChargingProfile_1 is the full request; OCPP_External_ChargingProfileSet_1 is status-only reply ( producer / consumer / status ) — profile fields are not on the sink index Technical discussions / reviews / pairing help
- Comment on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424): Ran EVLM bi-weekly tracker + Confluence refresh: committed chore(tracker): bi-weekly refresh 2026-08-13 ( 115252f ) Tracker: portal incentives marked live; enrollment manual TX map noted; work items 35 done / 4 in-progress (backend) Updated EVLM Backend plus Requirements & Delivery Status, Known Limitations, Risks, Capabilities, Event Flows, Incentives, and Enrollment pages

**2026-08-14** — logged 1.0d (8h) of 1.0d (8h) available, 4 comments

- Worklog 1h on [HIEV-7482](https://elocity.atlassian.net/browse/HIEV-7482) (Sub-task, planned) — FE admin roles/users doc sync + 7482 worktree cleanup
- Worklog 4h on [HIEV-7426](https://elocity.atlassian.net/browse/HIEV-7426) (Sub-task, planned) — Sandbox Mode B live CPMS + LM isolation
- Worklog 3h on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Search framework discussion, Nagaraju LM testing, EIPRE SMTP, Leads sync, MR reviews
- Comment on [HIEV-7488](https://elocity.atlassian.net/browse/HIEV-7488): I have merged the changes. Pull it to relevant branch and deploy and then assign to Raju and let me know, i will put it to ready for testing.
- Comment on [HIEV-7482](https://elocity.atlassian.net/browse/HIEV-7482): Validated and updated evlm/docs/frontend/admin-roles-users-api.md against AMS/EVLM: role create/update uses generic 400s; SU_RESERVED_FOR_SERVICE_ACCOUNT is JSON user-assign only; CSV is AMS-only (201 + per-row remark); POST /users is 201; XXXX / SU login/refresh is fail-closed except the M2M service account Cleared leftover HIEV-7482 worktrees after yesterday’s merge onto the 7471 branches
- Comment on [HIEV-7426](https://elocity.atlassian.net/browse/HIEV-7426): Continued live CPMS sandbox Mode B on feat/cpms-telematics-evse-api-parity : seeded only customer 2786 (vehicle e34b029f-94ad-42ef-aa3c-a99187e982e2 , EVSE EVLM08860485 ) and hid Mode A placeholders from the Mode B participant list Diagnosed set-charging-profile with transactionId: null as sandbox placeholder TxProfile (real CPMS LM always passes the active OCPP transaction id); telematics /fleet/... calls were skipped because placeholder vehicle ids fall through to EVSE Fixed process crash on i
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Discussed the new search framework with Twisha and Deepak Supported Nagaraju on load-management testing (including load-summary GET vs CSV: export flattens sessions, so empty-session events drop out of the CSV) Helped with EIPRE SMTP setup Attended Leads sync-up Reviewed MRs

**2026-08-17** — logged 1.1d (8h) of 1.0d (8h) available, 7 comments

- Worklog 1h on [HIEV-7529](https://elocity.atlassian.net/browse/HIEV-7529) (Bug, mid-sprint) — Manual rebalance single-connector diagnose + fix
- Worklog 2h on [HIEV-7470](https://elocity.atlassian.net/browse/HIEV-7470) (Sub-task, planned) — MFA step-up verify + AMS_CLIENT wiring
- Worklog 1h on [HIEV-7426](https://elocity.atlassian.net/browse/HIEV-7426) (Sub-task, planned) — DR restore-by-pathway + sandbox Mode B CI
- Worklog 1h on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Session recreation discussion + MR reviews
- Worklog 1h 30m on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint) — Load management support + Smartcar simulator Connect
- Worklog 2h on [HIEV-6939](https://elocity.atlassian.net/browse/HIEV-6939) (Task, planned) — EVLM remediations 3–7, multi-tenancy plan, remaining items
- Comment on [HIEV-7529](https://elocity.atlassian.net/browse/HIEV-7529): Looked into this — the repro is largely a simulator vs real charger difference. Real Elocity chargers start at min current and only ramp up after receiving a SetChargingProfile, then operate at or below that profile. A single connector should not naturally enter a true overdraw/deviated state (realtime load > allotted load). The simulator can report meter values above the allotted profile independently, which is how Deviation shows up here. Meter-value deviation handling also does not re-apply a
- Comment on [HIEV-7529](https://elocity.atlassian.net/browse/HIEV-7529): Diagnosed why Manual Rebalance left a single-connector load group in deviation: distribution skipped the one-connector case, and meter-value deviation handling RemoteStops after 30s instead of re-applying a profile Noted simulator vs charger: real Elocity chargers start at min current and only ramp after SetChargingProfile , so a single connector should not naturally overdraw; the simulator can report meter values above the allotted profile. LDS still recalculates load for a single charger Appli
- Comment on [HIEV-7470](https://elocity.atlassian.net/browse/HIEV-7470): Implemented MFA step-up: POST /evlm/v1/auth/mfa/verify ( OpsAuthGuard only), 6-digit code, TTL 300s, rate limits; shared UAT pin with high default limits for staging Wired AMS_CLIENT into the notification handler via shared createAmsClientFromEnv Documented the verify contract and 401/429/503 outcomes; exposed MFA TTL and verify rate-limit knobs on staging helm Committed on evlm master : 9f48c81 feat MFA verify, a54605e docs; helm b511880d on k8s-helm-charts evlm-charts (not pushed)
- Comment on [HIEV-7426](https://elocity.atlassian.net/browse/HIEV-7426): Fixed DR restore to follow the chosen curtailment pathway at actual execution ( restoreCustomer in Temporal DR activities): EVSE set-charging-profile restores via clear-charging-profile (sandbox is trigger-only, same workflow) Fixed the sandbox Mode B unit job after the allowlist vehicle id change; pushed cd54ae2 on MR !25
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Discussed session recreation with Sudeep Reviewed MRs
- Comment on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424): Load management issue checks and support Helped with Smartcar simulated Connect: vehicle saved in CPMS but missing from the Smartcar dashboard; confirmed Simulator-issued Connect email/password (not a random login) and matching region/brand
- Comment on [HIEV-6939](https://elocity.atlassian.net/browse/HIEV-6939): Landed review remediations 3–7 on fix/review-remediations-3-7 : DR snapshot rehydrate + Kafka-required execute, search route order / dual-mount /v1/customer / JWT-only actor, admin permission allowlist, grid EvLoadComposePort inject, outbox leased_until claim, sandbox per-IP rate limit, production consent revoke + AT-007/008/012 Researched and planned EVLM multi-tenancy (HTTP isolation from AMS JWT tenant_id , tenant-scoped ops/customer APIs; infra shared) Discussed remaining EVLM items and next

**2026-08-18** — logged 1.0d (8h) of 1.0d (8h) available, 3 comments

- Worklog 6h 30m on [HIEV-7542](https://elocity.atlassian.net/browse/HIEV-7542) (Sub-task, planned) — Fail-closed tenant isolation, remediations merge, local migrate/dev, P1 FRDs
- Worklog 1h 30m on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — CPMS MR !1032 review comments and discussions
- Comment on [HIEV-7542](https://elocity.atlassian.net/browse/HIEV-7542): Implemented fail-closed HTTP tenant isolation: JWT tenant_id , tenant_id on primary tables (derived tables skipped), globally unique tx_id / ams_customer_id / CPMS ids, distinct error codes, existing rows backfilled as CA_ELO Reviewed the working-tree tenancy changes, applied high/medium/low fixes, and opened MR !27 ( feat/tenant-isolation → master ) Fast-forwarded remediations 3–7 onto local master (sandbox IP limiter, admin permission allowlist, outbox lease, DR Kafka-before-execute, abort sna
- Comment on [HIEV-7529](https://elocity.atlassian.net/browse/HIEV-7529): This change is deployed to stg.
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Reviewed MR !1032 (load-management lock / active-queue changes); verdict REQUEST CHANGES Posted four unresolved threads: fail-closed Redis lock (do not hold across 1-minute setChargingProfile ; high same-group event rate can queue/fail and also block StartTransaction); drop the new startup prune job and keep the existing reconcile job; ACTIVE-only session checks / remove excludeStatuses

**2026-08-19** — logged 1.0d (8h) of 1.0d (8h) available, 5 comments

- Worklog 3h 30m on [HIEV-7554](https://elocity.atlassian.net/browse/HIEV-7554) (Sub-task, planned) — P1 vehicles roster (EVLM-only)
- Worklog 1h 30m on [HIEV-7545](https://elocity.atlassian.net/browse/HIEV-7545) (Sub-task, planned) — Telematics API / vehicleGroupId design
- Worklog 1h 30m on [HIEV-7470](https://elocity.atlassian.net/browse/HIEV-7470) (Sub-task, planned) — Staging MFA API collection run
- Worklog 30m on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Pin Timescale image for EVLM smoke CI
- Worklog 1h on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint) — CPMS telematics rename MR review
- Comment on [HIEV-7554](https://elocity.atlassian.net/browse/HIEV-7554): Scoped P1 Vehicles as EVLM-only: Total vehicles KPI from the EVLM vehicle table, All-only chips, persist CPMS/Smartcar name on enroll (no live CPMS on list load). Shipped ops roster locally on evlm master (not pushed): GET /evlm/v1/ops/vehicles/metrics , list ( q / make / connector), and :vehicleId detail rail; migration 0011_vehicle_name . Commits: feat(enrollment) 36f40b1 , test(enrollment) c4d7537 , docs(enrollment) 8aac75e . Domain unit suite 631 passing. Filed later work under this parent: 
- Comment on [HIEV-7545](https://elocity.atlassian.net/browse/HIEV-7545): Started the later slice against the renamed CPMS telematics surface (former fleet APIs) for EVLM roster KPIs / live status. Confirmed GET-shaped reads; N vehicleId s in the query string will blow URL limits, so do not pass the full enrolled set. Proposed membership handle instead: EVLM upserts an “enrolled” vehicle group on enroll/unenroll, then GET /telematics/overview?vehicleGroupId=… and list + existing searchKey — postpone a new batch-id filter if that stays hard.
- Comment on [HIEV-7470](https://elocity.atlassian.net/browse/HIEV-7470): Mapped MFA as step-up on privileged ops actions (DR execute/abort, transformer onboard, incentive approve/reject), not login; staging tested with MFA_STAGING_BYPASS=false . Built a Postman Collection Runner: AMS login stores JWT; create+simulate DR in-run; assert MFA_REQUIRED / wrong code / valid verify; stop before execute; cleanup created data. Incentive cases used env entry IDs only. Ran the collection successfully against staging; local collection files were deleted after the run.
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Staging smoke on EVLM job 15975020196 failed: runner disk filled pulling timescale/timescaledb:latest-pg16 (tag had moved; parallel suites retried the pull). Fixed on master as bd44dc1 : pin timescale/timescaledb:2.28.1-pg16 , --test-concurrency=1 , stop retrying container start on no space left on device , prune/pull once in CI.
- Comment on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424): Reviewed MR !1026 (fleet → telematics rename). Renamed leftover fleet.service.spec.ts to telematics.service.spec.ts and pointed it at TelematicsService ; npm run test:unit -- test/services/telematics.service.spec.ts — 11 passed.

**2026-08-20** — logged 1.5d (12h) of 1.0d (8h) available, 7 comments

- Worklog 2h 30m on [HIEV-7563](https://elocity.atlassian.net/browse/HIEV-7563) (Bug, mid-sprint) — Decommission + LM cleanup implement + MR review fixes
- Worklog 3h 30m on [HIEV-7545](https://elocity.atlassian.net/browse/HIEV-7545) (Sub-task, planned) — Telematics enrolled roster implement + review fixes + paired MRs
- Worklog 4h on [HIEV-7542](https://elocity.atlassian.net/browse/HIEV-7542) (Sub-task, planned)
- Worklog 15m on [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539) (Bug, mid-sprint) — Code review + merge + staging deploy
- Worklog 30m on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — EVLM Confluence refresh + tracker MoM/risks
- Worklog 1h 30m on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint) — MR !1032 review + HIEV-7560 scope/recommendation
- Comment on [HIEV-7563](https://elocity.atlassian.net/browse/HIEV-7563): Root-caused decommission leaving OCPP charge box active and station still in Load Group Overview. Hardened existing deactivate pipeline: await OCPP UpsertEVSE, in-process deleteEvseGroupEvse , await UPSERT_LOAD_GROUP redistribution. Defense: Overview excludes DECOMMISSIONED ; allocation/offline paths COMMISSIONED-only. Forward-fix only. MR !1034 ; addressed follow-up review comments on the MR.
- Comment on [HIEV-7545](https://elocity.atlassian.net/browse/HIEV-7545): Implemented enrolled-scope telematics on CPMS ( enrolledOnly / excludeVehicles ) using Redis SET evlm:enrolled:vehicles:{tenantId} , with tenantId header resolution and scalar vehicleIds support. EVLM: fleet→ /telematics/* client rename, enrolled Redis ensure/rebuild + sandbox sync, ops vehicles metrics/list/detail compose from live CPMS fields (SoH still omitted). Addressed multi-agent review findings (tenant header drop of enrolledOnly , empty sentinel, OpenAPI/docs, caller retargets). Paired 
- Comment on [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539): Reviewed, merged and deployed to staging
- Comment on [HIEV-7502](https://elocity.atlassian.net/browse/HIEV-7502): Reviewed, merged and deployed to staging
- Comment on [HIEV-7499](https://elocity.atlassian.net/browse/HIEV-7499): Reviewed, merged and deployed to staging
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Ran EVLM Confluence bi-weekly refresh (hub + Known Limitations, Config, Security/Enrollment/DR business pages, architecture flows/gaps). Synced evlm-tracker work items / milestones / MoM from bi-weekly sync VTT; trimmed risks to Phase 1 and clarified L×I label. Confirmed SEC-002 stays in-progress (MFA verify shipped; staging bypass still on).
- Comment on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424): Multi-agent reviewed CPMS MR !1032 (load-distribution lock / ES / ongoing-session changes). Compared MR scope to HIEV-7560: config ChangeConfiguration failure path ≠ distribution race; recommended minimal Redis lock around read→LDS→awaited ES write only, keep hasOngoingSessions on source of truth. Posted review concern + recommended approach on HIEV-7560 and mirrored on the MR. Also clarified LM variance / unstable-session behavior and long-session / stop-timestamp edge cases for support context

**2026-08-21** — logged 1.1d (8h) of 1.0d (8h) available, 5 comments

- Worklog 3h 30m on [HIEV-7545](https://elocity.atlassian.net/browse/HIEV-7545) (Sub-task, planned) — Telematics enrolled roster + ops vehicles API handoff
- Worklog 1h on [HIEV-7542](https://elocity.atlassian.net/browse/HIEV-7542) (Sub-task, planned) — Tenant-only segregation close-out
- Worklog 2h on [HIEV-7470](https://elocity.atlassian.net/browse/HIEV-7470) (Sub-task, planned) — MFA staging bypass default + privileged mutate guards
- Worklog 1h 30m on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Notify durability, re-review, risks triage, onboard fixes
- Worklog 30m on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint) — CPMS MR !1036 metadata cache review
- Comment on [HIEV-7545](https://elocity.atlassian.net/browse/HIEV-7545): Shipped enrolled-roster telematics compose: CPMS Redis SET scope ( enrolledOnly / excludeVehicles + tenantId header) paired with EVLM /telematics/* client retarget and ops vehicles metrics/list/detail composition Fixed Nest build by exporting VehicleOpsStatus from @evlm/contracts ; EVLM MR merged to master Clarified frontend handoff: master-detail UX cut, SoH detail-only (em dash), status filter deferred; committed local doc update on ops-vehicles-roster-api.md MR !1035 (CPMS, open → aug26-relea
- Comment on [HIEV-7542](https://elocity.atlassian.net/browse/HIEV-7542): Confirmed product decision: tenant-only isolation (all businesses under a tenant visible in EVLM); no business-level data filter Documented as by-design / closed residual review gap; updated tracker close-out for MFA default + tenant-only segregation
- Comment on [HIEV-7470](https://elocity.atlassian.net/browse/HIEV-7470): Defaulted MFA_STAGING_BYPASS to false and applied MfaGuard on admin role/user mutates, onboarding finalize, and incentive program publish Updated security/integration/UAT docs and config tests for the new default and guards Local commit on evlm master (not pushed): feat(security,notify): harden MFA defaults and durable multi-channel delivery
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Added notification per-channel delivery status (migration 0013 ) and outbox semantics so processed only when all intended channels succeed Refreshed EVLM full-review canvas against master — prior criticals closed; remaining open items triaged Triaged evlm-tracker open risks for immediate vs blocked actions (e.g. SEC-007 FE/staging flags) Small EVLM fixes: optional name on customer onboard step 3; transformers return all on no match; moved API docs under docs/frontend/
- Comment on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424): Reviewed MR !1036 (EVSE model/manufacturer selective metadata cache refresh) for correctness Walked through refreshMetadataTypes key encoding ( METADATA_ + JSON.stringify params) and how JSON.parse rebuilds cache Get args

**2026-08-24** — logged 1.2d (10h) of 1.0d (8h) available, 4 comments

- Worklog 1h on [HIEV-7581](https://elocity.atlassian.net/browse/HIEV-7581) (Sub-task, planned) — Phase 1 Ops Web E2E plan + canvas
- Worklog 3h on [HIEV-7545](https://elocity.atlassian.net/browse/HIEV-7545) (Sub-task, planned)
- Worklog 2h on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — CI speed, Confluence refresh, GitLab remotes
- Worklog 1h on [HIEV-7220](https://elocity.atlassian.net/browse/HIEV-7220) (Sub-task, planned) — Sandbox Mode B live CPMS + DR participant prune
- Worklog 3h on [HIEV-7205](https://elocity.atlassian.net/browse/HIEV-7205) (Sub-task, planned) — Unit coverage 75% + Nest decorator TS fix
- Comment on [HIEV-7581](https://elocity.atlassian.net/browse/HIEV-7581): Scoped as the long-lived ticket for the full Phase 1 Ops Web manual testing lifecycle (not a one-day adhoc) Today: drafted the Phase 1 Ops Web manual E2E plan and an exhaustive local canvas (flows, cases, session log) for staging run-throughs Next: execute the plan against the deployed webapp and log findings on this ticket through close-out Related: HIEV-7205
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Planned and applied EVLM CI speed changes (uncommitted): parallel test jobs via needs: [] , publish only on master after build+test, drop DinD for host socket + BuildKit cache-from, no Nest build in test jobs, Bun 1.3.11 + Docker cache mounts Ran bi-weekly tracker + Confluence refresh (tracker 554e4a2 ): Requirements & Delivery Status , Known Limitations , Capabilities , EVLM Backend Migrated local git remotes from gitlab.com/elocity1 to self-managed gitlab.evnet.xyz , cleared leftover SaaS keyc
- Comment on [HIEV-7220](https://elocity.atlassian.net/browse/HIEV-7220): Continued sandbox live-CPMS work on worktree feat/cpms-telematics-evse-api-parity : kept Mode A fixture path unchanged and added Mode B mapping (live transformer, enrolled customer, dedicated chargePointId) Seeded Mode B with live customer 2786 / vehicle e34b029f-… / EVSE EVLM08860485 and removed other Mode B seed customers Fixed DR create so Mode B enrolls only allowlisted customers (UI was filtering participants but load-management still targeted everyone on the transformer) Traced CPMS dispat
- Comment on [HIEV-7205](https://elocity.atlassian.net/browse/HIEV-7205): Raised EVLM domain unit coverage toward a 75% line floor: injectable deps seams + behavioral tests for grid (transformers/groups), incentives (lifecycle, resolver, publish, payout), and sandbox (cleanup, DR executor, status/scenario) Created 16 local commits on evlm master (not pushed) across those waves, plus c8 --lines=75 and TEST_STRATEGY/CI soft-gate notes ( coverage still allow_failure ) Unblocked Nest/watch tsc after coverage seams: moved @Optional() / @Inject() off constructor overloads (

**2026-08-25** — logged 0.7d (6h) of 1.0d (8h) available, 3 comments

- Worklog 2h on [HIEV-7581](https://elocity.atlassian.net/browse/HIEV-7581) (Sub-task, planned) — MoM + Test Plan page in evlm-tracker
- Worklog 3h 30m on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — CI/Bun/remotes, offline-connector LM, gateway-preauth deploy help
- Comment on [HIEV-7584](https://elocity.atlassian.net/browse/HIEV-7584): @ Sahil Siddiqui Backend change is in — GET .../evse-groups/:id/overview now returns connectorType on each connectorCards item (same value as charger details: connector.evseModelConnector.connectorType.ui_name ). Please use connectorType from the overview response to show the connector icon on the Load Group Overview cards. Commit: feat(load-management): add connectorType to EVSE group overview #HIEV-7584 on apr26-release .
- Comment on [HIEV-7581](https://elocity.atlassian.net/browse/HIEV-7581): Wrote MoM from the Deepak call and extracted focused testing items for Phase 1 Ops Web E2E Added a new Test Plan page in evlm-tracker (priorities, assignees: Sahil Kumar / Sahil Siddiqui / Deepak / Dinesh / Dhanush) UI edits persist via localStorage with a sync-to-local-JSON action ( data/testPlan.json ) Commit: added test plan in the tracker
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Fixed EVLM CI failures after pipeline speed-up: restored bun run build before lint/test (packages export from dist/ ), switched test image back to node:22-bookworm (Bun’s node shim breaks tsx ), and hardened integration teardown + timeouts Diagnosed Mac mini shell-runner Bun install races ( flock / concurrent ~/.bun ); wrote ci-runner-bun-setup.md for DevOps and clarified arm (Mac mini) vs amd (OCI) handling Migrated local repo remotes from gitlab.com/elocity1 → self-managed gitlab.evnet.xyz ; c

**2026-08-26** — logged 1.1d (8h) of 1.0d (8h) available, 2 comments

- Worklog 3h on [HIEV-7581](https://elocity.atlassian.net/browse/HIEV-7581) (Sub-task, planned) — CA_THY cold-start E2E plan + MOB API scope
- Worklog 5h 30m on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Prettier standardize 10 MRs + portal S3 docs
- Comment on [HIEV-7581](https://elocity.atlassian.net/browse/HIEV-7581): Rewrote Phase 1 Ops Web E2E plan + canvas for tenant CA_THY / sahil+ca_thy@elocitytech.com as a dual cold-start (empty EVLM + AMS/CPMS bootstrap), dropping TX-1071 / prior-seed assumptions Ordered runbook: Login → Dashboard → Create TX (UI) → historical readings (API) → AMS/CPMS BOOT (API) → onboard → vehicles → DR → incentives → reports; empty lists treated as Pass Pointed live Ops Web at EVLM stg S3 site ; added MOB-1…MOB-9 customer JWT API consistency checks vs Ops data (mobile app UI still N
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Standardized Prettier (spaces) across elocity1/backend repos: updated .prettierrc , ran format + eslint autofix, smoke-ran builds, then opened MRs to aug26-release Created missing aug26-release branches (from apr26-release / master) and retargeted MRs; assigned @sahil / reviewer @deepak MRs: ams !388 , cpms !1039 , payment !199 , analytics !136 , session-utility !134 , ocpp !113 , email !36 , pns !24 , sms !26 , evlm !29 Updated EVLM portal docs + Confluence for GitLab Pages → S3 hosts (stg/demo

**2026-08-27** — logged 1.1d (8h) of 1.0d (8h) available, 2 comments

- Worklog 2h 30m on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Vinay release help, calls, AMS captcha guidance
- Worklog 6h on [HIEV-6939](https://elocity.atlassian.net/browse/HIEV-6939) (Task, planned) — EVLM baseline/RFP analysis + DR restore stagger dwell
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Helped Vinay with release-related process explanation (~1h) Calls and discussions (~1h) Walked through AMS POST /auth/user/login reCAPTCHA behavior for API automation (when ENABLE_CAPTCHA_WEB + secret apply; service-account / env-off escapes; prod must keep captcha on for normal users)
- Comment on [HIEV-6939](https://elocity.atlassian.net/browse/HIEV-6939): Implemented Phase 1 DR restore stagger dwell for Cold-Load Pick-Up mitigation: DR_RESTORE_STAGGER_MS (default 15s) between customer restores in runStaggeredRestore ; mid-event opt-out stays immediate; focused tests 22/22 Documented stagger behavior on Confluence: DR Restore Stagger Dwell (CLPU mitigation) ; synced related DR / config / event-flow pages Pushed to evlm master : 31daa77 — feat(dr): add configurable restore stagger dwell for CLPU Reviewed RFP load-disaggregation claims vs current Ph

**2026-08-31** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 2h on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425) (Task, mid-sprint) — Team meetings and discussions
- Worklog 4h on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424) (Task, mid-sprint) — UAT release
- Comment on [HIEV-7425](https://elocity.atlassian.net/browse/HIEV-7425): Team meetings and discussions
- Comment on [HIEV-7424](https://elocity.atlassian.net/browse/HIEV-7424): Helped Vinay with UAT release.

### Sahil Siddiqui — 15.1 of 16.0d (121h of 128h)

**2026-08-03** — logged 0.0d (0h) of 0.0d (0h) available, 4 comments

- Comment on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377): Dhanush K G mentioned this issue in commit dfabfb40 of Elocity / Frontend / mobile / CPMS-MobileApp on branch fix/HIEV-7377-reservation-slots-settings-order : fix( ): gate reservation slots on settings and stop filter refetch loop Wait for reservation settings minPeriodMinute before calling slots with customSlotDuration, refetch on return from Join Queue, and keep connector filter sequence stable when slots clear so the timeline no longer loops or shows false red gaps. Co-authored-by: Cursor <cu
- Comment on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377): Dhanush K G mentioned this issue in merge request !487 of Elocity / Frontend / mobile / CPMS-MobileApp on branch fix/HIEV-7377-reservation-slots-settings-order : fix( ): gate reservation slots on settings and stop filter refetch loop
- Comment on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377): Dhanush K G mentioned this issue in commit 831a7924 of Elocity / Frontend / mobile / CPMS-MobileApp : fix( ): gate reservation slots on settings and stop filter refetch loop
- Comment on [HIEV-7377](https://elocity.atlassian.net/browse/HIEV-7377): Dhanush K G mentioned this issue in commit bd8d14b9 of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : Merge branch 'fix/HIEV-7377-reservation-slots-settings-order' into 'react-doctor-score-improvements' fix( ): gate reservation slots on settings and stop filter refetch loop See merge request elocity1/frontend/mobile/CPMS-MobileApp!487

**2026-08-04** — logged 1.0d (8h) of 1.0d (8h) available, 34 comments

- Worklog 6m on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342) (Bug, mid-sprint) — MR !779 code review (GHG batch) — HIEV-7342 missing bars / console.log blocker. Combined 30m across HIEV-7333/7335/7336/7337/7342.
- Worklog 6m on [HIEV-7337](https://elocity.atlassian.net/browse/HIEV-7337) (Bug, mid-sprint) — MR !779 code review (GHG batch) — HIEV-7337 zoom-out top grid. Combined 30m across HIEV-7333/7335/7336/7337/7342.
- Worklog 6m on [HIEV-7336](https://elocity.atlassian.net/browse/HIEV-7336) (Bug, mid-sprint) — MR !779 code review (GHG batch) — HIEV-7336 dual-axis sync. Combined 30m across HIEV-7333/7335/7336/7337/7342.
- Worklog 6m on [HIEV-7335](https://elocity.atlassian.net/browse/HIEV-7335) (Bug, mid-sprint) — MR !779 code review (GHG batch) — HIEV-7335 zoom intervals. Combined 30m across HIEV-7333/7335/7336/7337/7342.
- Worklog 6m on [HIEV-7333](https://elocity.atlassian.net/browse/HIEV-7333) (Bug, mid-sprint) — MR !779 code review (GHG batch) — HIEV-7333 title rename. Combined 30m across HIEV-7333/7335/7336/7337/7342.
- Worklog 30m on [HIEV-7320](https://elocity.atlassian.net/browse/HIEV-7320) (Bug, mid-sprint) — MR !778 code review (My Profile batch) — HIEV-7320 Cancel / Submit color / logout copy / User Name label. Combined 2h split across HIEV-7313, 7315, 7317, 7320.
- Worklog 30m on [HIEV-7317](https://elocity.atlassian.net/browse/HIEV-7317) (Bug, mid-sprint) — MR !778 code review (My Profile batch) — HIEV-7317 email field disabled. Combined 2h split across HIEV-7313, 7315, 7317, 7320.
- Worklog 30m on [HIEV-7315](https://elocity.atlassian.net/browse/HIEV-7315) (Bug, mid-sprint) — MR !778 code review (My Profile batch) — HIEV-7315 refresh preserves filters. Combined 2h split across HIEV-7313, 7315, 7317, 7320.
- Worklog 30m on [HIEV-7313](https://elocity.atlassian.net/browse/HIEV-7313) (Bug, mid-sprint) — MR !778 code review (My Profile batch) — HIEV-7313 export success popup / progress / label. Combined 2h split across HIEV-7313, 7315, 7317, 7320.
- Worklog 30m on [HIEV-7296](https://elocity.atlassian.net/browse/HIEV-7296) (Bug, mid-sprint) — Code review MR !780
- Worklog 30m on [HIEV-7234](https://elocity.atlassian.net/browse/HIEV-7234) (Bug, mid-sprint) — Code review MR !780
- Worklog 20m on [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226) (Bug, mid-sprint) — Code review MR !781
- Worklog 20m on [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166) (Bug, mid-sprint) — Code review MR !781
- Worklog 1h on [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090) (Bug, mid-sprint) — HIEV-7090: aligned Alerts/Notifications date picker with other grids (removed applyOnSelection=false), verified root cause vs prior fix, pushed to v4-MainBranch + Alfanar-UAT. SME/QA: Rashmi Waghmare for retest.
- Worklog 20m on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062) (Bug, mid-sprint) — Code review MR !781
- Worklog 2.00h on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) (Task, mid-sprint)
- Worklog 0.25h on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) (Task, mid-sprint)
- Comment on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342): Sahil Siddiqui mentioned this issue in merge request !779 of Elocity / Frontend / web / Cpms Portal on branch v4-GHGFixes : Fixed Inconsistent spacing between the axis lines
- Comment on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342): Code review update — MR !779 This ticket (GHG bars not rendered) Item Status Greenhouse Gas bars missing; only Cumulative line shown ✅ Root cause fixed in code Root cause Chart was calling barLineGraphData(..., "energy") , but /reporting/GHG-reduction does not provide an energy field — so bar series was empty. Fix in MR Maps a GHG numeric field (defaults to ghgReduction , with detection fallback). Blocking / follow-ups before merge Remove console.log("[GHG Reduction Debug]...") — logs report pay
- Comment on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342): — please address the review comments on and push an update. Required before merge: Remove the production console.log("[GHG Reduction Debug]...") in GHCUsed/index.tsx (merge blocker — logs report payload). Harden GHG bar data-field selection — do not use “first numeric key”; prefer an explicit field (e.g. ghgReduction ) / allowlist. Add i18n keys Greenhouse Gas Reduction + description to remaining locales: kn , ko , pt , th . Keeping the other GHG tickets (HIEV-7333 / 7335 / 7336 / 7337) with me 
- Comment on [HIEV-7337](https://elocity.atlassian.net/browse/HIEV-7337): Sahil Siddiqui mentioned this issue in merge request !779 of Elocity / Frontend / web / Cpms Portal on branch v4-GHGFixes : Fixed Inconsistent spacing between the axis lines
- Comment on [HIEV-7337](https://elocity.atlassian.net/browse/HIEV-7337): Code review update — MR !779 This ticket (top grid line missing right-axis value after zoom out) Item Status Top horizontal grid line should have right Y-axis label after Zoom Out ✅ Code approach looks correct Same dual-axis sync changes as HIEV-7335/7336. Retest on STG Fullscreen → Zoom Out (−) once Confirm top grid line has matching left + right axis values MR verdict: REQUEST CHANGES (merge blocked by console.log ; this fix needs STG verification). Logged 6m (part of combined 30m across HIEV-
- Comment on [HIEV-7336](https://elocity.atlassian.net/browse/HIEV-7336): Sahil Siddiqui mentioned this issue in merge request !779 of Elocity / Frontend / web / Cpms Portal on branch v4-GHGFixes : Fixed Inconsistent spacing between the axis lines
- Comment on [HIEV-7336](https://elocity.atlassian.net/browse/HIEV-7336): Code review update — MR !779 This ticket (left/right Y-axis tick mismatch after zoom) Item Status Sync left (Cumulative) and right (GHG) tick counts after Zoom In ×2 ✅ Code approach looks correct Old zoom handlers only locked y1 (left), which explains desync with y2 (right). Both axes now share ticks.count: 10 + beginAtZero . Retest on STG Fullscreen → Zoom In (+) twice Confirm every horizontal grid line has corresponding left + right axis values MR verdict: REQUEST CHANGES (merge blocked by con
- Comment on [HIEV-7335](https://elocity.atlassian.net/browse/HIEV-7335): Sahil Siddiqui mentioned this issue in merge request !779 of Elocity / Frontend / web / Cpms Portal on branch v4-GHGFixes : Fixed Inconsistent spacing between the axis lines
- Comment on [HIEV-7335](https://elocity.atlassian.net/browse/HIEV-7335): Code review update — MR !779 This ticket (uneven Y-axis intervals after first zoom) Item Status Fix inconsistent intervals after first fullscreen Zoom In ✅ Code approach looks correct What changed Removed y1-only onZoom* / onPan* locks that forced left axis min/max independently. Both axes now use beginAtZero , suggestedMax , and ticks.count: 10 . Retest on STG (required) Reporting → Greenhouse Gas Reduction → Fullscreen Zoom In (+) once (first time after opening report) Confirm even Y-axis inte
- Comment on [HIEV-7333](https://elocity.atlassian.net/browse/HIEV-7333): Sahil Siddiqui mentioned this issue in merge request !779 of Elocity / Frontend / web / Cpms Portal on branch v4-GHGFixes : Fixed Inconsistent spacing between the axis lines
- Comment on [HIEV-7333](https://elocity.atlassian.net/browse/HIEV-7333): Code review update — MR !779 Reviewed v4-GHGFixes → v4-TempMay26Release . This ticket Item Status Rename “GHG Used” → reduction-focused title ✅ Implemented as Greenhouse Gas Reduction (nav, legend, constants) Follow-up New i18n keys added only in en / en-US / ar / fr — still missing kn / ko / pt / th . MR verdict: REQUEST CHANGES (blocking item is debug console.log on HIEV-7342 path; not specific to title rename). Logged 6m (part of combined 30m across HIEV-7333 / 7335 / 7336 / 7337 / 7342).
- Comment on [HIEV-7320](https://elocity.atlassian.net/browse/HIEV-7320): Sahil Siddiqui mentioned this issue in merge request !778 of Elocity / Frontend / web / Cpms Portal on branch v4-ProfilePageFixes : added progress bar for the download
- Comment on [HIEV-7320](https://elocity.atlassian.net/browse/HIEV-7320): Code review update — MR !778 Reviewed My Profile polish items on v4-ProfilePageFixes → v4-TempMay26Release . Coverage for this ticket Item Status Issue 1 — Submit button color aligned (Secondary / blue) ✅ Issue 2 — Cancel button added ⚠️ Partial — Cancel only resets fields , does not close the drawer (X still closes). Prefer Cancel → discard + close Issue 3 — Logout confirmation wording (“log out”) ✅ (key renamed in en / en-US / ar / fr; kn / ko / pt / th still missing ) Issue 4 — Filter label “
- Comment on [HIEV-7317](https://elocity.atlassian.net/browse/HIEV-7317): Sahil Siddiqui mentioned this issue in merge request !778 of Elocity / Frontend / web / Cpms Portal on branch v4-ProfilePageFixes : added progress bar for the download
- Comment on [HIEV-7317](https://elocity.atlassian.net/browse/HIEV-7317): Code review update — MR !778 Reviewed My Profile email edit lock on v4-ProfilePageFixes → v4-TempMay26Release . Coverage for this ticket Item Status Primary Email should not be editable ✅ Implemented ( disabled={true} on Primary Email in Edit Profile drawer) Retest Profile → Edit Confirm Primary Email field is disabled / not editable Save other fields (name/phone/language) without being able to change email Note: Overall MR !778 is REQUEST CHANGES due to HIEV-7313 success-popup gap; this ticket’
- Comment on [HIEV-7315](https://elocity.atlassian.net/browse/HIEV-7315): Sahil Siddiqui mentioned this issue in merge request !778 of Elocity / Frontend / web / Cpms Portal on branch v4-ProfilePageFixes : added progress bar for the download
- Comment on [HIEV-7315](https://elocity.atlassian.net/browse/HIEV-7315): Code review update — MR !778 Reviewed My Profile refresh fix on v4-ProfilePageFixes → v4-TempMay26Release . Coverage for this ticket Item Status Refresh must not reset applied Name filters ✅ Fixed What changed Removed the custom onRefreshAPI={handleRefresh} handler that cleared appliedUserNames / filter UI and forced reset. Grid refresh still calls refreshGrid() (reload datasource) without wiping filters. Retest Profile → Activity Logs Select Name filter(s) → Apply Click Refresh icon Confirm fil
- Comment on [HIEV-7313](https://elocity.atlassian.net/browse/HIEV-7313): Sahil Siddiqui mentioned this issue in merge request !778 of Elocity / Frontend / web / Cpms Portal on branch v4-ProfilePageFixes : added progress bar for the download
- Comment on [HIEV-7313](https://elocity.atlassian.net/browse/HIEV-7313): Code review update — MR !778 Reviewed v4-ProfilePageFixes → v4-TempMay26Release (My Profile export UX). Coverage for this ticket Item Status Issue 2 — keep label “Export Logs” (disable only) ✅ Implemented Issue 3 — progress bar ✅ Works via mounted RequestSubmittedModal + exportProgressEvent / DelayedLinearProgress Issue 1 — success pop-up after Export Logs ❌ Not working yet Blocking gap (Issue 1) activityLogsExport still sends async: false , and useExportFlow only opens RequestSubmittedModal whe
- Comment on [HIEV-7296](https://elocity.atlassian.net/browse/HIEV-7296): Sahil Siddiqui mentioned this issue in merge request !780 of Elocity / Frontend / web / Cpms Portal on branch v4-DiagnosticFixes : added export button to firmware jobs
- Comment on [HIEV-7296](https://elocity.atlassian.net/browse/HIEV-7296): Code review (MR ): Pass — Export Firmware Jobs wired on jobs grid (+ Export Stations on job details) via async export flow. STG retest: Export button visible with data; name modal → request submitted / download; filters + search applied. Minor follow-ups noted on MR (i18n kn/ko/pt/th, tablet disable).
- Comment on [HIEV-7234](https://elocity.atlassian.net/browse/HIEV-7234): Sahil Siddiqui mentioned this issue in merge request !780 of Elocity / Frontend / web / Cpms Portal on branch v4-DiagnosticFixes : added export button to firmware jobs
- Comment on [HIEV-7234](https://elocity.atlassian.net/browse/HIEV-7234): Code review (MR ): Pass — Job Status dropdown updated from Dispatch → Dispatching (`DISPATCHING` + i18n). API mappers accept both values. STG retest: Diagnostics → Job Status shows “Dispatching”; filter still returns expected jobs.
- Comment on [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226): Sahil Siddiqui mentioned this issue in merge request !781 of Elocity / Frontend / web / Cpms Portal on branch v4-ChargingSession : removed the refund option button when total cost is 0
- Comment on [HIEV-7226](https://elocity.atlassian.net/browse/HIEV-7226): Code review (MR ): Pass — Refund action gated on `total_cost > 0` in shared `ChargingSessionActionButtons`. STG retest: Corporate Charging Session with cost 0.00 → Refund hidden; cost > 0 → Refund still available when other conditions met.
- Comment on [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166): Sahil Siddiqui mentioned this issue in merge request !781 of Elocity / Frontend / web / Cpms Portal on branch v4-ChargingSession : removed the refund option button when total cost is 0
- Comment on [HIEV-7166](https://elocity.atlassian.net/browse/HIEV-7166): Code review (MR ): Pass — Reservation `to` now forced to end-of-day in `getReservations` (fixes DateRangePicker sending current time for Today). STG retest: add a reservation starting later today → filter Today / This Year → row should appear. Also smoke calendar week view.
- Comment on [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090): Sahil Siddiqui mentioned this issue in commit f543b1b4 of Elocity / Frontend / web / Cpms Portal on branch v4-MainBranch : fix( ): align Alerts date picker Apply with other grids Remove applyOnSelection=false so draft filters update on selection like other pages, enabling Apply after Last Year and other presets.
- Comment on [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090): Sahil Siddiqui mentioned this issue in commit 5081c185 of Elocity / Frontend / web / Cpms Portal on branch Alfanar-UAT : fix( ): align Alerts date picker Apply with other grids Remove applyOnSelection=false so draft filters update on selection like other pages, enabling Apply after Last Year and other presets.
- Comment on [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090): Fix re-applied — ready for retest SME / QA: please retest on UAT / CA_ELO. What was wrong The earlier fix set applyOnSelection={false} only on Alerts & Notifications date pickers. With that flag, selecting a preset (e.g. Last Year, This Week, This Month) updated only the picker’s local state. Parent draft filters did not update until the picker closed, so filters still matched lastAppliedFilters and Apply / Reset stayed disabled — matching the retest findings. Why other pages were fine Grids suc
- Comment on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062): Sahil Siddiqui mentioned this issue in merge request !781 of Elocity / Frontend / web / Cpms Portal on branch v4-ChargingSession : removed the refund option button when total cost is 0
- Comment on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062): Code review (MR ): Pass — CIN column removed from Business export config. STG retest: Business → Export Business → confirm CIN is absent from the downloaded report.
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Code review — MR (July fixes / Surya). Verdict: Request Changes — posted on the MR. Blockers called out: MultiSelectDropdown — ClickAwayListener likely closes menu on option click (Autocomplete listbox is portaled); breaks multi-select stay-open. validateNonEmpty 255-char check calls .trim() without a string guard — runtime risk for non-string values. Also reviewed: dashboard/fleet date presets, station blocked→decommissioned modal routing, report subscription close, network selector RSuite moda
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Read / reviewed July 2026 Sprint Retrospective (was absent):

**2026-08-05** — logged 0.9d (7h) of 1.0d (8h) available, 21 comments

- Worklog 45m on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388) (Task, mid-sprint) — Code review MR !782 — location filter on Utility Tariff Reports. Request Changes.
- Worklog 25m on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388) (Task, mid-sprint)
- Worklog 1h on [HIEV-7279](https://elocity.atlassian.net/browse/HIEV-7279) (Bug, mid-sprint) — MR !776 Guest Charging — code review + re-review / merge verification.
- Worklog 2.00h on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) (Task, mid-sprint)
- Worklog 3.00h on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) (Task, mid-sprint)
- Comment on [HIEV-7399](https://elocity.atlassian.net/browse/HIEV-7399): Sahil Siddiqui mentioned this issue in merge request !776 of Elocity / Frontend / web / Cpms Portal on branch v4-GuestChargingUpdation : Fixed the Guest Charging UI fixes
- Comment on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388): Code review — MR !782 Verdict: Request Changes (posted on MR) Blockers getApiFilters() uses draft filtersRef , not appliedFilters — year change can send unapplied selections; reload restores UI filters but first chart fetch ignores them. Use dropdownValueKey="locationPk" (not id ) — align with LaunchedTariffsGrid and ticket PK requirement. Minor Unused GRID_FILTERS import, unused locationFilter prop on ReportChartHeader , hardcoded modal hex colors. @Dharshini M — please fix #1 and #2, then move
- Comment on [HIEV-7388](https://elocity.atlassian.net/browse/HIEV-7388): re reviewed and merged
- Comment on [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385): Dhanush K G mentioned this issue in commit f4955ff4 of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : fix( ): map OCPI opening hours with ISO weekday (Sun=7) Location Detail showed Closed on Sundays because CardHeader compared JS getDay() (Sun=0) to API/OCPI regularHours (Mon=1…Sun=7). Use getISODay for CardHeader, map markers, and ChargingLocation. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385): Dhanush K G mentioned this issue in commit 204f5a58 of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : fix( ): map OCPI opening hours with ISO weekday (Sun=7) Location Detail showed Closed on Sundays because CardHeader compared JS getDay() (Sun=0) to API/OCPI regularHours (Mon=1…Sun=7). Use getISODay for CardHeader, map markers, and ChargingLocation. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385): Dhanush K G mentioned this issue in commit a466cdaa of Elocity / Frontend / mobile / CPMS-MobileApp on branch fix/HIEV-7385-sunday-iso-weekday : fix( ): map OCPI opening hours with ISO weekday (Sun=7) Location Detail showed Closed on Sundays because CardHeader compared JS getDay() (Sun=0) to API/OCPI regularHours (Mon=1…Sun=7). Use getISODay for CardHeader, map markers, and ChargingLocation. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7342](https://elocity.atlassian.net/browse/HIEV-7342): Re-review (MR https://gitlab.com/elocity1/frontend/web/cpms-portal/-/merge_requests/779): Pass / Approve — prior blockers fixed. Removed debug console.log; field detection uses allowlist first; i18n added for kn/ko/pt/th.
- Comment on [HIEV-7337](https://elocity.atlassian.net/browse/HIEV-7337): Re-review MR !779 batch: blockers cleared on HIEV-7342; sibling tickets remain Pass. MR Approve posted.
- Comment on [HIEV-7336](https://elocity.atlassian.net/browse/HIEV-7336): Re-review MR !779 batch: blockers cleared on HIEV-7342; sibling tickets remain Pass. MR Approve posted.
- Comment on [HIEV-7335](https://elocity.atlassian.net/browse/HIEV-7335): Re-review MR !779 batch: blockers cleared on HIEV-7342; sibling tickets remain Pass. MR Approve posted.
- Comment on [HIEV-7333](https://elocity.atlassian.net/browse/HIEV-7333): Re-review MR !779 batch: blockers cleared on HIEV-7342; sibling tickets remain Pass. MR Approve posted.
- Comment on [HIEV-7320](https://elocity.atlassian.net/browse/HIEV-7320): Re-review MR !778 batch: blockers cleared on HIEV-7313; sibling tickets remain Pass. MR Approve posted.
- Comment on [HIEV-7317](https://elocity.atlassian.net/browse/HIEV-7317): Re-review MR !778 batch: blockers cleared on HIEV-7313; sibling tickets remain Pass. MR Approve posted.
- Comment on [HIEV-7315](https://elocity.atlassian.net/browse/HIEV-7315): Re-review MR !778 batch: blockers cleared on HIEV-7313; sibling tickets remain Pass. MR Approve posted.
- Comment on [HIEV-7313](https://elocity.atlassian.net/browse/HIEV-7313): Re-review (MR ): Pass / Approve — prior blockers fixed. Success popup now opens via SavedSuccessModal on sync export onDirectSuccess . Cancel closes drawer; logout i18n + classes.disabled added.
- Comment on [HIEV-7295](https://elocity.atlassian.net/browse/HIEV-7295): Fix review comments and send back
- Comment on [HIEV-7279](https://elocity.atlassian.net/browse/HIEV-7279): Fix review comments and send back
- Comment on [HIEV-7279](https://elocity.atlassian.net/browse/HIEV-7279): Code review + merge — MR !776 Merged v4-GuestChargingUpdation → v4-MainBranch . Review / re-review coverage (this ticket as Guest Charging umbrella) Area Status Empty session status → no incorrect “Swipe to Stop” ✅ Handled ( Unknown Session Status / retry path) Navbar Guest logo ✅ GuestSideBarIcon Related Guest Charging UAT fixes in same MR Loaders, unavailable connectors, horizontal scroll, duration format, realtime charger details, Guest Charging filter on grids Follow-up (non-blocking) Poll f
- Comment on [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090): Test on uat.hiev.network
- Comment on [HIEV-7062](https://elocity.atlassian.net/browse/HIEV-7062): Please retest now. Due to pipeline failure code din’t get deployed
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Re-review cumulative (2h): MR !778 My Profile + MR !779 GHG — prior blockers cleared, Approve posted on both. Skipped Surya MR !777.

**2026-08-06** — logged 0.8d (6h) of 1.0d (8h) available, 8 comments

- Worklog 2h on [HIEV-7427](https://elocity.atlassian.net/browse/HIEV-7427) (Sub-task, mid-sprint) — AI Companion demo review — watched Demo Run, drafted Confluence open questions & bugs sheet for peer review.
- Worklog 2h 30m on [HIEV-7414](https://elocity.atlassian.net/browse/HIEV-7414) (Sub-task, mid-sprint) — Smartcar Firebase RTDB non-prod override (resolveSmartcarConfig + SmartcarAuth), iOS CI Tahoe codesign fixes (assert script + Fastlane), Confluence doc under CSMS Mobile Application, Jira update.
- Worklog 1h 30m on [HIEV-7407](https://elocity.atlassian.net/browse/HIEV-7407) (Sub-task, mid-sprint) — Investigated main pipeline failures (lint/unit/android), identified patched node_modules cache + Watchman hang root causes, shipped CI fixes to main and cherry-picked cache fix to react-doctor-score-improvements and feature/evlm-enrollment.
- Comment on [HIEV-7427](https://elocity.atlassian.net/browse/HIEV-7427): AI Companion review complete (2h) Created a Confluence review sheet from the Demo Run video covering: Companion timeline with video timestamps Open product / functionality questions Companion-only bugs (cost mismatch, portfolio counts, Demand Trends nav, PDF provenance, payback what-if) Findings doc (please review / edit): https://elocity.atlassian.net/wiki/spaces/EIPARE/pages/2177565109/AI+Companion+Open+Questions+Demo+Review Fellow reviewers (Sahil / Dinesh): please add or remove points as nee
- Comment on [HIEV-7414](https://elocity.atlassian.net/browse/HIEV-7414): Work completed (2026-08-06) — feature/evlm-enrollment 1) Smartcar Firebase RTDB config override (HIEV Canada, non-prod) Goal: Allow Smartcar OAuth credentials to be changed at runtime via Firebase RTDB for development / staging / uat without a rebuild. Production still uses .env / apiConfig . App changes Added core/utils/resolveSmartcarConfig.ts — non-empty RTDB/ appConfig values override apiConfig in non-prod; production always uses apiConfig . Wired SmartcarAuth to resolve via useAppSettings()
- Comment on [HIEV-7414](https://elocity.atlassian.net/browse/HIEV-7414): Sahil Siddiqui mentioned this issue in commit e00feabd of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : docs: document Smartcar Firebase RTDB override for follow-up rollout Capture HIEV Canada non-prod behaviour, RTDB keys, code map, security notes, and checklist for extending to other brands / production ( ). Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7414](https://elocity.atlassian.net/browse/HIEV-7414): Sahil Siddiqui mentioned this issue in commit b4ef059e of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : docs: remove Smartcar Firebase override markdown from repo Documentation lives on Confluence under CSMS / Mobile Application ( ). Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7414](https://elocity.atlassian.net/browse/HIEV-7414): Work completed (2026-08-06) — feature/evlm-enrollment 1) Smartcar Firebase RTDB config override (HIEV Canada, non-prod) Goal: Allow Smartcar OAuth credentials to be changed at runtime via Firebase RTDB for development / staging / uat without a rebuild. Production still uses .env / apiConfig . App changes Added core/utils/resolveSmartcarConfig.ts — non-empty RTDB/ appConfig values override apiConfig in non-prod; production always uses apiConfig . Wired SmartcarAuth to resolve via useAppSettings()
- Comment on [HIEV-7407](https://elocity.atlassian.net/browse/HIEV-7407): Root cause Main-branch CI ( lint_check , unit_test , build_android ) failed during yarn install postinstall — not during lint/tests/Gradle itself. Patched node_modules restored from GitLab cache CI caches node_modules/ . Local patches are applied via scripts/apply-local-patches.sh on postinstall. On a cache hit, packages are already patched, so git apply fails for ~20 patches. In CI, PATCH_STRICT=1 , so install exits with: error: 20 patch(es) failed in strict mode . Watchman hang on Android rele
- Comment on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362): https://www.figma.com/proto/65jdp0nt3j3neBpECbxsNs/Security-Profile?node-id=8192-81&viewport=34%2C2…
- Comment on [HIEV-7279](https://elocity.atlassian.net/browse/HIEV-7279): merged and sent for testing

**2026-08-09** — logged 0.6d (5h) of 0.0d (0h) available, 26 comments

- Worklog 15m on [HIEV-7430](https://elocity.atlassian.net/browse/HIEV-7430) (Task, mid-sprint) — Code review + merge (!786) — low complexity (1 file label mapping).
- Worklog 30m on [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404) (Bug, mid-sprint) — Code review + merge (!785) — small complexity (reservation validation + export modal spacing).
- Worklog 15m on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391) (Bug, mid-sprint) — Code review MR !784 — custom key enablement verified; blocked pending 7390 multi-CP fix.
- Worklog 30m on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390) (Bug, mid-sprint) — Code review MR !784 — sent back for multi-CP consumer fix (primary ticket).
- Worklog 15m on [HIEV-7328](https://elocity.atlassian.net/browse/HIEV-7328) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 30m on [HIEV-7321](https://elocity.atlassian.net/browse/HIEV-7321) (Bug, mid-sprint) — Added client-side validation for Minimum Balance (max 100000000 / 9 digits) on Station Details, Add Station, and Bulk Station Update. Pushed to v4-MainBranch.
- Worklog 15m on [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 15m on [HIEV-7236](https://elocity.atlassian.net/browse/HIEV-7236) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 15m on [HIEV-7235](https://elocity.atlassian.net/browse/HIEV-7235) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 15m on [HIEV-7218](https://elocity.atlassian.net/browse/HIEV-7218) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 15m on [HIEV-7215](https://elocity.atlassian.net/browse/HIEV-7215) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 15m on [HIEV-7207](https://elocity.atlassian.net/browse/HIEV-7207) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 15m on [HIEV-7204](https://elocity.atlassian.net/browse/HIEV-7204) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 15m on [HIEV-7202](https://elocity.atlassian.net/browse/HIEV-7202) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 15m on [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 15m on [HIEV-7094](https://elocity.atlassian.net/browse/HIEV-7094) (Bug, mid-sprint) — Code review for MR !777 (high complexity, 37 files) — portion allocated to this ticket.
- Worklog 0.25h on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) (Task, mid-sprint)
- Comment on [HIEV-7430](https://elocity.atlassian.net/browse/HIEV-7430): Sahil Siddiqui mentioned this issue in merge request !786 of Elocity / Frontend / web / Cpms Portal on branch v4-EventType : mapping more defined and accurate names in the frontend for EventType parameter
- Comment on [HIEV-7430](https://elocity.atlassian.net/browse/HIEV-7430): Reviewed and merged MR !786 into v4-TempMay26Release . Changes: EventType display names updated (Wallet Credit / Wallet Refund / Session Refund / Session Debit). Moved to Ready for Testing.
- Comment on [HIEV-7404](https://elocity.atlassian.net/browse/HIEV-7404): Reviewed and merged MR !785 into v4-TempMay26Release . Fix: Reservation duration validation now falls back to local global settings and correctly compares min/max limits (fixes Save not calling Create Reservation API). Moved to Ready for Testing.
- Comment on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391): Sahil Siddiqui mentioned this issue in merge request !784 of Elocity / Frontend / web / Cpms Portal on branch v4-BulkOperationFixes : Enabled Perform Action Button for Custom Option
- Comment on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391): Sent back to developer (Dharshini) with MR !784. Custom-key Perform Action enablement looks correct for this ticket, but the shared MR is blocked on HIEV-7390 (only first selected CPID is sent as consumer ). Please address the multi-CP consumer handling on !784, then move both tickets back to In Review together. MR: https://gitlab.com/elocity1/frontend/web/cpms-portal/-/merge_requests/784
- Comment on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390): Sahil Siddiqui mentioned this issue in merge request !784 of Elocity / Frontend / web / Cpms Portal on branch v4-BulkOperationFixes : Enabled Perform Action Button for Custom Option
- Comment on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390): Sent back to developer (Dharshini) — MR !784 needs rework. Blocking issue (HIEV-7390): Get Configuration still sends only the first selected charge point as consumer . Sibling bulk OCPP actions pass all selected CPIDs via consumers / bulk APIs. Multi-select therefore still ignores all but the first CP. Please fix: Confirm with backend whether a bulk get-configuration endpoint exists. If yes — use it with all selected CPIDs. If no — either loop per CPID or clearly restrict UI to single CP and doc
- Comment on [HIEV-7328](https://elocity.atlassian.net/browse/HIEV-7328): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . Report Subscription modal X close behavior updated. Moved to Ready for Testing.
- Comment on [HIEV-7321](https://elocity.atlassian.net/browse/HIEV-7321): Fixed and pushed to v4-MainBranch . Changes Added validateMinWalletBalance — rejects values above 100000000 with inline error Restricted Minimum Balance input to 9 digits ( requireTrim ) Applied on Station Details, Add Station, and Bulk Station Update Commit: fix(HIEV-7321): add client-side max validation for Minimum Balance
- Comment on [HIEV-7321](https://elocity.atlassian.net/browse/HIEV-7321): Sahil Siddiqui mentioned this issue in commit ceb2e521 of Elocity / Frontend / web / Cpms Portal on branch v4-MainBranch : fix( ): add client-side max validation for Minimum Balance Enforce max value of 100000000 and 9-digit input limit so oversized numeric input is rejected inline instead of only failing on save.
- Comment on [HIEV-7321](https://elocity.atlassian.net/browse/HIEV-7321): Fixed and pushed to v4-MainBranch . Changes Added validateMinWalletBalance — rejects values above 100000000 with inline error Restricted Minimum Balance input to 9 digits ( requireTrim ) Applied on Station Details, Add Station, and Bulk Station Update Commit: fix(HIEV-7321): add client-side max validation for Minimum Balance
- Comment on [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . Client-side max length validation (255) added via validateNonEmpty path for location/character-limit handling. Moved to Ready for Testing.
- Comment on [HIEV-7236](https://elocity.atlassian.net/browse/HIEV-7236): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . User Details action button styling fixed. Moved to Ready for Testing.
- Comment on [HIEV-7235](https://elocity.atlassian.net/browse/HIEV-7235): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . Title ellipsis/tooltip for long station names updated. Moved to Ready for Testing.
- Comment on [HIEV-7218](https://elocity.atlassian.net/browse/HIEV-7218): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . Tariff validation clear on checkbox unselection fixed. Moved to Ready for Testing.
- Comment on [HIEV-7215](https://elocity.atlassian.net/browse/HIEV-7215): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . Dropdown blur/close behavior updated for multi-select / reservation charge-point selectors. Moved to Ready for Testing.
- Comment on [HIEV-7207](https://elocity.atlassian.net/browse/HIEV-7207): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . Add New Location timings layout / button cropping fixed. Moved to Ready for Testing.
- Comment on [HIEV-7204](https://elocity.atlassian.net/browse/HIEV-7204): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . Includes Overall/Fleet date filter updates (Yesterday / Last Week / Last Month defaults). Moved to Ready for Testing.
- Comment on [HIEV-7202](https://elocity.atlassian.net/browse/HIEV-7202): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . Blocked → Decommissioned now shows the correct decommission confirmation modal. Moved to Ready for Testing.
- Comment on [HIEV-7202](https://elocity.atlassian.net/browse/HIEV-7202): Please note that although the ticket is with regard to Canada prod. We will not be deploying the fix immediately to Canada prod, since it's a non-breaking, very low-priority issue, which should not trigger a production release on its own. Please check the fix for the same issue on the Stage env. In the next major release fix will be deployed to Canada prod
- Comment on [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . Batch of low-priority portal UI fixes included in this MR (network selector modal, text-field placeholder on error, shared dropdown/title polish). Moved to Ready for Testing.
- Comment on [HIEV-7094](https://elocity.atlassian.net/browse/HIEV-7094): Covered by MR !777 (July fixes) — merged into v4-TempMay26Release . RFID modal outside-click / close behavior updated. Moved to Ready for Testing.
- Comment on [HIEV-7094](https://elocity.atlassian.net/browse/HIEV-7094): Please note that although the ticket is with regard to Canada prod. We will not be deploying the fix immediately to Canada prod, since it's a non-breaking, very low-priority issue, which should not trigger a production release on its own. Please check the fix for the same issue on the Stage env. In the next major release fix will be deployed to Canada prod
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Fixed unit_tests CI failures on v4-TempMay26Release (28 failing → 0). Root causes / fixes: basicValidation imported MAX_MIN_WALLET_BALANCE from GeneralConstants (pulls COUNTRY_CODE ) → moved constants to SharedFeatureConstants . MultiSelectDropdown / StationManagement tests missing ClickAwayListener mock after close-on-blur change. FleetDashboard tests: incomplete DateRange + CustomDate mocks for YESTERDAY/LAST_WEEK presets. Verification: npx vitest run — 318 files / 1563 tests passed. Branch: v
- Comment on [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836): Dhanush K G mentioned this issue in commit c4d349f1 of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : fix( ): restore in-app campaigns and sequence map overlays Gate campaign fetch/show on isLoggedIn (not stripped access_token), use the env-aware Firebase campaigns path, and show tour → biometric → campaign so overlays no longer race. Also tighten CampaignModal UX (CloseIcon, Got it CTA, content-sized height) and keep campaigns out of redux-persist. Co-a
- Comment on [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836): Dhanush K G mentioned this issue in commit 1c57db63 of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : fix( ): restore in-app campaigns and sequence map overlays Gate campaign fetch/show on isLoggedIn (not stripped access_token), use the env-aware Firebase campaigns path, and show tour → biometric → campaign so overlays no longer race. Also tighten CampaignModal UX (CloseIcon, Got it CTA, content-sized height) and keep campaigns out of redux-persist. Co-authored-

**2026-08-10** — logged 1.2d (10h) of 1.0d (8h) available, 9 comments

- Worklog 1h on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440) (Task, mid-sprint) — Doc review of Customer Module developer implementation flow Confluence page; posted review findings (Request changes) on ticket.
- Worklog 1h on [HIEV-7348](https://elocity.atlassian.net/browse/HIEV-7348) (Task, planned) — Design / architecture: arrive at Encrypted Bearer JWT + gateway edge-decrypt solution (no cookies); update Confluence implementation guide.
- Worklog 3h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned) — Customer Onboard/Detail live API hardening: contract-aligned payloads, hide MFA, null-safe review/detail, suggested-TX radius 100km. Blocked on transformer GIS — interim map API with Deepak. Commit 19eb556.
- Worklog 4.00h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Worklog 0.50h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Dhanush K G mentioned this issue in commit f9ee5e63 of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : fix( ): harden campaign maxDisplayCount enforcement Normalize Firebase campaign id/displayRules (including flattened top-level fields), fail closed on invalid maxDisplayCount, persist impressions with read-back verification, gate the show path with an in-flight session lock, and remove the duplicate RTDB listener from CommonFeaturesHooks so counts cannot
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Dhanush K G mentioned this issue in commit ae6ac9a4 of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : fix( ): harden campaign maxDisplayCount enforcement Normalize Firebase campaign id/displayRules (including flattened top-level fields), fail closed on invalid maxDisplayCount, persist impressions with read-back verification, gate the show path with an in-flight session lock, and remove the duplicate RTDB listener from CommonFeaturesHooks so counts cannot be skip
- Comment on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440): Doc review — Request changes Reviewed: Developer code Implementation flow of Customer Module (v21) against cpms-portal . Verdict: Not ready to Approve. Structure matches the Dashboard template and most Customer/RFID/wallet/session coverage is directionally correct, but several sections are factually wrong (especially Refund) and should be fixed before approval. Blocking / high-priority accuracy fixes §6.9 Refund is incorrect src/pages/Customer/Refund is a modal ( RefundModal ) used from wallet /
- Comment on [HIEV-7348](https://elocity.atlassian.net/browse/HIEV-7348): Solution decision log (design / architecture) Context Reviewed the original obfuscation POC and our Istio gateway JWT behaviour. Goal: hide the JWT on the wire while keeping the existing Bearer auth model (cookies ruled out). Decision Encrypted Bearer JWT + edge decrypt (no cookies). Keep Authorization: Bearer … (existing way). Encrypt only the JWT value with a per-visit AES-256-GCM session key (handshake at app start). Decrypt at the API Gateway before Istio JWT validation. Nest services stay a
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): Work log — Customer Onboard / Detail live API hardening (3h) Done Hardened Customer Onboard request builders to send only entered form values (no silent mock/default leakage: enrollment type, empty VIN/year, consent defaults, etc.). Aligned validations with staging OpenAPI enums/rules ( mappingMethod , auth, VIN, SOC, opt-out, manual override requires transformer). Removed unsupported MFA code UI from Review — live FinalizeBodyDto has no MFA field; finalize posts documentVersion only. Null-safe 
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): Transformers (GRID) API integration — pushed to main Commit: 366a82e feat(transformers): live GRID provider onboard, load-profile chart, and sync #HIEV-6941 What's done Onboard wizard: provider → test-connection ( providerId → { ok, message } ) → catalog asset pick → create with paired providerId + externalAssetId Detail: live load-profile + chart-overlays ; Sync from catalog; 30s poll for header metrics List: predictive-risk filter/badge hidden (Phase 2); feederId filter kept Bugfix: keep opera
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): Customer Onboard — manual transformer map API (GIS bypass) Wired contract §2.6a PUT /evlm/v1/ops/customers/onboard/{onboardingId}/transformer into the Address step Manual override flow. What shipped New client mapOnboardingTransformer + mock Manual override: save address without overrideTransformerId , then call map API with { transformerId } Override dropdown populated from ops transformers roster when Manual override is selected (Auto GIS still uses GIS suggestions only) Session mapping update
- Comment on [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836): Dhanush K G mentioned this issue in commit f0226af1 of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : fix( ): enforce campaign maxDisplayCount by counting on show Record AsyncStorage impressions when the campaign modal opens so force-quit or navigate-away cannot skip the counter. Stop double-counting on close, fail closed on storage errors, and keep lower priority numbers shown first for multi-campaign carousels. Co-authored-by: Cursor <cursoragent@curso
- Comment on [HIEV-5836](https://elocity.atlassian.net/browse/HIEV-5836): Dhanush K G mentioned this issue in commit ec2b92b2 of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : fix( ): enforce campaign maxDisplayCount by counting on show Record AsyncStorage impressions when the campaign modal opens so force-quit or navigate-away cannot skip the counter. Stop double-counting on close, fail closed on storage errors, and keep lower priority numbers shown first for multi-campaign carousels. Co-authored-by: Cursor <cursoragent@cursor.com>

**2026-08-11** — logged 0.9d (7h) of 1.0d (8h) available, 6 comments

- Worklog 1h on [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237) (Bug, mid-sprint) — Reviewed Address Line 1 / autocomplete character-limit failure path and evaluated architecture options for the best fix. Considered approaches: Rely only on existing validateNonEmpty (255) on blur/Save — insufficient, because autocomplete API fires while typing and already surfaces HTTP 500 → ServiceGlitchModal. Suppress SERVICE_GLITCH for /location-autocomplete in axios — safety net only; does not stop bad requests or give field-level UX. Guard inside AddressAutocomplete (preferred) — block searchLocationAutocomplete when input exceeds max length, show the same character-limit validation message, optionally set maxLength on the input, with a hard early-return in fetchSuggestions as defense in depth. Conclusion: client-side max-length guard in AddressAutocomplete is the correct architectural fix; axios glitch skip is optional hardening only. Documented recommended implementation for Surya on the ticket.
- Worklog 6.00h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Comment on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458): Dhanush K G mentioned this issue in commit 3f3dd418 of Elocity / Frontend / mobile / CPMS-MobileApp on branch bugfixes/ui-and-metadata : fix( ): stop country-code loader flash and filter picker on first open Treat empty metadata countryCallingCode as not-loaded so the picker uses major-country fallback immediately, and always show the selected flag/code instead of a spinner while metadata loads. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Dhanush K G mentioned this issue in commit 9f5d456d of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : fix( ): restore multi-campaign rules and RTDB casing tolerance Enforce maxDisplayCount, cooldownHours, and onlyOnce per campaign in the carousel; tolerate Firebase key casing typos (e.g. maxdisplayCount) that dropped welcome from multi-campaign shows; fix session/show races and dismiss all pages on close. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Dhanush K G mentioned this issue in commit 3180b7a0 of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : fix( ): restore multi-campaign rules and RTDB casing tolerance Enforce maxDisplayCount, cooldownHours, and onlyOnce per campaign in the carousel; tolerate Firebase key casing typos (e.g. maxdisplayCount) that dropped welcome from multi-campaign shows; fix session/show races and dismiss all pages on close. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237): — Review notes for the remaining Address Line 1 / Autocomplete character-limit issue (Location Name is already verified as fixed). Root Cause AddressAutocomplete calls /location-autocomplete as soon as input length ≥ minChars (3), with no upper-bound check . Long paste/type (~200+ chars) → API returns HTTP 500 → axios interceptor emits SERVICE_GLITCH → generic “Something went wrong!” popup. validateNonEmpty (255-char check) only runs on blur / Save , so it does not prevent the autocomplete API c
- Comment on [HIEV-6942](https://elocity.atlassian.net/browse/HIEV-6942): Dhanush K G mentioned this issue in commit 3a8db1ab of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : feat( ): align Smartcar Connect My Car with backend API contract Point Vehicle Details at get-smartcar-info, use path-based charge/security/disconnect actions, handle null telemetry blocks, and keep SMARTCAR_USE_MOCK_DATA for local info mocks only. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): Progress: DR Events API integration (EVLM portal) Completed Live DR API integration aligned with existing customer/transformers patterns Normalize layer ( normalizeDr.ts ) mapping live @evlm/contracts / DrService envelopes to portal UX shapes (list, detail, simulate, participants, event-log, compliance) Query param mapping : fromDate / toDate / pageSize → dateFrom / dateTo / limit Axios-aware parseDrApiError + MFA detection matching Onboard/Transformers patterns MFA staging bypass ; removed inte

**2026-08-12** — logged 1.2d (10h) of 1.0d (8h) available, 15 comments

- Worklog 30m on [HIEV-7468](https://elocity.atlassian.net/browse/HIEV-7468) (Bug, mid-sprint) — Investigated and fixed Create Load Group infinite Save spinner (validateNonEmpty trim on station array). Pushed to v4-TempMay26Release.
- Worklog 30m on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391) (Bug, mid-sprint) — Code review and merge of MR !784 (Get Configuration custom key Perform Action enablement).
- Worklog 30m on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390) (Bug, mid-sprint) — Code review and merge of MR !784 (Get Configuration bulk ops fixes).
- Worklog 8.00h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Comment on [HIEV-7474](https://elocity.atlassian.net/browse/HIEV-7474): Dhanush K G mentioned this issue in commit 3bfba8cb of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : feat( ,7475,7476): reservation card UX and 12h AM/PM times Add connector icons and middle-dot schedule formatting on reservation cards, and standardize user-facing clock times to 12-hour AM/PM across reservations, notifications, home charging, reports, and related surfaces. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7474](https://elocity.atlassian.net/browse/HIEV-7474): Dhanush K G mentioned this issue in commit d4fde752 of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : feat( ,7475,7476): reservation card UX and 12h AM/PM times Add connector icons and middle-dot schedule formatting on reservation cards, and standardize user-facing clock times to 12-hour AM/PM across reservations, notifications, home charging, reports, and related surfaces. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7468](https://elocity.atlassian.net/browse/HIEV-7468): Root cause Regression from commit that added a 255-char check in validateNonEmpty ( val.trim().length > 255 ). Create Load Group validates selected stations with validateNonEmpty(evseUids) where evseUids is an array . After stations are selected, the empty-array check passes, then .trim() is called on the array → TypeError: val.trim is not a function . That exception aborted onClickSave before setSavingProgressText("") and before AddLoadGroup / the /evse-group API call → infinite spinner, no net
- Comment on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458): Dhanush K G mentioned this issue in commit 339551ab of Elocity / Frontend / mobile / CPMS-MobileApp on branch bugfixes/ui-and-metadata : fix( ): replace cold-start spinner with branded BootSplash Show looping GIF for Total Energies/Alfanar and AppLogo for other brands during boot/profile wait, and let HIEV Canada read VERSION_NAME/BUILD_NUMBER from .env like the other flavors. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458): Dhanush K G mentioned this issue in merge request !488 of Elocity / Frontend / mobile / CPMS-MobileApp on branch bugfixes/ui-and-metadata : fix( ): country picker boot splash and cold-start BootSplash
- Comment on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458): Dhanush K G mentioned this issue in commit 157325dc of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : Merge branch 'bugfixes/ui-and-metadata' into 'react-doctor-score-improvements' fix( ): country picker boot splash and cold-start BootSplash See merge request elocity1/frontend/mobile/CPMS-MobileApp!488
- Comment on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458): Dhanush K G mentioned this issue in commit fcdb50a2 of Elocity / Frontend / mobile / CPMS-MobileApp : fix( ): country picker boot splash and cold-start BootSplash
- Comment on [HIEV-7458](https://elocity.atlassian.net/browse/HIEV-7458): Dhanush K G mentioned this issue in commit cf0956dc of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : fix( ): country picker boot splash and cold-start BootSplash
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Dhanush K G mentioned this issue in commit 7363f9bb of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : test( ): cover independent maxDisplayCount across multi-campaign set Lock in 5 vs 3 behavior: both show until the lower max, then only the remaining campaign continues, and exhausted counts are not incremented. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Dhanush K G mentioned this issue in commit f23c1dc7 of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : test( ): cover independent maxDisplayCount across multi-campaign set Lock in 5 vs 3 behavior: both show until the lower max, then only the remaining campaign continues, and exhausted counts are not incremented. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Dhanush K G mentioned this issue in commit d02448d8 of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : fix( ): count multi-campaign impressions per viewed page only Closing while on campaign-001 no longer burns campaign-002's maxDisplayCount. First visible page is counted on open; siblings count when swiped to, so the next eligible campaign still shows after one hits max. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7446](https://elocity.atlassian.net/browse/HIEV-7446): Dhanush K G mentioned this issue in commit 5d92c33d of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : fix( ): count multi-campaign impressions per viewed page only Closing while on campaign-001 no longer burns campaign-002's maxDisplayCount. First visible page is counted on open; siblings count when swiped to, so the next eligible campaign still shows after one hits max. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7391](https://elocity.atlassian.net/browse/HIEV-7391): Re-reviewed MR !784 after the follow-up fixes. Custom configuration key path (trim/dedupe + Perform Action enablement when typed custom key is present) looks addressed for this ticket. Logged 30m for re-review and merge. MR !784 merged into v4-TempMay26Release . MR: https://gitlab.com/elocity1/frontend/web/cpms-portal/-/merge_requests/784
- Comment on [HIEV-7390](https://elocity.atlassian.net/browse/HIEV-7390): Re-reviewed MR !784 after the follow-up fixes. Multi-CP consumer handling via parseChargePoints + per-CP getConfiguration calls looks addressed for this ticket. Logged 30m for re-review and merge. MR !784 merged into v4-TempMay26Release . MR: https://gitlab.com/elocity1/frontend/web/cpms-portal/-/merge_requests/784
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): Incentive Management — work completed Full documentation of UI, API layer, wiring, stage integration, tests, and commit (supersedes the earlier brief note on this comment). UI / Screens Replaced the old Payout Approval Queue with the Figma Incentive Management experience Routes/nav: Incentive Management section (Overview, Ledger, History); Create Rule wizard; Ledger detail Screens delivered: Overview / Dashboard Create Rule wizard (type → setup → payment → review) Ledger Ledger Detail Payout Bat

**2026-08-13** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 5m on [HIEV-7489](https://elocity.atlassian.net/browse/HIEV-7489) (Bug, mid-sprint)
- Worklog 8.00h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Comment on [HIEV-7489](https://elocity.atlassian.net/browse/HIEV-7489): Hi , hiding the Export option in Peak hours was a decision made by Backend team members, and . Also additionally ticket was approved and closed by the QA team(Documented ticket reference for the same -> ). Sending this ticket back to you. Please have a discussion with Vinay and Sahil Kumar if we want to reinstate the Download button Option in the peak hours report.
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): EVLM frontend — document migration, docs, hardening, and unit-test coverage (2026-08-13) Work landed on main as a8054a0 ( test: raise Vitest coverage and document EVLM frontend test inventory ). No PR created. 1. Document migration (CSMS → EVLM Confluence) Copied (not moved) the CSMS EVLM Frontend documentation tree into the EVLM space so CSMS originals remain in place. Hub page: EVLM Web App Frontend — https://elocity.atlassian.net/wiki/spaces/EVLM/pages/2188378116 (page 2188378116 ). Renames a

**2026-08-14** — logged 0.5d (4h) of 1.0d (8h) available, 9 comments

- Worklog 1h on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503) (Bug, mid-sprint) — Investigated HIEV-7503, patched portal metadata refresh after EVSE model create on v4-TempMay26Release, reproduced remaining backend gap (slow POST /evse-model + new model missing from GET /metadata).
- Worklog 3h on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359) (Task, planned) — Implemented Unique Drivers graph enhancement: v2 stacked first-time vs returning bars, summary metrics, export, i18n, and Vitest coverage. Also applied Unique Drivers chart height layout to other reporting graphs. Raised MR !787 against v4-TempMay26Release.
- Comment on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503): Sahil Siddiqui mentioned this issue in commit 1c7e4c4c of Elocity / Frontend / web / Cpms Portal on branch v4-TempMay26Release : fix( ): refresh EVSE model list in Redux after create The grid reads Redux metadata, but a successful create only wrote localStorage. Fetch tenant-filtered metadata into Redux so the new model appears in list and search.
- Comment on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503): CC: , Frontend status Portal refresh fix is in place on v4-TempMay26Release . After a successful EVSE model create, we now refetch tenant-filtered metadata into Redux (the source the EVSE Models grid/search actually reads), instead of only writing localStorage. That FE path is working — list/search correctly reflects whatever GET /metadata returns. This remaining issue is backend Two backend problems: Create API is slow. POST /evse-model takes almost 20–30 seconds before it returns success. That
- Comment on [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477): Dhanush K G mentioned this issue in commit 3d6a3af5 of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : feat( ): add reservation entry points from list and location cards Expose Reserve next to Directions and a Reservation-tab + so users can start the existing booking flow without changing charger or time logic. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7477](https://elocity.atlassian.net/browse/HIEV-7477): Dhanush K G mentioned this issue in commit b98bc38b of Elocity / Frontend / mobile / CPMS-MobileApp on branch react-doctor-score-improvements : feat( ): add reservation entry points from list and location cards Expose Reserve next to Directions and a Reservation-tab + so users can start the existing booking flow without changing charger or time logic. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7468](https://elocity.atlassian.net/browse/HIEV-7468): it can be tested. it is deployed to stage
- Comment on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359): Sahil Siddiqui mentioned this issue in commit 6173a4a3 of Elocity / Frontend / web / Cpms Portal : feat( ): enhance Unique Drivers reporting graph Switch Unique Drivers to the v2 stacked first-time vs returning view, summary metrics, export, and i18n, with Vitest coverage.
- Comment on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359): Sahil Siddiqui mentioned this issue in commit 174dfcad of Elocity / Frontend / web / Cpms Portal on branch feature/HIEV-7359-unique-drivers-graph : fix( ): fill unused space in reporting graphs Let chart-only reports grow into leftover card height instead of staying at 50%, matching Unique Drivers layout.
- Comment on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359): Sahil Siddiqui mentioned this issue in merge request !787 of Elocity / Frontend / web / Cpms Portal on branch feature/HIEV-7359-unique-drivers-graph : feat( ): enhance Unique Drivers reporting graph
- Comment on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359): Work log — 14 Aug 2026 (3h) Implemented the Unique Drivers graph enhancement on the Reporting Dashboard: Switched graph and export to v2 APIs (stacked first-time vs returning bars, headline unique-driver count, average active days per driver) Added i18n keys in all 8 locales and Vitest coverage Applied the Unique Drivers chart height layout to other reporting graphs so they fill leftover card space Raised MR: https://gitlab.com/elocity1/frontend/web/cpms-portal/-/merge_requests/787 Note: fronten

**2026-08-17** — logged 0.9d (8h) of 1.0d (8h) available, 9 comments

- Worklog 10m on [HIEV-7516](https://elocity.atlassian.net/browse/HIEV-7516) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7515](https://elocity.atlassian.net/browse/HIEV-7515) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7514](https://elocity.atlassian.net/browse/HIEV-7514) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7513](https://elocity.atlassian.net/browse/HIEV-7513) (Bug, mid-sprint)
- Worklog 6.00h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Comment on [HIEV-7516](https://elocity.atlassian.net/browse/HIEV-7516): Hi , Thank you for raising this ticket and for sharing the recordings — I appreciate you documenting this after our Teams conversation so we could take a closer look. I have gone through the reported scenarios on UAT, and followed the reproduction steps step by step: Creating a new location with Payment Type = Prepaid Checking Country and Time Zone dropdowns Opening an existing location in both View and Edit Editing an existing station and reviewing Advanced Controls (including Make / Model) On 
- Comment on [HIEV-7515](https://elocity.atlassian.net/browse/HIEV-7515): Same root cause as HIEV-7513 The Contact Number field did validate . No error appeared because the mobile validator returned success , so the red helper text was never rendered. This is not a skipped validation, a missing error component, or a save-path bypass. This is the same shared validator as Corporate Add ( HIEV-7513 ). Administration → Add New User ( /ca/add-new-user ) is a different screen, but it uses the same PhoneInputField + validatePhoneNumber + isMobilePhone path. 1. Add New User a
- Comment on [HIEV-7514](https://elocity.atlassian.net/browse/HIEV-7514): Same root cause as HIEV-7513 and HIEV-7515 The Location Contact Number field did validate . No error appeared because the mobile validator returned success , so the red helper text was never rendered. This is not a skipped validation, a missing error component, or a Next-step bypass. This is the same shared validator as Corporate Add ( HIEV-7513 ) and Add New User ( HIEV-7515 ). Add Location ( /ca/add-new-location ) is a different screen, but it uses the same PhoneInputField + isMobilePhone path
- Comment on [HIEV-7513](https://elocity.atlassian.net/browse/HIEV-7513): Root cause: validation ran and passed — error UI is only shown on failure The Contact Number field did validate . No error appeared because the mobile validator returned success , so the red helper text was never rendered. This is not a skipped validation, a missing error component, or a save-path bypass. 1. Corporate already uses the mobile-only validator Add Corporate ( /ca/add-corporate ) uses PhoneInputField without contactNumberValidationType="business_contact_phone" . Default type is phone
- Comment on [HIEV-7269](https://elocity.atlassian.net/browse/HIEV-7269): deplyed to uat. please test
- Comment on [HIEV-7150](https://elocity.atlassian.net/browse/HIEV-7150): Dhanush K G mentioned this issue in commit 2ff5089b of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : feat( ): poll live session data and wire fleet history dates Reuse chargeSessionStatus polling and the existing websocket on FleetSession so kW, energy, duration, and SoC update after start. Pass dateFrom/dateTo from the history calendar into transactions?fleet=true. Leave group-wide Live dashboard and notifications on placeholders until backend confirms those A
- Comment on [HIEV-7150](https://elocity.atlassian.net/browse/HIEV-7150): Dhanush K G mentioned this issue in commit 0c3380fa of Elocity / Frontend / mobile / CPMS-MobileApp : feat( ): wire Fleet tab to the mobile fleet manager API contract Replace placeholder /mobile/v1/fleet mocks with /fleet/mobile stations, start/stop, and reused evse/history APIs so fleet charging uses real CPMS responses. Leave fleet vs EVLM user detection unchanged until the access flag is confirmed on profile or login. Co-authored-by: Cursor <cursoragent@cursor.com>
- Comment on [HIEV-7150](https://elocity.atlassian.net/browse/HIEV-7150): Dhanush K G mentioned this issue in commit 9b33d46e of Elocity / Frontend / mobile / CPMS-MobileApp on branch feature/evlm-enrollment : fix( ): correct fleet contract gaps found in review Start no longer reports failure when the contract's 200 response carries an empty body, and a manager's own public session can no longer paint the fleet session card — the live chargeSessionStatus payload is only merged when its session and EVSE ids agree with the fleet session on screen. Live cards now carry s
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): 17 Aug 2026 — EVLM portal (daily log) Shipped create-role on Admin ( POST /roles ) and wired the EVLM ops-admin roles/users client (HIEV-7471). Staging still has no /ops/admin on Swagger. Shipped Sign in with Microsoft using the existing CPMS Entra app and AMS Azure login ( x-product: EVLM ). Live click still needs EVLM {origin}/azure-ad on the Entra allow-list and matching AMS AZURE_REDIRECT_URI (HIEV-7482). Published the team Screen and API Integration Status page in Confluence (EVLM): backend

**2026-08-18** — logged 1.2d (10h) of 1.0d (8h) available, 1 comments

- Worklog 8.00h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Worklog 2.00h on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) (Task, mid-sprint)
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): Work completed — 18 Aug 2026 (1d) Production-grade @abstract shells and Save Draft hide on evlm-portal . Draft persist stays in sagas/APIs/hooks; the CTAs are gone from wizard UI. Save Draft (UI only) Removed Save Draft / Save as Draft from Onboard , Incentive Create , and Transformer Create (header + footer). Kept SAVE_DRAFT_* actions, saveOnboardingDraft , saveDraft saga/hook, and Incentive ensureDraftVersion() (still used on Continue/Publish). Page tests now assert those buttons are absent . 

**2026-08-21** — logged 1.1d (8h) of 1.0d (8h) available, 1 comments

- Worklog 8.50h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): Daily log — 21 Aug 2026 (Frontend) Live API integrations Vehicles roster — wired @api/vehicles to staging ( GET /v1/ops/vehicles/* ); KPIs Total/Active/Inactive; API_INTEGRATION.vehicles = true . Dashboard / Reports — already live on staging ( /v1/ops/dashboard/* , /v1/ops/reports/* ); confirmed in status docs. Incentives — new Figma screens shipped Built and routed under Incentive Management: Version comparison — /demand-response/incentives/compare (Figma 3940:5603) Edit rule as new draft — Ove

**2026-08-24** — logged 0.3d (2h) of 1.0d (8h) available, 17 comments

- Worklog 30m on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492) (Bug, mid-sprint) — Code review of MR !795 — Employee ID 50-char validation. Requested missing locales + clarified input maxLength vs ticket expected result.
- Worklog 30m on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440) (Task, mid-sprint) — Re-reviewed Customer Module developer-flow Confluence doc (v29) against cpms-portal. Requested remaining refund payload/flow + Status fixes.
- Worklog 30m on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364) (Task, planned) — Code review of MR !790 — download toast framework. Requested changes (i18n gaps, dual success UX, error/retry handling).
- Worklog 1.00h on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) (Task, mid-sprint)
- Comment on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503): Dharshini M mentioned this issue in commit 6dbade15 of Elocity / Frontend / web / Cpms Portal : test( ): mock useDispatch in AddEVSEModel unit tests The create-success refresh now uses useDispatch; the previous mock only exported useSelector and broke the Vitest suite.
- Comment on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503): Dharshini M mentioned this issue in commit 1c7e4c4c of Elocity / Frontend / web / Cpms Portal : fix( ): refresh EVSE model list in Redux after create The grid reads Redux metadata, but a successful create only wrote localStorage. Fetch tenant-filtered metadata into Redux so the new model appears in list and search.
- Comment on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492): Sahil Siddiqui mentioned this issue in merge request !795 of Elocity / Frontend / web / Cpms Portal on branch v4-EmployeeIDField : Added 50 character limit for Employee ID and validation message
- Comment on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492): Reviewed MR !795: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/795 Verdict: REQUEST CHANGES What the MR does well: adds a 50-char check in shared validateOptionalEmployeeId (covers Add + Edit employee), with i18n message on blur/submit. Blocking: i18n key cannot exceed 50 characters missing in ko, kn, th, pt (only en/en-US/ar/fr) Also noted: Ticket expected “characters should not be accepted beyond max” — input still allows ~700 chars because Editable/TF.tsx hardco
- Comment on [HIEV-7468](https://elocity.atlassian.net/browse/HIEV-7468): Dharshini M mentioned this issue in commit 9774a5db of Elocity / Frontend / web / Cpms Portal : fix( ): stop Create Load Group save hang on station validation validateNonEmpty was calling trim() on station ID arrays, throwing before the API ran and leaving Save stuck loading. Guard string-only checks and harden save/API error handling.
- Comment on [HIEV-7440](https://elocity.atlassian.net/browse/HIEV-7440): Doc re-review — Request changes (narrow leftover) Re-checked Developer code Implementation flow of Customer Module v29 against cpms-portal after the 19 Aug update. Verdict: Much improved vs v21. Previous blockers (Refund files , Feedbacks dispatch, NewCustomer bulk, checklist endpoints, refund permissions, HIEV-7440, walletsRefresh.ts , CustomerInfo, getCustomers payload, typos) look addressed. Not ready to Approve yet because Refund contract is still wrong. Remaining must-fix §4.15 initiateRefu
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): Reviewed MR !790 (v4-NewExportFramework → v4-TempMay26Release): https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/790 Verdict: REQUEST CHANGES. Local Vitest passed (1570 tests). GitLab pipelines 67485 / 67469 failed — please re-run. Blocking: Download toast i18n keys missing in ko, kn, th, pt (only en, en-US, ar, fr updated) Export History success shows both DownloadToast (“Download Completed”) and LinearProgressWithLabel (“is being downloaded, please wait”) — conflicti
- Comment on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359): Sahil Siddiqui mentioned this issue in commit 2f167d4e of Elocity / Frontend / web / Cpms Portal on branch feature/HIEV-7359-unique-drivers-graph : Merge branch 'v4-TempMay26Release' of https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal into feature/HIEV-7359-unique-drivers-graph
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Sahil Siddiqui mentioned this issue in commit 7bd68811 of Elocity / Frontend / web / Cpms Portal : chore( ): second empty commit to verify GitLab–Jira link
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Sahil Siddiqui mentioned this issue in commit 9d1c4f59 of Elocity / Frontend / web / Cpms Portal on branch chore/HIEV-6785-gitlab-jira-push-test : chore( ): second empty commit to verify GitLab–Jira link
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Sahil Siddiqui mentioned this issue in commit 40e07a49 of Elocity / Frontend / web / Cpms Portal on branch chore/HIEV-6785-gitlab-jira-push-test : fix( ): install Node 22.14 in unit_tests for shell runners Shell executor ignores Docker image; pin a local Node so Vitest 4 can load ESM deps.
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Sahil Siddiqui mentioned this issue in commit 830d1d7d of Elocity / Frontend / web / Cpms Portal on branch chore/HIEV-6785-gitlab-jira-push-test : fix( ): drop apt-get from deploys; bootstrap AWS CLI locally Shell runners cannot apt-get; install Node 22.14 and AWS CLI into the job workspace instead.
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Sahil Siddiqui mentioned this issue in commit dc0fc0e0 of Elocity / Frontend / web / Cpms Portal on branch chore/HIEV-6785-gitlab-jira-push-test : chore( ): temporary AuthPage slogan "Test" for deploy smoke test Revert after deployment verification.
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Sahil Siddiqui mentioned this issue in commit f7c19d86 of Elocity / Frontend / web / Cpms Portal on branch chore/HIEV-6785-gitlab-jira-push-test : Revert "chore( ): temporary AuthPage slogan "Test" for deploy smoke test" This reverts commit dc0fc0e03f5d01d1d63aa71fc6e4bccdc31b4e86.
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Sahil Siddiqui mentioned this issue in merge request !794 of Elocity / Frontend / web / Cpms Portal on branch chore/HIEV-6785-gitlab-jira-push-test : fix( ): install Node 22.14 in unit_tests for shell runners
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Sahil Siddiqui mentioned this issue in commit eba9b212 of Elocity / Frontend / web / Cpms Portal on branch v4-TempMay26Release : Merge branch 'chore/HIEV-6785-gitlab-jira-push-test' into 'v4-TempMay26Release' Pipeline Fix and optimizations See merge request elocity1/frontend/web/cpms-portal!794
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Ad hoc – GitLab migration setup & documentation (1h) Time spent on preparing the Frontend migration from gitlab.com → gitlab.evnet.xyz : Set up / validated HTTPS + PAT push flow and related CI readiness checks Authored the Frontend migration/setup guide for cpms-portal and cpms-Mobile Published the Confluence page and prepared the team message for Frontend engineers Confluence: Frontend: Migrate from gitlab.com to gitlab.evnet.xyz (cpms-portal & cpms-Mobile)

**2026-08-25** — logged 0.7d (6h) of 1.0d (8h) available, 35 comments

- Worklog 10m on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558) (Bug, mid-sprint) — Code review for Utility Tariff MR !796 (shared across linked tickets)
- Worklog 10m on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558) (Bug, mid-sprint) — Re-review, CI follow-ups, and merge readiness for MR !796.
- Worklog 10m on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540) (Bug, mid-sprint) — Code review for Utility Tariff MR !796 (shared across linked tickets)
- Worklog 10m on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540) (Bug, mid-sprint) — Re-review, CI follow-ups, and merge readiness for MR !796.
- Worklog 10m on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538) (Bug, mid-sprint) — Code review for Utility Tariff MR !796 (shared across linked tickets)
- Worklog 10m on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538) (Bug, mid-sprint) — Re-review, CI follow-ups, and merge readiness for MR !796.
- Worklog 10m on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534) (Bug, mid-sprint) — Code review for Utility Tariff MR !796 (shared across linked tickets)
- Worklog 10m on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534) (Bug, mid-sprint) — Re-review, CI follow-ups, and merge readiness for MR !796.
- Worklog 10m on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533) (Bug, mid-sprint) — Code review for Utility Tariff MR !796 (shared across linked tickets)
- Worklog 10m on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533) (Bug, mid-sprint) — Re-review, CI follow-ups, and merge readiness for MR !796.
- Worklog 10m on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530) (Bug, mid-sprint) — Code review for Utility Tariff MR !796 (shared across linked tickets)
- Worklog 10m on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530) (Bug, mid-sprint) — Re-review, CI follow-ups, and merge readiness for MR !796.
- Worklog 2.00h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Worklog 0.42h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Worklog 1.00h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Worklog 0.23h on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) (Task, mid-sprint)
- Comment on [HIEV-7578](https://elocity.atlassian.net/browse/HIEV-7578): Yes, this is an agreed-upon approach in the product. Even our clients are trained for the same. We will keep this as it is for now until the product team (Dinesh/ ) ask for changes; any change to this will impact the whole product, since all these are abstracted logic used in many other pages, and it should be picked up as a separate task altogether in a new sprint. , this is agreed upon apporach and not a bug as of now of clearing the Stations if the location selection changes. If you want this
- Comment on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558): Sahil Siddiqui mentioned this issue in merge request !796 of Elocity / Frontend / web / Cpms Portal on branch v4-UtilityTariffFixes : fix(utility-tariff): resolve validations, view/edit active tab, and report chart rendering
- Comment on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558): Code review completed for MR !796 . Verdict: REQUEST CHANGES — full review logged on the MR. This ticket (HIEV-7558): Removed x.stacked = true and enabled zoom via openRevenueVsCost . Likely intentional for design match — please verify visually vs design after zoom out (Energy Cost series must remain visible). Broader MR blockers still apply (i18n, CI, global validation). Returning to To Do and assigning back to @Dharshini M.
- Comment on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558): Re-review completed for MR !796 . Verdict: APPROVE This ticket (HIEV-7558): Report chart rendering/tick spacing addressed via shared chart option opt-in. Pipeline green. Full notes on the MR.
- Comment on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558): MR !796 is approved and being merged to v4-TempMay26Release . Ready for testing once merge/deploy lands. Please verify Utility Tariff report chart rendering/tick spacing.
- Comment on [HIEV-7558](https://elocity.atlassian.net/browse/HIEV-7558): Deployed and ready for testing. Pipeline succeeded and the fix is live on Staging (merged via MR !796 to v4-TempMay26Release ). Please verify on staging.
- Comment on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540): Code review completed for MR !796 . Verdict: REQUEST CHANGES — full review logged on the MR. This ticket (HIEV-7540): Changes in shared DoubleBarChartOptions + Revenue vs Cost zoom wiring. Shared dual-axis config is used outside Utility Tariff — please scope or QA Dashboard dual-axis charts. Confirm axis labels/grid remain correct after zoom in/out. Returning to To Do and assigning back to @Dharshini M.
- Comment on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540): Re-review completed for MR !796 . Verdict: APPROVE This ticket (HIEV-7540): Dual-bar layout/zoom addressed (unstacked + ticksCount ). Pipeline green. Full notes on the MR.
- Comment on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540): MR !796 is approved and being merged to v4-TempMay26Release . Ready for testing once merge/deploy lands. Please verify Revenue vs Energy Cost dual-bar chart layout/zoom.
- Comment on [HIEV-7540](https://elocity.atlassian.net/browse/HIEV-7540): Deployed and ready for testing. Pipeline succeeded and the fix is live on Staging (merged via MR !796 to v4-TempMay26Release ). Please verify on staging.
- Comment on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538): Code review completed for MR !796 . Verdict: REQUEST CHANGES — full review logged on the MR. This ticket (HIEV-7538): Chart Y-axis changes ( beginAtZero , suggestedMax , ticks.count: 10 ) are in shared BarChartOptions , which also powers Dashboard Reporting charts. Please scope Utility Tariff overrides or explicitly QA Dashboard bar charts after zoom. Returning to To Do and assigning back to @Dharshini M.
- Comment on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538): Sahil Siddiqui mentioned this issue in merge request !796 of Elocity / Frontend / web / Cpms Portal on branch v4-UtilityTariffFixes : fix(utility-tariff): resolve validations, view/edit active tab, and report chart rendering
- Comment on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538): Re-review completed for MR !796 . Verdict: APPROVE This ticket (HIEV-7538): Chart axis/tick rendering addressed via optional ticksCount (Utility Reports opt-in; Dashboard unchanged). Pipeline green. Full notes on the MR.
- Comment on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538): MR !796 is approved and being merged to v4-TempMay26Release . Ready for testing once merge/deploy lands. Please verify Utility Tariff report chart axis/tick rendering.
- Comment on [HIEV-7538](https://elocity.atlassian.net/browse/HIEV-7538): Deployed and ready for testing. Pipeline succeeded and the fix is live on Staging (merged via MR !796 to v4-TempMay26Release ). Please verify on staging.
- Comment on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534): Sahil Siddiqui mentioned this issue in merge request !796 of Elocity / Frontend / web / Cpms Portal on branch v4-UtilityTariffFixes : fix(utility-tariff): resolve validations, view/edit active tab, and report chart rendering
- Comment on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534): Code review completed for MR !796 . Verdict: REQUEST CHANGES — full review logged on the MR. This ticket (HIEV-7534): getUtilityTariffActiveTab looks like a solid fix (defaultActiveType + TIERD alias + slot fallback). Please add unit tests for this helper. Broader MR blockers (missing locales, failed CI, global validator blast radius) still need fixing before merge. Returning to To Do and assigning back to @Dharshini M.
- Comment on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534): Re-review completed for MR !796 . Verdict: APPROVE This ticket (HIEV-7534): Addressed via getUtilityTariffActiveTab + normalizeActiveType with unit tests. Pipeline green. Full notes on the MR.
- Comment on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534): MR !796 is approved and being merged to v4-TempMay26Release . Ready for testing once merge/deploy lands. Please verify view/edit opens on the correct active tab (TOU vs Tiered).
- Comment on [HIEV-7534](https://elocity.atlassian.net/browse/HIEV-7534): Deployed and ready for testing. Pipeline succeeded and the fix is live on Staging (merged via MR !796 to v4-TempMay26Release ). Please verify on staging.
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): Code review completed for MR !796 . Verdict: REQUEST CHANGES — full review logged on the MR. This ticket (HIEV-7533): Price uses positive_include_zero (now max 10 chars); kWh Min/Max use new positive_include_zero_max_5 . Direction is good, but the 10-char cap was applied globally to all positive_include_zero consumers (Tariff Edit, taxes, schedules, etc.) — please scope to Utility Tariff fields only. Also: missing i18n for cannot exceed 5/30 characters in ko / kn / th / pt , and CI is red. Retur
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): Sahil Siddiqui mentioned this issue in merge request !796 of Elocity / Frontend / web / Cpms Portal on branch v4-UtilityTariffFixes : fix(utility-tariff): resolve validations, view/edit active tab, and report chart rendering
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): Re-review completed for MR !796 . Verdict: APPROVE This ticket (HIEV-7533): Addressed via scoped validators ( positive_include_zero_max_5 for kWh, _max_10 for Price). Pipeline green. Full notes on the MR.
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): MR !796 is approved and being merged to v4-TempMay26Release . Ready for testing once merge/deploy lands. Please verify Tiered kWh (≤5) and Price (≤10) validation.
- Comment on [HIEV-7533](https://elocity.atlassian.net/browse/HIEV-7533): Deployed and ready for testing. Pipeline succeeded and the fix is live on Staging (merged via MR !796 to v4-TempMay26Release ). Please verify on staging.
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): Sahil Siddiqui mentioned this issue in merge request !796 of Elocity / Frontend / web / Cpms Portal on branch v4-UtilityTariffFixes : fix(utility-tariff): resolve validations, view/edit active tab, and report chart rendering
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): Code review completed for MR !796 . Verdict: REQUEST CHANGES — full review logged on the MR. This ticket (HIEV-7530): Partially addressed. Tariff Name error copy improved ( cannot exceed 30 characters ), TOU Price length capped via shared positive_include_zero (10 chars). Still missing: prevent typing past 30 / helper text “Maximum 30 characters”. Please address before re-review: Add i18n keys to all 8 locales ( ko , kn , th , pt missing) Fix failed CI pipeline Avoid global change to positive / 
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): Re-review completed for MR !796 . Verdict: APPROVE This ticket (HIEV-7530): Addressed. TOU Price capped via positive_include_zero_max_10 ; Tariff Name shows clearer “cannot exceed 30 characters” with live validation ( duplicateFieldValidation ). Optional follow-up: hard maxLength / helper text. Prior blockers (i18n, scoped validators, CI, chart opt-in, unit tests) are resolved. Pipeline 68140 green. Full notes on the MR.
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): MR !796 is approved and being merged to v4-TempMay26Release . Ready for testing on staging once the merge/deploy lands. Code review complete — please verify Tariff Name (30-char messaging/live validation) and TOU Price (max 10 chars).
- Comment on [HIEV-7530](https://elocity.atlassian.net/browse/HIEV-7530): Deployed and ready for testing. Pipeline succeeded and the fix is live on Staging (merged via MR !796 to v4-TempMay26Release ). Please verify on staging.
- Comment on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359): I need the Backend Api’s to be made available on Dev or Staging for Integration Test. Have informed , to make it available. cc:
- Comment on [HIEV-7348](https://elocity.atlassian.net/browse/HIEV-7348): Ticket currently blocked by the Backend team’s ticket. Need the contract, or at least a Confluence doc or any doc to make changes. This ticket has not started yet from the Frontend side, since we do not have anything to start with. Have informed the Backend Dev regarding the same. They are working on it to get it merged. cc: ,
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): Pipeline / S3 UI hosts (25 Aug 2026) — 2h logged Moved deploys off GitLab Pages → S3 static website hosting (cpms-portal AWS keys) Manual jobs on main : stg_deploy (live), demo_deploy (fixtures), aionev_deploy (fixtures + AIONEV brand) UI URLs: http://evlm-stg.evnet.xyz.s3-website-us-east-1.amazonaws.com http://evlm-demo.evnet.xyz.s3-website-us-east-1.amazonaws.com http://evlm-aionev-portal.evnet.xyz.s3-website-us-east-1.amazonaws.com Still open: CloudFront / custom HTTPS, UAT/prod jobs, Azure c
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): Product decisions shipped (FE) Dispute Incentive — removed button from DR event detail Customers Bulk Upload — hidden Forecasts / Audit — hidden on live/stg ( IS_LIVE_BUILD ); kept on demo + aionev Confluence Decision column marked Done for these three.
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Pending Design Discussions with Marish and Dinesh for EVLm Web

**2026-08-27** — logged 1.4d (11h) of 1.0d (8h) available, 23 comments

- Worklog 2h on [HIEV-7599](https://elocity.atlassian.net/browse/HIEV-7599) (Sub-task, mid-sprint) — Code review MR !788 — Station Management + Load Management fixes
- Worklog 30m on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546) (Bug, mid-sprint) — Code review, merge MR !797, cherry-pick to v4-MainBranch
- Worklog 30m on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492) (Bug, mid-sprint) — Re-review after conflict fix; mergeability check; approved and merged MR !795.
- Worklog 30m on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364) (Task, planned) — Re-reviewed MR !790 after fixes; verified prior findings resolved and approved.
- Worklog 1h on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359) (Task, planned) — FE: Unique Drivers overview card stacked unique_drivers_v2 visualization, colors, unit tests, MR ready.
- Worklog 6h on [HIEV-7348](https://elocity.atlassian.net/browse/HIEV-7348) (Task, planned) — FE: Encrypted Bearer JWT Phase 1 — secureTransport + axios encrypt/KID_UNKNOWN retry + tests
- Worklog 5m on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326) (Bug, mid-sprint)
- Worklog 0.50h on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785) (Task, mid-sprint)
- Comment on [HIEV-7599](https://elocity.atlassian.net/browse/HIEV-7599): Sahil Siddiqui mentioned this issue in merge request !788 of Elocity / Frontend / web / Cpms Portal on branch fixes/august : Station Management enhancement + Load Management fixes
- Comment on [HIEV-7599](https://elocity.atlassian.net/browse/HIEV-7599): Completed code review for MR !788 . Verdict: REQUEST CHANGES (Risk: HIGH) Blocking: Missing i18n keys cannot exceed / characters in ko, kn, th, pt for AddressAutocomplete max-length message. Also noted: incomplete optional chaining on deviation.unit in ChargerDetailsDrawer; ListCard vs Overview load-zone threshold mismatch; missing tests for some new behaviors. Review posted on the MR.
- Comment on [HIEV-7599](https://elocity.atlassian.net/browse/HIEV-7599): Deep-review follow-up (not yet on GitLab note): Additional High: mobile ChargerDetailsDrawer renderMobileBody can call renderDetailFields(null) when socket data exists but HTTP connectorDetails is null — use connectorDetails ?? socketConnectorDetails . Also confirm maintenanceSlots API replace vs append semantics before merge.
- Comment on [HIEV-7599](https://elocity.atlassian.net/browse/HIEV-7599): Sahil Siddiqui mentioned this issue in commit aee04167 of Elocity / Frontend / web / Cpms Portal on branch fixes/august : fix( ): unblock MR 788 CI and AddressAutocomplete i18n Fix BusinessDatagrid tablet export test mock, add missing cannot exceed/characters keys for ko/kn/th/pt, and harden deviation optional chaining.
- Comment on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546): Reviewed MR !797: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/797 Verdict: APPROVE Shows “Starting charging session…” when minWalletBalanceNeeded is 0; otherwise keeps “Processing payment...”. Tests pass; prior CI green. Please QA on UAT with a zero min-wallet guest station to confirm the API field is present as minWalletBalanceNeeded . Full notes on the MR.
- Comment on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546): Sahil Siddiqui mentioned this issue in merge request !797 of Elocity / Frontend / web / Cpms Portal on branch v4-GuestCharhingDetails : Added a new loader message when the min wallet balance is zero
- Comment on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546): Sahil Siddiqui mentioned this issue in commit c8172bb4 of Elocity / Frontend / web / Cpms Portal : fix( ): show starting session loader when min wallet balance is zero
- Comment on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546): Sahil Siddiqui mentioned this issue in commit c3d25591 of Elocity / Frontend / web / Cpms Portal on branch v4-MainBranch : fix( ): show starting session loader when min wallet balance is zero
- Comment on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546): Merged MR !797 into v4-TempMay26Release and cherry-picked onto v4-MainBranch ( c3d255911 — fix(HIEV-7546): show starting session loader when min wallet balance is zero). Logged 30m for review + merge + cherry-pick.
- Comment on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546): Available to test on UAT
- Comment on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492): Conflict re-check on MR !795: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/795 Merge conflicts with v4-TempMay26Release are resolved — MR is mergeable again. Verdict updated: APPROVE (prior code findings remain fixed; confirm pipeline 68253 goes green before merge).
- Comment on [HIEV-7492](https://elocity.atlassian.net/browse/HIEV-7492): FE MR merged: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/795 ( v4-EmployeeIDField → v4-TempMay26Release ) Moving to Ready for Testing.
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): Re-reviewed MR !790 after fixes: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/790 Verdict: APPROVE — prior blocking findings are resolved (i18n all 8 locales, single toast UX, error toast no auto-hide, retry CTA, dependency direction, tests). CI pipeline green. Details posted on the MR.
- Comment on [HIEV-7364](https://elocity.atlassian.net/browse/HIEV-7364): Available for test on Staging
- Comment on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359): Sahil Siddiqui mentioned this issue in commit b4edccc7 of Elocity / Frontend / web / Cpms Portal on branch feature/HIEV-7359-unique-drivers-graph : Merge branch 'v4-TempMay26Release' of https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal into feature/HIEV-7359-unique-drivers-graph
- Comment on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359): Sahil Siddiqui mentioned this issue in commit 6a0303b5 of Elocity / Frontend / web / Cpms Portal on branch feature/HIEV-7359-unique-drivers-graph : feat( ): stack Unique Drivers overview card for unique_drivers_v2 Render first-time vs returning drivers as stacked bars with Utilization pie colors, and point the card at unique_drivers_v2.
- Comment on [HIEV-7359](https://elocity.atlassian.net/browse/HIEV-7359): FE complete — Unique Drivers overview card (final) Integration tests finished. MR ready to merge: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/787 What changed Overview card calls unique_drivers_v2 Stacked bars: first-time (teal) + returning (peach), Utilization pie colors Header: totalUniqueDrivers ; tooltips include total active drivers Unit coverage for stacked chart data mapper Logged 1h on this ticket.
- Comment on [HIEV-7348](https://elocity.atlassian.net/browse/HIEV-7348): FE progress — Encrypted Bearer JWT (Phase 1) Implemented frontend work against the Encrypted Bearer JWT API Contract . Done secureTransport.ts — Web Crypto handshake (RSA-OAEP wrap) + AES-GCM JWT encrypt, single-flight ensureReady / recoverSecureTransport cryptoHandshake.ts — AMS GET /crypto/handshake + POST /crypto/session (no Bearer interceptors) ams_axios.ts — encrypt Bearer after attach; headers x-enc: 1 + x-kid ; silent re-handshake + one retry on KID_UNKNOWN ; skip /crypto/* Session cleanu
- Comment on [HIEV-7348](https://elocity.atlassian.net/browse/HIEV-7348): FE implementation documentation published under CPMS Web App (CSMS): ➡️ Encrypted Bearer JWT — FE Implementation (cpms-portal) (HIEV-7348) Also linked from the CPMS Web App index. Architecture guide remains: HIEV-6699 Implementation Guide .
- Comment on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326): Correction: Hold on merge / Ready for Testing. The FE MR linked here needs confirmation first — see next comment.
- Comment on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326): — MR mismatch / title issue on this ticket. You linked MR !798 here for HIEV-7326 (Activity Logs Description column). But the MR title is about E-Wallet Event Type filter options (Session Refund / Wallet Refund / Session Debit / Wallet Credit), while the branch is v4-ActivityLogs and the diff includes both : Activity Logs Description column (this ticket) Unrelated E-Wallet filter options Please confirm: Is !798 the correct FE MR for HIEV-7326? If yes, please update the MR title/description to me
- Comment on [HIEV-6785](https://elocity.atlassian.net/browse/HIEV-6785): Update (30m logged): Staging login reCAPTCHA for API automation Investigated how CPMS Web App login uses Google reCAPTCHA v2 Invisible and what that means for QA API automation on Staging. Findings POST /auth/user/login requires header recaptchaToken Token is generated by Google’s browser SDK ( grecaptcha.execute / executeAsync ), not by any CPMS/AMS API disable2FA only skips email OTP — it does not disable reCAPTCHA Pure Postman/API scripts cannot mint a valid token Recommended approach Playwri
- Comment on [HIEV-7357](https://elocity.atlassian.net/browse/HIEV-7357): WebApp FE complete (HIEV-7359) Integration tests finished. MR ready to merge: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/787 Overview Unique Drivers card now uses unique_drivers_v2 with stacked first-time / returning visualization (Utilization pie colors).

**2026-08-31** — logged 1.5d (12h) of 1.0d (8h) available, 8 comments

- Worklog 2h on [HIEV-7615](https://elocity.atlassian.net/browse/HIEV-7615) (Sub-task, mid-sprint) — Built August 2026 sprint retrospective: Jira actuals vs sheet, leave-adjusted expected hours, bugs worked, Teams scrum attendance, person view, CSV export. Published at https://funnybonesware.github.io/august-26-sprint-retro/
- Worklog 1h on [HIEV-7607](https://elocity.atlassian.net/browse/HIEV-7607) (Sub-task, mid-sprint) — MR !800 review and unit test fix for Load Management. Review:  Full code review of connector icon changes, ConnectorConfig aliases, delete redirect, time interval validation, and Load Summary column updates. Posted review on GitLab with REQUEST CHANGES due to failing  useLoadGroupData  tests. Fix:  Updated  vitest/pages/LoadManagement/LoadGroupInfo/useLoadGroupData.test.ts  to mock shared  validateTimeInterval  and assert  { textVal1, textVal2 }  payload. Commit  03bbd67d3  pushed; MR merged as  c23394d8 .
- Worklog 20m on [HIEV-7420](https://elocity.atlassian.net/browse/HIEV-7420) (Bug, mid-sprint) — Updated Created Time Slots to show start and end date/time, aligned calendar icons, and added missing locale keys. Pushed  1bb04f753  to v4-TempMay26Release.
- Worklog 20m on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326) (Bug, mid-sprint) — review and Merge
- Worklog 8.00h on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941) (Task, planned)
- Comment on [HIEV-7607](https://elocity.atlassian.net/browse/HIEV-7607): Completed MR !800 review and blocking unit test fix. Reviewed 11 files across Load Management, ConnectorStatus, and validation utilities Blocking finding: useLoadGroupData.test.ts missing validateTimeInterval mock after refactor to shared validator Fixed test mock + updated validator assertions; all LoadGroupInfo tests passing (99/99) Pushed 03bbd67d3 , merged MR !800 into v4-TempMay26Release GitLab: https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/800
- Comment on [HIEV-7420](https://elocity.atlassian.net/browse/HIEV-7420): Sahil Siddiqui mentioned this issue in commit 1bb04f75 of Elocity / Frontend / web / Cpms Portal : fix( ): show maintenance slot start and end date/time Created Time Slots now display both start and end datetimes so multi-day windows are readable, with matching calendar icons and missing locale keys.
- Comment on [HIEV-7420](https://elocity.atlassian.net/browse/HIEV-7420): Fix pushed to v4-TempMay26Release . Commit: 1bb04f753 — fix(HIEV-7420): show maintenance slot start and end date/time What changed Created Time Slots cards now show Start Date/Time and End Date/Time (API already returns endTs ; UI was only rendering the start date). Both rows use the calendar icon so start/end look consistent. Filled missing Start Date/Time / End Date/Time keys in kn, ko, and pt locales. Multi-day maintenance windows now display the full date range instead of only the start date
- Comment on [HIEV-7420](https://elocity.atlassian.net/browse/HIEV-7420): Available for Testing . It can be tested now on Stage and UAT.
- Comment on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326): THis ticket was for this MR → https://gitlab.evnet.xyz/elocity1/frontend/web/cpms-portal/-/merge_requests/798 . It is merged and deployed to UAT and Staging
- Comment on [HIEV-7321](https://elocity.atlassian.net/browse/HIEV-7321): Sahil Siddiqui mentioned this issue in commit ceb2e521 of Elocity / Frontend / web / Cpms Portal : fix( ): add client-side max validation for Minimum Balance Enforce max value of 100000000 and 9-digit input limit so oversized numeric input is rejected inline instead of only failing on save.
- Comment on [HIEV-7090](https://elocity.atlassian.net/browse/HIEV-7090): Sahil Siddiqui mentioned this issue in commit f543b1b4 of Elocity / Frontend / web / Cpms Portal : fix( ): align Alerts date picker Apply with other grids Remove applyOnSelection=false so draft filters update on selection like other pages, enabling Apply after Last Year and other presets.
- Comment on [HIEV-6941](https://elocity.atlassian.net/browse/HIEV-6941): 31 Aug 2026 — EVLM portal (ops UI + status) Shipped Figma Changes screens and updated the go-live status page. Portal (pushed to main : 09e2e14 ) /profile — My Profile (session name/email; AMS change-password live; extra fields hardcoded until BE APIs exist) /help — FAQ & Support (client-only, no API) /admin/users list / create / detail — never show SU ; export off (no client CSV); delete is fixture-only (no DELETE API) Header bell inbox dropdown (hardcoded items; mark-read local) Nav: User Mana

### Shambu — 13.1 of 19.0d (105h of 152h)

**2026-08-02** — logged 0.8d (6h) of 0.0d (0h) available, 0 comments

- Worklog 6h on [HIEV-7340](https://elocity.atlassian.net/browse/HIEV-7340) (Task, mid-sprint)

**2026-08-03** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 4h on [HIEV-7216](https://elocity.atlassian.net/browse/HIEV-7216) (Bug, mid-sprint)
- Worklog 3h on [HIEV-7121](https://elocity.atlassian.net/browse/HIEV-7121) (Bug, mid-sprint)
- Comment on [HIEV-7216](https://elocity.atlassian.net/browse/HIEV-7216): resolved review comments

**2026-08-04** — logged 0.8d (6h) of 1.0d (8h) available, 3 comments

- Worklog 3h on [HIEV-7121](https://elocity.atlassian.net/browse/HIEV-7121) (Bug, mid-sprint)
- Worklog 30m on [HIEV-6988](https://elocity.atlassian.net/browse/HIEV-6988) (Task, planned)
- Worklog 3h on [HIEV-6607](https://elocity.atlassian.net/browse/HIEV-6607) (Bug, mid-sprint)
- Comment on [HIEV-7121](https://elocity.atlassian.net/browse/HIEV-7121): The issue was creating a mocked request context. We didn't clear the DB connection after request-scoped export jobs ran, so we now manually clear connections when a job finishes (success or failure).
- Comment on [HIEV-6988](https://elocity.atlassian.net/browse/HIEV-6988): done
- Comment on [HIEV-6607](https://elocity.atlassian.net/browse/HIEV-6607): understood the code, need to debug further

**2026-08-05** — logged 0.9d (8h) of 1.0d (8h) available, 5 comments

- Worklog 3h on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347) (Task, planned)
- Worklog 30m on [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275) (Bug, mid-sprint)
- Worklog 4h on [HIEV-6607](https://elocity.atlassian.net/browse/HIEV-6607) (Bug, mid-sprint)
- Comment on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347): went through documentation
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): done MR :
- Comment on [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275): https://gitlab.com/elocity1/backend/cpms/-/merge_requests/1018
- Comment on [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275): replaced query builder with typeorm find() in getLocationsForMaps
- Comment on [HIEV-6607](https://elocity.atlassian.net/browse/HIEV-6607): DISABLE_JOB was set to true in secrets, which stopped the cron jobs that send push notifications. I toggled it to false, and now it works.

**2026-08-06** — logged 1.2d (10h) of 1.0d (8h) available, 0 comments

- Worklog 2h on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347) (Task, planned)
- Worklog 1d on [HIEV-7172](https://elocity.atlassian.net/browse/HIEV-7172) (Bug, mid-sprint)

**2026-08-07** — logged 0.4d (3h) of 1.0d (8h) available, 1 comments

- Worklog 3h on [HIEV-7172](https://elocity.atlassian.net/browse/HIEV-7172) (Bug, mid-sprint)
- Comment on [HIEV-7172](https://elocity.atlassian.net/browse/HIEV-7172): My earlier speculation was wrong. It works locally and I can't reproduce the issue. It may be a network problem. I will debug further if it recurs.

**2026-08-10** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 1d on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347) (Task, planned)
- Comment on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347): continued with the requirements documentation
- Comment on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347): generated implementation plan containing changes in ams

**2026-08-11** — logged 1.0d (8h) of 1.0d (8h) available, 0 comments

- Worklog 1d on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347) (Task, planned)

**2026-08-12** — logged 0.1d (1h) of 1.0d (8h) available, 2 comments

- Worklog 1h on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347) (Task, planned)
- Comment on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347): made initial changes in gateway-preauth and api-gateway
- Comment on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347): worked on review comments

**2026-08-13** — logged 0.6d (5h) of 1.0d (8h) available, 4 comments

- Worklog 2h on [HIEV-7495](https://elocity.atlassian.net/browse/HIEV-7495) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7490](https://elocity.atlassian.net/browse/HIEV-7490) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7488](https://elocity.atlassian.net/browse/HIEV-7488) (Bug, mid-sprint)
- Comment on [HIEV-7490](https://elocity.atlassian.net/browse/HIEV-7490): RFID lookups filter customers by is_active: true , and a blocked card is excluded from that customer's returned rfids list even though the customer account itself is active — so the backend can't resolve the card to a customer and treats it as "not found." That null result then gets used to fetch a customerId without a null check, which is what throws the raw 500 instead of a proper error. Need to discuss more about the fix
- Comment on [HIEV-7488](https://elocity.atlassian.net/browse/HIEV-7488): fix: reconstruct evsesMetadataMap from serialized form in processExportJob BullMQ flattens evsesMetadataMap to an array before storing in Redis. Reconstruct it back to a Map in processExportJob so CSV builders receive proper Map semantics, not array iteration semantics. This fixes trailing junk rows (array indices + "N/A") appearing at the end of all async CSV exports (energy-used, availability, faults, outages, etc). MR link: https://gitlab.com/elocity1/backend/analytics/-/merge_requests/135
- Comment on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291): Changes were done, MR is not merged yet
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): accidently added wrong MR link, the issue was fixed in other MR linked below MR:

**2026-08-17** — logged 1.1d (9h) of 1.0d (8h) available, 7 comments

- Worklog 4h on [HIEV-7491](https://elocity.atlassian.net/browse/HIEV-7491) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7490](https://elocity.atlassian.net/browse/HIEV-7490) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7487](https://elocity.atlassian.net/browse/HIEV-7487) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282) (Bug, mid-sprint)
- Comment on [HIEV-7491](https://elocity.atlassian.net/browse/HIEV-7491): the reason for this bug is same as MR:
- Comment on [HIEV-7490](https://elocity.atlassian.net/browse/HIEV-7490): fixed, the function that looks up the customer checks specifically for this blocked-card case and can report it clearly. As a result, remote-start-transaction now returns a proper "RFID is blocked" error instead of a 500 crash MR: https://gitlab.com/elocity1/backend/cpms/-/merge_requests/1029
- Comment on [HIEV-7487](https://elocity.atlassian.net/browse/HIEV-7487): made the timestamp user friendly MR:
- Comment on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291): done
- Comment on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291): everything is fixed, pod wasnt restarted, so changes were not reflected yet, now restarted.
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): done
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): pod was not restarted, changes were not reflected at the time of testing, now they are available

**2026-08-18** — logged 0.3d (2h) of 1.0d (8h) available, 1 comments

- Worklog 2h on [HIEV-7526](https://elocity.atlassian.net/browse/HIEV-7526) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7495](https://elocity.atlassian.net/browse/HIEV-7495) (Bug, mid-sprint)
- Comment on [HIEV-7495](https://elocity.atlassian.net/browse/HIEV-7495): added a check for commissioned date in pre session validation logic MR:

**2026-08-19** — logged 0.9d (8h) of 1.0d (8h) available, 3 comments

- Worklog 2h on [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7526](https://elocity.atlassian.net/browse/HIEV-7526) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7502](https://elocity.atlassian.net/browse/HIEV-7502) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7499](https://elocity.atlassian.net/browse/HIEV-7499) (Bug, mid-sprint)
- Comment on [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539): Added a database lock when updating the overall job status so simultaneous station completions no longer overwrite each other, fixing the job status getting stuck at "In Progress" even after all stations finished.
- Comment on [HIEV-7502](https://elocity.atlassian.net/browse/HIEV-7502): Added a database lock when updating the overall job status so simultaneous station completions no longer overwrite each other, fixing the job status getting stuck at "In Progress" even after all stations finished.
- Comment on [HIEV-7499](https://elocity.atlassian.net/browse/HIEV-7499): Added a database lock when updating the overall job status so simultaneous station completions no longer overwrite each other, fixing the job status getting stuck at "In Progress" even after all stations finished.

**2026-08-20** — logged 0.1d (0h) of 1.0d (8h) available, 1 comments

- Worklog 30m on [HIEV-7559](https://elocity.atlassian.net/browse/HIEV-7559) (Bug, mid-sprint)
- Comment on [HIEV-7559](https://elocity.atlassian.net/browse/HIEV-7559): configured correct stripe keys

**2026-08-21** — logged 0.2d (2h) of 1.0d (8h) available, 5 comments

- Worklog 2h on [HIEV-7560](https://elocity.atlassian.net/browse/HIEV-7560) (Bug, mid-sprint)
- Comment on [HIEV-7560](https://elocity.atlassian.net/browse/HIEV-7560): went through possible solutions, need to discuss further
- Comment on [HIEV-7560](https://elocity.atlassian.net/browse/HIEV-7560): It’s working now. The problem was a separate bug that showed a decommissioned charger, that bug has been fixed, so this issue won’t recur.
- Comment on [HIEV-7539](https://elocity.atlassian.net/browse/HIEV-7539): Job-State Synchronization Issue the job status gets updated as soon as we send message to the charger saying it should start uploading the diagnostic file, each station’s state only gets updated when we receive response from the charger, so in lower environements when stations are offline, we do no receive response and this scenario occurs, if we somehow keep job status in sync with station’s status, in this case, the job status will change back to pending state and the recovery job picks this j
- Comment on [HIEV-7502](https://elocity.atlassian.net/browse/HIEV-7502): The state remains inProgress in lower environments because we do not connect to real physical chargers that respond and lead to change in the status
- Comment on [HIEV-7499](https://elocity.atlassian.net/browse/HIEV-7499): Job-state synchronization issue We update the job status as soon as we send the message to the charger for the firmware update. Each station’s state updates only when we receive a response from the charger. In lower environments where stations are offline, we receive no response and this mismatch occurs. If we keep the job status in sync with the station’s status, the job status will revert to pending. The recovery job then picks it up and we resend the message to the charger, which is redundant

**2026-08-25** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 1d on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347) (Task, planned)
- Comment on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347): had some discussions and made necessary changes and will test it in dev today

**2026-08-26** — logged 0.7d (6h) of 1.0d (8h) available, 0 comments

- Worklog 30m on [HIEV-7590](https://elocity.atlassian.net/browse/HIEV-7590) (Bug, mid-sprint)
- Worklog 5h on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347) (Task, planned)

**2026-08-27** — logged 0.0d (0h) of 1.0d (8h) available, 1 comments

- Comment on [HIEV-7590](https://elocity.atlassian.net/browse/HIEV-7590): there was no record in settings repository for this business, i added one and it works fine now

**2026-08-31** — logged 1.0d (8h) of 1.0d (8h) available, 4 comments

- Worklog 2h on [HIEV-7614](https://elocity.atlassian.net/browse/HIEV-7614) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7597](https://elocity.atlassian.net/browse/HIEV-7597) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7597](https://elocity.atlassian.net/browse/HIEV-7597) (Bug, mid-sprint)
- Comment on [HIEV-7614](https://elocity.atlassian.net/browse/HIEV-7614): this was due to report subscription of a particular user (246) consisting of 4 report types, need to find the exact cause.
- Comment on [HIEV-7597](https://elocity.atlassian.net/browse/HIEV-7597): created implementation plan
- Comment on [HIEV-7597](https://elocity.atlassian.net/browse/HIEV-7597): made necessary changes, need to discuss further and choose the right approach.
- Comment on [HIEV-7347](https://elocity.atlassian.net/browse/HIEV-7347): deployed in dev

### Srikant — 11.9 of 17.0d (95h of 136h)

**2026-08-03** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 6h on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238) (Task, mid-sprint) — Configured gitlab-backup and DR plan
- Comment on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238): Image registry using object storage.
- Comment on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722): Audit report of all env with the root container access.

**2026-08-04** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238) (Task, mid-sprint) — DR Testing — Instance Replaced, Volumes Intact (Path A)/Volumes Lost, Restore from Bronze Backup (Path B)
- Comment on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238): Configured gitlab-backup to upload nightly directly to OCI Object Storage , 30-day retention. Verified with a real manual run — 1.71GB archive uploaded and confirmed present in the bucket. Built a separate encrypted backup for gitlab.rb + gitlab-secrets.json (not covered by GitLab's own backup tool), uploaded daily via GitLab's bundled fog-aws, AES-256 encrypted. Verified with a full round-trip: downloaded, decrypted, confirmed byte-identical to the live files. Applied a 30-day object lifecycle 

**2026-08-05** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238) (Task, mid-sprint) — DR Restore- Complete failure
- Comment on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238): DR Testing — Instance Replaced, Volumes Intact (Path A) Confirm/simulate instance loss Detach boot + data volume attachments from old instance Launch new instance in same AD/subnet/NSG, booting from the existing boot volume (not a fresh image) Attach existing data volume, confirm it mounts at /var/opt/gitlab Reattach Reserved Public IP to new instance gitlab-ctl start — no restore needed, should come up as-is(verified) Ran verification checklist (services, health check, login, git push, registry

**2026-08-06** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 4h on [HIEV-7429](https://elocity.atlassian.net/browse/HIEV-7429) (Sub-task, mid-sprint) — doc review and MR review
- Worklog 1h on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238) (Task, mid-sprint) — meeting and internal discussion
- Worklog 3h on [HIEV-6925](https://elocity.atlassian.net/browse/HIEV-6925) (Task, planned) — review of existing lgtm deployment
- Comment on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238): DR Restore Drills Ran all three disaster-recovery paths against throwaway OCI instances/volumes — no simulation, real production secrets/backups, all drill resources terminated afterward. Production was never down. Path C (full rebuild from object storage) — GitLab itself restored correctly (verified health checks, real git clone with commit history, login). Found a critical gap: the container registry's repository/tag metadata lives in a separate local Postgres database that gitlab-backup never

**2026-08-07** — logged 1.2d (10h) of 1.0d (8h) available, 3 comments

- Worklog 2h on [HIEV-7441](https://elocity.atlassian.net/browse/HIEV-7441) (Sub-task, planned) — Infr Doc review of lower-env
- Worklog 2h on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238) (Task, mid-sprint) — Reviewed few user access and identity management use cases
- Worklog 6h on [HIEV-6925](https://elocity.atlassian.net/browse/HIEV-6925) (Task, planned) — Worked on lower-env setup and updating with new APM implementation.
- Comment on [HIEV-7429](https://elocity.atlassian.net/browse/HIEV-7429): MR review of and infra Doc review and discussion of flow
- Comment on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238): Briefed a meeting on the implementation and internal discussion
- Comment on [HIEV-6925](https://elocity.atlassian.net/browse/HIEV-6925): Reviewed implementation of LGTM

**2026-08-10** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 2h on [HIEV-7441](https://elocity.atlassian.net/browse/HIEV-7441) (Sub-task, planned) — Infra doc review
- Worklog 4h on [HIEV-6925](https://elocity.atlassian.net/browse/HIEV-6925) (Task, planned) — helm implementation and teams workflow design.
- Comment on [HIEV-7441](https://elocity.atlassian.net/browse/HIEV-7441): Infr Doc review of lower-env
- Comment on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238): Reviewed few user access and identity management use cases

**2026-08-11** — logged 0.7d (6h) of 1.0d (8h) available, 2 comments

- Worklog 1h on [HIEV-7473](https://elocity.atlassian.net/browse/HIEV-7473) (Sub-task, mid-sprint) — Reviewing and reading of deployment and api gateway deployment doc
- Worklog 1h on [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395) (Sub-task, planned) — Doc review
- Worklog 1h on [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394) (Sub-task, planned) — Doc Review
- Worklog 2h on [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393) (Sub-task, planned) — Doc review
- Worklog 30m on [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372) (Task, planned) — reviewing KT items.
- Comment on [HIEV-7441](https://elocity.atlassian.net/browse/HIEV-7441): Infra Doc review of lower-env
- Comment on [HIEV-6925](https://elocity.atlassian.net/browse/HIEV-6925): Updated the helm charts and images related to common dashboard and worked on the MS teams workflow for alerts.

**2026-08-12** — logged 0.8d (6h) of 1.0d (8h) available, 5 comments

- Worklog 3h on [HIEV-7484](https://elocity.atlassian.net/browse/HIEV-7484) (Sub-task, mid-sprint) — Implementation discussion of OCI onboarding using entraID
- Worklog 1h on [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395) (Sub-task, planned)
- Worklog 1h on [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394) (Sub-task, planned)
- Worklog 1h on [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393) (Sub-task, planned)
- Comment on [HIEV-7473](https://elocity.atlassian.net/browse/HIEV-7473): Reviewing and reading of deployment and api gateway deployment doc
- Comment on [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395): Doc review Document Link:-
- Comment on [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394): Doc Review of Document Link:-
- Comment on [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393): Document review link -
- Comment on [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372): Review and reading of KT items.

**2026-08-13** — logged 0.0d (0h) of 0.0d (0h) available, 4 comments

- Comment on [HIEV-7484](https://elocity.atlassian.net/browse/HIEV-7484): Implementation discussion of OCI onboarding using entraID
- Comment on [HIEV-7395](https://elocity.atlassian.net/browse/HIEV-7395): doc review completed
- Comment on [HIEV-7394](https://elocity.atlassian.net/browse/HIEV-7394): doc review done
- Comment on [HIEV-7393](https://elocity.atlassian.net/browse/HIEV-7393): Doc Review complete

**2026-08-17** — logged 0.5d (4h) of 1.0d (8h) available, 0 comments

- Worklog 4h on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238) (Task, mid-sprint)

**2026-08-18** — logged 0.0d (0h) of 1.0d (8h) available, 1 comments

- Comment on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238): configured email and tested few placeholders

**2026-08-20** — logged 1.0d (8h) of 1.0d (8h) available, 0 comments

- Worklog 5h on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238) (Task, mid-sprint)
- Worklog 3h on [HIEV-6925](https://elocity.atlassian.net/browse/HIEV-6925) (Task, planned)

**2026-08-21** — logged 1.2d (10h) of 1.0d (8h) available, 2 comments

- Worklog 1d 2h on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238) (Task, mid-sprint)
- Comment on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238): Worked on user creation and cleanup plan for new migration.
- Comment on [HIEV-6925](https://elocity.atlassian.net/browse/HIEV-6925): Tested and fixed teams flow in lower

**2026-08-24** — logged 0.6d (5h) of 1.0d (8h) available, 1 comments

- Worklog 2h on [HIEV-7508](https://elocity.atlassian.net/browse/HIEV-7508) (Sub-task, planned)
- Worklog 2h on [HIEV-7507](https://elocity.atlassian.net/browse/HIEV-7507) (Sub-task, planned)
- Worklog 1h on [HIEV-7371](https://elocity.atlassian.net/browse/HIEV-7371) (Task, planned)
- Comment on [HIEV-7238](https://elocity.atlassian.net/browse/HIEV-7238): Migration of gitlab from seas to self managed completed

**2026-08-25** — logged 0.6d (5h) of 1.0d (8h) available, 0 comments

- Worklog 5h on [HIEV-7587](https://elocity.atlassian.net/browse/HIEV-7587) (Sub-task, mid-sprint)

**2026-08-26** — logged 0.6d (5h) of 1.0d (8h) available, 2 comments

- Worklog 5h on [HIEV-7606](https://elocity.atlassian.net/browse/HIEV-7606) (Sub-task, mid-sprint)
- Comment on [HIEV-7587](https://elocity.atlassian.net/browse/HIEV-7587): updated k8s helm repo and updated argued application URL and synced them with new target in lower env
- Comment on [HIEV-7371](https://elocity.atlassian.net/browse/HIEV-7371): Review complete

**2026-08-31** — logged 0.6d (4h) of 1.0d (8h) available, 1 comments

- Worklog 3h on [HIEV-7606](https://elocity.atlassian.net/browse/HIEV-7606) (Sub-task, mid-sprint)
- Worklog 30m on [HIEV-7372](https://elocity.atlassian.net/browse/HIEV-7372) (Task, planned)
- Worklog 1h on [HIEV-6722](https://elocity.atlassian.net/browse/HIEV-6722) (Task, mid-sprint)
- Comment on [HIEV-7606](https://elocity.atlassian.net/browse/HIEV-7606): worked on cleaning up Mac mini and fixing runner issue.

### Sudeep — 17.1 of 19.0d (137h of 152h)

**2026-08-03** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): adding tariff activation logic

**2026-08-04** — logged 1.9d (16h) of 1.0d (8h) available, 6 comments

- Worklog 1h on [HIEV-7381](https://elocity.atlassian.net/browse/HIEV-7381) (Task, mid-sprint)
- Worklog 6h on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Worklog 1h on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Worklog 7h 30m on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Comment on [HIEV-7381](https://elocity.atlassian.net/browse/HIEV-7381): provided connector sequence in guest location api and deployed to UAT
- Comment on [HIEV-7381](https://elocity.atlassian.net/browse/HIEV-7381): fixed is_guest filter boolean parsing error
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): completed adding tariff relaunch logic in session modification api and tested in UAT, most of the cases working
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): parking sessions are facing errors, as we are not publishing status notification messages
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): supported relaunching active tariffs with necessary validations
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): started recreating adani sessions

**2026-08-05** — logged 1.0d (8h) of 1.0d (8h) available, 9 comments

- Worklog 7h on [HIEV-7403](https://elocity.atlassian.net/browse/HIEV-7403) (Task, mid-sprint)
- Worklog 30m on [HIEV-7381](https://elocity.atlassian.net/browse/HIEV-7381) (Task, mid-sprint)
- Worklog 15m on [HIEV-7381](https://elocity.atlassian.net/browse/HIEV-7381) (Task, mid-sprint)
- Worklog 20m on [HIEV-7199](https://elocity.atlassian.net/browse/HIEV-7199) (Bug, mid-sprint)
- Comment on [HIEV-7403](https://elocity.atlassian.net/browse/HIEV-7403): processed payments for 12 postpaid sessions
- Comment on [HIEV-7403](https://elocity.atlassian.net/browse/HIEV-7403): 1 session’s payment failed, made it prepaid manually, to disable razorpay payment link
- Comment on [HIEV-7403](https://elocity.atlassian.net/browse/HIEV-7403): deployed create order fix to prevent multiple payment reruns for failing sessions
- Comment on [HIEV-7403](https://elocity.atlassian.net/browse/HIEV-7403): added a validation before switching a location from prepaid to postpaid based on evse minimum wallet balance
- Comment on [HIEV-7381](https://elocity.atlassian.net/browse/HIEV-7381): added few charger details in charge session status api response
- Comment on [HIEV-7381](https://elocity.atlassian.net/browse/HIEV-7381): connector ui name added in response
- Comment on [HIEV-7381](https://elocity.atlassian.net/browse/HIEV-7381): Pending things: Refund support Cronjob to release payment intent for sessions which doesn’t get any charging transaction id
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): Sessions excel
- Comment on [HIEV-7199](https://elocity.atlassian.net/browse/HIEV-7199): deployed to canada prod

**2026-08-06** — logged 0.8d (7h) of 1.0d (8h) available, 2 comments

- Worklog 40m on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Worklog 6h on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): for relaunching active tariffs, added reassigning location tariff mapping
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): recreated all adani sessions with accurate cost except for one, because of no external OCPP start transaction and Stop transaction message for that session

**2026-08-07** — logged 0.5d (4h) of 1.0d (8h) available, 1 comments

- Worklog 3h on [HIEV-7436](https://elocity.atlassian.net/browse/HIEV-7436) (Task, mid-sprint)
- Worklog 1h on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Comment on [HIEV-7436](https://elocity.atlassian.net/browse/HIEV-7436): added the fix and raised the mr

**2026-08-09** — logged 0.9d (7h) of 0.0d (0h) available, 1 comments

- Worklog 7h on [HIEV-6989](https://elocity.atlassian.net/browse/HIEV-6989) (Task, planned)
- Comment on [HIEV-6989](https://elocity.atlassian.net/browse/HIEV-6989): resolved all review comments

**2026-08-10** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 1d on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): restructured session modification api to execute excluded steps

**2026-08-11** — logged 1.0d (8h) of 1.0d (8h) available, 4 comments

- Worklog 1d on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): recreated sessions with transaction id 94268 and 94286 by cleaning up wrong payment details
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): created a backup of all 41 impacted sessions and removed wrong payment details from all those sessions in both cpms single session and cpms terminated session index
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): added a guard to sanitise credit reference ids to prevent similar issue and raised the mr
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): supporting set charging profile message republishing

**2026-08-12** — logged 0.2d (2h) of 1.0d (8h) available, 2 comments

- Worklog 1h 30m on [HIEV-7483](https://elocity.atlassian.net/browse/HIEV-7483) (Task, mid-sprint)
- Comment on [HIEV-7483](https://elocity.atlassian.net/browse/HIEV-7483): processed payment for a session manually
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): worked on review comments on the session modification api and faced a lot of issue because of mapping mismatch

**2026-08-13** — logged 2.1d (17h) of 1.0d (8h) available, 4 comments

- Worklog 1h on [HIEV-7485](https://elocity.atlassian.net/browse/HIEV-7485) (Task, mid-sprint)
- Worklog 2d on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Comment on [HIEV-7485](https://elocity.atlassian.net/browse/HIEV-7485): started creating a flowchart
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): supported republishing of set charge profile messages and charge box offline messages
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): reverted cpms branch in canada prod and adani prod to v5.9.0
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): working on restoring tariff changes after session recreation

**2026-08-17** — logged 1.0d (8h) of 1.0d (8h) available, 4 comments

- Worklog 15m on [HIEV-7517](https://elocity.atlassian.net/browse/HIEV-7517) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7485](https://elocity.atlassian.net/browse/HIEV-7485) (Task, mid-sprint)
- Worklog 1h on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326) (Bug, mid-sprint)
- Worklog 3h on [HIEV-7304](https://elocity.atlassian.net/browse/HIEV-7304) (Bug, mid-sprint)
- Comment on [HIEV-7517](https://elocity.atlassian.net/browse/HIEV-7517): this is fixed
- Comment on [HIEV-7485](https://elocity.atlassian.net/browse/HIEV-7485): flowchart done and sent it to dinesh
- Comment on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326): worked on sending an individual field for both this params
- Comment on [HIEV-7304](https://elocity.atlassian.net/browse/HIEV-7304): fixed this in the framework for location route

**2026-08-18** — logged 0.5d (4h) of 1.0d (8h) available, 1 comments

- Worklog 4h on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): had discussions to resolve those review comments and started working on the changes

**2026-08-20** — logged 1.0d (8h) of 1.0d (8h) available, 5 comments

- Worklog 4h on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373) (Task, mid-sprint)
- Worklog 2h on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7323](https://elocity.atlassian.net/browse/HIEV-7323) (Bug, mid-sprint)
- Comment on [HIEV-7373](https://elocity.atlassian.net/browse/HIEV-7373): resolved refund backup and other review comments
- Comment on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326): fixed this and deployed to stg
- Comment on [HIEV-7326](https://elocity.atlassian.net/browse/HIEV-7326): i have removed note and changeSummary field from activity log api, and used a common field named as description as requested by lavanya, u can include a column for this and also update in export csv api parameters
- Comment on [HIEV-7323](https://elocity.atlassian.net/browse/HIEV-7323): fixed this and deployed to stg for integration
- Comment on [HIEV-7323](https://elocity.atlassian.net/browse/HIEV-7323): this also supported and deployed to stg, u can now request in the csv api

**2026-08-26** — logged 3.3d (27h) of 1.0d (8h) available, 12 comments

- Worklog 4h on [HIEV-7589](https://elocity.atlassian.net/browse/HIEV-7589) (Task, mid-sprint)
- Worklog 1h 30m on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7449](https://elocity.atlassian.net/browse/HIEV-7449) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7449](https://elocity.atlassian.net/browse/HIEV-7449) (Bug, mid-sprint)
- Worklog 6h on [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439) (Bug, mid-sprint)
- Worklog 3h on [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7324](https://elocity.atlassian.net/browse/HIEV-7324) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7304](https://elocity.atlassian.net/browse/HIEV-7304) (Bug, mid-sprint)
- Comment on [HIEV-7589](https://elocity.atlassian.net/browse/HIEV-7589): added the cronjob in payment service to release the cardhold when transaction id doesnt get assigned
- Comment on [HIEV-7546](https://elocity.atlassian.net/browse/HIEV-7546): this is now supported and deployed to UAT
- Comment on [HIEV-7544](https://elocity.atlassian.net/browse/HIEV-7544): can u add relevant details like what was incorrect for which session and all
- Comment on [HIEV-7449](https://elocity.atlassian.net/browse/HIEV-7449): this is now fixed
- Comment on [HIEV-7449](https://elocity.atlassian.net/browse/HIEV-7449): business id tracking for tariff operations is updated
- Comment on [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439): This was caused by business id not being recorded, this framework fix is done
- Comment on [HIEV-7439](https://elocity.atlassian.net/browse/HIEV-7439): this record will come under location tariff table
- Comment on [HIEV-7324](https://elocity.atlassian.net/browse/HIEV-7324): this is working, can be tested now
- Comment on [HIEV-7323](https://elocity.atlassian.net/browse/HIEV-7323): this is working directly in the report without any frontend changes itseems, so marking this as done
- Comment on [HIEV-7304](https://elocity.atlassian.net/browse/HIEV-7304): fallback mechanism implemented for all routes instead of just location route
- Comment on [HIEV-7302](https://elocity.atlassian.net/browse/HIEV-7302): filename is changed like this, if it needs to be in some other format pls let me know Before: ActivityLogs_tenant_2026-07-27T11_31_59.038Z.csv After: Activity_Logs_2026-07-27_11-31-59.csv
- Comment on [HIEV-7302](https://elocity.atlassian.net/browse/HIEV-7302): the tenant/user/business segment is removed as it leaks an internal view

**2026-08-31** — logged 1.0d (8h) of 1.0d (8h) available, 4 comments

- Worklog 5m on [HIEV-7493](https://elocity.atlassian.net/browse/HIEV-7493) (Bug, mid-sprint)
- Worklog 1d on [HIEV-7422](https://elocity.atlassian.net/browse/HIEV-7422) (Task, planned)
- Comment on [HIEV-7493](https://elocity.atlassian.net/browse/HIEV-7493): this is reviewed and merged
- Comment on [HIEV-7422](https://elocity.atlassian.net/browse/HIEV-7422): Went through the implement guide for this task and also studied the data abstraction layer already implemented in cpms repo
- Comment on [HIEV-7422](https://elocity.atlassian.net/browse/HIEV-7422): started the implementation of DAL in payment service first
- Comment on [HIEV-7095](https://elocity.atlassian.net/browse/HIEV-7095): timezone wont get auto populated by the location autocomplete api, user needs to manually select it

### Surya — 11.4 of 20.0d (92h of 160h)

**2026-08-06** — logged 0.7d (6h) of 1.0d (8h) available, 0 comments

- Worklog 30m on [HIEV-7423](https://elocity.atlassian.net/browse/HIEV-7423) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7413](https://elocity.atlassian.net/browse/HIEV-7413) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7319](https://elocity.atlassian.net/browse/HIEV-7319) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7316](https://elocity.atlassian.net/browse/HIEV-7316) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7314](https://elocity.atlassian.net/browse/HIEV-7314) (Bug, mid-sprint)
- Worklog 1h 30m on [HIEV-7312](https://elocity.atlassian.net/browse/HIEV-7312) (Bug, mid-sprint)
- Worklog 45m on [HIEV-7310](https://elocity.atlassian.net/browse/HIEV-7310) (Bug, mid-sprint)

**2026-08-07** — logged 0.9d (8h) of 1.0d (8h) available, 0 comments

- Worklog 6h on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362) (Epic, planned)
- Worklog 30m on [HIEV-7351](https://elocity.atlassian.net/browse/HIEV-7351) (Task, planned)
- Worklog 1h on [HIEV-7204](https://elocity.atlassian.net/browse/HIEV-7204) (Bug, mid-sprint)

**2026-08-10** — logged 1.1d (9h) of 1.0d (8h) available, 9 comments

- Worklog 5h on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362) (Epic, planned)
- Worklog 45m on [HIEV-7331](https://elocity.atlassian.net/browse/HIEV-7331) (Task, mid-sprint)
- Worklog 10m on [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7209](https://elocity.atlassian.net/browse/HIEV-7209) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7018](https://elocity.atlassian.net/browse/HIEV-7018) (Bug, mid-sprint)
- Worklog 2h on [HIEV-6752](https://elocity.atlassian.net/browse/HIEV-6752) (Task, mid-sprint)
- Worklog 15m on [HIEV-6446](https://elocity.atlassian.net/browse/HIEV-6446) (Bug, mid-sprint)
- Comment on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362): Frontend Branch : feature/certificate-management Figma designs : https://www.figma.com/proto/65jdp0nt3j3neBpECbxsNs/Security-Profile?node-id=8192-81&viewport=34%2C2… Feature doc : https://elocity.atlassian.net/wiki/spaces/CSMS/pages/2152857611/Security+Profile+3+SP3+Certificate+Management+Module
- Comment on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362): Initiated code changes required for new module setup , routes, permissions. UI layout for the new certificate management module is initiated.
- Comment on [HIEV-7331](https://elocity.atlassian.net/browse/HIEV-7331): The dropdown filter is updated to both stg and uat build from UI. Currently, backend filter support for guest charging is only available in UAT.
- Comment on [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237): Requesting to review the character limit validation for auto-complete address input field.
- Comment on [HIEV-7209](https://elocity.atlassian.net/browse/HIEV-7209): Fixed and deployed to stg.
- Comment on [HIEV-7018](https://elocity.atlassian.net/browse/HIEV-7018): Updated and deployed to stg. Maps-data GET API will now use locations payload when we use the charger dropdown filter and get the relevant response - which will be reflected in the maps. No changes for station-overview GET API - it will continue using uids payload when charger dropdown is used.
- Comment on [HIEV-6752](https://elocity.atlassian.net/browse/HIEV-6752): React doctor score uplift was conducted , starting with updating to latest version of react-doctor and obtaining the latest score with respect to all the new updates from react-doctor standards for code scoring. Phase wise implementation was taken up to reduce risk of changing abstracted / reusable coding components which will affect huge number of places where the components are used. Phase wise implementation plan , execution and results are captured in the following confluence folder: The imp
- Comment on [HIEV-6752](https://elocity.atlassian.net/browse/HIEV-6752): The react-doctor update MR : MR was merged and 2-3 weeks of testing time was used to find potential changes/bugs due to the changes. No new bugs were raised since. Requesting to review and close ticket as code changes are internal.
- Comment on [HIEV-6446](https://elocity.atlassian.net/browse/HIEV-6446): We have merged few features and bug fixes branch with our main branch and deployed the main branch to stg. This update is available in stg.

**2026-08-11** — logged 0.8d (6h) of 1.0d (8h) available, 3 comments

- Worklog 30m on [HIEV-7466](https://elocity.atlassian.net/browse/HIEV-7466) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362) (Epic, planned)
- Worklog 1h on [HIEV-7351](https://elocity.atlassian.net/browse/HIEV-7351) (Task, planned)
- Worklog 1h on [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237) (Bug, mid-sprint)
- Comment on [HIEV-7466](https://elocity.atlassian.net/browse/HIEV-7466): Once we make any successful update, we re-render the page triggering the station details API again to get the latest station details data. The page re-render will reset all the accordions to default state - setting the first accordion to be open and the rest to be closed. With this scenario being set, we will not target to maintain the states of each accordion on any update or page re-renders as we don't have necessity to maintain the open/close states as more number of accordions grow in same p
- Comment on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362): Ui layout and mock data with figma design info are added for all the pages : 1) Data grid 2) Data grid filters 3) Certificate Renewal Modals 4) Certificate details pages with all tabs + accordions Phases of code refactoring will be taken up before integration
- Comment on [HIEV-7351](https://elocity.atlassian.net/browse/HIEV-7351): Requirement : 1) “Refunded Amount” column to be added to the customer e-wallet charging sessions tab 2) Update the payload for export functionality in e-wallet to include the refunded amount

**2026-08-12** — logged 0.9d (7h) of 1.0d (8h) available, 3 comments

- Worklog 5h on [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363) (Task, planned)
- Worklog 2h on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362) (Epic, planned)
- Worklog 10m on [HIEV-7264](https://elocity.atlassian.net/browse/HIEV-7264) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7214](https://elocity.atlassian.net/browse/HIEV-7214) (Bug, mid-sprint)
- Comment on [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363): Rolled out Tariff module Revenue share Marketing Invoice (campaign) module Remaining ADMINISTRATION ASSETS BULK_LOCATION BUSINESS CORPORATE CUSTOMER DASHBOARD DEMAND_RESPONSE FLEET COMMISSION_REPORT LOAD_MANAGEMENT NOTIFICATION PROFILE RESERVATIONS REWARDS SCHEDULE_CHARGING ROAMING_PARTNERS And other abstracted pages + new feature modules in development
- Comment on [HIEV-7264](https://elocity.atlassian.net/browse/HIEV-7264): This resolution is also tied to Details : We should be able to receive the Un-authorisation 401 response headers and trigger the logout sequence from frontend. This can be verified in stg.
- Comment on [HIEV-7214](https://elocity.atlassian.net/browse/HIEV-7214): 401 Unauthorized Handling Resolved Initially, we were unable to catch or evaluate the 401 Unauthorized status code on the frontend during authentication errors. Due to CORS restrictions, the browser blocked access to the response details, preventing us from reading the specific status code and executing the necessary fallback logic (such as token refreshes or login redirects). Resolution Details: The backend team has now updated the CORS configuration to properly expose the required headers duri

**2026-08-13** — logged 0.9d (7h) of 1.0d (8h) available, 0 comments

- Worklog 5h on [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363) (Task, planned)
- Worklog 2h on [HIEV-7351](https://elocity.atlassian.net/browse/HIEV-7351) (Task, planned)

**2026-08-14** — logged 0.9d (8h) of 1.0d (8h) available, 1 comments

- Worklog 30m on [HIEV-7505](https://elocity.atlassian.net/browse/HIEV-7505) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7504](https://elocity.atlassian.net/browse/HIEV-7504) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7501](https://elocity.atlassian.net/browse/HIEV-7501) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363) (Task, planned)
- Worklog 1h on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362) (Epic, planned)
- Comment on [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363): Updated Modules : Assets , Administration

**2026-08-15** — logged 0.4d (3h) of 0.0d (0h) available, 2 comments

- Worklog 15m on [HIEV-7512](https://elocity.atlassian.net/browse/HIEV-7512) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7511](https://elocity.atlassian.net/browse/HIEV-7511) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7510](https://elocity.atlassian.net/browse/HIEV-7510) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7509](https://elocity.atlassian.net/browse/HIEV-7509) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7148](https://elocity.atlassian.net/browse/HIEV-7148) (Task, planned)
- Comment on [HIEV-7148](https://elocity.atlassian.net/browse/HIEV-7148): Type check fixes are completed. Fleet management revamp feature is ready for API integration.
- Comment on [HIEV-7148](https://elocity.atlassian.net/browse/HIEV-7148): The Existing fleet management is now renamed to Vehicle Telematics and the revamp feature and updates will now be considered as “Fleet management” module. I have updated the existing Fleet API endpoints to be mapped to the new /telematics API end point. Awaiting confirmation on the same for existing fleet management routes, pages and components.

**2026-08-17** — logged 1.3d (10h) of 1.0d (8h) available, 2 comments

- Worklog 1h on [HIEV-7528](https://elocity.atlassian.net/browse/HIEV-7528) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7527](https://elocity.atlassian.net/browse/HIEV-7527) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7519](https://elocity.atlassian.net/browse/HIEV-7519) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363) (Task, planned)
- Worklog 6h on [HIEV-7148](https://elocity.atlassian.net/browse/HIEV-7148) (Task, planned)
- Comment on [HIEV-7528](https://elocity.atlassian.net/browse/HIEV-7528): There was no mention of color scheme to be used for this progress bar. Since we dont make use of only Yellow progress bar anywhere in load management - this is also updated to use Green, yellow and red. Green : <90% values Yellow : =90% value && >90% values Red : = 100% value && >100% values
- Comment on [HIEV-7527](https://elocity.atlassian.net/browse/HIEV-7527): Following are the GET APIs available for load management modue : 1) evse-group : For load management group data grid 2) {id}/overview : Overview tab details + graph 3) {id}/charger-details : Overview tab → charger details drawer 4) {id}/load-analytics-data : Analytics tab details + graph 5) {id}/load-summary : Load summary tab data grid We don't have a specific fetch API to get load group specific details on refresh. So, we redirect to load groups data grid page, get all group details and on cli

**2026-08-18** — logged 0.9d (7h) of 1.0d (8h) available, 3 comments

- Worklog 4h on [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363) (Task, planned)
- Worklog 2h on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362) (Epic, planned)
- Worklog 1h on [HIEV-7183](https://elocity.atlassian.net/browse/HIEV-7183) (Task, mid-sprint)
- Worklog 10m on [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133) (Bug, mid-sprint)
- Comment on [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363): Updated all modules , pending check to verify components and other folders for potential date-format util upgrade from existing flow. Additionally, new modules like load management, vehicle telematics and certificate management should be updated later.
- Comment on [HIEV-7148](https://elocity.atlassian.net/browse/HIEV-7148): Received Contracts for new fleet APIs. Updated the frontend code to implement the changes. Yet to check the API flow with awaiting backend support for the same..
- Comment on [HIEV-7133](https://elocity.atlassian.net/browse/HIEV-7133): The + and - icons for address represents show/hide action. So address details will be retained whereas the vehicle details is an optional and - will remove the details added. This is not an issue and is an expected workflow.

**2026-08-19** — logged 0.0d (0h) of 1.0d (8h) available, 1 comments

- Comment on [HIEV-7363](https://elocity.atlassian.net/browse/HIEV-7363): Updated and migrated all user facing date month labels and components using date to follow country specific date format

**2026-08-20** — logged 0.5d (4h) of 1.0d (8h) available, 0 comments

- Worklog 30m on [HIEV-7565](https://elocity.atlassian.net/browse/HIEV-7565) (Suggestion, mid-sprint)
- Worklog 30m on [HIEV-7562](https://elocity.atlassian.net/browse/HIEV-7562) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7561](https://elocity.atlassian.net/browse/HIEV-7561) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7549](https://elocity.atlassian.net/browse/HIEV-7549) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7518](https://elocity.atlassian.net/browse/HIEV-7518) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7362](https://elocity.atlassian.net/browse/HIEV-7362) (Epic, planned)
- Worklog 1h on [HIEV-7183](https://elocity.atlassian.net/browse/HIEV-7183) (Task, mid-sprint)

**2026-08-24** — logged 1.0d (8h) of 1.0d (8h) available, 4 comments

- Worklog 30m on [HIEV-7578](https://elocity.atlassian.net/browse/HIEV-7578) (Observation, mid-sprint)
- Worklog 30m on [HIEV-7565](https://elocity.atlassian.net/browse/HIEV-7565) (Suggestion, mid-sprint)
- Worklog 15m on [HIEV-7562](https://elocity.atlassian.net/browse/HIEV-7562) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7561](https://elocity.atlassian.net/browse/HIEV-7561) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7549](https://elocity.atlassian.net/browse/HIEV-7549) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7518](https://elocity.atlassian.net/browse/HIEV-7518) (Bug, mid-sprint)
- Worklog 5h on [HIEV-6944](https://elocity.atlassian.net/browse/HIEV-6944) (Task, planned)
- Comment on [HIEV-7578](https://elocity.atlassian.net/browse/HIEV-7578): We have been following the approach of removing stations once there is a change in locations dropdown since we have this approach for some dependent dropdown. Should we have to change the approach or keep it the same way?
- Comment on [HIEV-7561](https://elocity.atlassian.net/browse/HIEV-7561): Can you please let me know if this is reproducible , i checked on different days - yet to reproduce the issue with country code dropdown.
- Comment on [HIEV-7549](https://elocity.atlassian.net/browse/HIEV-7549): The validations currently set is expected flow. 1) We will have ‘From’ should not be same as ‘To’ time validation for all schedule charging rows except when we input 12:00 AM for both fields since From 00:00 - To 00:00 is considered as 24 hours/full day for that selected days. (This is why we get overlap error/warning when we already have 12:00 to 12:00 full selected day and when we try to add any other time for the same selected day) 2) We will not have a separate validations for rows that are 
- Comment on [HIEV-7518](https://elocity.atlassian.net/browse/HIEV-7518): For validation to check if existing EVSE are included in creation of new load group, we show the message directly from the API response. This shall be updated in the backend.

**2026-08-26** — logged 0.6d (5h) of 1.0d (8h) available, 0 comments

- Worklog 5h on [HIEV-6944](https://elocity.atlassian.net/browse/HIEV-6944) (Task, planned)

**2026-08-27** — logged 0.0d (0h) of 1.0d (8h) available, 14 comments

- Comment on [HIEV-7549](https://elocity.atlassian.net/browse/HIEV-7549): Updated to stg.
- Comment on [HIEV-7512](https://elocity.atlassian.net/browse/HIEV-7512): Fixed the width of the new guest charging dropdown filter. Updated in stg.
- Comment on [HIEV-7511](https://elocity.atlassian.net/browse/HIEV-7511): 255 char limit validation is added. Deployed to stg.
- Comment on [HIEV-7510](https://elocity.atlassian.net/browse/HIEV-7510): 255 char limit validation is added. Deployed to stg.
- Comment on [HIEV-7509](https://elocity.atlassian.net/browse/HIEV-7509): Fixed and deployed to stg.
- Comment on [HIEV-7505](https://elocity.atlassian.net/browse/HIEV-7505): Redirection from grid view to load group details is added. Deployed to stg.
- Comment on [HIEV-7423](https://elocity.atlassian.net/browse/HIEV-7423): This ticket can be followed up/closed since we are updating all the export buttons in our web app with a standard abstracted button. Reference :
- Comment on [HIEV-7413](https://elocity.atlassian.net/browse/HIEV-7413): Positioning of remove slot icon is fixed. Deployed the change to stg.
- Comment on [HIEV-7319](https://elocity.atlassian.net/browse/HIEV-7319): Ration duration uses an abstracted component which allows user to input duration. The textfield input inside this component is removed. Fixed and deployed to stg
- Comment on [HIEV-7316](https://elocity.atlassian.net/browse/HIEV-7316): Placeholder and selected value will not be overriden. Fixed and deployed to stg
- Comment on [HIEV-7314](https://elocity.atlassian.net/browse/HIEV-7314): Fixed and updated to stg. We will now have a mandatory custom slot when “Custom Slot” radio button is selected. User will have option to remove the second/third and rest of the slot, first one will not have a remove slot option.
- Comment on [HIEV-7312](https://elocity.atlassian.net/browse/HIEV-7312): Fixed and deployed to stg. Maintenance data will stay intact on succesful station detail update.
- Comment on [HIEV-7310](https://elocity.atlassian.net/browse/HIEV-7310): We will have a label displayed during an active maintenance period/slot. This is updated to stg env.
- Comment on [HIEV-7237](https://elocity.atlassian.net/browse/HIEV-7237): The address field autocomplete component is updated as suggested. i.e : before we make use of address check API call from the component, we will validate the length of the input char. If it satisfies or stays within the limit of 255 char, we will call the api and list the available options if any. Else, error/warning about the character limit will be displayed

**2026-08-28** — logged 0.4d (3h) of 0.0d (0h) available, 4 comments

- Worklog 3h on [HIEV-7584](https://elocity.atlassian.net/browse/HIEV-7584) (Suggestion, mid-sprint)
- Comment on [HIEV-7528](https://elocity.atlassian.net/browse/HIEV-7528): Load usage meter with its corresponding color config is updated to reflect other meter / the legend described colors. Deployed to stg.
- Comment on [HIEV-7519](https://elocity.atlassian.net/browse/HIEV-7519): Load Usage meter with its color config is updated. Deployed the change to stg
- Comment on [HIEV-7504](https://elocity.atlassian.net/browse/HIEV-7504): The config issue in connector details dashboard is fixed. Deployed to stg
- Comment on [HIEV-7501](https://elocity.atlassian.net/browse/HIEV-7501): Fixed and deployed to stg.

**2026-08-29** — logged 0.1d (1h) of 0.0d (0h) available, 0 comments

- Worklog 30m on [HIEV-7585](https://elocity.atlassian.net/browse/HIEV-7585) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7565](https://elocity.atlassian.net/browse/HIEV-7565) (Suggestion, mid-sprint)
- Worklog 15m on [HIEV-7562](https://elocity.atlassian.net/browse/HIEV-7562) (Bug, mid-sprint)

**2026-08-31** — logged 0.0d (0h) of 1.0d (8h) available, 4 comments

- Comment on [HIEV-7585](https://elocity.atlassian.net/browse/HIEV-7585): Validations (value to be less than or equal to 10000000) are updated to the round robin time interval input field. Will reflect in both add new load group and the load group details. Deployed to stg
- Comment on [HIEV-7584](https://elocity.atlassian.net/browse/HIEV-7584): Connector icon (with connector name tooltip) + connector sequence and connector name will be displayed in each connector card in the overview section of load group. Deployed to stg.
- Comment on [HIEV-7565](https://elocity.atlassian.net/browse/HIEV-7565): Unstable session and variance event count is removed from both the grid and the export file config. Updated and deployed to stg.
- Comment on [HIEV-7562](https://elocity.atlassian.net/browse/HIEV-7562): Successful load group deletion will now redirect user to load group list. Deployed to stg.

### Tarun — 17.2 of 20.0d (138h of 160h)

**2026-08-03** — logged 1.6d (13h) of 1.0d (8h) available, 2 comments

- Worklog 6h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Worklog 6h 30m on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Worklog 30m on [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145) (Task, planned)
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): Implemented the Charger logs validation tool and I gave demo to dinesh and deepak,anyway the demo didn’t go well and dinesh gave suggestions for the implementation and got the full requirement documentation from deepak and anyhow i have implemented few things in the requirements and started working on the other requirements which i havent implemented.
- Comment on [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145): Updated the few minor changes pushed the changes as well and apart from this Deepak published all those new changes into main docs site and brought that site into live with new changes. Note : New changes were done upto Reservation Module in WebApp User Manual.

**2026-08-05** — logged 2.0d (16h) of 1.0d (8h) available, 2 comments

- Worklog 5h 30m on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Worklog 2h on [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145) (Task, planned)
- Worklog 1d 30m on [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145) (Task, planned)
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): Firstly i gone through the full requirement documentation and then started the implementation documentation and anyway few of the requirements are already done but those are also need to ignore as per the feedback. I want to change the implementation structure because the previous version is not good to push forward. I will discuss with deepak regarding this implementation documentation.
- Comment on [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145): Firstly I generated the readme.md file for corporate module by using the documentation given by Dinesh and also I updated the Bulk Operation module and half of the part in Push notification module. I removed Roaming, Fleet Management and Demand Reponse becuase those modules are not yet live.

**2026-08-06** — logged 0.1d (1h) of 1.0d (8h) available, 3 comments

- Worklog 1h on [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145) (Task, planned)
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I worked on this implementation documentation and i prepared that documentation but I need to send it to Deepak for review and also checked the previous implementation which was rejected by dinesh and deepak to know the issues by comparing that with the provided requirements documentation.
- Comment on [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145): I Updated the following modules in web app user manual: Administration Module >>> Global Settings Business Module Load Management Module Corporate Module Push Notification Invoice Campaign I will publish all these changes to main docs site with the help of Deepak.
- Comment on [HIEV-7145](https://elocity.atlassian.net/browse/HIEV-7145): I updated few things in Load Management and once again checked every module which i have updated and riased MR to deepak to publish the changes.

**2026-08-09** — logged 0.4d (3h) of 0.0d (0h) available, 1 comments

- Worklog 3h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): Did few modifications in the implementation documentation and sent it to deepak and after getting the approval on the implementation documentation then will start the implementation as per that plan.

**2026-08-10** — logged 0.9d (8h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445) (Task, mid-sprint)
- Worklog 3h 30m on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445): Started updating the mobile user manual and I have updated the following modules in andorid: Intro Downloading App Creating Account Signing In Exploring App Start and Stopping Charging Session(Half Done).
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I got the approval from deepak on the implementation plan and started the implementing as per that plan and completed upto 6 validation rules out of given 20 rules in PRD.

**2026-08-11** — logged 1.0d (8h) of 1.0d (8h) available, 0 comments

- Worklog 5h on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445) (Task, mid-sprint)
- Worklog 3h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)

**2026-08-12** — logged 1.0d (8h) of 1.0d (8h) available, 4 comments

- Worklog 4h on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445) (Task, mid-sprint)
- Worklog 4h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445): I completed updating the following modules in andorid: Editing Profile Viewing Transactions and Invocies Managing Wallet Reach Out To Support Managing Settings and I added two new modules: Chat With Customer Support Managing Reports I need to discuss about these two new modules with dinesh if he accpet those i will keep those in user manual otherwise I’ll remove those.
- Comment on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445): Andorid User Manual: I Updated the Reservation and Location Modules in andorid user manual. For these two modules I deleted the previous version completely and created one single readme file for each module. With this I have completed the andorid user manual and sent all those files to Dinesh for review. IOS User Manual: I started working on the IOS modules and the thing is I am using the same script for this IOS which i already generated for Andorid User Manual. And I need to update the screens
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I completed hlaf of the valdiation rules and and I need to test those rules with sample log files.
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I was testing the implemented validations with some sample charger log files and i got few issues when i was testing like some validation rules are working and some were not working as expected. I started working on those particular validations which are not working as expected.

**2026-08-13** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 5h on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445) (Task, mid-sprint)
- Worklog 3h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445): I Updated almost half of the part in IOS user manual. Below are the details about the modules which I updated: Downloading the App Creating Account Signing In Exploring the App View Location Details Editing Profile Reach Out To Support Chat With Customer Support
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I was workign on few validation rules which i got errors and did few changes in the implementation and along with that implemented few more validation. As of now I have completed 15 validations and I need to work on 5 more as per given PRD and need to test those too.

**2026-08-16** — logged 1.0d (8h) of 0.0d (0h) available, 2 comments

- Worklog 5h on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445) (Task, mid-sprint)
- Worklog 3h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445): Completed the below IOS User Manual Modules: Start & Stop Charging Session View Transaction & Invoices Reservations Managing Wallet Manage Settings Manage Reports With these modules I completed the full IOS User Manual Part.
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I completed the implementing remaining validation and I need to test with sample log file with all the validations at once.

**2026-08-17** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 1d on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445): Dinesh Reviewed the Android User manual and didnt get any changes so andorid part is fine.
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): Worked on testing the 20 validations with log files and i got few issues in some valdiations and i solved some and some are not resolved and taking more time and i need to work on those and also updating the interactive dashbaord for this validation tool.

**2026-08-18** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I tested the validations one more time because previously i got lot of issues with validations and now the validations are wokring as expected with sample log files and one more thing is i have updated the the dashboard also and i need to discuss this with deepak after that i will move to review state

**2026-08-19** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): In the first half I worked on teting the validations one more time and prpeared some log files for demo session and in the second half I gave the demo to dinesh and deepak and it’s ok and I need to push that code in to gitlab repo.

**2026-08-20** — logged 0.9d (7h) of 1.0d (8h) available, 1 comments

- Worklog 7h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I got enhancement in the implementation below are the changes that I did in the current implementation: Improved the tool by replacing manual CSV file upload with automated API log fetching. Added input fields for Charge Point ID, From Date, and To Date to directly query charger logs. Integrated the Authentication API ( /auth/user/login ) for user login Integrated the CPMS Logs API ( /ocpp/logs ) with pagination support to fetch and feed raw logs directly into the validation engine. I did for st

**2026-08-23** — logged 0.9d (7h) of 0.0d (0h) available, 1 comments

- Worklog 7h on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I worked on the new enhancement task which i got from deepak and I added all environments (Dev,UAT and prod ) apis for both user login and ocpp logs and i tested across all the environments and working as expected

**2026-08-24** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 1d on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7445](https://elocity.atlassian.net/browse/HIEV-7445): Review was finished from Dinesh end and Deepak Published the changes. Now the website is live.
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): I worked on new changes like I added adani and alfanar prod user login api and charger logs api and checked that as well and working fine and added a download button to download the detailed error logs file

**2026-08-25** — logged 0.1d (0h) of 1.0d (8h) available, 1 comments

- Worklog 30m on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254) (Task, planned)
- Comment on [HIEV-7254](https://elocity.atlassian.net/browse/HIEV-7254): Pushed the code into scripts repository

**2026-08-26** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 1d on [HIEV-7591](https://elocity.atlassian.net/browse/HIEV-7591) (Task, mid-sprint)
- Comment on [HIEV-7591](https://elocity.atlassian.net/browse/HIEV-7591): I went through the PRD document and also went through the wallet apis but didn't get the full clarity but need to explore more about this task after that will start the implementation plan

**2026-08-30** — logged 0.9d (7h) of 0.0d (0h) available, 1 comments

- Worklog 7h on [HIEV-7591](https://elocity.atlassian.net/browse/HIEV-7591) (Task, mid-sprint)
- Comment on [HIEV-7591](https://elocity.atlassian.net/browse/HIEV-7591): Worked on the implementation plan

**2026-08-31** — logged 0.9d (7h) of 1.0d (8h) available, 0 comments

- Worklog 7h on [HIEV-7591](https://elocity.atlassian.net/browse/HIEV-7591) (Task, mid-sprint)

### Twisha — 13.3 of 18.0d (107h of 144h)

**2026-08-02** — logged 2.2d (18h) of 0.0d (0h) available, 7 comments

- Worklog 2h on [HIEV-7301](https://elocity.atlassian.net/browse/HIEV-7301) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7244](https://elocity.atlassian.net/browse/HIEV-7244) (Bug, mid-sprint)
- Worklog 3h on [HIEV-7243](https://elocity.atlassian.net/browse/HIEV-7243) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7240](https://elocity.atlassian.net/browse/HIEV-7240) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7031](https://elocity.atlassian.net/browse/HIEV-7031) (Task, mid-sprint)
- Comment on [HIEV-7301](https://elocity.atlassian.net/browse/HIEV-7301): that specific customer soft deleted is not in active list, i rechecked it. also i recreated the same situation by adding a new customer and then deleting. it works fine can you please retest it again.
- Comment on [HIEV-7244](https://elocity.atlassian.net/browse/HIEV-7244): it is being shown as cancelled can you please recheck this?
- Comment on [HIEV-7244](https://elocity.atlassian.net/browse/HIEV-7244): the cancelled reservations are supposed to stay in upcoming tab and then moved to past after they are expired but as you said, a cancelled badge should be shown, which is now in place
- Comment on [HIEV-7243](https://elocity.atlassian.net/browse/HIEV-7243): the slots api was not showing occupied slots, now it is resolved and also i have tested it in stg. and i have put it for review.
- Comment on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242): I had initially implemented the logic of applying locks in the database but later was asked to find an approach that deals in application layer. so now i have done a redis distributed lock approach and have given it for review. the first approach only had taken much time as i had to implement and also test. so adding time log that includes doing both the approaches.
- Comment on [HIEV-7240](https://elocity.atlassian.net/browse/HIEV-7240): this issue was occurring due to failure of slots api to show occupied slots. now that it is fixed maybe this scenario is also resolved. can you please retest this one and let me know.
- Comment on [HIEV-7031](https://elocity.atlassian.net/browse/HIEV-7031): i checked for both payment and session-utility services. i found few in payment service but none in session-utility. have completed and raised MR for review.

**2026-08-03** — logged 0.2d (2h) of 1.0d (8h) available, 2 comments

- Worklog 2h on [HIEV-7311](https://elocity.atlassian.net/browse/HIEV-7311) (Bug, mid-sprint)
- Comment on [HIEV-7311](https://elocity.atlassian.net/browse/HIEV-7311): last month logs were deleted and from now we only retain logs of previous 3 days. hence this is not a bug.
- Comment on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242): concurrency control is added to post reservation logic. and also tested in stg.

**2026-08-04** — logged 0.5d (4h) of 1.0d (8h) available, 2 comments

- Worklog 2h on [HIEV-7379](https://elocity.atlassian.net/browse/HIEV-7379) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344) (Task, planned)
- Comment on [HIEV-7379](https://elocity.atlassian.net/browse/HIEV-7379): that business didnt have a currency allotted. now it is resolved. you can check
- Comment on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344): studied the implementation plan.

**2026-08-05** — logged 0.4d (3h) of 1.0d (8h) available, 4 comments

- Worklog 3h on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350) (Task, planned)
- Comment on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350): studied the codebase to understand the rrefund flow for botht the scenarios. one from the session to wallet, and the other from the wallet to account(source). today will be adding the logic to differentiate these two refunds. the other validation logic is in place already.
- Comment on [HIEV-7243](https://elocity.atlassian.net/browse/HIEV-7243): https://gitlab.com/elocity1/backend/cpms/-/merge_requests/1021
- Comment on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242): https://gitlab.com/elocity1/backend/cpms/-/merge_requests/1022
- Comment on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032): https://gitlab.com/elocity1/backend/session-utility/-/merge_requests/130 hi vinay, i have closed the previous MR and this is the new one.

**2026-08-06** — logged 1.7d (13h) of 1.0d (8h) available, 4 comments

- Worklog 5h on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350) (Task, planned)
- Worklog 4h on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350) (Task, planned)
- Worklog 4h on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032) (Bug, mid-sprint)
- Comment on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350): i got the clear requirement yesterday, will start implementing today.
- Comment on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350): i have completed the task and also tested it in uat. i have raised a MR. and it is in review now.
- Comment on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032): i have done the required implementation need to test it today.
- Comment on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032): testing is also done it works fine.

**2026-08-07** — logged 0.6d (5h) of 1.0d (8h) available, 0 comments

- Worklog 3h on [HIEV-7358](https://elocity.atlassian.net/browse/HIEV-7358) (Task, planned)
- Worklog 2h on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350) (Task, planned)

**2026-08-08** — logged 0.0d (0h) of 0.0d (0h) available, 2 comments

- Comment on [HIEV-7358](https://elocity.atlassian.net/browse/HIEV-7358): i have prepared the implentation plan and submitted to deepak. upon his approval, i will start the implementation
- Comment on [HIEV-7350](https://elocity.atlassian.net/browse/HIEV-7350): i added the same logic for the export-csv api as well, and also tested it in uat. it is also in review.

**2026-08-10** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7358](https://elocity.atlassian.net/browse/HIEV-7358) (Task, planned)
- Comment on [HIEV-7358](https://elocity.atlassian.net/browse/HIEV-7358): i have completed the implementation, also created v2 version of export-csv api. it is now in review.

**2026-08-11** — logged 0.1d (1h) of 1.0d (8h) available, 1 comments

- Worklog 1h on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242) (Bug, mid-sprint)
- Comment on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242): had discussions in the morning, and few changes were suggested, i have made those changes and also pushed.

**2026-08-12** — logged 1.1d (9h) of 1.0d (8h) available, 3 comments

- Worklog 4h on [HIEV-7352](https://elocity.atlassian.net/browse/HIEV-7352) (Bug, mid-sprint)
- Worklog 3h on [HIEV-7352](https://elocity.atlassian.net/browse/HIEV-7352) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344) (Task, planned)
- Comment on [HIEV-7352](https://elocity.atlassian.net/browse/HIEV-7352): i have been working on this bug fix, yesterday i was running charging sessions to identify the reason behind the issue, but reaching the desired SoC is taking too much time, so will look into a way to handle it and finish it today.
- Comment on [HIEV-7352](https://elocity.atlassian.net/browse/HIEV-7352): the issue was not reporducable from my end, so i have assigned it back to so that he can recheck it.
- Comment on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344): i have started to write the implementation plan.

**2026-08-13** — logged 0.5d (4h) of 1.0d (8h) available, 2 comments

- Worklog 4h on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344) (Task, planned)
- Comment on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344): completed the implementation plan and it is in review now. once i get the approval will start the implmentation.
- Comment on [HIEV-7165](https://elocity.atlassian.net/browse/HIEV-7165): this ticket is currently out of scope and is not reporducable.

**2026-08-14** — logged 0.2d (2h) of 1.0d (8h) available, 1 comments

- Worklog 2h on [HIEV-7324](https://elocity.atlassian.net/browse/HIEV-7324) (Bug, mid-sprint)
- Comment on [HIEV-7324](https://elocity.atlassian.net/browse/HIEV-7324): i worked on this, and completed it, will raise the MR today and get it reviewed.

**2026-08-17** — logged 0.8d (6h) of 1.0d (8h) available, 1 comments

- Worklog 6h on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344) (Task, planned)
- Comment on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344): Had few discussions regarding the implementation logic. Was researchning on it. And by EOD the we agreed upon an approach. will be starting implementation today.

**2026-08-20** — logged 0.0d (0h) of 1.0d (8h) available, 2 comments

- Worklog 15m on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242) (Bug, mid-sprint)
- Comment on [HIEV-7531](https://elocity.atlassian.net/browse/HIEV-7531): this is not a bug. it is not related to reservation duration, but it is related to the number of active reservations allowed per customer based on the business they are using. this business has a limit of only one actuve reservation. hence you are getting this.
- Comment on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242): review comments are resolved. https://gitlab.com/elocity1/backend/cpms/-/merge_requests/1022

**2026-08-21** — logged 1.0d (8h) of 1.0d (8h) available, 2 comments

- Worklog 1d on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503) (Bug, mid-sprint)
- Comment on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503): the issue was with the redis storage mechanism. it is fixed now.
- Comment on [HIEV-7503](https://elocity.atlassian.net/browse/HIEV-7503): time logged for yesterday and today together. yesterday we had discussions regarding this. and i had researched on the causes and the solutions for it.

**2026-08-25** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 1d on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344) (Task, planned)
- Comment on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344): working on the implementation.

**2026-08-26** — logged 1.4d (11h) of 1.0d (8h) available, 3 comments

- Worklog 3h on [HIEV-7564](https://elocity.atlassian.net/browse/HIEV-7564) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7493](https://elocity.atlassian.net/browse/HIEV-7493) (Bug, mid-sprint)
- Worklog 1d on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344) (Task, planned)
- Comment on [HIEV-7564](https://elocity.atlassian.net/browse/HIEV-7564): i have added the logic to support these event types under filter. i have also raised an MR and it is under review. assigning back to , you can support frm frontend now.
- Comment on [HIEV-7493](https://elocity.atlassian.net/browse/HIEV-7493): have added length restriction from backend.
- Comment on [HIEV-7344](https://elocity.atlassian.net/browse/HIEV-7344): i have completed the implementation and it is now in review

**2026-08-31** — logged 0.8d (6h) of 1.0d (8h) available, 4 comments

- Worklog 1h on [HIEV-7552](https://elocity.atlassian.net/browse/HIEV-7552) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7420](https://elocity.atlassian.net/browse/HIEV-7420) (Bug, mid-sprint)
- Worklog 4h on [HIEV-7416](https://elocity.atlassian.net/browse/HIEV-7416) (Bug, mid-sprint)
- Worklog 40m on [HIEV-7303](https://elocity.atlassian.net/browse/HIEV-7303) (Bug, mid-sprint)
- Comment on [HIEV-7552](https://elocity.atlassian.net/browse/HIEV-7552): the error is being thrown because the data is deleted from the database. its not any logical error.
- Comment on [HIEV-7420](https://elocity.atlassian.net/browse/HIEV-7420): from backend we are sending the start date and end date. so the changes are needed from the frontend. can please look into this.
- Comment on [HIEV-7416](https://elocity.atlassian.net/browse/HIEV-7416): the data in cache was not being refreshed. hence this was occuring. i have resolved it and also tested in stg. it works fine. now it is in review.
- Comment on [HIEV-7303](https://elocity.atlassian.net/browse/HIEV-7303): this is not an issue. we send the date format similar on both the apis. it is in frontend where the format is enhanced in the webapp. we send the same date format in other reports as well.

### Vinay — 6.0 of 19.0d (48h of 152h)

**2026-08-03** — logged 0.5d (4h) of 1.0d (8h) available, 2 comments

- Worklog 3h on [HIEV-7159](https://elocity.atlassian.net/browse/HIEV-7159) (Task, mid-sprint)
- Worklog 45m on [HIEV-7159](https://elocity.atlassian.net/browse/HIEV-7159) (Task, mid-sprint)
- Comment on [HIEV-7159](https://elocity.atlassian.net/browse/HIEV-7159): movem location timings debug, doesnt seem to have any issue from backend, might be a display related, have to check with Dhanush
- Comment on [HIEV-7159](https://elocity.atlassian.net/browse/HIEV-7159): retrospective

**2026-08-04** — logged 0.6d (5h) of 1.0d (8h) available, 2 comments

- Worklog 45m on [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385) (Bug, mid-sprint)
- Worklog 1h on [HIEV-6988](https://elocity.atlassian.net/browse/HIEV-6988) (Task, planned)
- Worklog 3h on [HIEV-6649](https://elocity.atlassian.net/browse/HIEV-6649) (Task, mid-sprint)
- Comment on [HIEV-6988](https://elocity.atlassian.net/browse/HIEV-6988): a test is failing, please check and we can approve it
- Comment on [HIEV-6649](https://elocity.atlassian.net/browse/HIEV-6649): optimisation and other edge case handling

**2026-08-05** — logged 0.5d (4h) of 1.0d (8h) available, 15 comments

- Worklog 10m on [HIEV-7299](https://elocity.atlassian.net/browse/HIEV-7299) (Bug, mid-sprint)
- Worklog 15m on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282) (Bug, mid-sprint)
- Worklog 20m on [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7243](https://elocity.atlassian.net/browse/HIEV-7243) (Bug, mid-sprint)
- Worklog 2h on [HIEV-7199](https://elocity.atlassian.net/browse/HIEV-7199) (Bug, mid-sprint)
- Worklog 1h on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032) (Bug, mid-sprint)
- Worklog 5m on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032) (Bug, mid-sprint)
- Comment on [HIEV-7385](https://elocity.atlassian.net/browse/HIEV-7385): this can be released i guess, dont think testing is required
- Comment on [HIEV-7299](https://elocity.atlassian.net/browse/HIEV-7299): done, will be deployed later with other fixes on lower envs
- Comment on [HIEV-7297](https://elocity.atlassian.net/browse/HIEV-7297): done, merged
- Comment on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291): done
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): merged
- Comment on [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275): please add MR link here
- Comment on [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275): i dont think you need ti usse query builder its straight forward DB query using TYPEORM basic methods. please check again, if at all query builder is mandatory use the framework that we built
- Comment on [HIEV-7243](https://elocity.atlassian.net/browse/HIEV-7243): please add MR link here
- Comment on [HIEV-7243](https://elocity.atlassian.net/browse/HIEV-7243): merged
- Comment on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242): pplease add MR link here
- Comment on [HIEV-7199](https://elocity.atlassian.net/browse/HIEV-7199): reviewed and merged to master, you can deploy to MOVEM, you may send to testig once deployed
- Comment on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032): please add MR link, if you have any old MRs related to same fix please close them
- Comment on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032): review done added comments
- Comment on [HIEV-6988](https://elocity.atlassian.net/browse/HIEV-6988): review done
- Comment on [HIEV-6649](https://elocity.atlassian.net/browse/HIEV-6649): Done and will be deployed after review approval data migration: analytics: cpms:

**2026-08-10** — logged 1.0d (8h) of 1.0d (8h) available, 1 comments

- Worklog 1d on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406) (Task, planned)
- Comment on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406): got the requirements clear, will plan for Mobile APIs

**2026-08-12** — logged 0.8d (6h) of 1.0d (8h) available, 2 comments

- Worklog 5h on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406) (Task, planned)
- Worklog 1h on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242) (Bug, mid-sprint)
- Comment on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406): implementation plan is ready
- Comment on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242): had revierw discussion with the team and suggested few changes

**2026-08-16** — logged 1.2d (10h) of 0.0d (0h) available, 0 comments

- Worklog 1d 2h on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406) (Task, planned)

**2026-08-17** — logged 0.7d (6h) of 1.0d (8h) available, 13 comments

- Worklog 15m on [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275) (Bug, mid-sprint)
- Worklog 30m on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242) (Bug, mid-sprint)
- Worklog 10m on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032) (Bug, mid-sprint)
- Worklog 1h on [HIEV-6989](https://elocity.atlassian.net/browse/HIEV-6989) (Task, planned)
- Worklog 4h on [HIEV-6649](https://elocity.atlassian.net/browse/HIEV-6649) (Task, mid-sprint)
- Comment on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406): shared API contract to Dhanush on Thursday(13th Aug)
- Comment on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406): implemented OCPP side changes (DataTransfer msgs)
- Comment on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291): please do rebase
- Comment on [HIEV-7291](https://elocity.atlassian.net/browse/HIEV-7291): merged, please restart the service EOD
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): please keep everything in kWh
- Comment on [HIEV-7282](https://elocity.atlassian.net/browse/HIEV-7282): merged
- Comment on [HIEV-7275](https://elocity.atlassian.net/browse/HIEV-7275): added review comments please check and test the response
- Comment on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242): added review comments
- Comment on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032): changes are approved and waiting for rebase
- Comment on [HIEV-7032](https://elocity.atlassian.net/browse/HIEV-7032): new branch was created, reviewed below, its merged now
- Comment on [HIEV-6989](https://elocity.atlassian.net/browse/HIEV-6989): reviewed and ready to merge
- Comment on [HIEV-6649](https://elocity.atlassian.net/browse/HIEV-6649): addressed review comments and fixed few corner cases
- Comment on [HIEV-6649](https://elocity.atlassian.net/browse/HIEV-6649): it is merged

**2026-08-25** — logged 0.0d (0h) of 1.0d (8h) available, 1 comments

- Comment on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406): validated OCPP and implemented CPMS side comsumer for events

**2026-08-27** — logged 0.0d (0h) of 1.0d (8h) available, 7 comments

- Comment on [HIEV-7495](https://elocity.atlassian.net/browse/HIEV-7495): merged
- Comment on [HIEV-7491](https://elocity.atlassian.net/browse/HIEV-7491): merged
- Comment on [HIEV-7490](https://elocity.atlassian.net/browse/HIEV-7490): merged
- Comment on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406): validated CPMS changes found few gaps and worked on them
- Comment on [HIEV-7242](https://elocity.atlassian.net/browse/HIEV-7242): please test this on UAT, since this is merged just before UAT release, you wouldn’t have had enough time to test it on STG
- Comment on [HIEV-6988](https://elocity.atlassian.net/browse/HIEV-6988): merged
- Comment on [HIEV-6945](https://elocity.atlassian.net/browse/HIEV-6945): cpms unit tests will be reviewed after UAT release

**2026-08-31** — logged 0.6d (5h) of 1.0d (8h) available, 1 comments

- Worklog 5h on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406) (Task, planned)
- Comment on [HIEV-7406](https://elocity.atlassian.net/browse/HIEV-7406): worked on few changes in cpms, edge cases
