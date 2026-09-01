"""HTML shell for the August retrospective."""

import html as html_lib


def th(label: str, formula: str, num: bool = False) -> str:
    cls = " class='num'" if num else ""
    title = html_lib.escape(formula)
    return (
        f"<th{cls} title='{title}'>{html_lib.escape(label)}"
        f"<small class='formula'>{html_lib.escape(formula)}</small></th>"
    )


FORMULAS_HTML = """
      <section class="block" id="formulas">
        <h2>Formulas</h2>
        <p class="note">Every ratio, percentage, and “of available” figure on this page uses these identities. Units: <strong>1 person-day = 8 hours = 28 800 seconds</strong>. Days and hours are rounded for display (days to 1 decimal, hours to whole hours, ratios to 2 decimals, percentages to 0 or 1 decimal as labelled).</p>
        <div class="formula-grid">
          <div class="formula-card">
            <dt>Hours and days</dt>
            <dd>Convert Jira worklog seconds.</dd>
            <code>hours = seconds ÷ 3600
days = seconds ÷ 28 800</code>
          </div>
          <div class="formula-card">
            <dt>Available (person)</dt>
            <dd>Working days are Mon–Fri excluding Fri 28 Aug PH. Leave fraction is 1 (full day) or 0.5 (half day).</dd>
            <code>day_available = 1 − leave_fraction
  (0 on weekends and PH)
available_days = Σ day_available over 1–31 Aug
available_hours = available_days × 8
leave_days = Σ leave_fraction in August</code>
          </div>
          <div class="formula-card">
            <dt>Logged of available</dt>
            <dd>Not a percentage. Big number is days; small line is hours.</dd>
            <code>logged_days of available_days
logged_hours of available_hours</code>
          </div>
          <div class="formula-card">
            <dt>Utilisation</dt>
            <dd>Person and team. &gt; 1.0 means logged more than available. Colour: green ≥ 0.90, amber ≥ 0.75, else red.</dd>
            <code>util = logged_days ÷ available_days
team_util = Σ logged_days ÷ Σ available_days</code>
          </div>
          <div class="formula-card">
            <dt>Sprint planned / mid-sprint mix %</dt>
            <dd>Share of that person’s (or the team’s) August worklog seconds. Sprint planned = keys on the sprint plan. Mid-sprint = keys added after planning, not on the plan.</dd>
            <code>planned% = 100 × planned_seconds ÷ (planned + mid-sprint)
mid% = 100 × mid_sprint_seconds ÷ (planned + mid-sprint)</code>
          </div>
          <div class="formula-card">
            <dt>Estimation accuracy</dt>
            <dd>Same-scope only. Missing or NA sprint-plan PD → that key is skipped. 1.00 = exact; &gt; 1 over-ran the numbered estimate. Colour: green ≤ 1.10, amber ≤ 1.50, else red. Open/NA plan keys (e.g. EVLM) stay in sprint-planned mix, not in this ratio. The mix bar beside it is sprint-planned hours vs mid-sprint / ad hoc hours (share of all logged time).</dd>
            <code>ticket_acc = August_days_on_that_key ÷ sprint_plan_PD
person_acc = August_days_on_keys_with_numeric_PD ÷ sprint_plan_PD
mean_ticket_acc = average(ticket_acc)
  only keys with a numeric plan and logged &gt; 0</code>
          </div>
          <div class="formula-card">
            <dt>Logged-of-available bar fill</dt>
            <dd>How full the person bar is. Caps at 100% even if util &gt; 1.</dd>
            <code>bar% = min(100, 100 × logged_seconds ÷ available_seconds)</code>
          </div>
          <div class="formula-card">
            <dt>Bug-count bar fill</dt>
            <dd>Unique Bug keys with an August worklog or comment by that person.</dd>
            <code>bar% = 100 × person_bug_keys ÷ max(person_bug_keys)</code>
          </div>
          <div class="formula-card">
            <dt>Scrum attendance %</dt>
            <dd>Expected calls = recorded ~09:30 IST weekday scrums minus PH 28 minus leave that covers the call. Joining on leave is not a miss.</dd>
            <code>attendance% = 100 × attended_expected ÷ expected
missed = expected − attended_expected
avg_duration = mean(join duration on calls joined)</code>
          </div>
          <div class="formula-card">
            <dt>Heatmap cell colour</dt>
            <dd>Hours that calendar day from worklogs (or changelog fill date). Blank = 0h and not leave.</dd>
            <code>h1: 0 &lt; h &lt; 2 h2: 2 ≤ h &lt; 4
h3: 4 ≤ h &lt; 6 h4: 6 ≤ h &lt; 8 h5: h ≥ 8</code>
          </div>
        </div>
      </section>
"""

