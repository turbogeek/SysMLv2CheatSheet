# SysML v2.0 Language Reference

Alias: SysMLv2

## Overview

Systems Modeling Language (SysML) v2.0 is an OMG standard for model-based systems engineering. It extends the Kernel Modeling Language (KerML) to provide comprehensive modeling capabilities for complex systems.

### Consulting Official Specifications
If you encounter edge cases, ambiguous syntax, or need to verify the official OMG standards, you have two options:

1. **Search via Script:** Run `python ../src/query_specs.py "your search query"` in your terminal to get the most relevant sections.
2. **Direct Markdown Access:** If you need to read the specifications in depth, the raw markdown files are located in `../LLM_skills/Specifications_Markdown/`. You should use your `view_file` tool to read the specific files based on your needs:
   - `SysMLv2.md`: For deep questions on SysMLv2 syntax, modeling rules, and language architecture.
   - `KerML.md`: For core Kernel Modeling Language foundations (what SysML is built upon), type systems, and base semantics.
   - `SysML2API.md`: For instructions and reference on interacting with the SysMLv2 REST API and systems services.
   - `SysMV1toSysMLv2Transform.md`: For understanding how to map, convert, or transform older SysML v1 models into the new SysML v2 semantics.

### Using Standard Libraries
When you need to perform mathematical calculations, query collections, model 3D geometry, use cause-and-effect dynamics, or create custom/compound units (like `[ms]` or `ducks per meter`), you **MUST** consult `../LLM_skills/standard_libraries_skill.md`. This dedicated skill explains how to leverage and extend the 9.x Domain Libraries from SysMLv2 and KerML.

## Core Concepts

### Key things to remember

NEVER use single line comments `/* ` in the SysMLv2 language because these are not persisted to the model and are lost. */
**Import Visibility (Repository Style Rule):**
Lack of visibility on import statements (plain `import`) is forbidden in this repository. 
While standard SysMLv2 allows plain `import`, this repository's strict best practice is to always use `private import` (e.g., `private import ScalarValues::*;`) to prevent namespace pollution. 
`public import` should be avoided except in rare circumstances when there is a specific need to expose the imported elements to the public or to avoid circular dependencies.

**One root package per file (CATIA Magic namespace naming):**
Keep exactly ONE package at the root of the file's namespace; put everything else (helper packages, math extensions, etc.) NESTED inside it. CATIA Magic / Cameo names the imported namespace after the FIRST root element in the containment tree, so a single named root package gives the model a clean, predictable name. Two or more sibling root packages (or a leading bare comment as the first element) produce an awkwardly-named or ambiguous namespace. Put the file's overview in that root package's `doc`, not in a comment above it.

**Reuse the model in the tool — undo, don't pollute (Cameo workflow):**
When iterating against a live Cameo session via a load/REST harness, each successful textual import COMMITS into the open project. Before re-loading an edited version, UNDO the previous load (Cameo has full undo) or remove the previously-loaded packages — otherwise the project accumulates duplicate root packages, and `import Foo::*` may resolve to a STALE earlier copy (missing your new members). Prefer undo/cleanup over renaming packages to dodge the clash. A fresh project or a harness reset also gives a clean load.

**Provide proper diagrams, not just `view` elements:**
A textual model with `view`/`viewpoint` elements is not "diagrammed" until the views are realized as actual diagrams in the tool. For a deliverable, generate the standard diagrams (e.g., the package/containment overview, a BDD-style definition view of the parts, an IBD-style internal view showing ports & connections, a requirements table, and any state-machine/action diagrams) so the model is reviewable visually, not only as text.

**Validate in BOTH the standalone validator and the production tool:**
Run the standalone SysML v2 validator AND load into the live Cameo/Dassault plugin. They are not equivalent — the production plugin is stricter (e.g. it rejects `satisfy <requirement def>`; you must `satisfy` a requirement USAGE). Treat a clean load in the production tool as authoritative.

**Math the standard library lacks goes in a Groovy textual representation:**
`ln`, `exp`, etc. are NOT in the SysML v2 standard Kernel Function Library. Declare them in a nested `MathExtensions` package as a `calc def` with a Groovy textual representation, e.g. `calc def ln { in x : Real[1]; return result : Real[1]; rep lnGroovy language "Groovy" /* result = Math.log(x) */ }`, so a scripting-capable tool can execute them. `sqrt`, `**`, and `^` ARE available.

**Element documentation goes INSIDE the element as `doc`:**
A comment about an element belongs inside it with the `doc` keyword (`attribute mass : MassValue { doc /* ... */ }`), because `doc` persists as element documentation. A comment about a group of following lines is a single block comment above them. Never stack many one-line block comments to fake a multi-line comment, and never embed a `*/` inside another block comment (block comments do not nest).

### Definition and Usage Pattern

The fundamental pattern in SysML v2 is the **definition-usage** relationship:

- **Definitions** classify things (types, templates)
- **Usages** apply definitions in specific contexts (instances, applications)

This pattern applies throughout the language for all major constructs.

### Reserved Words to Avoid

You must never use these reserved words as element names:
`about`, `abstract`, `accept`, `action`, `actor`, `after`, `alias`, `all`, `allocate`, `allocation`, `analysis`, `and`, `as`, `assert`, `assign`, `assume`, `at`, `attribute`, `bind`, `binding`, `by`, `calc`, `case`, `comment`, `concern`, `connect`, `connection`, `constant`, `constraint`, `crosses`, `decide`, `def`, `default`, `defined`, `dependency`, `derived`, `do`, `doc`, `else`, `end`, `entry`, `enum`, `event`, `exhibit`, `exit`, `expose`, `false`, `filter`, `first`, `flow`, `for`, `fork`, `frame`, `from`, `hastype`, `if`, `implies`, `import`, `in`, `include`, `individual`, `inout`, `interface`, `istype`, `item`, `join`, `language`, `library`, `locale`, `loop`, `merge`, `message`, `meta`, `metadata`, `nonunique`, `not`, `null`, `objective`, `occurrence`, `of`, `or`, `ordered`, `out`, `package`, `parallel`, `part`, `perform`, `port`, `private`, `protected`, `public`, `redefines`, `ref`, `references`, `render`, `rendering`, `rep`, `require`, `requirement`, `return`, `satisfy`, `send`, `snapshot`, `specializes`, `stakeholder`, `standard`, `state`, `subject`, `subsets`, `succession`, `terminate`, `then`, `timeslice`, `to`, `transition`, `true`, `until`, `use`, `variant`, `variation`, `verification`, `verify`, `via`, `view`, `viewpoint`, `when`, `while`, `xor`

