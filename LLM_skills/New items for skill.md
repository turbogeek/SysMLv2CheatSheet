---

## Key Lessons from Drone Model Debugging

- **Ports vs Interfaces**
  - `port def` defines an interaction point.
  - `interface def` connects ports; ends are ports, not parts.
  - Use conjugation (`~`) to reverse direction; direction is not declared on interface ends.
  - Inside an interface, use `flow source.item to target.item` (no `of`, no `from`).

- **Bindings**
  - Syntax: `binding bind a = b` (must use `=`, not `to`).
  - No indices or multiplicity ranges inside a binding.
  - To bind an array of parts, declare each part individually (`esc1`, `esc2`, …) and bind one by one.
  - Binding to an entire multi‑part (`battery.pwrOut = escs.pwrIn`) is allowed only when the target side is a part with multiplicity and no indexing is needed.

- **State Machines**
  - Use `if` guard, not `where`.
  - Multiple source states require separate transitions (`or` is not allowed in `first`).
  - Actions (e.g., `ArmMotors`) must be defined in the same part scope as the state machine so that attributes like `batteryVoltage` are visible.

- **Allocations**
  - Only between **usages**, never definitions.
  - Create a dedicated package with part instances (`myLogical`, `myPhysical`) and place `allocate` statements there.

- **Requirements**
  - Use `requirement <'ID'> 'Short Name' : Type { ... }`.
  - Include `subject`, measured & target attributes, and `require constraint { ... }` (no semicolon inside).
  - No `//` comments; use `/* ... */` or `doc /* ... */`.

- **Units & Quantities**
  - Define custom units via `ConversionByPrefix` (e.g., `mAh`).
  - Battery capacity: `ISQ::electricCharge` or `ISQInformation::storageCapacity`.
  - Import `ISQInformation::*` for `byte`, `storageCapacity`, etc.

- **Views & Filters**
  - `filter @AllocationUsage` (not `@Allocation`).
  - Base views package: `package <BV> BaseViews`.
  - Generic graphical view: `DS_Views::SymbolicViews::gv`.

---

## Core SysML v2 Reference (unchanged from the original skill, but with above corrections applied)

[Place the full SysML v2 reference content here, updated with the corrections listed above and in the attached final drone model code.]
