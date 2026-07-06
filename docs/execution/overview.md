# 🌐 Execution & Dashboard Overview

When you click **Run Monitoring** in the [Pre-Running](../protocols/pre_running.md) window, the orchestrator hands
your protocol off to a separate execution engine that actually talks to the hardware. In ChemUnited terminology this
running engine is informally called the **work-server**. It runs independently of the desktop app, exposes a
browser-based dashboard, and can be controlled remotely over a REST or MCP API.

<div class="info-block">
<strong>💡 Note</strong><br>
You do not need to start the work-server yourself for a normal run — the orchestrator launches it automatically
when you click <strong>Run Monitoring</strong>. This page is for users who want to run it standalone (e.g. headless,
on a lab server, or exposed to other machines on the network).
</div>

## Starting the work-server manually

The work-server ships as its own command-line tool:

```bash
chemunited-workflow serve [project_dir] [OPTIONS]
```

Running the bare `chemunited-workflow` command with no arguments is equivalent to `serve` with defaults.

| Flag | Description |
|---|---|
| `--host` | Interface to bind to (defaults to localhost-only). |
| `--port` | Port to serve the dashboard/API on. |
| `--reload` | Auto-restart the server on code changes (development use). |
| `--advertise` | Bind to all interfaces and announce the server on the local network via mDNS/Zeroconf, so it can be discovered by other machines. |
| `--advertise-name` | Custom name to advertise the server as, when `--advertise` is used. |
| `--with-mcp` | Expose the [MCP tool interface](api_and_mcp.md) on the same port as the dashboard. |
| `--tray` | Run the server in the background with a system-tray icon (Windows), with quick actions to open the dashboard, check status, or quit. |
| `--silent` | Detach the console window. Requires `--tray`, and is not compatible with `--reload`. |

<div class="warning-block">
<strong>⚠️ Warning</strong><br>
The work-server does not require authentication. When started with <code>--advertise</code> (or bound to a
non-localhost <code>--host</code>), anyone on the same network can view and control the run. Only use this on
trusted lab networks.
</div>

## Next steps

Once the work-server is running, see [The Dashboard](dashboard.md) for a tour of its browser pages, or
[API & MCP Tools](api_and_mcp.md) if you want to script or automate against it directly.