When you need to use concepts like "standard", "type", "default", "interface", etc., use alternative names like `communicationStandard`, `dataType`, `defaultValue`, `commInterface`, `busInterface`, etc.

**Common Reserved Word Alternatives:**

- `standard` → `communicationStandard`, `protocolStandard`
- `type` → `dataType`, `elementType`, `messageType`
- `default` → `defaultValue`, `defaultSetting`
- `interface` → `commInterface`, `busInterface`, `portInterface`
- `connection` → use as keyword only, not as attribute name
- `state` → `currentState`, `systemState` (when used as attribute)
- **`event` → `buttonEvent`, `userEvent`, `signalEvent`** (CRITICAL - very common mistake as parameter name)
- **`port` → `portNumber`, `tcpPort`, `commPort`** (CRITICAL - conflicts with `port` keyword when used as attribute name)

---

## 1. STRUCTURAL MODELING

### 1.1 Packages (7.5)

Packages organize model elements into namespaces.

```sysml
package VehicleSystem {
    private import ScalarValues::*; /* Or explicitly: private import ScalarValues::Real; */
    /* Package members */
}
```

**Key Features:**

- Provide namespaces for organizing models
- Support imports. Always prefer `private import PackageName::*;` to avoid polluting the namespace of other packages that import yours.
- **CRITICAL RULE:** Any use of scalar values (like `Real`, `Integer`, `String`, `Boolean`) must be accompanied by an import, e.g., `private import ScalarValues::Real;` or `private import ScalarValues::*;`. Without this import, these types are not in scope and will cause errors.
- **Example:**
```sysml
package MyPackage {
    private import ScalarValues::*;
    attribute flag : Boolean;
}
```
- Can be filtered by element kind
- Enable model library organization

### 1.2 Attributes (7.7)

Attributes represent data values, always referential (not composite).

```sysml
attribute def SensorRecord {
    ref part sensor : Sensor;
    attribute reading : Real;
    attribute timestamp : DateTime;
}

part def Vehicle {
    attribute mass : MassValue;
    attribute vin : String;
}
```

**Key Features:**

- Typed by primitive types or attribute definitions
- Always referential (ref)
- Can have feature values (=, :=, default)
- Support redefinition and subsetting

### 1.3 Enumerations (7.8)

Enumerations define restricted sets of enumerated values.

```sysml
enum def TrafficLight {
    enum red;
    enum yellow;
    enum green;
}

enum def Priority :> Integer {
    low = 1;
    medium = 5;
    high = 10;
}
```

**Key Features:**

- Cannot specialize other enumerations
- Can specialize attribute definitions
- Support literal values
- Enumeration variants can have attributes

### 1.4 Occurrences (7.9)

Occurrences are things with temporal extent (lifetime) and possibly spatial extent.

```sysml
occurrence def Flight {
    ref part aircraft : Aircraft;
    attribute departureTime : DateTime;
}

/* Time slices */
occurrence def Mission {
    timeslice planning[1];
    timeslice execution[1];
    timeslice review[1];
}

/* Individuals */
individual def Flight_248 :> Flight;

/* Snapshots */
snapshot def SystemSnapshot :> System;
```

**Key Features:**

- Have lifetimes (temporal extent)
- May have spatial extent
- Support time slices (portions of lifetime)
- Support snapshots (instantaneous states)
- Individuals represent unique entities

### 1.5 Items (7.10)

Items are identifiable passive objects that may be acted upon.

```sysml
item def Fuel {
    attribute octaneRating : Real;
}

part def FuelTank {
    item fuel : Fuel[0..1];
}
```

**Key Features:**

- Passive (acted upon)
- Identifiable objects
- May have spatial extent
- Can flow between parts

### 1.6 Parts (7.11)

Parts are modular structural units that can perform actions.

```sysml
part def Vehicle {
    ref part driver[0..1] : Person;
    part engine : Engine;
    part wheels[4] : Wheel;
    part transmission : Transmission;
}

part vehicle1 : Vehicle {
    perform action startEngine;
}
```

**Key Features:**

- Active (can perform actions)
- Compositional structure
- Support multiplicity
- Can be ordered/unordered, unique/nonunique
- Central to system decomposition

### 1.7 Ports (7.12)

Ports are connection points for interactions, with directed features.

```sysml
port def FuelingPort {
    out fuelOut : Fuel;
    in fuelReturn : Fuel;
    attribute flowRate : Real;
}

part def FuelTank {
    port fuelOutPort : FuelingPort;
}

/* Conjugated port (reversed directions) */
part def Engine {
    port fuelInPort : ~FuelingPort;  /* Conjugated */
}
```

**Key Features:**

- Define interaction points
- Have directional features (in/out/inout)
- Support conjugation (direction reversal)
- Enable port-based connections

### 1.8 Connections (7.13)

Connections are binary relationships with end features.

```sysml
connection def DeviceConnection {
    end part hub : Hub;
    end part device : Device;
    attribute bandwidth : Real;
}

/* Binding connection */
bind part2.feature = part3.feature; /* Must use '=', not 'to' */

/* Bindings cannot contain indices or multiplicity ranges.
   To bind an array of parts, declare each part individually and bind one by one. 
   Binding to an entire multi-part is only allowed when the target side is a part with multiplicity and no indexing is needed. */
bind battery.pwrOut = escs.pwrIn;

/* Succession */
first action1 then action2;
```

**Key Features:**

- Binary relationships with ends
- Support binding (equality)
- Support succession (ordering)
- Can have attributes and constraints

### 1.9 Interfaces (7.14)

Interfaces are connections where all ends are port usages.

```sysml
interface def FuelingInterface {
    end port tankPort : FuelingPort; /* Ends must be ports, not parts */
    end port vehiclePort : ~FuelingPort; /* Use conjugation (~) to reverse direction */
    
    /* Inside an interface, use flow without 'of' and 'from' */
    flow tankPort.fuelOut to vehiclePort.fuelIn;
}
```

**Key Features:**

- All ends must be ports
- Define interaction protocols
- Often use conjugated ports

### 1.10 Allocations (7.15)

Allocations are used to show that one element is realized by another. For example, a logical function can be allocated to a physical component. Allocations map elements across system structures and must apply between usages, not definitions. Allocations are generally an untyped usage unless you are implementing a pattern.

```sysml
/* Here we are using the allocation to map from logical to physical domains */
package LogicalSystem {
    part def PowerSource;
    part power: PowerSource;
}
package PhysicalSystem {
    part def Battery;
    part battery : Battery;
}
package LogicalToPhysicalAllocation {
    /* The canonical and generally preferred syntax for allocations */
    allocation allocate PhysicalSystem::battery to LogicalSystem::power;
}
```

