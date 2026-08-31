"""HTML shell for the August retrospective."""

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
      const on = title.match(/On sheet\s+([\d.]+)%/i);
      const off = title.match(/Off sheet\s+([\d.]+)%/i);
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
        "on_sheet_pct",
        "off_sheet_pct",
        "on_sheet_days",
        "on_sheet_hours",
        "off_sheet_days",
        "off_sheet_hours",
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
      const headers = ["person", "date", "kind", "key", "hours", "on_sheet", "comment"];
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
            const onSheet = /sheet/i.test(typeText) && !/other/i.test(typeText)
              ? "sheet"
              : (/other/i.test(meta + " " + typeText) ? "other" : (/sheet/i.test(typeText) ? "sheet" : ""));
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
          { name: prefix + "-sheet.csv", content: exportSheetCsv(name) },
          { name: prefix + "-offsheet.csv", content: exportOffsheetCsv(name) },
          { name: prefix + "-bugs.csv", content: exportBugsCsv(name) },
          { name: prefix + "-heatmap.csv", content: exportHeatmapCsv(name) },
          { name: prefix + "-scrum.csv", content: exportScrumCsv(name) },
          { name: prefix + "-scrum-days.csv", content: exportScrumDaysCsv(name) },
          { name: prefix + "-journal.csv", content: exportJournalCsv(name) }
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
    journal,
) -> str:
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
      <label class="nav-person">Person report
        <select id="reportPerson">
          <option value="">Team overview</option>
          {person_opts}
        </select>
      </label>
      <span class="nav-hint" id="personViewHint">Team overview</span>
      <a href="#overview">Overview</a>
      <a href="#people">People</a>
      <a href="#sheet">Sheet tickets</a>
      <a href="#offsheet">Off-sheet work</a>
      <a href="#accuracy">Estimation</a>
      <a href="#quality">Bugs &amp; fix hours</a>
      <a href="#daily">Daily time</a>
      <a href="#scrum">Scrum attendance</a>
      <a href="#journal">Work log</a>
    </nav>
    <div class="content">
      <header class="hero" id="overview">
        <h1>August 2026 sprint retrospective</h1>
        <p class="lead" id="heroLead">Sheet plan from Deepak’s August 26 workbook, plus every HIEV task and bug the team logged time or comments on during 1–31 Aug 2026. Conversion is fixed: <strong>8 hours = 1 person-day</strong>. Pick a name in the sidebar (or click a name in a table) to open that person’s full report.</p>
        <div class="meta-row">
          <span class="chip">Period 1–31 Aug 2026</span>
          <span class="chip">8h = 1d</span>
          <span class="chip sheet team-only">On sheet {on_hours_label}</span>
          <span class="chip other team-only">Off sheet {off_mix_label}</span>
          <span class="chip sheet person-only" id="personOnChip" hidden></span>
          <span class="chip other person-only" id="personOffChip" hidden></span>
          <span class="chip">Jira project HIEV</span>
        </div>
        <div class="export-bar">
          <button type="button" class="export-btn" id="exportCsvZip">Export CSV</button>
          <span class="export-hint" id="exportHint">Downloads a zip of UTF-8 CSVs for the full team. Person view exports that person only.</span>
        </div>
      </header>

      <div class="kpis team-only">
        <div class="kpi"><strong>{total_plan:.0f} PD</strong><span>Numeric sheet estimates</span></div>
        <div class="kpi"><strong>{kpi_logged}</strong><span>Logged of available · 8h = 1d</span></div>
        <div class="kpi"><strong>{team_util if team_util is not None else "n/a"}</strong><span>Team util (logged ÷ available)</span></div>
        <div class="kpi"><strong>{avg_acc if avg_acc is not None else "n/a"}</strong><span>Mean ticket accuracy (worked keys)</span></div>
        <div class="kpi"><strong>{off_count}</strong><span>Off-sheet keys · {off_hours_label}</span></div>
        <div class="kpi"><strong>{kpi_scrum}</strong><span>Scrum attendance (leave-adjusted)</span></div>
      </div>
      <div class="kpis person-only" id="personKpis" hidden>
        <div class="kpi"><strong id="pkLogged"></strong><span>Logged of available · 8h = 1d</span></div>
        <div class="kpi"><strong id="pkLeave"></strong><span>Leave</span></div>
        <div class="kpi"><strong id="pkUtil"></strong><span>Util (logged ÷ available)</span></div>
        <div class="kpi"><strong id="pkPlan"></strong><span>Sheet plan PD</span></div>
        <div class="kpi"><strong id="pkBugs"></strong><span>Unique bugs worked</span></div>
        <div class="kpi"><strong id="pkScrum"></strong><span>Scrum attendance</span></div>
      </div>

      <div class="split">
        <div class="card team-only">
          <h2>Where August time went</h2>
          <p class="note">Share of logged hours on planned sheet tickets versus everything else.</p>
          <div class="mix" style="height:14px;margin:12px 0 8px">
            <span class="on" style="width:{on_pct}%"></span>
            <span class="off" style="width:{off_pct}%"></span>
          </div>
          <div class="legend">
            <span><i class="swatch sheet"></i>Sheet {on_pct}%</span>
            <span><i class="swatch other"></i>Off-sheet {off_pct}%</span>
          </div>
          <p class="note">Nine long-running tickets exceeded Jira’s 20-worklog payload cap. Missing August logs were rebuilt from changelog time deltas and checked against each issue’s timespent.</p>
        </div>
        <div class="card">
          <h2>Logged of available</h2>
          <p class="note">Bar fills toward that person’s available time. Label is <em>logged of available</em> (days, then hours).</p>
          <div class="bars">{people_mix}</div>
        </div>
      </div>

      <section class="block" id="people">
        <h2>1. Planned vs actual</h2>
        <p class="note">Every time figure is <strong>logged of available</strong>: days first, hours underneath. Available = weekdays − Fri 28 PH − that person’s leave (8h = 1d). Util = logged ÷ available. Mix is sheet vs off-sheet share of logged time.</p>
        <div class="legend"><span><i class="swatch sheet"></i>On sheet</span><span><i class="swatch other"></i>Off sheet</span></div>
        <div class="wrap">
          <table>
            <thead>
              <tr>
                <th>Person</th>
                <th class="num">Plan PD</th>
                <th class="num">Leave</th>
                <th class="num">Logged of available</th>
                <th class="num">Util</th>
                <th>Mix</th>
                <th class="num">On sheet of avail</th>
                <th class="num">Off sheet of avail</th>
                <th class="num">Accuracy</th>
                <th class="num">Logs</th>
                <th class="num">Comments</th>
              </tr>
            </thead>
            <tbody id="peopleBody">{people_trs}</tbody>
          </table>
        </div>
      </section>

      <section class="block" id="sheet">
        <h2>Sheet tickets</h2>
        <p class="note team-only">Rows from the August 26 sheet. Accuracy is August days on that key ÷ sheet PD. Search by feature, assignee, or key.</p>
        <p class="note person-only" id="sheetPersonNote" hidden></p>
        <div class="controls">
          <label class="field">Search <input type="search" id="sheetSearch" placeholder="Filter sheet tickets…" /></label>
        </div>
        <div class="wrap tall">
          <table>
            <thead>
              <tr>
                <th>Jira</th><th>Section</th><th>Feature</th><th>Assignee</th>
                <th class="num">Plan</th><th class="num">Logged of assignee avail</th><th class="num">Accuracy</th><th>Status</th>
              </tr>
            </thead>
            <tbody id="sheetBody">{ticket_trs}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="sheetBody" hidden>No sheet tickets for this person.</p>
      </section>

      <section class="block" id="offsheet">
        <h2>Off-sheet tasks and bugs</h2>
        <p class="note team-only">{offsheet_count} keys had August worklogs or comments but were not on the plan. Included in person totals, heatmap, and the journal (marked <em>other</em>).</p>
        <p class="note person-only" id="offsheetPersonNote" hidden></p>
        <div class="controls">
          <label class="field">Type
            <select id="offTypeFilter">
              <option value="">All types</option>
              {type_opts}
            </select>
          </label>
          <label class="field">Search <input type="search" id="offSearch" placeholder="Filter off-sheet…" /></label>
        </div>
        <div class="wrap tall">
          <table>
            <thead>
              <tr>
                <th>Jira</th><th>Type</th><th>Summary</th><th>Logged by</th>
                <th class="num">Logged of available</th><th class="num">Comments</th><th>Status</th>
              </tr>
            </thead>
            <tbody id="offsheetBody">{offsheet_trs}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="offsheetBody" hidden>No off-sheet keys this person logged or commented on.</p>
      </section>

      <section class="block" id="accuracy">
        <h2>2. Estimation accuracy</h2>
        <p class="note team-only">Same-scope only. Ticket = days on that key ÷ sheet PD. Person = days on that person’s planned keys ÷ their sheet PD. Off-sheet time is not an estimate miss. Bar is scaled so 2.0 fills the track. Green ≤1.1, amber ≤1.5, red above.</p>
        <p class="note person-only" id="accPersonNote" hidden></p>
        <div class="wrap">
          <table>
            <thead>
              <tr>
                <th>Person</th>
                <th class="num">Plan PD</th>
                <th class="num">Actual on plan</th>
                <th class="num">Logged of available</th>
                <th>Ratio</th>
                <th class="num">Accuracy</th>
              </tr>
            </thead>
            <tbody id="accBody">{person_acc_trs}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="accBody" hidden>No numeric sheet estimate for this person, so accuracy is not computed.</p>
      </section>

      <section class="block" id="quality">
        <h2>3. Bugs worked in August and 4. Fix hours</h2>
        <p class="note team-only">{bug_note}</p>
        <p class="note person-only" id="bugPersonNote" hidden></p>
        <div class="split">
          <div class="card">
            <h2>Bugs worked in August</h2>
            <p class="note">Bars are unique bug keys each person logged time on or commented on in August.</p>
            <div class="bars">{bug_bars}</div>
            <p class="empty-msg" data-empty-for-bars="1" hidden>No August bug worklogs or comments for this person.</p>
          </div>
          <div class="card">
            <h2>Fix hours</h2>
            <p class="note team-only">Bugs {fh_bug}. Tasks {fh_task}. Other {fh_other}.</p>
            <p class="note person-only" id="fhPersonNote" hidden></p>
            <div class="wrap" style="max-height:280px;border:0;padding:0">
              <table>
                <thead><tr><th>Person</th><th class="num">Bug of available</th><th class="num">Task of available</th></tr></thead>
                <tbody id="fixBody">{fix_trs}</tbody>
              </table>
            </div>
          </div>
        </div>
        <h3 class="note" style="margin-top:18px">Bug list</h3>
        <div class="wrap">
          <table>
            <thead>
              <tr>
                <th>Key</th><th>Summary</th><th>Status</th><th>Who worked it</th>
                <th class="num">August hours</th>
              </tr>
            </thead>
            <tbody id="bugBody">{bug_detail}</tbody>
          </table>
        </div>
        <p class="empty-msg" data-empty-for="bugBody" hidden>No bugs this person worked in August.</p>
      </section>

      <section class="block" id="daily">
        <h2>5. Daily logged time</h2>
        <p class="note">Cell values are hours that day. Row total is <strong>logged of available</strong> for the month. Blank = no Jira log. <strong>L</strong> / <strong>½L</strong> = leave (available 0 or 4h). Saturday gold, Sunday rose, Fri 28 PH green, leave purple.</p>
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
        <div class="wrap heatmap">
          <table>
            <thead><tr><th>Person</th>{daily_head}<th class="num">Logged of available</th></tr></thead>
            <tbody id="heatBody">{daily_body}</tbody>
          </table>
        </div>
      </section>

      <section class="block" id="scrum">
        <h2>6. Scrum call attendance</h2>
        <p class="note team-only">{scrum_note}</p>
        <p class="note person-only" id="scrumPersonNote" hidden></p>
        <div class="wrap">
          <table>
            <thead>
              <tr>
                <th>Person</th>
                <th class="num">Expected</th>
                <th class="num">Attended</th>
                <th class="num">Missed</th>
                <th class="num">On leave joined</th>
                <th class="num">Attendance</th>
                <th class="num">Avg duration</th>
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
        <div class="wrap heatmap">
          <table id="scrumTicks">
            <thead><tr><th>Person</th>{scrum_tick_head}</tr></thead>
            <tbody id="scrumTickBody">{scrum_tick_body}</tbody>
          </table>
        </div>
      </section>

      <section class="block" id="journal">
        <h2>Daily worklogs and comments</h2>
        <p class="note">Expand a day to see ticket keys, time spent, and comments. <em>sheet</em> = August 26 plan; <em>other</em> = off-sheet. The sidebar person control filters this journal with the rest of the report.</p>
        <div id="journal">{journal}</div>
        <p class="empty-msg" id="journalEmpty" hidden>No August worklogs or comments for this person.</p>
      </section>

      <footer class="foot">Generated 31 Aug 2026 from SharePoint <em>Sprint wise employe task list.xlsx</em> (August 26) and Jira HIEV worklogs. Local repo august-26-sprint-retro.</footer>
    </div>
  </div>
  <script type="application/json" id="personStats">{person_stats_json}</script>
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
      const barEmpty = document.querySelector("[data-empty-for-bars]");
      if (barEmpty) {{
        if (!name) barEmpty.hidden = true;
        else {{
          const any = [...document.querySelectorAll("#quality .bars .row")].some((row) => !row.hidden);
          barEmpty.hidden = any;
        }}
      }}
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
      if (onChip) onChip.innerHTML = "On sheet " + stats.on_html;
      if (offChip) offChip.innerHTML = "Off sheet " + stats.off_html;
      setText("sheetPersonNote", stats.sheet
        ? (stats.sheet + " sheet ticket" + (stats.sheet === 1 ? "" : "s") + " this person owns or touched (worklog or comment).")
        : "No sheet tickets for this person.");
      setText("offsheetPersonNote", stats.offsheet
        ? (stats.offsheet + " off-sheet key" + (stats.offsheet === 1 ? "" : "s") + " this person logged time on or commented on.")
        : "No off-sheet keys this person logged or commented on.");
      setText("accPersonNote", "Same-scope only: this person’s August days on their planned keys ÷ their sheet PD. Off-sheet time is not an estimate miss.");
      setText("bugPersonNote", stats.bugs
        ? (stats.bugs + " unique bug" + (stats.bugs === 1 ? "" : "s") + " this person logged time on or commented on in August.")
        : "No bugs this person worked in August.");
      const fh = document.getElementById("fhPersonNote");
      if (fh) fh.innerHTML = "Bug time " + stats.bug_hours_html + ". Task time " + stats.task_hours_html + ".";
      setText("scrumPersonNote", stats.scrum_html
        ? (stats.scrum_html + " expected scrums" + (stats.scrum_missed ? (", " + stats.scrum_missed + " missed") : "") + ". Avg duration " + (stats.scrum_avg || "—") + ".")
        : "No expected scrum calls for this person.");
    }}
    function applyPersonView(name) {{
      name = name || "";
      document.body.classList.toggle("person-mode", !!name);
      const hint = document.getElementById("personViewHint");
      if (hint) hint.textContent = name ? "Personal report" : "Team overview";
      const h1 = document.querySelector(".hero h1");
      if (h1) h1.textContent = name ? name + " · August 2026" : TITLE_TEAM;
      const lead = document.getElementById("heroLead");
      if (lead) {{
        lead.innerHTML = name
          ? "This view is <strong>" + name + "</strong> only — their logged of available, leave, util, sheet and off-sheet tickets they touched, bugs they worked, scrum attendance, heatmap, and work log. Team totals are hidden. 8h = 1d. <button type='button' class='name-link' id='backToTeam'>Back to team overview</button>."
          : LEAD_TEAM;
        const back = document.getElementById("backToTeam");
        if (back) back.addEventListener("click", () => applyPersonView(""));
      }}
      document.querySelectorAll("[data-people], [data-person]").forEach((el) => {{
        el.hidden = !matchesPerson(el, name);
        if (el.tagName === "TR" || el.classList.contains("row") || el.classList.contains("person-day")) {{
          el.style.display = "";
        }}
      }});
      fillPersonCopy(name);
      const sel = document.getElementById("reportPerson");
      if (sel && sel.value !== name) sel.value = name;
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
          : "Downloads a zip of UTF-8 CSVs for the full team. Person view exports that person only.";
      }}
      if (name) window.scrollTo(0, 0);
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
    const reportPerson = document.getElementById("reportPerson");
    if (reportPerson) {{
      reportPerson.addEventListener("change", () => applyPersonView(reportPerson.value));
    }}
    document.body.addEventListener("click", (e) => {{
      const btn = e.target.closest("[data-open-person]");
      if (!btn) return;
      applyPersonView(btn.getAttribute("data-open-person"));
    }});
    window.addEventListener("popstate", () => applyPersonView(personFromUrl()));
    applyPersonView(personFromUrl());
""" + EXPORT_JS + """
  </script>
</body>
</html>
"""
