# Customize dashboard

The [browser dashboard](../execution/dashboard.md) served by the work-server (`chemunited-workflow`) is built from
Jinja2 templates and static assets that ship with the package. Each page — Dashboard, Run Control, Report,
Protocols, Logs, Devices — can be overridden on a per-project basis without modifying the installed package.

## 🎨 Override locations

Inside a project directory, two folders are checked before falling back to the built-in defaults:

```text
my_project/
├── ui/
│   ├── templates/       # Jinja2 template overrides, one file per page
│   └── static/
│       └── custom.css   # extra/overriding CSS loaded on every page
```

To customize a page, copy the corresponding built-in template into `ui/templates/` under the same filename and
edit it; the work-server will serve your version instead of the default the next time it starts. To just tweak
appearance (colors, branding, layout tweaks) without touching markup, `ui/static/custom.css` is loaded after the
built-in stylesheet, so its rules take precedence.

<div class="info-block">
<strong>💡 Note</strong><br>
There is currently no CLI command to scaffold these files for you automatically — you create the
<code>ui/templates/</code> and <code>ui/static/</code> folders yourself and copy in only the files you want to
override. Everything else keeps using the built-in default.
</div>

## What you can override

Any of the pages described in [The Dashboard](../execution/dashboard.md) — Dashboard, Run Control, Report,
Protocols, Logs, Devices — can be replaced individually. You do not need to override every page; unmodified pages
continue to use the built-in template.

## Next steps

See [Working with Backend](backend.md) for the rest of the project file format, and
[API & MCP Tools](../execution/api_and_mcp.md) if the dashboard's REST/MCP surface itself is what you want to
extend rather than its appearance.