Ensure you allocate between specific usages (e.g., parts), not defs:
part def LogicalSystem {
    part func : Function;
}
part def PhysicalSystem {
    part comp : Component;
}

part logicalUsage : LogicalSystem;
part physicalUsage : PhysicalSystem;

allocation allocate physicalUsage.comp to logicalUsage.func;

```

**Key Features:**

- Assert target realizes source intent
- Support traceability
- Map across abstraction levels
- **Must be applied between usages, not definitions**
- **Create a dedicated package** with part instances (e.g. `myLogical`, `myPhysical`) and place `allocate` statements there.

### 1.11 Units and Quantities

SysMLv2 handles units and quantities through the `ISQ` and `SI` libraries.

```sysml
package ProjectUnits {
    private import SI::*;
    private import ISQInformation::*; /* Required for 'byte', 'storageCapacity', etc. */
    private import MeasurementReferences::ConversionByPrefix;

    /* Define custom units via ConversionByPrefix */
    attribute <ms> millisecond : DurationUnit {
        :>> unitConversion : ConversionByPrefix {
            :>> prefix = milli;
            :>> referenceUnit = s;
        }
    }
}

part def Battery {
    /* Use standard quantity kinds rather than raw Reals when applicable */
    attribute capacity : ISQ::electricCharge; /* Correct for physical batteries (mAh / Ah) */
    attribute storage : ISQInformation::storageCapacity; /* Correct for data storage (bytes) */
}
```

**Key Features:**

- Explicit tracking of units avoids mismatch errors.
- Custom units can be built using prefix conversions or formulas based on reference units.
- Use libraries like `ISQ`, `SI`, and `ISQInformation` properly to keep definitions precise.

---

## 2. BEHAVIORAL MODELING

### 2.1 Flows and Messages (7.16)

**Messages** - Abstract instantaneous transfers:

```sysml
message of ControlSignal
    from controller.sendControl
    to engine.receiveControl;
```

**Streaming Flows** - Continuous transfers:

```sysml
flow fuelFlow : FuelFlow of fuel : Fuel
    from tank.fuelOut to engine.fuelIn;
```

**Succession Flows** - Ordered item transfers:

```sysml
succession flow focus.image to shoot.image;
```

**Key Features:**

- Three types: messages, streaming, succession
- Connect occurrences for transfer
- Can specify items/values transferred
- Support interaction modeling

### 2.2 Actions (7.17)

Actions coordinate other actions and generate effects.

```sysml
action def TakePicture {
    in scene : Scene;
    out picture : Picture;

    action focus : Focus {
        in scene;
        out image;
    }

    first focus then shoot;
    flow focus.image to shoot.image;

    action shoot : Shoot {
        in image;
        out picture;
    }
}
```

**Control Nodes:**

```sysml
fork fork1;
first fork1 then action1;
first fork1 then action2;

join join1;
first action1 then join1;
first action2 then join1;

decide decision1;
first decision1 if condition1 then action1;
first decision1 if condition2 then action2;

merge merge1;
```

**Send Actions:**

```sysml
send payload via signalPort to destination;
```

**Accept Actions:**

```sysml
accept reading : SensorReading via controller;
accept when level > threshold;
accept at Iso8601DateTime("2024-02-01T00:00:00Z");
accept after 30 [s];
```

**Assignment Actions:**

```sysml
assign vehicle.position := vehicle.position + vehicle.velocity * deltaT;
```

**Terminate Actions:**

```sysml
terminate process;
```

**If Actions:**

```sysml
if selectedSensor != null {
    assign reading := selectedSensor.reading;
} else {
    assign reading := undefinedValue;
}
```

**Loop Actions:**

```sysml
/* While loop */
while t < endTime {
    assign y := 2*x;
    then assign x := x + increment;
} until x >= 10;

/* For loop */
for i in 1..n {
    assign y := y + i;
}
```

**Key Features:**

- Parameters (in, out, inout)
- Control flow (succession, fork, join, decide, merge)
- Data flow (flows between actions)
- Communication (send/accept)
- State changes (assignment)
- Conditional and iterative execution

### 2.3 States (7.18)

States represent conditions under which actions execute.  

```sysml
state def OperationalStates {
    entry;
    then off; /* shorthand of the the two lines is equivelent of 'transition 'un-named transition' first entry then off;' */

    state off;
    state starting;
    state on;

    transition off_to_on /* name of transition */
        first off /* transitioning from state (multiple source states require separate transitions; 'or' is not allowed in 'first') */
        accept TurnOn via commPort/* event */
        if isEnabled /* guard (use 'if', not 'where') */
        do action powerUp : PowerUp; /* do action aka effect. Actions must be defined in the same part scope as the state machine to access attributes like batteryVoltage. */
        then on /* transition to state*/; 
}

/* State with actions */
state def Exercising {
    entry action warmup : WarmUp;
    do action exercise : Exercise {
        action strengthTraining;
        then action cardioTraining;
    }
    exit action cooldown : Cooldown;
}
```

**Parallel States:**

```sysml
state def VehicleStates parallel {
    state operationalStates : OperationalStates;
    state healthStates : HealthStates;
}
```

**Exhibit States:**

```sysml
part def Vehicle {
    exhibit state operatingState references VehicleStates::operating;
}
```

**Key Features:**

- Entry, do, exit actions
- Transitions with triggers (accept), guards (if), effects (do)
- Parallel states for concurrency
- Exhibit states for parts
- State-based behavior modeling

### 2.4 Calculations (7.19)

Calculations are evaluations that return results without side effects.

```sysml
calc def Pythagorean {
    in a : Real;
    in b : Real;
    return c : Real = sqrt(a**2 + b**2);
}

/* Calculation usage */
calc hypotenuse : Pythagorean {
    in a = 3.0;
    in b = 4.0;
}
```

**Key Features:**

- Pure functions (no side effects)
- Return results
- Support mathematical expressions
- Can reference external solvers

### 2.5 Constraints (7.20)

Constraints are boolean conditions that must be true.

```sysml
constraint def MassLimit {
    in mass : MassValue;
    in limit : MassValue;
    mass <= limit
}

/* Constraint usage */
constraint vehicleMassLimit : MassLimit {
    in mass = vehicle.mass;
    in limit = 2000[kg];
}

### 2.6 Collection Functions (8.3.11)

When using collection functions such as `size`, `isEmpty`, `forAll`, etc., the function must be qualified with the standard library package name, **without** the `KerML::` prefix.

**Correct Usage:**
```sysml
CollectionFunctions::size(stocks)
```

**Common Mistake:**
Do not use `KerML::CollectionFunctions::size(stocks)`.
```

**Assert Constraints:**

```sysml
assert constraint positiveValue {
    value > 0;
}

