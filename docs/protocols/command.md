# Command

## What is a Command module

A **Command module** represents a single command sent to one associated device — the lowest-level instruction in
the [protocol hierarchy](build_protocols.md#explanation-of-each-level). It requires no code: rather than writing Python, you pick a
device and one of its exposed commands, and the platform builds the request for you.

It is one of the [four module types](module_workflows.md#module-types) that make up a workflow (alongside Script,
Loop, and Conditional), but it behaves differently from the other three:

* Script, Loop, and Conditional modules are created empty from the canvas menu and then written/configured.
* A Command module is never created empty — it is dragged directly from the
  [Command List](build_protocols.md#command-list) onto the canvas, which creates a block already bound to that
  exact device/command pair.

<div class="info-block"> <strong>
💡 Information</strong><br> The <a href="script_editor.md">Script Editor</a>'s <strong>Add Command</strong> helper
exposes this same underlying concept — device, command, parameters, execution options — but produces a different
result: it inserts an equivalent call into the Python source of a Script module, instead of configuring a
standalone Command block.
</div>

## Building a Command block

To configure a Command block, **double-click it** on the canvas. This opens the command window:

![Alt text](../_static/command_block.png)

At the top, a breadcrumb header shows the block type (**command**) and the selected
**Device | Method | Command name** (e.g. `MSPump | PUT | infuse`) — this reflects the device/command chosen when
the block was dragged from the Command List and is not editable here.

### Parameters

Below the header, one field is shown for each parameter of the selected command. Each field displays:

* the parameter title and a type badge (`quantity`, `str`, `bool`, `float`, …),
* a short description of what the parameter controls,
* an input widget matching its type — a numeric stepper with a unit dropdown for `quantity` values, a plain text
  box for `str`, a toggle for `bool`, and so on.

Every field also has a small external-link icon next to its title. Clicking it opens a picker to bind that field
to a predefined **Main Parameter** or **Process Parameter** instead of typing a literal value:

![Alt text](../_static/command_block_using_parameters.png)

<div class="info-block"> <strong>
💡 Information</strong><br> Selecting <strong>None</strong> clears the binding and uses the literal value entered
in the field. This is the same underlying concept as <strong>Add Process Parameter</strong> / <strong>Add Main
Parameter</strong> in the <a href="script_editor.md">Script Editor</a> — see <a href="parameters.md">Parameters</a>
for how these variables are defined.
</div>

<div class="warning-block">
<strong>⚠️ Warning</strong><br>
The selected parameter must match the field's expected type <strong>and unit</strong>. A <code>quantity</code>
field defines a specific unit family (e.g. volume: <code>ml | l | ...</code>, time: <code>s | min | h | ...</code>),
and the bound parameter must resolve to a compatible value — binding a time parameter to a volume field (or vice
versa) will not work.
</div>

### Execution Options

<img src="../_static/command_timeline.png" width="400" style="vertical-align:middle; margin-right:45px;">

* **Wait time after command execution** (`float`)

  Seconds to wait after the command runs before the workflow continues.

* **Wait for feedback status** (`bool`)

  If enabled, execution blocks until the feedback command reports the expected value.

* **Feedback Status Command** (`str`)

  The command used to poll the device's status (e.g. `is-pumping`).

* **Expected Feedback Answer** (`str`)

  The value that counts as success once the feedback command is checked (e.g. `true`).

<div class="info-block"> <strong>
💡 Information</strong><br> Both share the same behavior as the <a href="script_editor.md">Script Editor</a>'s
Execution control, but the Command block is more user-friendly, since it does not require editing the script.
It is a great fit for simple workflows — for more complex logic, use a Script module instead.
</div>

### Label & Description

* **Label** — the block's identifier shown on the canvas (e.g. `command_3`).
* **Description** — a free-text note about what the block does (e.g. `ms pump`).

### Save / Cancel

**Save** applies the configuration to the block; **Cancel** closes the window and discards any changes.

### Generated code

Like the rest of the workflow, a Command block's configuration is stored as a method in the process file
(`...\<project_folder>\protocols\<process_name>.py`, see [Saving](module_workflows.md#saving)).

For example, a block labeled `command_1` — a `pt100` device's `power-on` command, with no wait time, feedback
disabled and description "Turn on temperature controlling" — becomes:

```python
def command_1(self, ctx: NodeExecutionContext) -> bool:
    self.platform["pt100"].put(
        "power-on",
        description="Turn on temperature controlling",
        wait_time=0.0,
        wait_feedback_status=False,
        feedback_status_command="",
        feedback_answer="true",
    )
    return True
```

Each field in the command window maps 1:1 to a keyword argument here: `description`, `wait_time`,
`wait_feedback_status`, `feedback_status_command`, and `feedback_answer`.
