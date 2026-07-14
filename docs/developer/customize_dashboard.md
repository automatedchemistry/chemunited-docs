# Customize dashboard

There is currently **no supported way to customize the browser [dashboard](../dashboard/overview.md)'s appearance
on a per-project basis.**

The dashboard used to be built from Jinja2 templates and static assets, with a per-project `ui/templates/` and
`ui/static/custom.css` override mechanism. That system was fully replaced by a compiled Vue single-page app
(`chemunited_workflow/web/index.html` + a JS/CSS bundle) — every dashboard route now serves the same static bundle,
routed client-side. The Jinja2/HTMX templates and the override mechanism built around them no longer exist in the
codebase.

<div class="info-block">
<strong>💡 Note</strong><br>
The work-server still exposes <code>GET /project-static/&#123;filename&#125;</code>, which serves raw files from
<code>&lt;project&gt;/ui/static/&lt;filename&gt;</code>. This is a generic file passthrough only — the dashboard
does not automatically load anything from it (no stylesheet, logo, or script is wired in), so it isn't a
customization hook today. A project can only reach a file placed there by linking to its URL directly from
somewhere else.
</div>

If you need to change what the dashboard looks like or shows, the current options are to fork/patch the frontend
source directly, or to build your own client against the same REST/MCP API instead of the bundled dashboard — see
[API & MCP Tools](../execution/api_and_mcp.md).

## Next steps

See [Working with Backend](backend.md) for the rest of the project file format.
