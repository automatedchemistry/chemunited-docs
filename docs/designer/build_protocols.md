# Build Protocols

The objective of this frame is to create and organize the protocols that define how the platform operates.

Before explaining how the orchestration system is designed to build these protocols, it is important to understand 
how the protocol structure is organized within the package.

## 🧩 Protocol Hierarchy

The following diagram illustrates the hierarchical relationship between the different elements that make up a protocol:

![Alt text](../_static/protocol_hierarchy.svg)

<div class="info-block">
<strong>💡 Information</strong><br> 
This hierarchical organization allows the orchestration to combine automation logic with flexible scripting. 
Complex experimental protocols can therefore be built by combining processes, modules, and component-level commands. 
</div>

## Explanation of Each Level

### 💻 Protocol

A protocol is the highest level in the orchestration hierarchy.
It is composed of a series of processes, which are executed sequentially, one after another.

### <img src="../_static/icons/process_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> Process

Each process contains one or more workflows composed of modules.
Processes are executed in sequence, but within a process, the modules can run simultaneously through a multithreading workflow.

### <img src="../_static/icons/python.svg" width="16" style="vertical-align:middle; margin-right:4px;"> Module

A module represents a Python script containing a sequence of commands.
This design gives the user complete flexibility — any Python libraries can be used to support the protocol development.

### <img src="../_static/icons/play_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> Command

A command is the lowest-level instruction in the hierarchy.
It represents a specific request or actuation sent to an electronic component in the system (e.g., start a pump, read a sensor, open a valve).

### <img src="../_static/icons/variable_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> Parameters

The Parameters script defines a set of variables that the user can create and reuse across the entire platform.
This feature is optional, but extremely helpful for complex setups where protocols depend on shared values, user-defined constants, or validation logic.

There are two types of parameters:

* Main Parameters – global variables available to all protocols in the project.
These typically define general configuration values that remain consistent throughout the orchestration.

* Process Parameters – local variables defined within a specific process.
They apply only to that process and allow fine-tuning of parameters without affecting other parts of the platform.

Using parameters promotes modularity and flexibility: the same protocol can be reused with different parameter sets, and complex workflows can automatically validate or adjust values before execution.

## ChemUnited Protocols Frame

![Alt text](../_static/protocol_clean.png)

* <img src="../_static/icons/variable_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Experiment Parameters**

...

* <img src="../_static/icons/move_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Inspect Modules**

...

* <img src="../_static/icons/Add_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Create Connection**

...

* <img src="../_static/icons/Cut_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Remove Object**

...

* <img src="../_static/icons/Save_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Save Draw**

...

* <img src="../_static/icons/Add_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Add Component**

...

* <img src="../_static/icons/Info_black.svg" width="16" style="vertical-align:middle; margin-right:4px;"> **Inspect Draw**

...
