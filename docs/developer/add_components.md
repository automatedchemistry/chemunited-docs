# Add new components

Components are the drawable building blocks (pumps, valves, sensors, vessels...) available in the
[Draw](../drawing/drawing.md) canvas — see [Components available](../reference/components.md) for the full
current library. This page is for adding a new one that isn't in that list.

## Anatomy of a Component

Most components live in `chemunited-core`, not in the orchestrator itself. A component definition has three parts:

* A **data class** describing its type and behavior (e.g. `ComponentType.ELECTRONIC`, `ComponentType.VALVE`).
* A **mode class** describing its user-editable parameters (the fields shown when you configure it on the canvas).
* An entry in the shared `COMPONENTS` registry that ties the two together, along with its **category** (which
  section of the Add tree it appears in, matching the categories in
  [Components available](../reference/components.md)) and its **port positions**.

For most new components — anything that behaves like a simple pass-through device — this registry entry is
**all** you need to write. The orchestrator auto-generates the canvas figure, tree entry, and property editor from
it; no changes to the orchestrator itself are required.

## Steps to Add a Component

<div class="info-block">
<strong>💡 Note</strong><br>
For anything beyond a simple pass-through device, <code>chemunited-core</code>'s own <code>Instruction.md</code>
("How to Build a New Component") covers this in much more depth than the summary below — lifecycle diagram, base
classes to subclass from, and the full <code>ComponentMode</code> field-metadata conventions.
</div>

1. Define the component's data/mode classes in `chemunited-core` (or reuse an existing base if your component is
   a variant of one, e.g. another valve port/position combination).
2. Add an entry for it to the shared `COMPONENTS` registry, giving it a name, category, and port positions.
3. Provide its canvas icon as an SVG (see below) — this is picked up automatically once named correctly.
4. (Optional) If the component needs custom rendering beyond the default auto-generated shape, add an explicit
   subclass in the orchestrator's component glossary instead of relying on auto-generation.
5. (Optional) For simulation support, give the component a resistance/behavior model in `chemunited-sim` so it can
   be included in [digital twin](../simulation/digital_twins.md) runs — see the reaction-model contract in
   [Customize protocols](add_features.md) for the equivalent idea on the reaction side.

<div class="info-block">
<strong>💡 Note</strong><br>
New components without simulation support still work perfectly for real-hardware runs — only <strong>Run
Simulation</strong> coverage is affected.
</div>

## Icons

Two icons are involved: the full canvas figure (the shape drawn on the platform) and the small icon shown in the
Add tree panel — the same icon set documented in
[Components available](../reference/components.md). Name new icon files after the component, following the
existing convention (`ComponentName.svg`, with a `LIGHT`/`DARK` theme-pair variant where applicable).

## Simplest example

The **Source** and **Sink** components (see the Generic category in
[Components available](../reference/components.md)) are the simplest possible components — a registry entry with no custom orchestrator code at all — and are a good starting
template to copy when adding a new simple component.