/* Negated assertion */
not assert constraint {
    mass > maxMass;
}
```

**Key Features:**

- Boolean predicates
- Can be asserted (must be true)
- Support logical operators
- Used in requirements and analysis

---

## 3. REQUIREMENTS AND ANALYSIS

### 3.1 Requirements (7.21)

Requirements specify stakeholder-imposed constraints.
**CRITICAL RULE:** A `satisfy` relationship is **always** to a requirement *usage*. All requirements intended as requirements of the system must be declared as usages (`requirement`), not definitions (`requirement def`).

Use a `requirement def` ONLY when creating a specific *kind* or *type* of requirement (e.g., PerformanceRequirement, SafetyRequirement).

```sysml
/* Define requirement types (Defs) */
package <RT> RequirementTypes {
    requirement def PerformanceRequirement {
        doc /* A requirement that requires a specific metric to be met. */
    }
    requirement def SafetyRequirement {
        doc /* A requirement that mandates a safety condition. */
    }
}

/* Instantiate actual system requirements (Usages) */
package Requirements {
    /* Use the <'ID'> shortcut syntax for the ID and provide a short name */
    requirement <'REQ-PERF-01'> 'Minimum System MTBF' : RT::PerformanceRequirement {
        doc /* The system shall have a mean time between failures of greater than 5 years. */
        attribute MTBF : Time::Iso8601DateTimeStructure; 
        attribute MTBF_target : Time::Iso8601DateTimeStructure = 5[Time::Iso8601DateTimeStructure::year];

        require constraint {
            MTBF >= MTBF_target /* No semicolon inside constraint block */
        }
    }
    
    requirement <'REQ-SAFE-01'> 'Max Temperature' : RT::SafetyRequirement {
        doc /* The external chassis temperature shall not exceed 45°C. No /* comments allowed! */ */
    }
}
```

**Subjects, Actors, Stakeholders:**

```sysml
/* NOTE: `actor` and `stakeholder` are USAGE keywords, not definition keywords. */
/* The types they reference must be defined as `part def` or `item def` (e.g., `part def Person;`). */
requirement def BrakingRequirement {
    subject vehicle : Vehicle;
    actor environment : DrivingEnvironment;
    stakeholder driver : Person;

    assume constraint { /* environment conditions */ }
    require constraint { /* braking performance */ }
}
```

**Concerns:**

```sysml
concern def SafetyConcern {
    subject system : System;
    stakeholder operator : Person;
    require constraint { /* safety conditions */ }
}

requirement def SafetyRequirement {
    frame concern safetyConcern : SafetyConcern;
}
```

**Satisfy Requirements:**

```sysml
satisfy requirement vehicleMaxMass by vehicle1;

/* In context */
part vehicle1 : Vehicle {
    satisfy rqts : VehicleRequirementsGroup;
}

/* Negated */
not satisfy vehicleMaxMass by vehicle2;
```

**Key Features:**

- Subject (what is constrained)
- Assumed constraints (preconditions)
- Required constraints (postconditions)
- Actors and stakeholders
- Concerns (stakeholder interests)
- Satisfaction assertions
- Requirement IDs (short names)
- Decomposition into subrequirements

### 3.2 Cases (7.22)

Cases produce results to achieve objectives.

```sysml
case def FaultRecovery {
    subject system : AutomationSystem;
    actor engineer : Person;

    objective {
        doc /* Engineer resolves fault and restores system. */
    }

    /* Case actions */
    action diagnoseFault;
    action applyFix;
    action verifyRecovery;
}
```

**Key Features:**

- Subject (what is analyzed/verified/used)
- Objective (requirement to satisfy)
- Actors (external participants)
- Actions/calculations to achieve objective

### 3.3 Analysis Cases (7.23)

Analysis cases perform analyses on subjects.

```sysml
analysis def FuelEconomyAnalysis {
    subject vehicle : Vehicle;

    in drivingCycle : DrivingCycle;
    return fuelEconomy : Real;

    objective fuelEconomyObjective {
        doc /* Determine fuel economy for given driving cycle. */
    }

    /* Analysis actions */
    calc dynamicsAnalysis;
    calc fuelConsumptionAnalysis;
}
```

**Key Features:**

- Subject is analyzed
- Objective concerns the result
- Returns analysis results
- Can use calculations and constraints

### 3.4 Verification Cases (7.24)

Verification cases verify that subjects satisfy requirements.

```sysml
verification def MaxMassVerification {
    subject testVehicle : Vehicle;

    objective massRequirement : MaximumMass {
        subject vehicle = testVehicle;
    }

    /* Verification actions */
    action measureMass;
    action compareToLimit;
}
```

**Key Features:**

- Subject is verified
- Objective requirement subject = case subject
- Verifies requirement satisfaction

### 3.5 Use Cases (7.25)

Use cases specify system usage by actors.

```sysml
use case def PurchaseItem {
    subject :>> item : Item;
    actor customer : Customer;
    actor paymentSystem : PaymentSystem;

    objective {
        doc /* Customer successfully purchases item. */
    }

    include use case authenticateUser;
    include use case processPayment;
}
```

**Key Features:**

- Focus on actor interactions
- Include/extend relationships
- Specify system usage scenarios

### 3.6 Views and Viewpoints (7.26)

Viewpoints frame stakeholder concerns; views satisfy viewpoints. It is highly recommended to use the `expose` keyword along with predefined standard views and filters (such as `EssentialElementsFilter` and `NonStandardLibraryElementFilter`) to ensure views layout properly.

```sysml
package <BV> BaseViews {
    doc /* A set of reusable views. These form the base of the zoo of views and are intended to be the starting point for the creation of new views. For example, the partDefTableView is a filtered and constrained table of parts. It inherits from the generic table and adds a default filter of parts.  */
    private import DS_Views::SymbolicViewsByExpression::*;
    private import DS_Views::TabularViews::*;
    private import SysML::Systems::*;
    
 /* A set of reusable views. These form the base of the zoo. This also serves as training and laboratory for the views */
    
    view partsView : UsagesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
    view genericGraphicalView : DS_Views::SymbolicViews::gv, EssentialElementsFilter, NonStandardLibraryElementFilter;
    view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
        filter @PartDefinition;
        filter @PartUsage;
        /* Note: Always use usage or definition explicitly, e.g. filter @AllocationUsage instead of @Allocation */
    }
    view actionsTreeView : ActionsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;
    view actionsNestedView : ActionsNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
    view 'parts&PortsNestedView' : 'Parts&PortsNestedView', EssentialElementsFilter, NonStandardLibraryElementFilter;
    view requirementsTreeView : RequirementsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;
    view statesNestedView : StatesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
    
    view partsTableView : gt, EssentialElementsFilter, NonStandardLibraryElementFilter {
        filter @PartUsage;
    }
    view partDefTableView : gt, EssentialElementsFilter, NonStandardLibraryElementFilter {
        filter @PartDefinition;
    }
    view requirementTableTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
        filter @RequirementUsage;
    }
    view portDefTableView : gt, EssentialElementsFilter, NonStandardLibraryElementFilter {
        filter @PortDefinition;
    }
}

