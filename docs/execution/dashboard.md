# 📊 The Dashboard

Once the [work-server](overview.md) is running, it serves a browser-based dashboard alongside its API. Open the
URL shown in the console (or in the orchestrator's Pre-Running dashboard launcher) in any browser — no separate
installation or build step is required.

## Dashboard (`/`)

The landing page: current run status at a glance, quick links to the other pages below, and a summary of the
loaded project.

<div class="info-block">
<strong>📸 Screenshot needed</strong><br>
Capture: Dashboard home page (<code>/</code>), showing the active-run status and quick-start links.<br>
Save as: <code>docs/_static/dashboard01.png</code>, then replace this block with:<br>
<code>![Alt text](../_static/dashboard01.png)</code>
</div>

## Run Control (`/run-control`)

Start or cancel a run, and watch a live event feed as it executes (streamed over Server-Sent Events, so the page
updates in real time without needing a manual refresh). This is the browser equivalent of clicking **Start
protocol** / **Stop protocol** in the orchestrator's [Monitor window](../monitoring/run_monitoring.md), but reachable
from any machine with access to the dashboard.

<div class="info-block">
<strong>📸 Screenshot needed</strong><br>
Capture: Run Control page mid-run, with the live event feed visible.<br>
Save as: <code>docs/_static/run_control01.png</code>, then replace this block with:<br>
<code>![Alt text](../_static/run_control01.png)</code>
</div>

## Report (`/report`)

A per-node outcome table for the current or most recent run: which steps ran, in what order, and whether each
succeeded, failed, or was skipped.

<div class="info-block">
<strong>📸 Screenshot needed</strong><br>
Capture: Report page showing the per-node outcome table.<br>
Save as: <code>docs/_static/report01.png</code>, then replace this block with:<br>
<code>![Alt text](../_static/report01.png)</code>
</div>

## Protocols (`/protocols-ui`)

Lists the protocol script files saved in the project (the same files shown as cards in
[Pre-Running](../protocols/pre_running.md)), with the ability to inspect or delete them from the browser.

<div class="info-block">
<strong>📸 Screenshot needed</strong><br>
Capture: Protocols page listing saved protocol files.<br>
Save as: <code>docs/_static/protocols_ui01.png</code>, then replace this block with:<br>
<code>![Alt text](../_static/protocols_ui01.png)</code>
</div>

## Logs (`/logs-ui`)

Browse and tail the work-server's log files — useful for diagnosing a failed run without needing terminal/file
access to the machine running the server.

<div class="info-block">
<strong>📸 Screenshot needed</strong><br>
Capture: Logs page with a log file open/tailing.<br>
Save as: <code>docs/_static/logs_ui01.png</code>, then replace this block with:<br>
<code>![Alt text](../_static/logs_ui01.png)</code>
</div>

## Devices (`/devices`)

A connectivity map of the components associated in [Connect Devices](../connectivity/connectivity.md), with a
ping check to confirm each device is reachable before starting a run.

<div class="info-block">
<strong>📸 Screenshot needed</strong><br>
Capture: Devices page showing the connectivity map and ping status.<br>
Save as: <code>docs/_static/devices01.png</code>, then replace this block with:<br>
<code>![Alt text](../_static/devices01.png)</code>
</div>

<div class="info-block">
<strong>💡 Note</strong><br>
Each of these pages can be customized per project by overriding the templates the work-server ships with. This is
an advanced/developer topic — see <a href="../developer/customize_dashboard.md">Customize dashboard</a>.
</div>

## Next steps

For scripting or automating against the same functionality shown here, see [API & MCP Tools](api_and_mcp.md).
