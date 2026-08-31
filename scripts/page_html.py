"""HTML shell for the August retrospective."""


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
      </header>

      <div class="kpis team-only">
        <div class="kpi"><strong>{total_plan:.0f} PD</strong><span>Numeric sheet estimates</span></div>
        <div class="kpi"><strong>{kpi_logged}</strong><span>Logged of available · 8h = 1d</span></div>
        <div class="kpi"><strong>{team_util if team_util is not None else "n/a"}</strong><span>Team util (logged ÷ available)</span></div>
        <div class="kpi"><strong>{avg_acc if avg_acc is not None else "n/a"}</strong><span>Mean ticket accuracy (worked keys)</span></div>
        <div class="kpi"><strong>{off_count}</strong><span>Off-sheet keys · {off_hours_label}</span></div>
      </div>
      <div class="kpis person-only" id="personKpis" hidden>
        <div class="kpi"><strong id="pkLogged"></strong><span>Logged of available · 8h = 1d</span></div>
        <div class="kpi"><strong id="pkLeave"></strong><span>Leave</span></div>
        <div class="kpi"><strong id="pkUtil"></strong><span>Util (logged ÷ available)</span></div>
        <div class="kpi"><strong id="pkPlan"></strong><span>Sheet plan PD</span></div>
        <div class="kpi"><strong id="pkBugs"></strong><span>Unique bugs worked</span></div>
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
          ? "This view is <strong>" + name + "</strong> only — their logged of available, leave, util, sheet and off-sheet tickets they touched, bugs they worked, heatmap, and work log. Team totals are hidden. 8h = 1d. <button type='button' class='name-link' id='backToTeam'>Back to team overview</button>."
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
  </script>
</body>
</html>
"""