package Examples {
    view partsViewOfRoadVehicle :> BV::partsView {
        expose Tests::Structure::RoadVehicle::**;
    }
    view partsViewOfRoadVehicleTreeView :> BV::partsTreeView {
        expose Tests::Structure::RoadVehicle::**;
    }
}
```

**Key Features:**

- Viewpoints are requirements
- Views satisfy viewpoints
- Frame stakeholder concerns
- Organize information presentation
- Use `expose` to auto-display the context within a view.
- Always use `EssentialElementsFilter` and `NonStandardLibraryElementFilter` with base views to aid in ensuring that views with an expose statement do not include details that are not relivent to the stakeholders. In other words, it's often better to start with a filtered view rather than a base view.

---

## 4. METADATA (7.27)

Metadata annotates model elements with additional information.

```sysml
metadata def <mid> ReviewMetadata {
    attribute reviewer : String;
    attribute reviewDate : String;
    attribute status : String;
}

@ReviewMetadata {
    reviewer = "John Doe";
    reviewDate = "2024-01-15";
    status = "Approved";
}
part criticalComponent : Component;
```

**Key Features:**

- Annotate model elements
- Custom metadata definitions
- Support tool integration
- Enable model management

---

## 5. KEY SYNTAX PATTERNS

### Feature Values

```sysml
/* Bind (equality) */
attribute count : Integer = 12;

/* Initial value */
attribute counter : Integer := 0;

/* Default value */
attribute cutoff : Real default = 0.75 * average;
```

### Multiplicities

```sysml
part wheels[4] : Wheel;           /* Exactly 4 */
part driver[0..1] : Person;       /* Optional */
part passengers[*] : Person;      /* Any number */
part engines[1..*] : Engine;      /* At least 1 */
```

### Ordered and Unique

The modifiers `ordered`, `unordered`, `unique`, `nonunique` are placed **after** the multiplicity specifier, **not inside braces**. 

```sysml
part orderedList[*] ordered nonunique;
part uniqueSet[*] unordered unique;
attribute stocks : StockData[*] ordered nonunique;
```

### Specialization

```sysml
part def SportsCar specializes Vehicle;
part def SportsCar :> Vehicle;  /* Shorthand */
```

### Redefinition

```sysml
attribute :>> mass = vehicle.totalMass;
```

### Subsetting

```sysml
part :> vehicles;
```

### References

```sysml
ref part owner : Person;
```

### Documentation

```sysml
doc /* This is a documentation comment. */
```

### Comments

```sysml
/* Single line comment */
/* Multi-line
   comment */
```

---

## 6. MODEL LIBRARIES (Section 9)

SysML v2 includes standard model libraries:

- **Kernel Libraries** (KerML base)
- **Core Libraries** (basic types and functions)
- **Domain Libraries** (units, quantities, geometry, etc.)
- **Systems Libraries** (requirements, cases, actions, states, etc.)
- **Analysis Libraries** (trade studies, verification, etc.)

Standard imports:

```sysml
private import ScalarValues::*;
private import ISQ::*;
private import SI::*;
```

---

## 7. COMMON PATTERNS

### Requirement Template Pattern

Define general requirement, specialize for contexts:

```sysml
requirement def MaximumValue {
    attribute actual : Real;
    attribute required : Real;
    require constraint { actual <= required }
}

requirement maxSpeed : MaximumValue {
    :>> actual = vehicle.currentSpeed;
    :>> required = speedLimit;
}
```

### Port-Interface Pattern

Use conjugated ports for connections:

```sysml
port def DataPort {
    out data : DataType;
    in ack : Boolean;
}

part sender {
    port out : DataPort;
}

part receiver {
    port in : ~DataPort;  /* Conjugated */
}