# Plain JS (not an f-string) so `{` / `}` stay valid.
EXPORT_JS = r"""
    function currentPerson() {
      return (document.getElementById("reportPerson") || {}).value || personFromUrl() || "";
    }
    function personSlug(name) {
      return String(name || "team")
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-+|-+$/g, "") || "team";
    }
    function filePrefix(name) {
      return name ? personSlug(name) : "team";
    }
    function csvCell(value) {
      const s = value == null ? "" : String(value);
      if (/[",\n\r]/.test(s)) return '"' + s.replace(/"/g, '""') + '"';
      return s;
    }
    function toCsv(headers, rows) {
      const lines = [headers.map(csvCell).join(",")];
      for (const row of rows) lines.push(row.map(csvCell).join(","));
      return "\uFEFF" + lines.join("\r\n") + "\r\n";
    }
    function cellText(el) {
      return (el && (el.innerText || el.textContent) || "").replace(/\s+/g, " ").trim();
    }
    function parseHd(text) {
      const t = String(text || "").trim();
      const both = t.match(/([\d.]+)\s*d\s*\(\s*([\d.]+)\s*h\s*\)/i);
      if (both) return { days: both[1], hours: both[2] };
      const daysOnly = t.match(/([\d.]+)\s*d/i);
      const hoursOnly = t.match(/([\d.]+)\s*h/i);
      return {
        days: daysOnly ? daysOnly[1] : "",
        hours: hoursOnly ? hoursOnly[1] : ""
      };
    }
    function parseTimepair(el) {
      const pair = el && el.querySelector ? el.querySelector(".timepair") : null;
      if (!pair) return { loggedDays: "", availDays: "", loggedHours: "", availHours: "", ...parseHd(cellText(el)) };
      const bold = pair.querySelectorAll("b");
      const small = pair.querySelector("small");
      const loggedDays = bold[0] ? String(bold[0].textContent).replace(/[^\d.]/g, "") : "";
      const availDays = bold[1] ? String(bold[1].textContent).replace(/[^\d.]/g, "") : "";
      let loggedHours = "", availHours = "";
      if (small) {
        const m = String(small.textContent).match(/([\d.]+)\s*h\s*of\s*([\d.]+)\s*h/i);
        if (m) {
          loggedHours = m[1];
          availHours = m[2];
        }
      }
      return { loggedDays, availDays, loggedHours, availHours, days: loggedDays, hours: loggedHours };
    }
    function personRows(selector, name) {
      return [...document.querySelectorAll(selector)].filter((el) => matchesPerson(el, name));
    }
    function mixPercents(td) {
      const mix = td && td.querySelector ? td.querySelector(".mix") : null;
      const title = (mix && mix.getAttribute("title")) || "";
      const on = title.match(/Sprint planned\s+([\d.]+)%/i);
      const off = title.match(/Mid-sprint\s+([\d.]+)%/i);
      return { on: on ? on[1] : "", off: off ? off[1] : "" };
    }
    function worklogHours(label) {
      const m = String(label || "").match(/([\d.]+)\s*h/i);
      return m ? m[1] : "";
    }

    const CRC_TABLE = (function () {
      const t = new Uint32Array(256);
      for (let n = 0; n < 256; n++) {
        let c = n;
        for (let k = 0; k < 8; k++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
        t[n] = c >>> 0;
      }
      return t;
    })();
    function crc32(bytes) {
      let c = 0xFFFFFFFF;
      for (let i = 0; i < bytes.length; i++) c = CRC_TABLE[(c ^ bytes[i]) & 0xFF] ^ (c >>> 8);
      return (c ^ 0xFFFFFFFF) >>> 0;
    }
    function u16(n) {
      const b = new Uint8Array(2);
      b[0] = n & 255;
      b[1] = (n >>> 8) & 255;
      return b;
    }
    function u32(n) {
      const b = new Uint8Array(4);
      b[0] = n & 255;
      b[1] = (n >>> 8) & 255;
      b[2] = (n >>> 16) & 255;
      b[3] = (n >>> 24) & 255;
      return b;
    }
    function concatBytes(parts) {
      let len = 0;
      for (const p of parts) len += p.length;
      const out = new Uint8Array(len);
      let o = 0;
      for (const p of parts) {
        out.set(p, o);
        o += p.length;
      }
      return out;
    }
    function zipStore(files) {
      const encoder = new TextEncoder();
      const locals = [];
      const centrals = [];
      let offset = 0;
      for (const file of files) {
        const nameBytes = encoder.encode(file.name);
        const data = encoder.encode(file.content);
        const crc = crc32(data);
        const local = concatBytes([
          u32(0x04034b50),
          u16(20),
          u16(0x0800),
          u16(0),
          u16(0),
          u16(0),
          u32(crc),
          u32(data.length),
          u32(data.length),
          u16(nameBytes.length),
          u16(0),
          nameBytes,
          data
        ]);
        const central = concatBytes([
          u32(0x02014b50),
          u16(20),
          u16(20),
          u16(0x0800),
          u16(0),
          u16(0),
          u16(0),
          u32(crc),
          u32(data.length),
          u32(data.length),
          u16(nameBytes.length),
          u16(0),
          u16(0),
          u16(0),
          u16(0),
          u32(0),
          u32(offset),
          nameBytes
        ]);
        locals.push(local);
        centrals.push(central);
        offset += local.length;
      }
      const centralDir = concatBytes(centrals);
      const end = concatBytes([
        u32(0x06054b50),
        u16(0),
        u16(0),
        u16(files.length),
        u16(files.length),
        u32(centralDir.length),
        u32(offset),
        u16(0)
      ]);
      return concatBytes([...locals, centralDir, end]);
    }
    function downloadBlob(filename, blob) {
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 1500);
    }

    function exportPeopleCsv(name) {
      const headers = [
        "person",
        "plan_pd",
        "leave_days",
        "expected_days",
        "expected_hours",
        "logged_days",
        "logged_hours",
        "util",
        "sprint_planned_pct",
        "mid_sprint_pct",
        "sprint_planned_days",
        "sprint_planned_hours",
        "mid_sprint_days",
        "mid_sprint_hours",
        "accuracy",
        "worklogs",
        "comments"
      ];
      const rows = personRows("#peopleBody tr", name).map((tr) => {
        const td = tr.children;
        const logged = parseTimepair(td[3]);
        const on = parseTimepair(td[6]);
        const off = parseTimepair(td[7]);
        const mix = mixPercents(td[5]);
        return [
          cellText(td[0]),
          cellText(td[1]),
          cellText(td[2]).replace(/d$/i, ""),
          logged.availDays,
          logged.availHours,
          logged.loggedDays,
          logged.loggedHours,
          cellText(td[4]),
          mix.on,
          mix.off,
          on.loggedDays,
          on.loggedHours,
          off.loggedDays,
          off.loggedHours,
          cellText(td[8]),
          cellText(td[9]),
          cellText(td[10])
        ];
      });
      return toCsv(headers, rows);
    }
    function exportSheetCsv(name) {
      const headers = [
        "jira",
        "section",
        "feature",
        "assignee",
        "plan_pd",
        "logged_days",
        "logged_hours",
        "assignee_available_days",
        "assignee_available_hours",
        "accuracy",
        "status"
      ];
      const rows = personRows("#sheetBody tr", name).map((tr) => {
        const td = tr.children;
        const logged = parseTimepair(td[5]);
        return [
          cellText(td[0]),
          cellText(td[1]),
          cellText(td[2]),
          cellText(td[3]),
          cellText(td[4]),
          logged.loggedDays,
          logged.loggedHours,
          logged.availDays,
          logged.availHours,
          cellText(td[6]),
          cellText(td[7])
        ];
      });
      return toCsv(headers, rows);
    }
    function exportOffsheetCsv(name) {
      const headers = [
        "jira",
        "type",
        "summary",
        "logged_by",
        "logged_days",
        "logged_hours",
        "available_days",
        "available_hours",
        "comments",
        "status"
      ];
      const rows = personRows("#offsheetBody tr", name).map((tr) => {
        const td = tr.children;
        const logged = parseTimepair(td[4]);
        return [
          cellText(td[0]),
          cellText(td[1]),
          cellText(td[2]),
          cellText(td[3]),
          logged.loggedDays,
          logged.loggedHours,
          logged.availDays,
          logged.availHours,
          cellText(td[5]),
          cellText(td[6])
        ];
      });
      return toCsv(headers, rows);
    }
    function exportBugsCsv(name) {
      const headers = [
        "key",
        "summary",
        "status",
        "worked_by",
        "august_days",
        "august_hours"
      ];
      const rows = personRows("#bugBody tr", name).map((tr) => {
        const td = tr.children;
        const hd = parseHd(cellText(td[4]));
        return [
          cellText(td[0]),
          cellText(td[1]),
          cellText(td[2]),
          cellText(td[3]),
          hd.days,
          hd.hours
        ];
      });
      return toCsv(headers, rows);
    }
    function exportHeatmapCsv(name) {
      const headCells = [...document.querySelectorAll("#daily thead th")];
      const dateCols = [];
      headCells.forEach((th, i) => {
        if (!th.classList.contains("dayh")) return;
        const day = parseInt(String(th.childNodes[0] && th.childNodes[0].textContent).trim(), 10);
        if (!day) return;
        dateCols.push({ index: i, iso: "2026-08-" + String(day).padStart(2, "0") });
      });
      const headers = ["person", ...dateCols.map((c) => c.iso), "logged_days", "logged_hours", "expected_days", "expected_hours"];
      const rows = personRows("#heatBody tr", name).map((tr) => {
        const cells = [...tr.children];
        const logged = parseTimepair(cells[cells.length - 1]);
        const values = dateCols.map((c) => cellText(cells[c.index]));
        return [cellText(cells[0]), ...values, logged.loggedDays, logged.loggedHours, logged.availDays, logged.availHours];
      });
      return toCsv(headers, rows);
    }
    function exportScrumCsv(name) {
      const headers = [
        "person",
        "expected",
        "attended",
        "missed",
        "attended_on_leave",
        "attendance_pct",
        "avg_duration"
      ];
      const rows = personRows("#scrumBody tr", name).map((tr) => {
        const td = tr.children;
        return [
          cellText(td[0]),
          cellText(td[1]),
          cellText(td[2]),
          cellText(td[3]),
          cellText(td[4]),
          cellText(td[5]),
          cellText(td[6])
        ];
      });
      return toCsv(headers, rows);
    }
    function exportScrumDaysCsv(name) {
      const headCells = [...document.querySelectorAll("#scrumTicks thead th")];
      const dateCols = [];
      headCells.forEach((th, i) => {
        if (!th.classList.contains("dayh")) return;
        const day = parseInt(String(th.childNodes[0] && th.childNodes[0].textContent).trim(), 10);
        if (!day) return;
        dateCols.push({ index: i, iso: "2026-08-" + String(day).padStart(2, "0") });
      });
      const headers = ["person", ...dateCols.map((c) => c.iso)];
      const rows = personRows("#scrumTickBody tr", name).map((tr) => {
        const cells = [...tr.children];
        const values = dateCols.map((c) => cellText(cells[c.index]));
        return [cellText(cells[0]), ...values];
      });
      return toCsv(headers, rows);
    }
    function exportJournalCsv(name) {
      const headers = ["person", "date", "kind", "key", "hours", "sprint_planned", "comment"];
      const rows = [];
      personRows("#journal .person-day", name).forEach((section) => {
        const person = (section.getAttribute("data-person") || cellText(section.querySelector("h3"))).replace(/\s+\d.*/, "").trim();
        section.querySelectorAll("details").forEach((block) => {
          const summary = cellText(block.querySelector("summary"));
          const dateMatch = summary.match(/(\d{4}-\d{2}-\d{2})/);
          const date = dateMatch ? dateMatch[1] : "";
          block.querySelectorAll("li").forEach((li) => {
            const meta = cellText(li.querySelector(".meta"));
            const key = cellText(li.querySelector("a"));
            const typeEl = li.querySelector(".type");
            const typeText = cellText(typeEl);
            const onSheet = /planned/i.test(typeText) && !/mid-sprint/i.test(typeText)
              ? "planned"
              : (/mid-sprint/i.test(meta + " " + typeText) ? "mid-sprint" : (/planned/i.test(typeText) ? "planned" : ""));
            let comment = "";
            const html = li.innerHTML;
            const dash = html.split(" — ");
            if (dash.length > 1) {
              const tmp = document.createElement("div");
              tmp.innerHTML = dash.slice(1).join(" — ");
              comment = cellText(tmp);
            }
            const kind = /^worklog/i.test(meta) ? "worklog" : "comment";
            rows.push([
              person,
              date,
              kind,
              key,
              kind === "worklog" ? worklogHours(meta) : "",
              onSheet,
              comment
            ]);
          });
        });
      });
      return toCsv(headers, rows);
    }

    async function exportCsvZip() {
      const btn = document.getElementById("exportCsvZip");
      const name = currentPerson();
      const prefix = filePrefix(name);
      if (btn) btn.disabled = true;
      try {
        const files = [
          { name: prefix + "-people.csv", content: exportPeopleCsv(name) },
          { name: prefix + "-sprint-planned.csv", content: exportSheetCsv(name) },
          { name: prefix + "-mid-sprint.csv", content: exportOffsheetCsv(name) },
          { name: prefix + "-bugs.csv", content: exportBugsCsv(name) },
          { name: prefix + "-heatmap.csv", content: exportHeatmapCsv(name) },
          { name: prefix + "-scrum.csv", content: exportScrumCsv(name) },
          { name: prefix + "-scrum-days.csv", content: exportScrumDaysCsv(name) },
          { name: prefix + "-journal.csv", content: exportJournalCsv(name) },
          { name: prefix + "-call-notes.csv", content: (typeof exportNotesCsv === "function" ? exportNotesCsv(name) : "") }
        ];
        const zipName = prefix + "-august-2026-csvs.zip";
        const bytes = zipStore(files);
        downloadBlob(zipName, new Blob([bytes], { type: "application/zip" }));
      } finally {
        if (btn) btn.disabled = false;
      }
    }
    const exportBtn = document.getElementById("exportCsvZip");
    if (exportBtn) exportBtn.addEventListener("click", () => { exportCsvZip(); });
"""

