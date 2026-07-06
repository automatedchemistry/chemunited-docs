# Run and Monitoring

The Monitoring window is intentionally simpler than the Setup window.
Its purpose is to **run a protocol that has already been created**, following the order of the processes listed 
under **Active Processes**.

![Alt text](../_static/monitoring01.png)

The buttons shown in the figure above is described as:

* <img src="../_static/icons/variable_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Show Parameters Summary** 

Opens a read-only view with all predefined parameters (main and process parameters), including their current values.

* <img src="../_static/icons/database_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Custom Data-Save Script** 

Opens the editor for a custom data-saving script.
Use this to define how experimental data should be stored (e.g., file format, naming, metadata), 
based on a predefined class/template provided by the application.

* <img src="../_static/icons/play_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Start protocol** 

Starts the execution of the full protocol, running all processes in the order shown in **Active Processes**.

* <img src="../_static/icons/stop_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Stop protocol**

Stops the currently running protocol execution.

## Running individual processes

In addition to starting the full protocol, each process listed under **Active Processes** includes its own option/menu
to run that process individually.
This is useful for testing a single process step without executing the full sequence.

## 🧑‍🏫 Tutorial Example

For this tutorial, you only need to click **Start Protocol**. The application will execute the processes listed in 
**Active Processes** in order.

<img src="../_static/monitoring02.gif" width="900px">

## Next steps

The Monitor window above is the desktop-side view of a run. Once a protocol starts, execution is actually handed off
to a separate execution engine (the "work-server") that also exposes a browser dashboard and a remote/automation API
— see [Execution & Dashboard](../execution/overview.md) to control or inspect a run from a browser or another machine.