interface connection sender.out to receiver.in;
```

### State Machine Pattern

Define states with transitions:

```sysml
state def SystemStates {
    entry; then idle;

    state idle;
    state active;
    state error;

    transition idle_to_active
        first idle
        accept Start
        then active;

    transition active_to_idle
        first active
        accept Stop
        then idle;
}
```

### Action Decomposition Pattern

Break down complex actions:

```sysml
action def ProcessOrder {
    in order : Order;
    out confirmation : Confirmation;

    action validateOrder {
        in order;
        out valid : Boolean;
    }

    first validateOrder;

    decide;
    if validateOrder.valid then processPayment;
    if not validateOrder.valid then rejectOrder;

    merge;
    then sendConfirmation;
}
```

---

## 8. BEST PRACTICES

1. **Use Definitions as Templates**: Create reusable definitions, specialize in usages
2. **Leverage Standard Libraries**: Import and use standard types and units
3. **Document Requirements**: Use doc comments for requirement text
4. **Use Short Names for IDs**: Provide requirement IDs with short names
5. **Organize with Packages**: Structure models into logical packages
6. **Type Everything**: Explicitly type features for clarity
7. **Use Ports for Interactions**: Model interactions through ports and interfaces
8. **Separate Structure and Behavior**: Parts for structure, actions/states for behavior
9. **Frame Concerns**: Use concerns to capture stakeholder needs
10. **Verify Requirements**: Create verification cases for requirements

---

## 9. COMPARISON WITH SysML v1

Major differences from SysML v1:

1. **Textual, Model and Diagrams**: SysML v2 has a textual syntax, so modelers can modify and interpret the model via text. The truth is still the model, but there are now many different methods for writing the model, including using an LLM.
2. **No Blocks**: Parts replace blocks as the primary structural element
3. **Unified Actions/Activities**: Integrated action model (v1 had separate concepts)
4. **Calculations**: New concept for side-effect-free computations
5. **Analysis/Verification Cases**: Formalized case concepts
6. **Stronger Typing**: More rigorous type system based on KerML
7. **Feature-Based**: Everything is a feature with consistent semantics
8. **Occurrence Semantics**: Explicit temporal and spatial extent modeling
9. **Conjugated Ports**: Built-in support for direction reversal
10. **Metadata Framework**: Standardized metadata annotations
11. **Views and Viewpoints**: Are closer to the concepts of INCOSE and ISO 15288. Viewpoints are a type of requirement for Views. Note that Views are still evolving in SysML v2 and not yet fully specified in the standard such that they can be used effectively by different vendor tools. Views have an expose that works like the package import to load data for the view to render and filter to remove items from the view.
12. **Concerns**: New concept in v2. A concern definition or usage is declared as a requirement definition or usage (see 7.21.2 ) using the kind keyword concern instead of requirement. Otherwise, a concern definition or usage is specified exactly like a regular requirement definition or usage. The intent, however, is that the concerns of one or more stakeholders can be modeled as the required constraints of a concern definition or usage with appropriate stakeholder parameters.
13. **constraint, assume constraint, and require constraint**:  New concept in v2. A constraint definition or usage is declared as a requirement definition or usage (see 7.21.2 ) using the kind keyword concern instead of requirement. Otherwise, a concern definition or usage is specified exactly like a regular requirement definition or usage. The intent, however, is that the concerns of one or more stakeholders can be modeled as the required constraints of a concern definition or usage with appropriate stakeholder parameters.One or more concerns can then be framed in other requirement definitions and usages. A framed concern usage is a subrequirement usage (see 7.21.2 ) indicated by prefixing a concern usage declaration with the keyword frame. As for an assumed or required constraint, the keyword **frame** can be used rather than frame concern to declare a framed concern using reference subsetting. In any case, since the framed concern usage itself is a subrequirement, it will automatically be considered a required constraint of its containing requirement definition or usage.

## 10. METAMODEL CONCEPTS (Section 8)

The SysML v2 metamodel defines:

- **Abstract Syntax**: The structure of model elements
- **Concrete Syntax**: Textual and graphical notation
- **Semantics**: Meaning and behavior of elements
- **Well-Formedness Rules**: Validity constraints

### Key metamodel concepts

- All elements are features
- Features can be types or usages
- Relationships: specialization, redefinition, subsetting, typing, featuring
- Namespaces and membership
- Feature chaining and qualification

---

## SUMMARY

SysML v2 provides a comprehensive, rigorous language for systems modeling with:

- **Structural modeling**: Parts, ports, connections, interfaces
- **Behavioral modeling**: Actions, states, flows, calculations
- **Requirements modeling**: Requirements, concerns, satisfaction
- **Analysis modeling**: Cases for analysis, verification, use
- **Strong semantics**: Based on KerML foundation
- **Textual notation**: Primary syntax for precision and version control
- **Graphical notation**: Supporting visualization
- **Extensibility**: Metadata and library mechanisms

The language supports model-based systems engineering from requirements through design, analysis, and verification.

## Modeling Conventions & Best Practices (Custom Additions)

- **Library Packages:** Always use library package (e.g., library package 'Requirement Templates') to house reusable templates and definitions (def). Place usages (e.g.,
equirement) in actual model context packages.
- **Requirement Definitions vs. Usages:**
equirement def elements should act as reusable abstractions and be relegated to library package. The specific statement/instance of a requirement should be an element usage (
equirement) typed by a definition.
- **Actions and States:** In a similar vein, ction def or state def define the flows/behavioral blocks. The usage ction or state sits inside the concrete parts that exhibit or execute them.
- **Views Placement:** Tables and tree views should be placed *directly within the package they are documenting* rather than grouped externally.
- **Structure Visualization:** For packages featuring structure or dependencies, leverage DS_Views::SymbolicViewsByExpression::TreeView (tree view) using expose PackageName::** to automatically evaluate and display elements.

---

# Exhibit states

Exhibited states are defined in a part definition or part usage and are used to model the states of a part.  The syntax is `exhibit state <name> : <state machine>`.

Example of exhibiting states:

```sysml
state def OperationalStates {
    entry;
    then off;
    state off;
    state starting;
    state on;
    transition off_to_on
        first off
        accept TurnOn via commPort
        if isEnabled
        do action powerUp : PowerUp
        then on;
}
part  Vehicle {
    exhibit state operatingState : OperationalStates;
}
\\n
# Requirements and Analysis

## Requirements

Requirements specify stakeholder-imposed constraints. Note that requirements are documented using the same syntax as other definitions and usages. The main difference is the intent. The definition of a requirement is a requirement that specifies a constraint that is a template for a kind of requirement, a pattern of a requirement. A usage of a requirement is a requirement of a specific type that specifies the ID, a name that is a summary of the shall statement, and the required constraint, measured and targeted values and or condition and acceptance criteria.
Example of a requirement definition

```sysml
package <RT> RequirementTypes {
    requirement def PerformanceRequirement {
        doc /* A requirement that requires a specific metric to be met. */
    }
}
`\\n
Example of a requirement usage
```sysml
package Requirements {
    requirement <'REQ-PERF-02'> 'Coil MTBF' : RT::PerformanceRequirement {
            doc /* The induction coil assembly shall have a Mean Time Between Failures (MTBF) of at least 10,000 cooking cycles. */
            attribute coilMTBFCycles : Real;
            attribute coilMTBFCycles_target : Real = 10000.0;
            require constraint {
                coilMTBFCycles >= coilMTBFCycles_target
            }
        }
        requirement <'REQ-PERF-03'> 'Energy Efficiency' : RT::PerformanceRequirement {
            doc /* The system shall convert at least 85% of drawn electrical energy into heat at the cooking surface. */
            attribute energyEfficiency : Real;
            attribute energyEfficiency_target : Real = 0.85;
            require constraint {
                energyEfficiency >= energyEfficiency_target
            }
        }
}
```

# Verification Definitions

# Views and Viewpoints

Views present structured subsets of the model. Prefer reusable base views and derived concrete views, and place concrete views near the packages they document when practical.

Example:

```sysml
verification def MaxMassVerification {
    subject testVehicle : Vehicle;

    objective massRequirement : MaximumMass {
        subject vehicle = testVehicle;
    }
}
```

# Critical Authoring Constraints

## Never invent syntax patterns when a standard pattern is known

When generating SysMLv2, prefer a known library/example-backed syntax pattern over an improvised one. If a construct is not clearly supported by the reference pattern in the skill or provided libraries, do not guess. Use a simpler, clearly valid pattern instead.

Examples:

- Do not invent unit names if they are not present in the imported libraries.
- Do not invent typed quantity names unless they are defined in a project or standard library.
- Do not invent interface endpoint paths that have not been explicitly declared.
- Do not invent view patterns when a project-specific BaseViews pattern exists.

## Requirements must always use the full requirement usage pattern

All actual system requirements shall be requirement usages, not definitions.

Required pattern:

```sysml
requirement <'REQ-ID'> 'Short Name' : RequirementType {
    doc /* Full shall statement. */
}
```

Rules:

- The ID must use the < 'ID' > form.
- The short name must be a concise summary of the requirement.
- The doc comment must contain the authoritative full “shall” statement.
- Do not omit the short name.
- Do not replace the shall statement with the short name.
- Do not create actual project/system requirements as requirement def.