NOTES_JS = r"""
    const NOTE_FIELDS = ["on_call", "went_well", "hard", "mid_sprint", "estimation", "quality", "blockers", "next_actions", "shoutout"];
    const NOTES_STORE = "august26-person-notes";
    function emptyPersonNotes() {
      const o = {};
      NOTE_FIELDS.forEach((k) => { o[k] = ""; });
      return o;
    }
    function parseNotesPayload(text) {
      try {
        const data = JSON.parse(text || "{}");
        if (!data.people || typeof data.people !== "object") data.people = {};
        return data;
      } catch (e) {
        return { sprint: "August 2026", updated: "", people: {} };
      }
    }
    const PUBLISHED_NOTES = parseNotesPayload((document.getElementById("personNotesPublished") || {}).textContent || "{}");
    let notesState = parseNotesPayload(localStorage.getItem(NOTES_STORE) || "null");
    if (!Object.keys(notesState.people || {}).length) {
      notesState = JSON.parse(JSON.stringify(PUBLISHED_NOTES));
    } else {
      const merged = JSON.parse(JSON.stringify(PUBLISHED_NOTES));
      merged.people = Object.assign({}, PUBLISHED_NOTES.people || {}, notesState.people || {});
      if (notesState.updated) merged.updated = notesState.updated;
      notesState = merged;
    }
    function notesFingerprint(data) {
      return JSON.stringify((data && data.people) || {});
    }
    function notesHasText(entry) {
      return NOTE_FIELDS.some((k) => String((entry || {})[k] || "").trim());
    }
    function snippet(text) {
      const t = String(text || "").replace(/\s+/g, " ").trim();
      if (!t) return "—";
      const cut = t.length > 80 ? t.slice(0, 77) + "…" : t;
      return cut.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
    }
    function persistNotesDraft() {
      notesState.updated = new Date().toISOString();
      localStorage.setItem(NOTES_STORE, JSON.stringify(notesState));
      updateNotesStatus();
      renderNotesTeam();
    }
    function updateNotesStatus() {
      const el = document.getElementById("notesStatus");
      if (!el) return;
      const dirty = notesFingerprint(notesState) !== notesFingerprint(PUBLISHED_NOTES);
      el.textContent = dirty
        ? "Saved on this computer only. When the call is done, say “commit and push call notes” here so the published page updates for everyone."
        : "These notes are already on the published page. Edit if you need to, then say “commit and push call notes” again.";
    }
    function renderNotesTeam() {
      const body = document.getElementById("notesTeamBody");
      if (!body) return;
      const names = Object.keys(PERSON_STATS || {}).sort();
      body.innerHTML = names.map((name) => {
        const entry = (notesState.people || {})[name] || {};
        const mark = notesHasText(entry) ? " has-notes" : "";
        const safe = name.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
        return "<tr class='" + mark.trim() + "'><td><button type='button' class='name-link' data-open-person=\"" + safe.replace(/"/g, "&quot;") + "\">" + safe + "</button></td>"
          + "<td>" + snippet(entry.on_call) + "</td>"
          + "<td>" + snippet(entry.went_well) + "</td>"
          + "<td>" + snippet(entry.hard) + "</td>"
          + "<td>" + snippet(entry.next_actions) + "</td></tr>";
      }).join("");
    }
    function fillNotesFacts(name) {
      const box = document.getElementById("notesFacts");
      const stats = PERSON_STATS[name];
      if (!box) return;
      if (!stats) { box.innerHTML = ""; return; }
      const groups = [
        {
          title: "Capacity",
          rows: [
            ["Logged of available", stats.logged_html],
            ["Util", stats.util],
            ["Leave", stats.leave],
            ["Scrum", stats.scrum_html || "—"]
          ]
        },
        {
          title: "Sprint mix",
          rows: [
            ["Sprint planned PD", stats.plan],
            ["Sprint planned time", stats.on_html],
            ["Mid-sprint time", stats.off_html],
            ["Planned tickets touched", String(stats.sheet)],
            ["Mid-sprint keys touched", String(stats.offsheet)]
          ]
        },
        {
          title: "Bugs & tasks",
          rows: [
            ["Bugs worked", String(stats.bugs)],
            ["Bug time", stats.bug_hours_html],
            ["Task time", stats.task_hours_html]
          ]
        }
      ];
      box.innerHTML = groups.map((g) => {
        const items = g.rows.map((r) => "<div><dt>" + r[0] + "</dt><dd>" + r[1] + "</dd></div>").join("");
        return "<section class='notes-metric-group'><h4>" + g.title + "</h4><div class='notes-metric-rows'>" + items + "</div></section>";
      }).join("");
    }
    function refreshCallNotes(name) {
      const title = document.getElementById("notesEditorTitle");
      if (title) title.textContent = name ? ("Call notes · " + name) : "Call notes";
      fillNotesFacts(name);
      const entry = name ? ((notesState.people || {})[name] || emptyPersonNotes()) : emptyPersonNotes();
      document.querySelectorAll("#notesEditor [data-note]").forEach((el) => {
        el.value = name ? (entry[el.getAttribute("data-note")] || "") : "";
        el.disabled = !name;
      });
      renderNotesTeam();
      updateNotesStatus();
    }
    document.querySelectorAll("#notesEditor [data-note]").forEach((el) => {
      el.addEventListener("input", () => {
        const name = currentPerson();
        if (!name) return;
        if (!notesState.people) notesState.people = {};
        if (!notesState.people[name]) notesState.people[name] = emptyPersonNotes();
        notesState.people[name][el.getAttribute("data-note")] = el.value;
        persistNotesDraft();
      });
    });
    fetch("person-notes.json", { cache: "no-store" }).then((res) => {
      if (!res.ok) return null;
      return res.json();
    }).then((remote) => {
      if (!remote || !remote.people) return;
      const remoteFp = notesFingerprint(remote);
      const pubFp = notesFingerprint(PUBLISHED_NOTES);
      const draftFp = notesFingerprint(notesState);
      Object.assign(PUBLISHED_NOTES, remote);
      if (!PUBLISHED_NOTES.people) PUBLISHED_NOTES.people = {};
      if (draftFp === pubFp || draftFp === notesFingerprint({ people: {} })) {
        notesState = JSON.parse(JSON.stringify(PUBLISHED_NOTES));
        localStorage.setItem(NOTES_STORE, JSON.stringify(notesState));
      } else if (remoteFp !== pubFp && draftFp === pubFp) {
        notesState = JSON.parse(JSON.stringify(PUBLISHED_NOTES));
      }
      refreshCallNotes(currentPerson());
    }).catch(() => {});
    function exportNotesCsv(name) {
      const headers = ["person"].concat(NOTE_FIELDS);
      const names = name ? [name] : Object.keys(PERSON_STATS || {}).sort();
      const rows = names.map((p) => {
        const entry = (notesState.people || {})[p] || {};
        return [p].concat(NOTE_FIELDS.map((k) => entry[k] || ""));
      });
      return toCsv(headers, rows);
    }
"""