## allocate, satisfy, and verify must connect usages only

Never connect definitions in

- allocate
- satisfy
- verify

## Only connect usages

Correct:

```sysml
part logicalDrone : LogicalDrone;
part physicalDrone : PhysicalDrone;

allocate physicalDrone.camera to logicalDrone.detect;
satisfy someRequirement by logicalDrone.detect;
```

Incorrect:

```sysml
allocate CameraModule to TargetDetectionSystem;
satisfy PerformanceRequirement by TargetDetectionSystem;
verify PerformanceRequirement;
```

### Interface ends must reference actual port usages

All interface def ends and interface usages must terminate on ports, not on parts unless those ends are explicitly part ends in a connection definition.

Rules:

- If an interface end is end port, the referenced target must be a port usage.
- Do not bind an end port to a part usage.
- If a logical subsystem needs to participate in an interface, that logical subsystem must explicitly declare the corresponding port.

Correct:

```sysml
part def TargetDetectionSystem {
    port videoIn : ~VideoDataPort;
}

interface videoFromCamera : VideoDataInterface {
    end port source = physicalDrone.cameraOut;
    end port sink = logicalDrone.detect.videoIn;
}
```

Incorrect:

```sysml
interface videoFromCamera : VideoDataInterface {
    end port source = physicalDrone.cameraOut;
    end port sink = logicalDrone.detect;
}
```

## Quantitative attributes must be explicitly typed

Do not emit:

```sysml
attribute minEndurance = 20 [min];
```

Use:

```sysml
attribute minEndurance : DurationValue = 20 [min];
```

Rules:

- Every quantitative attribute shall have an explicit type/kind.
- Use standard library quantity kinds if known and available.
- If the exact quantity kind is project-specific or uncertain, define a project value type first, then use it consistently.
- Do not leave engineering values as untyped attribute = value [unit].

## Units must exist in an imported library or be defined explicitly

Do not assume a unit symbol exists.

Rules:

- Before using a unit, verify that it exists in the imported libraries or define it in a project unit package.
- If a project-specific or missing prefixed unit is needed, define it using the same pattern as the SI library.
- If a unit requires ConversionByPrefix, explicitly import:

```sysml
private import MeasurementReferences::ConversionByPrefix;
```

Good example:

```sysml
package ProjectUnits {
    private import SI::*;
    private import MeasurementReferences::ConversionByPrefix;

    attribute <ms> millisecond : DurationUnit {
        :>> unitConversion : ConversionByPrefix {
            :>> prefix = milli;
            :>> referenceUnit = s;
        }
    }

    attribute <'mm/h'> 'millimetre per hour' : SpeedUnit = mm / h;
}
```

## Use the project’s exact view architecture when provided

If the project provides a view pattern, follow it exactly.

If a project-specific BaseViews pattern exists, use:

- reusable base views in a BaseViews package
- derived concrete views using :>
- EssentialElementsFilter
- NonStandardLibraryElementFilter
- expose ...::

Do not improvise alternate view structures if a project example has been supplied.

Place concrete views near the packages they document
When possible, concrete tree/table views should be placed in or near the package they document, not only in a single global view package.

Preferred:

```sysml
package Requirements {
    package Views {
        view requirementsTree :> Model::Views::BV::requirementsTreeView {
            expose Requirements::;
        }
    }
}
```

## doc comments must use exact SysML comment form

Always use:

```sysml
doc /* ... */
```

### Rules

- Do not use single-line comments (two forward slashes).
- Use normal block comments only where documentation semantics are not intended.
- use doc /*...*/ for requirement shall statements.
- Always use a doc comment to describe the contents of a package, part, port, interface definition, attribute, value, use case, analysis, or state, except when it is obvious or already documented somewhere else via a doc comment of the definition used.
- Always use a doc comment to describe the contents of a view.

## Be careful with keyword-sensitive syntax

Do not casually substitute similar-looking forms for actual SysMLv2 syntax.

Examples:

- frame is a SysMLv2 keyword and must be used deliberately and correctly.
- references has a specific meaning and must not be used as a substitute for typed usage syntax.
- exhibit state syntax must follow known valid patterns.
- to aid in accidentally creating non-keywords, use domain specific names and use camel case.
- For definitions, start with a capital letter and convert to lower camel case for usages of that definition, For example, if the definition is `TargetDetectionSystem`, the usage should be `targetDetectionSystem`.

## If the project or skill provides a correct example, mirror that example

## Prefer library package separation between defs and usages

Use library packages for reusable definitions:

- requirement def
- part def
- port def
- interface def
- analysis def
- state def
- action def

## Use non-library/model-context packages for usages

- requirement
- part
- state
- verification
- analysis
- interface usages / connections / allocations

## This separation should be preserved unless the user explicitly wants a flatter structure

## Add a pre-output validation checklist

Before returning SysMLv2, validate:

- Are all real requirements usages, not defs?
- Do all requirement usages use < 'ID' > 'Short Name' and doc /*... shall ...*/?
- Do allocate, satisfy, and verify only connect usages?
- Does every interface endpoint resolve to an actual declared port?
- Are all engineering-valued attributes typed?
- Does every unit used exist in imported libraries or project units?
- Are imports explicit and syntactically correct?
- Are comments using doc /*...*/ where intended?
- Do views follow the provided BaseViews pattern, if one exists?
- Is the output a single coherent file if the user requested a single file?

If any answer is “no”, revise before returning.

## When the user provides project conventions, those override generic style

If the user provides:

- a known BaseViews package pattern,
- a units library excerpt,
- a preferred requirement style,
- a correct example of state exhibition,
- a preferred package structure,

then the generated model should conform to those conventions, even if a more generic pattern would also be valid.

Examples:

- If the user provides a ProjectUnits example, use that exact style.
- If the user corrects exhibit-state syntax, use that syntax consistently thereafter.
- If the user provides a BaseViews pattern, stop improvising alternative view structures.

# Do not solve uncertainty by introducing weak placeholder abstractions

Avoid papering over uncertainty with vague project-local placeholders when a stronger standard-typed pattern is expected.

Examples:

- Do not create vague ValueTypes unless necessary; prefer explicit standard quantity kinds when available and known.
 If you do create project-local quantity types, explain that they are project abstractions and keep them consistent.
- Do not create structure that obscures whether an element is a definition or a usage.

# Canonical examples to follow

## Requirement usage

```sysml
requirement <'SYS-PER-002'> 'Maximum Tracking Latency' : PerformanceRequirement {
    doc /* The system shall update target tracks with end-to-end latency not greater than 50 [ms]. */
    attribute maxTrackingLatency : DurationValue = 50 [ms];
}
```

Project units

```sysml
package ProjectUnits {
    private import SI::*;
    private import MeasurementReferences::ConversionByPrefix;

    doc /* Project-specific units added where the standard SI library does not already provide the needed named unit. */

    attribute <ms> millisecond : DurationUnit {
        :>> unitConversion : ConversionByPrefix {
            :>> prefix = milli;
            :>> referenceUnit = s;
        }
    }

    attribute <'mm/h'> 'millimetre per hour' : SpeedUnit = mm / h;
}
```

Exhibit state

```sysml
part def Vehicle {
    exhibit state missionState : Behavior::DroneLifecycleStates;
}
```

Interface endpoint

```sysml
part def TargetDetectionSystem {
    port videoIn : ~VideoDataPort;
}

interface videoFromCamera : VideoDataInterface {
    end port source = physicalDrone.cameraOut;
    end port sink = logicalDrone.detect.videoIn;
}
```

Base views

```sysml
package <BV> BaseViews {
    private import DS_Views::SymbolicViewsByExpression::*;
    private import DS_Views::TabularViews::*;
    private import SysML::Systems::*;

    view partsView : UsagesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
    view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
        filter @PartDefinition;
        filter @PartUsage;
    }
    view requirementsTreeView : RequirementsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;
    view useCasesTree : DS_Views::SymbolicViews::gv, EssentialElementsFilter, NonStandardLibraryElementFilter {
        doc /* Tree view of all use cases. NOTE change the expose as necessary */
        expose CE::UseCases::**;
        filter @UseCaseUsage;
    }
}
```

# Why these additions matter

They directly target the errors that kept recurring:

- malformed comments,
- weak requirement formatting,
- wrong unit assumptions,
- missing imports,
- interface endpoints on nonexistent ports,
- usage/definition confusion,
- wrong exhibit-state syntax,
- drifting away from project-specific view conventions.

These are not just “nice to have” style notes — they are failure-prevention rules.

# Best Practices

- Use definitions as reusable templates and usages for concrete model content.
- Keep actual requirements as usages.
- Type everything that carries engineering meaning.
- Use only units that exist in imported libraries or explicit project units.
- Use ports for interactions and ensure interface ends point to ports.
- Separate structure and behavior.
- Place concrete views within or near the packages they document.
- Preserve user-provided project conventions.
- Validate usage-vs-definition discipline before returning output.
- When in doubt, use the simpler known-valid pattern rather than guessing.

## Summary

This skill is intended to produce SysMLv2 that is:
-syntactically disciplined,
-traceability-correct,
-tool-friendly,
-explicit about units and quantities,
-explicit about usage vs definition,
-aligned to project-specific conventions when provided.
 The highest-priority rules

- The highest-priority rule is: do not guess when a valid pattern is available or when uncertainty remains.
- If there is a question, ask.
- If there is a conflict between rules, ask.

---

## Additional Modeling Rules from Iterative Corrections (Toaster Example)

*These rules were derived from errors encountered and corrected during the development of a complete toaster model. They supplement the existing best practices and must be followed to avoid similar issues.*

- **System Subject for Use Cases**  
  The subject of a use case (and often the top‑level system) must be a `part def` (e.g., `part def ToasterSystemRoot`). Never use an undefined name.

- **Quoting of Special Characters in Units**  
  When a unit symbol contains characters that are not alphanumeric or underscore, enclose it in single‑quoted square brackets: `['°C']`. Unquoted versions like `[°C]` may be misinterpreted.

- **Prefer Standard ISQ Quantities**  
  Avoid inventing custom attribute definitions for physical quantities when a suitable ISQ quantity exists. For example, use `ISQElectromagnetism::electricPower` rather than `attribute def ElectricPower :> ISQ::power`. This ensures interoperability and reduces redundant definitions.

- **Conjugation is a Usage Modifier, not a Definition**  
  Never import a conjugated port definition (e.g., `private import LogicalDesign::~UserSettings`). Conjugation (`~`) is applied to a usage of a port, not to the definition. Always import the base port definition and write `~PortDef` where needed in usage contexts.

- **Complete Definition of Referenced Elements**  
  Every port, part, attribute, or action that is referenced must have a corresponding definition. For example, `wallPlug` must be declared as a port of the enclosing part, and every action in a state machine effect (like `StopHeatingAction`) must be defined (as `action def`).

- **Exhibit State Bindings**  
  Inside an `exhibit state` clause, use `bind attribute = externalAttribute;` to connect the state machine’s attributes to the owning part’s attributes. Do **not** use attribute redefinition (`:>>`) for this purpose.

- **Avoid Reserved Words in Port Names**  
  Port names such as `in`, `out`, `port`, `event`, etc., clash with keywords. Use longer descriptive names like `inPower`, `outPower`, `powerIn`, `powerOut`. This applies even to simple physical ports.

- **Multiple Connection Targets**  
  The `connect` statement accepts exactly one source and one target. To connect a single source to multiple destinations, use separate `connect` statements. For example:
  ```sysml
  connect timer.outputContacts to innerElements.powerIn;
  connect timer.outputContacts to outerElements.powerIn;
  ```

- **Avoid Keyword "requirement" in Satisfy Statements**  
  When satisfying a requirement, do not use the keyword `requirement` before the requirement usage name. Use `satisfy [RequirementName];` directly.
  *Incorrect:* `satisfy requirement Requirements::'Browning Time';`
  *Correct:* `satisfy Requirements::'Browning Time';`

- **Avoid Keyword "concern" in Frame Statements**  
  When framing a concern, use the `frame` keyword directly followed by the concern name. Do not include the word `concern`.
  *Incorrect:* `frame concern StakeholderConcerns::'User Safety';`
  *Correct:* `frame StakeholderConcerns::'User Safety';`

- **Ensure Defining Parts are in Reachable Scope**  
  When a part (or subject in a use case) is typed by a `part def`, that definition must be explicitly declared in the same scope or imported. Do not assume the existence of implicitly understood terms (e.g. `subject toaster : Toaster;` requires `part def Toaster;` to be defined or imported).

- **CollectionFunctions Prefix Usage**  
  Never use the `KerML::` prefix when calling collection functions. Use `CollectionFunctions::size(...)` or similar.

- **Ordered/Nonunique Modifier Placement**  
  Placement of `ordered`, `nonunique`, etc., must be directly after the multiplicity (e.g., `[*] ordered`) and **never** inside braces `{}`.

- **Explicit ScalarValues Import**  
  Always include `private import ScalarValues::*;` in any package that uses the primitive types `Boolean`, `Real`, `Integer`, or `String`.

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