def render_page(
    *,
    total_plan,
    total_hours,
    total_days,
    kpi_logged,
    team_util,
    avg_acc,
    off_count,
    off_hours_label,
    on_pct,
    off_pct,
    on_hours_label,
    off_mix_label,
    people_trs,
    people_mix,
    ticket_trs,
    offsheet_trs,
    type_opts,
    offsheet_count,
    person_acc_trs,
    bug_count,
    bug_note,
    bug_bars,
    bug_detail,
    fh_bug,
    fh_task,
    fh_other,
    fix_trs,
    daily_head,
    daily_body,
    kpi_scrum,
    scrum_note,
    scrum_trs,
    scrum_tick_head,
    scrum_tick_body,
    person_opts,
    person_stats_json,
    person_notes_json,
    journal,
) -> str:
    assignee_field = (
        '<label class="field assignee-field">Assignee '
        '<select class="js-assignee-filter" aria-label="Filter by assignee">'
        '<option value="">All (team)</option>'
        f"{person_opts}"
        "</select></label>"
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>August 2026 sprint retrospective</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,560;9..144,650&family=Source+Sans+3:wght@400;600;650&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <div class="layout">
    <nav class="toc">
      <div class="brand">Sprint retro<small>August 2026 · HIEV</small></div>
      <label class="nav-person">Assignee
        <select id="reportPerson" class="js-assignee-filter">
          <option value="">All (team)</option>
          {person_opts}
        </select>
      </label>
      <span class="nav-hint" id="personViewHint">All (team)</span>
      <a href="#overview">Overview</a>
      <a href="#formulas">Formulas</a>
      <a href="#people">People</a>
      <a href="#sheet">Sprint planned</a>
      <a href="#offsheet">Mid-sprint</a>
      <a href="#accuracy">Estimation</a>
      <a href="#quality">Bugs &amp; fix hours</a>
      <a href="#daily">Daily time</a>
      <a href="#scrum">Scrum attendance</a>
      <a href="#notes">Call notes</a>
      <a href="#journal">Work log</a>
    </nav>
    <div class="content">
      <header class="hero" id="overview">
        <h1>August 2026 sprint retrospective</h1>
        <p class="lead" id="heroLead">Sprint planned tickets from Deepak’s August 26 workbook, plus every HIEV task and bug the team logged time or comments on during 1–31 Aug 2026 — including work added mid-sprint. Conversion is fixed: <strong>8 hours = 1 person-day</strong>. Use the <strong>Assignee</strong> filter (sticky bar, sidebar, or any table) to show one person, or <strong>All (team)</strong> for the full set. Click a name in a table for the same filter.</p>
        <div class="meta-row">
          <span class="chip">Period 1–31 Aug 2026</span>
          <span class="chip">8h = 1d</span>
          <span class="chip sheet team-only">Sprint planned {on_hours_label}</span>
          <span class="chip other team-only">Mid-sprint {off_mix_label}</span>
          <span class="chip sheet person-only" id="personOnChip" hidden></span>
          <span class="chip other person-only" id="personOffChip" hidden></span>
          <span class="chip">Jira project HIEV</span>
        </div>
        <div class="export-bar">
          <button type="button" class="export-btn" id="exportCsvZip">Export CSV</button>
          <span class="export-hint" id="exportHint">Downloads a zip of UTF-8 CSVs for the full team. An assignee filter exports that person only.</span>
        </div>
      </header>
      <div class="assignee-bar" role="search">
        {assignee_field}
        <span class="assignee-bar-hint">Filters tables, heatmaps, bar charts, and the work log. Synced with the sidebar and <code>?person=</code>.</span>
      </div>

      <div class="kpis team-only">
        <div class="kpi"><strong>{total_plan:.0f} PD</strong><span>Sprint planned estimates<small class="formula">Σ sprint-plan PD (NA excluded)</small></span></div>
        <div class="kpi"><strong>{kpi_logged}</strong><span>Logged of available<small class="formula">Σ logged of Σ available · 8h = 1d</small></span></div>
        <div class="kpi"><strong>{team_util if team_util is not None else "n/a"}</strong><span>Team util<small class="formula">Σ logged days ÷ Σ available days</small></span></div>
        <div class="kpi"><strong>{avg_acc if avg_acc is not None else "n/a"}</strong><span>Mean ticket accuracy<small class="formula">avg(Aug days on key ÷ sprint-plan PD) for worked keys</small></span></div>
        <div class="kpi"><strong>{off_count}</strong><span>Mid-sprint keys<small class="formula">{off_hours_label} · not in sprint planning</small></span></div>
        <div class="kpi"><strong>{kpi_scrum}</strong><span>Scrum attendance<small class="formula">attended expected ÷ expected (leave-adjusted)</small></span></div>
      </div>
      <div class="kpis person-only" id="personKpis" hidden>
        <div class="kpi"><strong id="pkLogged"></strong><span>Logged of available<small class="formula">logged days of available days</small></span></div>
        <div class="kpi"><strong id="pkLeave"></strong><span>Leave<small class="formula">Σ leave fraction in August</small></span></div>
        <div class="kpi"><strong id="pkUtil"></strong><span>Util<small class="formula">logged days ÷ available days</small></span></div>
        <div class="kpi"><strong id="pkPlan"></strong><span>Sprint planned PD<small class="formula">Σ sprint-plan PD for this assignee</small></span></div>
        <div class="kpi"><strong id="pkBugs"></strong><span>Unique bugs worked<small class="formula">count of Bug keys with Aug log or comment</small></span></div>
        <div class="kpi"><strong id="pkScrum"></strong><span>Scrum attendance<small class="formula">attended expected ÷ expected</small></span></div>
      </div>
      {FORMULAS_HTML}

      <div class="split">
        <div class="card team-only">
          <h2>Where August time went</h2>
          <p class="note">Share of logged hours on <strong>sprint planned</strong> tickets versus <strong>mid-sprint</strong> work (added after planning).<small class="formula">planned% = 100 × planned seconds ÷ (planned + mid-sprint); mid% = 100 × mid-sprint seconds ÷ (planned + mid-sprint)</small></p>
          <div class="mix" style="height:14px;margin:12px 0 8px">
            <span class="on" style="width:{on_pct}%"></span>
            <span class="off" style="width:{off_pct}%"></span>
          </div>
          <div class="legend">
            <span><i class="swatch sheet"></i>Sprint planned {on_pct}%</span>
            <span><i class="swatch other"></i>Mid-sprint {off_pct}%</span>
          </div>
          <p class="note">Nine long-running tickets exceeded Jira’s 20-worklog payload cap. Missing August logs were rebuilt from changelog time deltas and checked against each issue’s timespent.</p>
        </div>
        <div class="card">
          <h2>Logged of available</h2>
          <p class="note">Bar fills toward that person’s available time. Label is <em>logged of available</em> (days, then hours).<small class="formula">fill% = min(100, 100 × logged seconds ÷ available seconds)</small></p>
          <div class="controls">{assignee_field}</div>
          <div class="bars" id="loggedBars">{people_mix}</div>
          <p class="empty-msg" data-empty-for-bars="loggedBars" hidden>No logged-of-available row for this person.</p>
        </div>
      </div>

      <section class="block" id="people">
        <h2>1. Planned vs actual</h2>
        <p class="note">Every time figure is <strong>logged of available</strong>: days first, hours underneath. See <a href="#formulas">Formulas</a>.</p>
        <div class="controls">{assignee_field}</div>
        <div class="legend"><span><i class="swatch sheet"></i>Sprint planned</span><span><i class="swatch other"></i>Mid-sprint</span></div>
        <div class="wrap">
          <table>
            <thead>
              <tr>
                {th("Person", "Canonical name")}
                {th("Plan PD", "Σ sprint-plan PD for this assignee (NA excluded)", True)}
                {th("Leave", "Σ leave fraction in August", True)}
                {th("Logged of available", "logged days of available days", True)}
                {th("Util", "logged days ÷ available days", True)}
                {th("Mix", "planned% = 100 × sprint-planned seconds ÷ (planned + mid-sprint)")}
                {th("Sprint planned of avail", "sprint-planned days of available days", True)}
                {th("Mid-sprint of avail", "mid-sprint days of available days", True)}
                {th("Accuracy", "August days on keys with a numeric PD ÷ sprint-plan PD", True)}
                {th("Logs", "count of August worklogs", True)}
                {th("Comments", "count of August comments", True)}
              </tr>
            </thead>
            <tbody id="peopleBody">{people_trs}</tbody>
          </table>
        </div>
      </section>

      <section class="block" id="sheet">
        <h2>Sprint planned tickets</h2>
        <p class="note team-only">Tickets that were part of sprint planning (August 26 workbook). Search by feature, assignee, or key.</p>
        <p class="note person-only" id="sheetPersonNote" hidden></p>
        <div class="controls">
          {assignee_field}
          <label class="field">Search <input type="search" id="sheetSearch" placeholder="Filter sprint planned…" /></label>
        </div>
        <div class="wrap tall">
          <table>
            <thead>
              <tr>
                {th("Jira", "Issue key")}
                {th("Section", "Sprint-plan section")}
                {th("Feature", "Sprint-plan feature")}
                {th("Assignee", "Sprint-plan assignee")}
                {th("Plan", "Sprint-plan PD", True)}
                {th("Logged of assignee avail", "August days on this key of assignee available days", True)}
                {th("Accuracy", "August days on this key ÷ sprint-plan PD", True)}
                {th("Status", "Jira status")}
              </tr>
            </thead>
            <tbody id="sheetBody">{ticket_trs}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="sheetBody" hidden>No sprint-planned tickets for this person.</p>
      </section>

      <section class="block" id="offsheet">
        <h2>Mid-sprint tickets</h2>
        <p class="note team-only">{offsheet_count} keys had August worklogs or comments but were <strong>not</strong> in sprint planning — they were added mid-sprint. Included in person totals, heatmap, and the journal (marked <em>mid-sprint</em>).</p>
        <p class="note person-only" id="offsheetPersonNote" hidden></p>
        <div class="controls">
          {assignee_field}
          <label class="field">Type
            <select id="offTypeFilter">
              <option value="">All types</option>
              {type_opts}
            </select>
          </label>
          <label class="field">Search <input type="search" id="offSearch" placeholder="Filter mid-sprint…" /></label>
        </div>
        <div class="wrap tall">
          <table>
            <thead>
              <tr>
                {th("Jira", "Issue key")}
                {th("Type", "Jira issuetype")}
                {th("Summary", "Jira summary")}
                {th("Logged by", "People with August worklogs on this key")}
                {th("Logged of available", "August days on this key of first logger’s available days", True)}
                {th("Comments", "August comment count", True)}
                {th("Status", "Jira status")}
              </tr>
            </thead>
            <tbody id="offsheetBody">{offsheet_trs}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="offsheetBody" hidden>No mid-sprint keys this person logged or commented on.</p>
      </section>

      <section class="block" id="accuracy">
        <h2>2. Estimation accuracy</h2>
        <p class="note team-only">Accuracy uses only sprint-planned keys with a numeric PD. The mix bar is share of <strong>all logged August hours</strong>: sprint planned (including open/NA PD keys) vs mid-sprint / ad hoc. Green ≤1.10, amber ≤1.50, red above.</p>
        <div class="legend"><span><i class="swatch sheet"></i>Sprint planned</span><span><i class="swatch other"></i>Mid-sprint / ad hoc</span></div>
        <p class="note person-only" id="accPersonNote" hidden></p>
        <div class="controls">{assignee_field}</div>
        <div class="wrap">
          <table>
            <thead>
              <tr>
                {th("Person", "Canonical name")}
                {th("Plan PD", "Σ sprint-plan PD", True)}
                {th("Actual on plan", "August days on sprint-planned keys that have a numeric PD", True)}
                {th("Logged of available", "all August days of available days", True)}
                {th("Sprint vs mid-sprint", "planned% = 100 × sprint-planned seconds ÷ (planned + mid-sprint)")}
                {th("Accuracy", "August days on keys with a numeric PD ÷ sprint-plan PD", True)}
              </tr>
            </thead>
            <tbody id="accBody">{person_acc_trs}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="accBody" hidden>No numeric sprint-plan estimate for this person, so accuracy is not computed.</p>
      </section>

      <section class="block" id="quality">
        <h2>3. Bugs worked in August and 4. Fix hours</h2>
        <p class="note team-only">{bug_note}</p>
        <p class="note person-only" id="bugPersonNote" hidden></p>
        <div class="card">
          <h2>Bugs worked in August</h2>
          <p class="note">Bars are unique bug keys each person logged time on or commented on in August.<small class="formula">fill% = 100 × person bug keys ÷ max person bug keys</small></p>
          <div class="controls">{assignee_field}</div>
          <div class="bars" id="bugBars">{bug_bars}</div>
          <p class="empty-msg" data-empty-for-bars="bugBars" hidden>No August bug worklogs or comments for this person.</p>
        </div>
        <h3 class="note" style="margin-top:18px">Fix hours</h3>
        <p class="note team-only">Bugs {fh_bug}. Tasks {fh_task}. Other {fh_other}.</p>
        <p class="note person-only" id="fhPersonNote" hidden></p>
        <div class="controls">{assignee_field}</div>
        <div class="wrap">
          <table>
            <thead><tr>{th("Person", "Canonical name")}{th("Bug of available", "Bug worklog days of available days", True)}{th("Task of available", "Task/Sub-task/Story/Epic worklog days of available days", True)}</tr></thead>
            <tbody id="fixBody">{fix_trs}</tbody>
          </table>
        </div>
        <h3 class="note" style="margin-top:18px">Bug list</h3>
        <div class="controls">{assignee_field}</div>
        <div class="wrap">
          <table>
            <thead>
              <tr>
                {th("Key", "Bug issue key")}
                {th("Summary", "Jira summary")}
                {th("Status", "Jira status")}
                {th("Who worked it", "People with August worklog or comment")}
                {th("August hours", "Σ August worklog hours on this bug", True)}
              </tr>
            </thead>
            <tbody id="bugBody">{bug_detail}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="bugBody" hidden>No bugs this person worked in August.</p>
      </section>

      <section class="block" id="daily">
        <h2>5. Daily logged time</h2>
        <p class="note">Cell values are hours that day. Row total is <strong>logged of available</strong> for the month. Blank = no Jira log. <strong>L</strong> / <strong>½L</strong> = leave (available 0 or 4h). Saturday gold, Sunday rose, Fri 28 PH green, leave purple.<small class="formula">cell hours = worklog seconds that date ÷ 3600; colour bands 0–2, 2–4, 4–6, 6–8, 8+</small></p>
        <div class="legend">
          <span>Scale:&nbsp;</span>
          <span class="heat h1" style="padding:2px 8px">0–2h</span>
          <span class="heat h2" style="padding:2px 8px">2–4h</span>
          <span class="heat h3" style="padding:2px 8px">4–6h</span>
          <span class="heat h4" style="padding:2px 8px">6–8h</span>
          <span class="heat h5" style="padding:2px 8px">8h+</span>
          <span class="heat sat" style="padding:2px 8px; background:#f3d18a; color:#5c3d08">Saturday</span>
          <span class="heat sun" style="padding:2px 8px; background:#e8a8b4; color:#6b1a2c">Sunday</span>
          <span class="heat holiday" style="padding:2px 8px; background:#8fce7a; color:#1d4a12">Public holiday</span>
          <span class="heat leave" style="padding:2px 8px; background:#d4c4f0; color:#3b2670">Leave</span>
        </div>
        <div class="controls">{assignee_field}</div>
        <div class="wrap heatmap">
          <table>
            <thead><tr>{th("Person", "Canonical name")}{daily_head}{th("Logged of available", "month logged days of available days", True)}</tr></thead>
            <tbody id="heatBody">{daily_body}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="heatBody" hidden>No heatmap row for this person.</p>
      </section>

      <section class="block" id="scrum">
        <h2>6. Scrum call attendance</h2>
        <p class="note team-only">{scrum_note}</p>
        <p class="note person-only" id="scrumPersonNote" hidden></p>
        <div class="controls">{assignee_field}</div>
        <div class="wrap">
          <table>
            <thead>
              <tr>
                {th("Person", "Canonical name")}
                {th("Expected", "recorded morning scrums minus leave covering the call", True)}
                {th("Attended", "expected calls joined", True)}
                {th("Missed", "expected − attended", True)}
                {th("On leave joined", "joined while on leave (not a miss)", True)}
                {th("Attendance", "100 × attended ÷ expected", True)}
                {th("Avg duration", "mean join duration on calls joined", True)}
              </tr>
            </thead>
            <tbody id="scrumBody">{scrum_trs}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="scrumBody" hidden>No scrum attendance row for this person.</p>
        <h3 class="note" style="margin-top:18px">Call days</h3>
        <p class="note">P present · M missed · L leave (not expected) · A attended on leave. Columns are the 20 recorded ~09:30 IST calls only.</p>
        <div class="legend">
          <span class="heat scrum-present" style="padding:2px 8px">P present</span>
          <span class="heat scrum-missed" style="padding:2px 8px">M missed</span>
          <span class="heat scrum-leave" style="padding:2px 8px">L leave</span>
          <span class="heat scrum-leave-attended" style="padding:2px 8px">A on leave</span>
        </div>
        <div class="controls">{assignee_field}</div>
        <div class="wrap heatmap">
          <table id="scrumTicks">
            <thead><tr>{th("Person", "Canonical name")}{scrum_tick_head}</tr></thead>
            <tbody id="scrumTickBody">{scrum_tick_body}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="scrumTickBody" hidden>No scrum call-day row for this person.</p>
      </section>

      <section class="block" id="notes">
        <h2>Call notes</h2>
        <ol class="notes-steps">
          <li><strong>Pick someone</strong> in Assignee (or the table below).</li>
          <li><strong>Type</strong> what they said. It saves on this computer as you type.</li>
          <li><strong>When the call is done</strong>, tell me here: <em>commit and push call notes</em>. I write them into the repo and push so the published page shows the same notes to everyone.</li>
        </ol>
        <p class="note" id="notesStatus"></p>
        <div class="card team-only" id="notesTeam">
          <h2>Team</h2>
          <p class="note">Click a name to open their sheet. After notes are published, this is the glance view for everyone.</p>
          <div class="wrap">
            <table>
              <thead>
                <tr>
                  <th>Person</th>
                  <th>On the call</th>
                  <th>Went well</th>
                  <th>Hard / slipped</th>
                  <th>Next sprint</th>
                </tr>
              </thead>
              <tbody id="notesTeamBody"></tbody>
            </table>
          </div>
        </div>
        <div class="card person-only notes-editor" id="notesEditor" hidden>
          <h2 id="notesEditorTitle">Notes</h2>
          <h3 class="notes-sub">From this report</h3>
          <p class="note">Read-only. Pulled from Jira and the sprint plan so you don’t retype numbers.</p>
          <div class="notes-facts" id="notesFacts"></div>
          <h3 class="notes-sub">What they said</h3>
          <label class="notes-field notes-field-lead">On the call
            <textarea data-note="on_call" rows="5" placeholder="Capture what they said…"></textarea>
          </label>
          <h3 class="notes-sub">Retro prompts</h3>
          <div class="notes-prompts">
            <label class="notes-field">What went well
              <textarea data-note="went_well" rows="4"></textarea>
            </label>
            <label class="notes-field">What was hard or slipped
              <textarea data-note="hard" rows="4"></textarea>
            </label>
            <label class="notes-field">Mid-sprint / ad hoc — why it landed
              <textarea data-note="mid_sprint" rows="4"></textarea>
            </label>
            <label class="notes-field">Plan vs actual / estimation
              <textarea data-note="estimation" rows="4"></textarea>
            </label>
            <label class="notes-field">Bugs / quality
              <textarea data-note="quality" rows="4"></textarea>
            </label>
            <label class="notes-field">Blockers / help needed
              <textarea data-note="blockers" rows="4"></textarea>
            </label>
            <label class="notes-field">Action for next sprint
              <textarea data-note="next_actions" rows="4"></textarea>
            </label>
            <label class="notes-field">Shout-out
              <textarea data-note="shoutout" rows="4"></textarea>
            </label>
          </div>
        </div>
      </section>

      <section class="block" id="journal">
        <h2>Daily worklogs and comments</h2>
        <p class="note">Expand a day to see ticket keys, time spent, and comments. <em>planned</em> = sprint planned; <em>mid-sprint</em> = added after planning. The assignee filter applies here with the rest of the report.</p>
        <div class="controls">{assignee_field}</div>
        <div id="journal">{journal}</div>
        <p class="empty-msg" id="journalEmpty" hidden>No August worklogs or comments for this person.</p>
      </section>

      <footer class="foot">Generated 31 Aug 2026 from SharePoint <em>Sprint wise employe task list.xlsx</em> (August 26) and Jira HIEV worklogs. Local repo august-26-sprint-retro.</footer>
    </div>
  </div>
  <script type="application/json" id="personStats">{person_stats_json}</script>
  <script type="application/json" id="personNotesPublished">{person_notes_json}</script>
  <script>
    const TITLE_TEAM = "August 2026 sprint retrospective";
    const LEAD_TEAM = document.getElementById("heroLead") ? document.getElementById("heroLead").innerHTML : "";
    const PERSON_STATS = JSON.parse(document.getElementById("personStats").textContent || "{{}}");
    function matchesPerson(el, name) {{
      if (!name) return true;
      const raw = el.getAttribute("data-people") || el.getAttribute("data-person") || "";
      return raw.split("|").filter(Boolean).includes(name);
    }}
    function personFromUrl() {{
      return new URLSearchParams(location.search).get("person") || "";
    }}
    function setText(id, text) {{
      const el = document.getElementById(id);
      if (el) el.textContent = text;
    }}
    function setHtml(id, html) {{
      const el = document.getElementById(id);
      if (el) el.innerHTML = html;
    }}
    function updateEmptyStates(name) {{
      document.querySelectorAll("[data-empty-for]").forEach((msg) => {{
        if (!name) {{
          msg.hidden = true;
          return;
        }}
        const id = msg.getAttribute("data-empty-for");
        const any = [...document.querySelectorAll("#" + id + " tr")].some(
          (row) => !row.hidden && row.style.display !== "none"
        );
        msg.hidden = any;
      }});
      const barEmpties = document.querySelectorAll("[data-empty-for-bars]");
      barEmpties.forEach((msg) => {{
        if (!name) {{
          msg.hidden = true;
          return;
        }}
        const id = msg.getAttribute("data-empty-for-bars");
        const root = id ? document.getElementById(id) : null;
        const any = [...((root && root.querySelectorAll(".row")) || [])].some(
          (row) => !row.hidden && row.style.display !== "none"
        );
        msg.hidden = any;
      }});
      const journalEmpty = document.getElementById("journalEmpty");
      if (journalEmpty) {{
        if (!name) journalEmpty.hidden = true;
        else {{
          const any = [...document.querySelectorAll("#journal .person-day")].some((el) => !el.hidden);
          journalEmpty.hidden = any;
        }}
      }}
    }}
    function fillPersonCopy(name) {{
      const stats = PERSON_STATS[name] || null;
      document.querySelectorAll(".person-only").forEach((el) => {{ el.hidden = !name; }});
      if (!name || !stats) return;
      setHtml("pkLogged", stats.logged_html);
      setText("pkLeave", stats.leave);
      setText("pkUtil", stats.util);
      setText("pkPlan", stats.plan);
      setText("pkBugs", String(stats.bugs));
      setText("pkScrum", stats.scrum_html || "—");
      const onChip = document.getElementById("personOnChip");
      const offChip = document.getElementById("personOffChip");
      if (onChip) onChip.innerHTML = "Sprint planned " + stats.on_html;
      if (offChip) offChip.innerHTML = "Mid-sprint " + stats.off_html;
      setText("sheetPersonNote", stats.sheet
        ? (stats.sheet + " sprint-planned ticket" + (stats.sheet === 1 ? "" : "s") + " this person owns or touched (worklog or comment).")
        : "No sprint-planned tickets for this person.");
      setText("offsheetPersonNote", stats.offsheet
        ? (stats.offsheet + " mid-sprint key" + (stats.offsheet === 1 ? "" : "s") + " this person logged time on or commented on.")
        : "No mid-sprint keys this person logged or commented on.");
      setText("accPersonNote", "Same-scope only: August days on this person’s sprint-planned keys that have a numeric PD ÷ their sprint-plan PD. NA/open plan keys and mid-sprint time are not estimate misses.");
      setText("bugPersonNote", stats.bugs
        ? (stats.bugs + " unique bug" + (stats.bugs === 1 ? "" : "s") + " this person logged time on or commented on in August.")
        : "No bugs this person worked in August.");
      const fh = document.getElementById("fhPersonNote");
      if (fh) fh.innerHTML = "Bug time " + stats.bug_hours_html + ". Task time " + stats.task_hours_html + ".";
      setText("scrumPersonNote", stats.scrum_html
        ? (stats.scrum_html + " expected scrums" + (stats.scrum_missed ? (", " + stats.scrum_missed + " missed") : "") + ". Avg duration " + (stats.scrum_avg || "—") + ".")
        : "No expected scrum calls for this person.");
    }}
    function syncAssigneeFilters(name) {{
      document.querySelectorAll(".js-assignee-filter").forEach((sel) => {{
        if (sel.value !== name) sel.value = name;
      }});
    }}
    function applyPersonView(name, opts) {{
      name = name || "";
      opts = opts || {{}};
      document.body.classList.toggle("person-mode", !!name);
      const hint = document.getElementById("personViewHint");
      if (hint) hint.textContent = name ? name : "All (team)";
      const h1 = document.querySelector(".hero h1");
      if (h1) h1.textContent = name ? name + " · August 2026" : TITLE_TEAM;
      const lead = document.getElementById("heroLead");
      if (lead) {{
        lead.innerHTML = name
          ? "Filtered to <strong>" + name + "</strong> — tables, heatmaps, bars, and the work log show this assignee only. Team totals are hidden. 8h = 1d. <button type='button' class='name-link' id='backToTeam'>Back to All (team)</button>."
          : LEAD_TEAM;
        const back = document.getElementById("backToTeam");
        if (back) back.addEventListener("click", () => applyPersonView(""));
      }}
      document.querySelectorAll("[data-people], [data-person]").forEach((el) => {{
        const show = matchesPerson(el, name);
        el.hidden = !show;
        if (el.tagName === "TR" || el.classList.contains("row") || el.classList.contains("person-day")) {{
          el.style.display = show ? "" : "none";
        }}
      }});
      fillPersonCopy(name);
      if (typeof refreshCallNotes === "function") refreshCallNotes(name);
      syncAssigneeFilters(name);
      const url = new URL(location.href);
      if (name) url.searchParams.set("person", name);
      else url.searchParams.delete("person");
      if (url.href !== location.href) history.replaceState(null, "", url);
      if (document.getElementById("sheetSearch")) filterRows("sheetSearch", "sheetBody");
      if (document.getElementById("offSearch")) filterRows("offSearch", "offsheetBody");
      updateEmptyStates(name);
      const exportHint = document.getElementById("exportHint");
      if (exportHint) {{
        exportHint.textContent = name
          ? "Downloads a zip of UTF-8 CSVs for " + name + " only."
          : "Downloads a zip of UTF-8 CSVs for the full team. An assignee filter exports that person only.";
      }}
      if (opts.scroll && name) window.scrollTo(0, 0);
    }}
    function filterRows(inputId, bodyId) {{
      const q = (document.getElementById(inputId).value || "").toLowerCase();
      const person = (document.getElementById("reportPerson") || {{}}).value || "";
      document.querySelectorAll("#" + bodyId + " tr").forEach((row) => {{
        const typeOk = bodyId !== "offsheetBody" || !window._offType || row.dataset.type === window._offType;
        const textOk = !q || row.innerText.toLowerCase().includes(q);
        const personOk = matchesPerson(row, person);
        row.style.display = typeOk && textOk && personOk && !row.hidden ? "" : "none";
      }});
    }}
    const offType = document.getElementById("offTypeFilter");
    window._offType = "";
    if (offType) {{
      offType.addEventListener("change", () => {{
        window._offType = offType.value;
        filterRows("offSearch", "offsheetBody");
      }});
    }}
    const offSearch = document.getElementById("offSearch");
    if (offSearch) offSearch.addEventListener("input", () => filterRows("offSearch", "offsheetBody"));
    const sheetSearch = document.getElementById("sheetSearch");
    if (sheetSearch) sheetSearch.addEventListener("input", () => filterRows("sheetSearch", "sheetBody"));
    document.querySelectorAll(".js-assignee-filter").forEach((sel) => {{
      sel.addEventListener("change", () => applyPersonView(sel.value));
    }});
    document.body.addEventListener("click", (e) => {{
      const btn = e.target.closest("[data-open-person]");
      if (!btn) return;
      applyPersonView(btn.getAttribute("data-open-person"), {{ scroll: true }});
    }});
    window.addEventListener("popstate", () => applyPersonView(personFromUrl()));
""" + NOTES_JS + """
    applyPersonView(personFromUrl());
""" + EXPORT_JS + """
  </script>
</body>
</html>
"""
