# SysML v2 AI Agent Skill / Comprehensive Reference

**Generated on:** 2026-05-07 11:53:46

---

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


---

# SysML v2 Cheat Sheets: Complete Collection

**Generated on:** 2026-05-07 11:53:46

---

## Table of Contents

- Action Patterns Sheet
- Actions Sheet
- Behavior Sheet
- Calc Sheet
- Cases Sheet
- Connections Sheet
- Constraints Sheet
- Graphical Sheet
- Patterns Sheet
- Reference Sheet
- Relationships Sheet
- Requirements Sheet
- Shorthand Sheet
- State Patterns Sheet
- States Sheet
- Structure Sheet
- Views Sheet

---

<div style='page-break-before: always;'></div>

# Action Patterns Sheet

# Action Patterns Cheat Sheet

*Standard Action Patterns*

## 1. While Loop

Iterate while condition is true.

```sysml
package WhileLoopExample {
    private import ScalarValues::*;
    action def Main {
        attribute x : Integer = 0;
        action loopAction {
            while x < 10 {
                assign x := x + 1;
            }
        }
    }
    view LoopView {
        expose Main;
    }
}
```

## 2. For Loop

Iterate over a range.

```sysml
package ForLoopExample {
    private import ScalarValues::*;
    action def Main {
        action process { in i : Integer; }
        action loopAction {
            for i in 1..10 {
                perform process { in i = i; }
            }
        }
    }
    view LoopView {
        expose Main;
    }
}
```

## 2b. Loop Variations

Collections, Until, & Infinite Loops.

```sysml
package LoopVariationsExample {
    private import ScalarValues::*;
    attribute def Power;
    attribute profile : Power[*];
    action def Main {
        attribute x : Integer = 0;
        attribute done : Boolean = false;
        
        action collectionLoop {
            for p : Power in profile {
                /* body */
            }
        }
        
        action whileUntilLoop {
            while x < 10 {
                assign x := x + 1;
            } until done;
        }
        
        action infiniteLoop {
            loop {
               assign x := x + 1;
            } until x > 100;
        }
    }
    view LoopView {
        expose Main;
    }
}
```

## 3. If / Else

Conditional execution.

```sysml
package ActionPatterns_3IfElse {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute x : Integer = 0;
        attribute y : Integer;
        if x > 0 {
           assign y := 1;
        } else {
           assign y := 0;
        }
    }
    view ExposeExample { expose Main; }
}
```

## 4. Accept Variations

Waiting for events/conditions.

```sysml
package ActionPatterns_4AcceptVariations {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute temp : Real;
        attribute s : Real;
        part schedule;
        action def StartSignal;
        action acceptSomething {
            accept startSignal : StartSignal;
            doc /* about startSignal ... */
            accept when temp > 100;
            accept at schedule;
            accept after 10 [s];
        }
    }
    view ExposeExample { expose Main; }
}
```

## 5. Send Variations

Named and unnamed sends.

```sysml
package ActionPatterns_5SendVariations {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        action def StartSignal;
        part p1;
        attribute sig : StartSignal;
        action sendA { send sig via p1; }
        send sig via p1;
        doc /* Named vs Unnamed */
    }
    view ExposeExample { expose Main; }
}
```

## 6. Control Nodes

Rules:
- **Fork**: Outgoing target [1].
- **Join**: Incoming source [1].
- **Decide**: Outgoing target [0..1].
- **Merge**: Incoming source [0..1].

```sysml
package ActionPatterns_6ControlNodes {
    private import ScalarValues::*;
    private import SysML::*;
    
    action def Main {
        /* 1. Fork: Outgoing target mult 1..1 */
        fork f1;
        
        /* 2. Join: Incoming source mult 1..1 */
        join j1;
        
        /* 3. Decide: Outgoing target mult 0..1 (Optional) */
        decide d1;
        
        /* 4. Merge: Incoming source mult 0..1 (Optional) */
        merge m1;
    }

    view ExposeExample {
        expose Main;
    }
}
```

## 7. Advanced Send

Binding params & flows.

```sysml
package ActionPatterns_7AdvancedSend {
    private import ScalarValues::*;
    private import ScalarValues::*;
    private import SysML::*;
    private import Base::*;
    action def Main {
        attribute val : Anything;
        part monitor;
        action sendReading send {
           in payload;
           in sender = monitor;
        }
        flow val to sendReading.payload;
    }
    view ExposeExample { expose Main; }
}
```



<div style='page-break-before: always;'></div>

# Actions Sheet

# Actions Cheat Sheet

*Action Definitions and Flow*

## 1. Action Definition

Reusable behavior spec.

```sysml
package Actions_1ActionDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Speed;
    attribute def Result;
    action def Serve {
       in speed : Speed;
       out result : Result;
       first toss;
       then strike;
       action toss;
       action strike;
    }
}
```

## 2. Action Usage

Executing an action.

```sysml
package Actions_2ActionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    action def Serve;
    action def Main {
        action playPoint {
           action serve : Serve;
           perform serve { /* ... */ }
           action serve2 : Serve;
           perform serve2;
        }
    }
    view ExposeExample { expose Main; }
}
```

## 4. Parameters

Input, Output, Return.

```sysml
package Actions_4Parameters {
    private import ScalarValues::*;
    private import SysML::*;
    action def ComputeValues {
       in x : Real;
       inout y : Real;
       out z : Real;
    }
}
```

## 5. Send/Accept Signal

Async communication.

```sysml
package Actions_5SendAcceptSignal {
    private import ScalarValues::*;
    private import SysML::*;
    package Signal { action def Stop; action def Resume; }
    action def Main {
        part pOut;
        part ctl;
        action communicate {
           attribute sig : Signal::Stop;
           send sig via pOut to ctl;
           accept Signal::Resume;
        }
    }
    view ExposeExample { expose Main; }
}
```

## 6. Succession (first/then)

Ordering of actions.

```sysml
package Actions_6Successionfirstthen {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        action start;
        action process;
        action finish;
        first start;
        then process;
        then finish;
        doc /* Control flow sequence */
    }
    view ExposeExample { expose Main; }
}
```

## 7. Assignment (assign)

Setting values.

```sysml
package Actions_7Assignmentassign {
    private import ScalarValues::*;
    action def Main {
        attribute x : Integer;
        attribute y : Integer;
        assign x := 42;
        assign y := x + 1;
        doc /* Value assignment */
    }
    view ExposeExample { expose Main; }
}
```

## 8. Trigger

Reacting to events.

```sysml
package Actions_8Trigger {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        action def Tick;
        part clock;
        attribute t : Real;
        accept tick : Tick via clock;
        accept when t > 10.0;
        doc /* Event trigger with guard */
    }
    view ExposeExample { expose Main; }
}
```



<div style='page-break-before: always;'></div>

# Behavior Sheet

# Behavior Cheat Sheet

*State Machines and Actions*

## 1. State Definition

States and lifecycle actions.

```sysml
package Behavior_1StateDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    state   def  PracticeSession  {
       entry ;  exit ;
       state  Idle ;
       state  Serving ;
    }
}
```

## 2. Transitions

Move between states on triggers.

```sysml
package Behavior_2Transitions {
    private import ScalarValues::*;
    private import SysML::*;
    state def Main {
        state Idle;
        state Serving;
        action def Log { in msg : String; }
        action def Start;
        part Remote { action start : Start; }
        transition startServe
           first Idle
           accept Remote.start
           do action log : Log { in msg = 'Serving'; }
           then Serving;
    }
}
```

## 3. Guards & Effects

Conditions and actions on transition.

```sysml
package Behavior_3GuardsEffects {
    private import ScalarValues::*;
    private import SysML::*;
    state def Main {
        state Green;
        state Red;
        attribute traffic : Integer;
        action resetTimer;
        transition t2 first Green if traffic == 0 do resetTimer then Red;
    }
}
```

## 3b. Internal Transition

Self-transition pattern.

```sysml
package Behavior_3bInternalTransition {
    private import ScalarValues::*;
    private import SysML::*;
    state def Monitoring {
       state selfCheck;
       action def tick;
       action check;
       transition t1 first selfCheck accept tick do check then selfCheck;
    }
}
```

## 4. Action Definition

Reusable behavior spec.

```sysml
package Behavior_4ActionDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Speed;
    attribute def Result;
    action def Serve {
       in speed : Speed;
       out result : Result;
       first toss;
       then strike;
       action toss;
       action strike;
    }
}
```

## 5. Action Usage

Executing an action.

```sysml
package Behavior_5ActionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    action def Serve { in speed : Integer; }
    /* Wrapped Snippet (Action Context) */
    action def Main {
        action  playPoint  {
           action  serve  :  Serve ;
           perform  serve  {
              in  speed  =  60 ;
           }
        }
    }

    view ExposeExample {
        expose Main;
    }
}
```

## 6. Use Cases

High-level user goals.

```sysml
package Behavior_6UseCases {
    private import ScalarValues::*;
    private import SysML::*;
    part def PickleBot;
    part def Player;
    use case def Practice {
       subject b : PickleBot;
       actor p : Player;
       objective {
          doc /* Improve skills */
       }
    }
}
```



<div style='page-break-before: always;'></div>

# Calc Sheet

# Calculation Cheat Sheet

*Calculations and Constraints*

## 1. Calculation Definition

Reusable math expressions.

```sysml
package Calculations_1CalculationDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Voltage;
    attribute def Current;
    attribute def Power;
    calc def PowerCalc {
       in v : Voltage;
       in i : Current;
       return p : Power = v * i;
    }
}
```

## 2. Calculation Usage

Performing a calculation.

```sysml
package Calculations_2CalculationUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Voltage; attribute def Current; attribute def Power;
    calc def PowerCalc { in v : Voltage; in i : Current; return p : Power; }
    /* Wrapped Snippet (Action Context) */
    action def Main {
        calc  p_motor  :  PowerCalc  {
           in  v  =  12.0 ;
           in  i  =  5.0 ;
        }
    }

    view ExposeExample {
        expose Main;
    }
}
```

## 4. Constraint Usage

Applying a constraint.

```sysml
package Calculations_4ConstraintUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    constraint def MassLimit { in m : Mass; in limit : Mass; }
    /* Wrapped Snippet (Action Context) */
    action def Main {
        attribute mass : Mass;
        constraint  checkMass  :  MassLimit  {
           in  m  =  mass ;
           in  limit  =  1000.0 ;
        }
    }

    view ExposeExample {
        expose Main;
    }
}
```

## 5. Assertions

Enforcing truth.

```sysml
package Calculations_5Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute x : Integer;
        attribute y : Integer;
        assert constraint {
           x > 0
        }
        assert constraint {
           not (y < 0)
        }
    }
    view ExposeExample { expose Main; }
}
```

## 6. Requirements

Assumptions and requirements.

```sysml
package Calculations_6Requirements {
    private import ScalarValues::*;
    private import SysML::*;
    requirement def Safety {
       attribute temp : Real;
       attribute pressure : Real;
       assume constraint { temp < 100 }
       require constraint { pressure < 50 }
    }
}
```



<div style='page-break-before: always;'></div>

# Cases Sheet

# Cases Cheat Sheet

*Use Cases, Analysis, Verification*

## 1. Use Case Definition

Functional goals.

```sysml
package Cases_1UseCaseDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Vehicle;
    attribute def Person;
    /* Wrapped Snippet (Structure Context) */
    use   case   def  DriveCar  {
        subject  vehicle  :  Vehicle ;
        actor  driver  :  Person ;
        objective  {
           doc  /* Transport safely */
        }
    }
}
```

## 2. Test Case (Verification)

Verifying requirements.

```sysml
package Cases_2TestCaseVerification {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Vehicle;
    attribute def Person;
    attribute def VerdictKind;
    /* Wrapped Snippet (Structure Context) */
    requirement brakeReq;
    requirement stoppingDistance;
    verification   def  TestBrakes  {
       objective {
           verify  brakeReq ;
           verify  stoppingDistance ;
       }
       return  verdict  :  VerdictKind ;
    }
}
```

## 3. Analysis Case

Evaluating properties.

```sysml
package Cases_3AnalysisCase {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Vehicle;
    /* Wrapped Snippet (Structure Context) */
    analysis   def  FuelEconomy  {
       subject  vehicle  :  Vehicle ;
       objective  {
          doc  /* Estimate MPG */
       }
       return  mpg  :  Real ;
    }
}
```

## 4. Case Usage

Instantiating a case.

```sysml
package Cases_4CaseUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Vehicle; attribute def Person;
    use case def DriveCar { subject vehicle : Vehicle; actor driver : Person; }
    part me : Person;
    /* Wrapped Snippet (Structure Context) */
    use   case  driveToWork  :  DriveCar  {
       actor  driver  =  me ;
    }
}
```



<div style='page-break-before: always;'></div>

# Connections Sheet

# Connections Cheat Sheet

*Connections and Flows*

## 1. Connection Definition

Defining connection types.

```sysml
package Connections_1ConnectionDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    part def Hub;
    part def Device;
    connection def DeviceConn {
       end hub : Hub;
       end device : Device;
    }
}
```

## 1b. Connection Usage

Connecting parts.

```sysml
package Connections_1bConnectionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    part def Hub;
    part def Device;
    connection def DeviceConn { end hub : Hub; end device : Device; }
    part context {
       part hub : Hub;
       part device : Device;
       connection c1 : DeviceConn
          connect hub to device;
    }
}
```

## 2. Binding Connector (=)

Equating elements. **CRITICAL**: No array indices are allowed (e.g. `a[1] = b[1]` is invalid).

```sysml
package Connections_2BindingConnector {
    private import ScalarValues::*;
    private import SysML::*;
    part def A { port p1; }
    part def B { port p2; }
    part system {
       part a : A;
       part b : B;
       bind a.p1 = b.p2;
       /* CRITICAL: No array indices allowed! Bind multiple items directly: */
       /* bind a.ports = b.ports; */
    }
}
```

## 3. Interface Connection

Flows within interfaces.

```sysml
package Connections_3InterfaceConnection {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    interface   def  IData  {
       end  source ;
       end  target ;
       flow  source  to  target ;
    }
}
```

## 4. Succession Flow

Control/Data flow.

```sysml
package Connections_4SuccessionFlow {
    private import ScalarValues::*;
    private import SysML::*;
    action process {
       action step1;
       action step2;
       first step1;
       then step2;
       doc /* Equivalent to: */
       flow from step1 to step2;
    }
}
```



<div style='page-break-before: always;'></div>

# Constraints Sheet

# Constraints Cheat Sheet

*Equations and Assertions*

## 1. Constraint Definition

Defining mathematical relationships.

```sysml
package Constraints_1ConstraintDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Force;
    attribute def Mass;
    attribute def Acceleration;
    constraint def NewtonLaw {
      in f : Force;
      in m : Mass;
      in a : Acceleration;
      f = m * a;
    }
}
```

## 2. Constraint Usage (Assert)

Enforcing constraints on parts.

```sysml
package Constraints_2ConstraintUsageAssert {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute def Acceleration;
    attribute def Force;
    constraint def NewtonLaw { in f : Force; in m : Mass; in a : Acceleration; }
    part Car {
      attribute mass : Mass;
      attribute accel : Acceleration;
      attribute force : Force;
      assert constraint n1 : NewtonLaw {
        in f = force;
        in m = mass;
        in a = accel;
      }
    }
}
```

## 2b. Inline Assertion

Simple boolean check.

```sysml
package Constraints_2bInlineAssertion {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute x : Integer;
        assert constraint {
           x > 0
        }
        /* Boolean expression */
    }
    view ExposeExample { expose Main; }
}
```

## 3. Calculation Definition

Reusable computation logic.

```sysml
package Constraints_3CalculationDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute def Speed;
    attribute def Energy;
    calc def calcKineticEnergy {
      in m : Mass;
      in v : Speed;
      return ke : Energy = 0.5 * m * v^2;
    }
}
```

## 4. Calculation Usage

Invoking calculations.

```sysml
package Constraints_4CalculationUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute def Speed;
    attribute def Energy;
    attribute kg;
    attribute m;
    attribute s;
    calc def calcKineticEnergy { in m : Mass; in v : Speed; return ke : Energy; }
    action def Main {
        attribute kEnergy : Energy = calcKineticEnergy(m = 100 [kg], v = 20 [m/s]);
    }
    view ExposeExample { expose Main; }
}
```



<div style='page-break-before: always;'></div>

# Graphical Sheet

# Graphical Cheat Sheet

*Standard Graphical Notation*

## 1. Nodes

## Part Definition

![Part Definition](../output/cheatsheets/assets/symbols/light/PartDefinition.svg)

**Notation**: Rectangle: 'part def'

**Syntax**: `part def Name;`

**Example**: `part def Vehicle;`

## Part Usage

![Part Usage](../output/cheatsheets/assets/symbols/light/PartUsage.svg)

**Notation**: Rounded Rect: 'part'

**Syntax**: `part name : Type;`

**Example**: `part engine : Engine;`

## Action Definition

![Action Definition](../output/cheatsheets/assets/symbols/light/ActionDefinition.svg)

**Notation**: Rectangle: 'action def'

**Syntax**: `action def Name;`

**Example**: `action def Drive;`

## Action Usage

![Action Usage](../output/cheatsheets/assets/symbols/light/ActionUsage.svg)

**Notation**: Rounded Rect: 'action'

**Syntax**: `action name : Type;`

**Example**: `action drive : Drive;`

## Requirement Def

![Requirement Def](../output/cheatsheets/assets/symbols/light/RequirementDef.svg)

**Notation**: Rectangle: 'requirement def'

**Syntax**: `requirement def Name;`

**Example**: `requirement def Perf;`

## Requirement Usage

![Requirement Usage](../output/cheatsheets/assets/symbols/light/RequirementUsage.svg)

**Notation**: Rounded Rect: 'requirement'

**Syntax**: `requirement name : Type;`

**Example**: `requirement req1 : Perf;`

## State Definition

![State Definition](../output/cheatsheets/assets/symbols/light/StateDefinition.svg)

**Notation**: Rectangle: 'state def'

**Syntax**: `state def Name;`

**Example**: `state def Idle;`

## State Usage

![State Usage](../output/cheatsheets/assets/symbols/light/StateUsage.svg)

**Notation**: Rounded Rect: 'state'

**Syntax**: `state name;`

**Example**: `state off;`

## 2. Relationships

## Specialization

![Specialization](../output/cheatsheets/assets/symbols/light/Specialization.svg)

**Notation**: Solid line, hollow triangle

**Syntax**: `def A :> B;`

**Example**: `part def Car :> Vehicle;`

## Composition

![Composition](../output/cheatsheets/assets/symbols/light/Composition.svg)

**Notation**: Solid line, filled diamond

**Syntax**: `part name : Type;`

**Example**: `part wheel : Wheel;`

## Reference

![Reference](../output/cheatsheets/assets/symbols/light/Reference.svg)

**Notation**: Solid line, hollow diamond

**Syntax**: `ref part name : Type;`

**Example**: `ref part driver : Person;`

## Import

![Import](../output/cheatsheets/assets/symbols/light/Import.svg)

**Notation**: Dashed line, open arrow

**Syntax**: `import Package::*;`

**Example**: `import SI::*;`

## Binding

![Binding](../output/cheatsheets/assets/symbols/light/Binding.svg)

**Notation**: Solid line, «bind»

**Syntax**: `bind a = b;`

**Example**: `bind p1 = p2;`

## Succession

![Succession](../output/cheatsheets/assets/symbols/light/Succession.svg)

**Notation**: Dashed line, open arrow

**Syntax**: `first a then b;`

**Example**: `first start then stop;`



<div style='page-break-before: always;'></div>

# Patterns Sheet

# Patterns Cheat Sheet

*Reusable Modeling Patterns*

## 1. Metadata (Annotations)

Tagging elements with data.

```sysml
package Patterns_1MetadataAnnotations {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    metadata   def  Status  {
      attribute  priority  :  Integer ;
      attribute  approved  :  Boolean ;
    }
    part  myPart  {
      metadata  Status  {
        priority  =  1 ;
      }
    }
}
```

## 2. Views

Visualizing the model.

```sysml
package Patterns_2Views {
    private import ScalarValues::*;
    private import SysML::*;
    part def GeneralDiagram;
    /* Wrapped Snippet (Structure Context) */
    view  MyView  :  GeneralDiagram  {
    /* filter Status; */
    }
    /* Rendering specific subsets */
}
```

## 3. Custom Units (Nano Banana)

Defining domain-specific units.

```sysml
package BananaUnits {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def LengthUnit {
        attribute prefix;
        attribute referenceUnit;
    }
    attribute nano;
    attribute <nB> nanoBanana : LengthUnit {
        attribute unitConversion;
        :>> prefix = nano;
        :>> referenceUnit = "Standard Banana";
    }
}
```

## 4. Abstract vs Individual

Templates vs Concrete instances.

```sysml
package Patterns_4AbstractvsIndividual {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    abstract  part  def  Wheel ;
    part  def  Bus  {
      abstract  part  wheel  [4]  :  Wheel ;
    }
    individual  part  myBus  :  Bus  {
      part  frontLeft  :>  wheel ;
    }
}
```



<div style='page-break-before: always;'></div>

# Reference Sheet

# Reference Cheat Sheet

*Keywords and Types*

## 1. Common Keywords

Core language definitions.

```sysml
package Reference_1CommonKeywords {
    doc /*
      package, import, private import
      attribute def, attribute
      part def, part
      action def, action
      item def, item
      state def, state
      interface def, port def, port
      connection def, connection
      requirement def, requirement
      constraint def, constraint, assert
      analysis def, analysis
      verification def, verification
      view def, view
      metadata def, metadata
    */
}
```

## 2. Primitive Types

Basic data types.

```sysml
package Reference_2PrimitiveTypes {
    private import ScalarValues::*;
    private import Base::*;
    private import SysML::*;
    attribute b : Boolean; /* true, false */
    attribute i : Integer; /* 1, -5, 0 */
    attribute r : Real; /* 3.14, 1.0 */
    attribute s : String; /* 'text' */
    attribute n : Natural; /* 0, 1, * (UnlimitedNatural in v1) */
}
```

## 3. Relationships

Connecting elements.

```sysml
package Reference_3Relationships {
    doc /*
      Generalization ( :> ) - Inheritance
      Subsetting ( :> ) - Hierarchy
      Redefinition ( :>> ) - Specialized replacement
      Reference ( references ) - Pointer
      Conjugation ( ~ ) - Reverse port
      Binding ( = ) - Equality
      Assignment ( := ) - Value set
      Succession ( first..then ) - Ordering
    */
}
```

## 4. Comments

Annotating code.

```sysml
package Reference_4Comments {
    /* Single line */
    /* Multi-line
       comment */
    doc /* Documentation */
    /* Single line */
    /* Multi-line
       comment */
    doc /* Documentation */
    part element;
    comment about element /* text */
}
```

## 5. Multiplicity

Cardinality & Ordering.

```sysml
package Reference_5Multiplicity {
    doc /*
      [1]      - Exactly one (Default)
      [0..1]   - Optional
      [*]      - Zero or more
      [1..*]   - One or more
      [2..5]   - Specific range
    */
}
```

## 6. Visibility

Access control.

```sysml
package Reference_6Visibility {
    doc /*
      public    (default) - Visible everywhere
      private   (private) - Visible only inside
      protected (protected) - Visible to children
    */
}
```



<div style='page-break-before: always;'></div>

# Relationships Sheet

# Relationships Cheat Sheet

*Structural and Behavioral Relationships*

## 1. Taxonomy (Def vs Usage)

Specialization matches Definitions.

```sysml
package 'Example: Taxonomy (Def vs Usage)' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Taxonomy (Def vs Usage)' {
        part def Vehicle {
            doc /* Definitions use specialize */
        }
        part def Car :> Vehicle {
            part wheel;
        }
        part sedan : Car {
            doc /* Usages use redefines/subsets */
            part betterWheel :>> wheel;
        }
    }
    view 'View: 1. Taxonomy (Def vs Usage)' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Taxonomy (Def vs Usage)'::'Taxonomy (Def vs Usage)'::*;
    }
}
```

## 2. Structural Links

Connecting and Binding usages.

```sysml
package 'Example: Structural Links' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Structural Links' {
        part def 'Connection Examples' {
            part p1;
            part p2;
            connect p1 to p2;
            bind p1 = p2;
        }
    }
    view 'View: 2. Structural Links' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Structural Links'::'Structural Links'::*;
    }
}
```

## 3. Behavioral Flow

Successions (Time) vs Flows (Data).

```sysml
package 'Example: Behavioral Flow' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Behavioral Flow' {
        action def Process {
            action step1;
            action step2;
            first step1 then step2;
            attribute x : Integer;
            flow x from step1 to step2;
            view Process : DS_Views::SymbolicViews::afv;
            action __unnamed84 terminate;
            first start then step1;
            first step2 then __unnamed84;
        }
    }
    view 'View: 3. Behavioral Flow' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Behavioral Flow'::'Behavioral Flow'::**;
    }
}
```

## 4. Cross-Cutting

Traceability and Assertions.

```sysml
package 'Example: Cross-Cutting' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Cross-Cutting' {
        requirement r1;
        part p satisfy r1;
        
        part abstractPart;
        part concretePart;
        
        refine abstractPart to concretePart;
        
        verification def Test;
        verification v1 : Test {
            subject p;
            objective {
                verify r1;
            }
        }
    }
    view 'View: 4. Cross-Cutting' {
        expose 'Example: Cross-Cutting'::'Cross-Cutting'::*;
    }
}
```

## 5. Import & Exposure

Managing namespace visibility.

```sysml
package 'Example: Import & Exposure' {
    private import ScalarValues::*;
    private import SysML::*;
    package P1 {
        part def A;
        part def B;
    }
    package P2 {
        private import P1::A;
        public import P1::B;
        alias MyA for A;
        part thing : A;
        part otherThing : B;
    }
    view 'View: 5. Import & Exposure' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Import & Exposure'::**;
    }
}
```



<div style='page-break-before: always;'></div>

# Requirements Sheet

# Requirements Cheat Sheet

*Requirements and Verification*

## 1. Requirement Definition

Defining requirement types.

```sysml
package Requirements_1RequirementDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Time;
    requirement def Performance {
      doc /* The system shall be fast. */
      attribute maxResponse : Time;
    }
}
```

## 2. Requirement Usage

Specific requirement instances using `<'ID'> 'Name' : Type`.

```sysml
package Requirements_2RequirementUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Time;
    attribute ms;
    requirement def Performance { attribute maxResponse : Time; }
    requirement <'REQ-001'> 'Fast' : Performance {
      doc /* Response < 10ms */
      attribute maxResponse = 10 [ms];
    }
}
```

## 3. Satisfy

Design meets requirement.

```sysml
package Requirements_3Satisfy {
    private import ScalarValues::*;
    private import SysML::*;
    requirement def Performance;
    requirement req1 : Performance;
    part server {
      satisfy req1;
    }
    /* satisfy req1 by server; */
}
```

## 4. Verify

Test case for requirement.

```sysml
package Requirements_4Verify {
    private import ScalarValues::*;
    private import SysML::*;
    requirement req1;
    verification def TestLatency {
      objective {
          verify req1;
      }
    }
}
```

## 5. Constraint Definition

Mathematical rules.

```sysml
package Requirements_5ConstraintDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute kg;
    constraint def CheckMass {
      in m : Mass;
      m <= 1000 [kg]
    }
}
```

## 6. Assert Constraint

Applying constraints directly. **CRITICAL**: No semicolon at the end of the constraint block.

```sysml
package Requirements_6Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute kg;
    part car {
      attribute mass : Mass;
      assert constraint {
        mass <= 1000 [kg]
      }
    }
}
```

## 7. Trace & Refine

Requirement relationships.

```sysml
package Requirements_7TraceRefine {
    private import ScalarValues::*;
    private import SysML::*;
    requirement req1;
    requirement old_doc_item;
    requirement req2 {
      doc /* Using dependency to represent relationships */
      dependency from req2 to req1;
      dependency from req2 to old_doc_item;
    }
}
```



<div style='page-break-before: always;'></div>

# Shorthand Sheet

# Shorthand Cheat Sheet

*Syntax Shortcuts*

## 1. Specialization (:>)

Shorthand for 'specializes'.

```sysml
package Shorthand_1Specialization {
    private import ScalarValues::*;
    private import SysML::*;
    part def Vehicle;
    /* Wrapped Snippet (Structure Context) */
    part  def  Car  :>  Vehicle ;
    doc  /* Equivalent to: 
            part  def  Car  specializes  Vehicle ; */
}
```

## 2. Subsetting (:>)

Shorthand for 'subsets'.

```sysml
package Shorthand_2Subsetting {
    private import ScalarValues::*;
    private import SysML::*;
    part parts;
    /* Wrapped Snippet (Structure Context) */
    part  engine  :>  parts ;
    doc  /* Equivalent to: 
            part  engine  subsets  parts ; */
}
```

## 3. Redefinition (:>>)

Shorthand for 'redefines'.

```sysml
comment about Shorthand_3Redefinition /* Source: Shorthand_3Redefinition.sysml */
package Shorthand_3Redefinition {
    private import ISQ::*;
    comment /* Wrapped Snippet (Structure Context)
    attribute partMass : ISQBase::mass  =  100.0 ;
    attribute partMass1 :>> partMass  =  101.0 ;   
    attribute  partMass2 redefines  partMass  =  101.0 ;
    comment about partMass1, partMass2 /* :>> and redefines are equivelnt */
}
```

## 4. Conjugation (~)

Shorthand for 'conjugated'.

```sysml
package Shorthand_4Conjugation {
    private import ScalarValues::*;
    private import SysML::*;
    port def Interface;
    /* Wrapped Snippet (Structure Context) */
    port  p  :  ~ Interface ;
    doc  /* Equivalent to: 
            port  p  :  conjugated  Interface ; */
}
```

## 5. Feature Values

Assignment variations.

```sysml
package Shorthand_5FeatureValues {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    attribute  x  =  1 ;  /* Binding (Equality) */
    attribute  y  :=  2 ;  /* Initial Value */
    attribute  z  default  =  3 ;  /* Default Value */
}
```

## 6. Multiplicity

Common shorthands.

```sysml
package Shorthand_6Multiplicity {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    part  many [*] ;  /* 0..* */
    part  one ;  /* 1..1 (Default) */
    part  opt [0..1] ;  /* 0..1 */
}
```



<div style='page-break-before: always;'></div>

# State Patterns Sheet

# State Patterns Cheat Sheet

*Advanced State Patterns*

## 1. Entry/Do/Exit

State lifecycle actions.

```sysml
package StatePatterns_1EntryDoExit {
    private import ScalarValues::*;
    private import SysML::*;
    action def logStart;
    action def maintain;
    action def logEnd;
    state def Active {
       entry action : logStart;
       do action : maintain;
       exit action : logEnd;
    }
}
```

## 2. Composite State

States within states.

```sysml
package StatePatterns_2CompositeState {
    private import ScalarValues::*;
    private import SysML::*;
    state def Composite {
       entry;
       state Sub1;
       state Sub2;
       transition t1
          first Sub1
          then Sub2;
    }
}
```

## 3. Exhibit State

Part exhibiting a state.

```sysml
package StatePatterns_3ExhibitState {
    private import ScalarValues::*;
    private import SysML::*;
    state def VehicleStates { state operating; }
    part def Vehicle {
       exhibit state opState : VehicleStates;
    }
}
```

## 4. Internal Transition

Transition without state change.

```sysml
package StatePatterns_4InternalTransition {
    private import ScalarValues::*;
    private import SysML::*;
    action def tick;
    action check;
    state def Monitoring {
       state Idle;
       /* Internal behavior (Self-transition) */
       transition t1 first Idle accept tick do check then Idle;
    }
}
```



<div style='page-break-before: always;'></div>

# States Sheet

# States Cheat Sheet

*State Machines*

## 1. State Definition

Defining states and lifecycle actions.

```sysml
package States_1StateDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    action def logStart;
    action def logEnd;
    state   def  TrafficLight  {
       entry  action : logStart ;
       exit   action : logEnd ;
       state  Red ;
       state  Green ;
    }
}
```

## 2. Transitions

Moving between states.

```sysml
package States_2Transitions {
    private import ScalarValues::*;
    private import SysML::*;
    state def Main {
        state Red;
        state Green;
        action def TimeEvent;
        transition t1
           first Red
           accept TimeEvent
           then Green;
    }
}
```

## 3. Guards & Effects

Conditions and actions on transition. **CRITICAL**: Use `if` for guards, not `where`. Transitions can only have one source state (no `or` in `first`). Actions must be defined in the same block.

```sysml
package States_3GuardsEffects {
    private import ScalarValues::*;
    private import SysML::*;
    state def Main {
        state Green;
        state Red;
        attribute traffic : Integer;
        action resetTimer;
        transition t2
           first Green
           if traffic == 0
           do resetTimer
           then Red;
    }
}
```

## 4. Composite States

States within states.

```sysml
package States_4CompositeStates {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    state Operational {
       entry;
       state Normal;
       state Maintenance;
    }
}
```

## 5. Parallel States

Concurrency.

```sysml
package States_5ParallelStates {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    state def System parallel {
       state Power;
       state Connectivity;
    }
}
```



<div style='page-break-before: always;'></div>

# Structure Sheet

# Structure Cheat Sheet

*Parts, Attributes, Packages*

## 1. Part Definition

Defining structural blocks.

```sysml
package Structure_1PartDefinition {
    private import ScalarValues::*;
    attribute def Mass;
    part def Engine;
    part def Vehicle {
      attribute massOfVehicle : Mass;
      part engine : Engine;
    }
}
```

## 2. Usage & Multiplicity

Instantiating parts with counts.

```sysml
package Structure_2PartUsage {
    private import ScalarValues::*;
    part def Vehicle;
    part def Wheel;
    part car : Vehicle {
      part wheels[4] : Wheel;
      part doors[2..4];
    }
}
```

## 3. Attributes

Data properties of parts.

```sysml
package Structure_3Attributes {
    private import ScalarValues::*;
    attribute def Status {
        attribute code : Integer;
    }
    part ecu {
        attribute id = "ECU-01";
    }
}
```

## 5. Items

Things that flow.

```sysml
package Structure_5Items {
    private import ScalarValues::*;
    item def Fuel;
    item def Gasoline :> Fuel;
    doc /* Items flow through ports */
}
```

## 6. Packages & Imports

Organizing model elements.

```sysml
package Structure_6Packages {
    package VehicleModel {
        private import ScalarValues::*;
        part car;
    }
}
```

## 7. Inheritance (:>)

Specialization of definitions.

```sysml
package Structure_7Inheritance {
    private import ScalarValues::*;
    part def Vehicle;
    part def ElectricCar :> Vehicle {
        part battery;
    }
}
```

## 8. Enumerations

Predefined sets of values.

```sysml
package Structure_8Enumerations {
    private import ScalarValues::*;
    enum def Color {
        Red; Green; Blue;
    }
}
```



<div style='page-break-before: always;'></div>

# Views Sheet

# System Views

*Views, Viewpoints, and Filtering*

## 1. View Definition

```sysml
view def ReportView {
    in part target_sys : System;
}
```

Defines a reusable view structure.

## 2. View Usage

```sysml
view report : ReportView {
    in part target_sys = mySystem;
}
```

Uses a definition to create a specific view.

## 3. Viewpoint

```sysml
viewpoint def SafetyAnalysis { doc "Focus on hazards"; }
viewpoint <'vp1'> 'sa' : SafetyAnalysis;
view mySafetyView { satisfy 'sa'; }
```

Connects a view to its stakeholder concern.

## 4. Expose Content

```sysml
view myView {
    expose myCar;      /* Single element */
    expose myCar::**;  /* Recursive import */
}
```

## 5. Filter

```sysml
filter @PartUsage; /* Keep only parts */
filter @AllocationUsage; /* Keep allocations */
```

**CRITICAL**: Always filter by Usage (e.g. `@PartUsage`, `@AllocationUsage`), not by Definition.

## 6. Rendering

```sysml
render asTable { ... }
style color = "red";
```





---

# SysML v2 Tutorials: Complete Collection

**Generated on:** 2026-05-07 11:53:46

---

## Table of Contents

- Actions Tutorial
- Allocation Tutorial
- Analysis Tutorial
- Connections Tutorial
- Coretypes Tutorial
- Datatypes Tutorial
- Domainlibs Tutorial
- Evaluation Tutorial
- Features Tutorial
- Filters Tutorial
- Flows Tutorial
- Multiplicity Tutorial
- Naming Tutorial
- Partsattributes Tutorial
- Portsinterfaces Tutorial
- Requirements Tutorial
- Semanticmetadata Tutorial
- Statemachine Tutorial
- Usecase Tutorial
- Variants Tutorial
- Viewpoints Tutorial
- Views Tutorial
- Cameo Features Tutorial

---

<div style='page-break-before: always;'></div>

# Actions Tutorial

# Actions & Behavior

*Modeling Activity Diagrams*

## 1. Action Basics

Actions represent distinct steps of behavior.
• **action def**: A reusable definition.
• **action**: A usage (step).

## 2. Flows and Control

- **first**: Marks the starting action.
- **flow**: Explicit succession (`flow from a to b`).
- **then**: Shorthand succession (`a then b`).
- **fork/join**: Implicit when multiple flows leave or enter an action.

## 3. Processing Pipeline Example

```sysml
package Actions_Tutorial {
    private import ScalarValues::*;
    
    /* reusable action */
    action def LogStatus { in msg : String; }

    action def ProcessData {
        /* Defining steps */
        action step1;
        action step2;
        action step3;
        
        /* --- Control Flow --- */
        /* 'first' implies the entry point */
        first step1;
        
        /* 'then' implies succession (step1 completes before step2 starts) */
        flow from step1 to step2; /* explicit */
        
        /* Shorthand for flow: */
        /* step2 then step3;  */ 
        
        /* --- Parallelism --- */
        action branchA;
        action branchB;
        
        /* Forking: step3 triggers both branches */
        flow from step3 to branchA;
        flow from step3 to branchB;
        
        /* --- Using Definitions --- */
        action logger : LogStatus {
            in msg = "Processing Complete";
        }
        
        /* Joining: both must finish before logger runs */
        flow from branchA to logger;
        flow from branchB to logger;
    }
}
```



<div style='page-break-before: always;'></div>

# Allocation Tutorial

# Allocation

*Mapping Behavior to Structure*

## 1. Allocation Concept

Allocation maps one model element to another, typically to show realization (e.g., Logical functionality allocated to Physical hardware). **CRITICAL**: Allocations must happen between usages (instances), NOT definitions. Use a dedicated `AllocationContext` package to hold the instances and their allocations.

## 2. Syntax

```sysml
allocate <source> to <target>;
```

## 3. Deployment Example

```sysml
package Allocation_Tutorial {
    
    /* --- Behavioral / Logical View --- */
    action def ComputePath;
    
    /* --- Physical / Structural View --- */
    part def FlightComputer;
    
    /* Create a dedicated package for allocations between usages */
    package AllocationContext {
        part ecu : FlightComputer;
        action plan : ComputePath;
        
        /* Allocate the action usage (plan) to the hardware usage (ecu) */
        /* Meaning: "The ECU executes the planning action" */
        allocate plan to ecu;
    }
}
```



<div style='page-break-before: always;'></div>

# Analysis Tutorial

# Analysis & Constraints

*Parametrics and Evaluation*

## 1. Constraints (Parametrics)

Constraints define mathematical equations that govern system properties.

```sysml
constraint def OhmLaw { in v; in i; in r; v == i * r }
```

## 2. Analysis Cases

Analysis cases specify the logic for evaluating system performance, often involving solving constraints or running simulations.

## 3. Mass Analysis Example

```sysml
package Analysis_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Constraint Definition --- */
    constraint def MassEquation {
        in total : Real;
        in p1 : Real;
        in p2 : Real;
        
        /* The math */
        total == p1 + p2
    }
    
    part def System {
        attribute mass : Real;
        attribute part1Mass : Real;
        attribute part2Mass : Real;
        
        /* --- 2. Constraint Usage (Parametrics) --- */
        /* Binding properties to the equation parameters */
        constraint massCheck : MassEquation {
            in total = mass;
            in p1 = part1Mass;
            in p2 = part2Mass;
        }
    }
    
    /* --- 3. Analysis Case --- */
    analysis def WeightCheck {
        subject system : System;
        
        /* Determining if mass is within limits */
        return result : Boolean = system.mass < 100.0;
    }
}
```



<div style='page-break-before: always;'></div>

# Connections Tutorial

# Connections

*Wiring Parts Together*

## 1. Connection Basics

- **connect a to b**: Standard connection between two endpoints.
- **bind a = b**: Equivalence connection. Often used for **delegation** (exposing an internal part's port to the boundary of the container).
- **Rule**: Bindings must always use `=` instead of `to`.
- **Rule**: Bindings cannot contain array indices or multiplicity ranges (e.g. `bind a[1] = b[1]` is invalid). Bind parts individually or as a complete multi-part instead.

## 2. Wiring Example

This example shows connecting a Battery to a Computer, and binding the internal Ethernet port to the outside.

```sysml
package Connections_Tutorial {
    private import ScalarValues::*;
    
    /* --- Interface Definitions --- */
    port def PowerInterface {
        out attribute powerLevel : Real;
    }
    
    port def DataLink {
        end source;
        end target;
        flow source to target;
    }

    /* --- Component Definitions --- */
    part def Battery {
        port pwrPort : PowerInterface;
    }

    part def Computer {
        port pwrIn : PowerInterface;
        port eth0 : DataLink;
    }
    
    part def System;
    
    part def PowerSystem :> System {
        part battery : Battery;
        part computer : Computer;
        
        /* --- Connection --- */
        /* Connecting compatible ports (PowerInterface vs ~PowerInterface) */
        connect battery.pwrPort to computer.pwrIn;
        
        /* --- Binding (Delegation) --- */
        /* Exposing the computer's ethernet port to the outside world */
        port externalEth : DataLink;
        
        /* 'bind' means internal eth0 IS the same interaction point as externalEth */
        /* MUST use '=' and NOT 'to' */
        bind externalEth = computer.eth0;
        
        /* --- Multiplicity Binding --- */
        /* Array indices are forbidden in bindings. */
        /* You can bind a single source to a multi-part target directly without indices: */
        /* bind battery.pwrOut = computers.pwrIn; */
    }
}
```



<div style='page-break-before: always;'></div>

# Coretypes Tutorial

# Core Types

*Parts, Items, Attributes, and Enumerations*

## 1. Parts vs Items

SysML v2 distinguishes between physical/logical structure and information/flow.
• **part**: Has mass, energy, or spatial extent (e.g., Engine, Server).
• **item**: Represents distinct headers or mass that flows (e.g., Water, DataMessage).

## 2. Attributes & Scalars

Attributes store data values within definitions.
• **attribute def**: Defines a reusable data type.
• **attribute**: A usage of a definition holding a value.

## 3. Enumerations

Enumerations define a fixed set of literals. Useful for states, modes, or configuration options.

## 4. Core Types Example

```sysml
package CoreTypes_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Enumerations --- */
    enum def Status {
        enum Active;
        enum Idle;
        enum Error;
    }

    /* --- 2. Attributes & Scalars --- */
    attribute def MassValue :> Real;
    
    /* --- 3. Parts (Structure) --- */
    part def StorageTank {
        attribute capacity : MassValue = 1000.0;
        attribute currentStatus : Status = Status::Idle;
    }

    /* --- 4. Items (Flow/Substance) --- */
    item def Water;
    
    part def WaterSystem {
        part tank1 : StorageTank;
        part tank2 : StorageTank;
        
        /* Items flow or are stored */
        item storedWater : Water;
    }
}
```



<div style='page-break-before: always;'></div>

# Datatypes Tutorial

# Data Types

*Primitives, Values, and Units*

## 1. Standard Primitive Types

SysML v2 provides familiar primitive types in the ScalarValues library:
• **String**: Textual data.
• **Integer**: Whole numbers.
• **Real**: Floating point numbers.
• **Boolean**: True/False flags.

## 2. ISQ Units (Physical Quantities)

For engineering, using standard quantities is critical. The `SI` library publicly imports `ISQ`. Use `ISQ::mass`, `ISQ::electricCharge`, and `ISQInformation::storageCapacity` for proper type definitions.

## 3. Custom Data Types

You can define domain-specific types:
• **attribute def**: A reusable value type definition.
• **struct**: A generalized structured data type.
• **ProjectUnits**: Explicitly define derived units or use `ConversionByPrefix` (e.g. for `mAh`).

## 4. Data Types and Values Example

```sysml
package DataTypes_Tutorial {
    private import ScalarValues::*;
    private import ISQ::*;
    private import SI::*;
    private import MeasurementReferences::*;

    /* --- 1. Custom Value Definitions --- */
    /* Specializing a primitive */
    attribute def IDString :> String;
    
    /* Struct for composite data (Kernel level concept often used) */
    attribute def Coordinates {
        attribute x : Real;
        attribute y : Real;
        attribute z : Real;
    }
    
    /* --- 2. Custom Units --- */
    package ProjectUnits {
        attribute <ms> millisecond : DurationUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = milli;
                :>> referenceUnit = s;
            }
        }
        attribute <'mm/h'> 'millimetre per hour' : SpeedUnit = mm / h;
        attribute mAh;
        attribute GB;
    }

    part def SensorSystem {
        /* --- 3. Using Primitives --- */
        attribute isActive : Boolean = true;
        attribute firmwareVersion : String = "v1.2.4";
        attribute cycleCount : Integer = 0;
        
        /* --- 4. Using ISQ Units --- */
        /* Type checking ensures you can't assign Mass to Length */
        /* Validating physical properties (Recommended) */
        attribute weight :> ISQ::mass = 5.5 [kg];
        attribute scanRange :> ISQ::length = 150 [m];
        
        /* Raw value storage (Context-free) */
        attribute rawData : MassValue = 10.0 [kg];
        
        /* Unit conversion is handled by checks (e.g. [km] -> [m]) */
        attribute speed :> ISQ::speed = 120 [km/h]; 
        
        /* --- 5. Using Custom Types --- */
        attribute sensorID : IDString = "SENS-001";
        attribute location : Coordinates {
             :>> x = 10.0;
             :>> y = 20.0;
             :>> z = 0.0;
        }
        
        /* Information units require ISQInformation */
        attribute memorySize :> ISQInformation::storageCapacity = 64 [ProjectUnits::GB];
        
        /* Battery capacity */
        attribute batteryCapacity :> ISQ::electricCharge = 1500 [ProjectUnits::mAh];
    }
}
```



<div style='page-break-before: always;'></div>

# Domainlibs Tutorial

# Domain Libraries

*ISQ, SI, and Time*

## 1. ISQ & SI

The standard libraries provide types for almost all physical quantities.

```sysml
private import SI::m; /* Publicly imports ISQ */
```

## 2. Units

Units are first-class citizens using square brackets.

```sysml
attribute len = 5 [m];
```

## 3. Physics Example

```sysml
package DomainLibs_Tutorial {
    private import ISQ::*;
    private import SI::*;
    private import SI::m;
    private import Time::*;
    
    /* --- 1. Using ISQ Types --- */
    part def MovingObject {
        attribute mass :> ISQ::mass;
        attribute velocity :> ISQ::speed;
        attribute startingTime : TimeInstantValue;
    }
    
    part car : MovingObject {
        /* --- 2. Using Units --- */
        attribute redefines mass = 1500 [kg];
        attribute redefines velocity = 120 [km/h];
        
        /* --- 3. Time ISO 8601 --- */
        attribute redefines startingTime = "2023-10-27T10:00:00Z";
    }
    
    /* --- 4. Geometry (Shape Library) --- */
    /* (Requires Shape library import usually) */
    /* part wheel : Cylinder { */
    /*    attribute radius = 30 [cm]; */
    /* } */
}
```



<div style='page-break-before: always;'></div>

# Evaluation Tutorial

# Evaluation

*Calculations and Analysis*

## 1. Evaluation Overview

SysML v2 integrates analysis and verification directly into the model.

## 2. Components

- **calc def**: Defines mathematical functions.
- **constraint**: Defines boolean rules (often used in Requirements).
- **verification**: Defines test cases to verify requirements.
- **analysis**: Defines trade studies to compare alternatives or optimize parameters.

## 3. Evaluation Example

```sysml
package Evaluation_Tutorial {
    private import ScalarValues::*;
    private import AnalysisCases::*;
    
    /* --- 1. Calculations --- */
    calc def PowerCalc {
        in force : Real;
        in velocity : Real;
        return power : Real = force * velocity;
    }

    package System {
        part engine {
            attribute force : Real = 1000.0;
            attribute maxPower : Real = 50000.0;
            
            /* Using the calculation */
            attribute currentPower : Real = PowerCalc(force, 25.0);
        }
    }

    /* --- 2. Requirements & Constraints --- */
    requirement def PowerLimit {
        attribute actualPower : Real;
        attribute limit : Real;
        
        /* Boolean check */
        require constraint {
            actualPower <= limit
        }
    }
    
    /* Requirement Usage at package level to allow verification */
    requirement checkPower : PowerLimit;

    part myEngine : System::engine {
        /* Satisfaction */
        satisfy checkPower {
            attribute :>> actualPower = myEngine.currentPower;
            attribute :>> limit = myEngine.maxPower;
        }
    }

    /* --- 3. Verification Case --- */
    verification def PowerTest {
        subject system : System::engine;
        
        objective {
            /* Verify that the requirement is met */
            verify checkPower {
                subject = system;
            }
        }
    }

    /* --- 4. Analysis (Trade Study) --- */
    analysis def Optimization {
        subject candidates : System::engine [1..*];
        
        objective maximizeObj {
            subject candidates = Optimization::candidates;
        }
        
        /* Define how we measure 'goodness' */
        calc evaluate {
            in part cand :> candidates;
            return result : Real = cand.currentPower;
        }
    }
}
```



<div style='page-break-before: always;'></div>

# Features Tutorial

# Features & Chaining

*Understanding Structure, Behavior, and feature paths*

## 1. What is a Feature?

In SysML v2, almost everything is a Feature. Features describe the characteristics of a defined type. They can be structural (parts, attributes, ports) or behavioral (actions, states).

## 2. Feature Chaining (Dot Notation)

Feature chaining allows you to access deeply nested features without redefining the entire hierarchy. You can 'reach into' a part to constrain or redefine its internal properties using the dot (.) operator.

```sysml
/* Feature Chaining Example */
part :>> engine.mass = 150 [ISQ::kg];
```

## 3. Modifying Features: Subsets vs Redefines

- **Subsetting (subsets)**: Classifies a feature as a member of a broader set. Both sets exist simultaneously.
- **Redefinition (redefines)**: Replaces an inherited feature completely. The original definition is hidden.

## 4. Full Example Code

```sysml
package Feature_Tutorial_Model {
    private import ISQ::*;
    private import SI::*;

    /* --- 1. Base Definitions --- */
    part def Engine {
        attribute horsepower :> ISQ::power;
        attribute mass :> ISQ::mass;
    }

    part def Wheel;

    part def Vehicle {
        part engine : Engine[1];
        part wheels : Wheel[4];
    }

    /* --- 2. Subsetting Example --- */
    part def Truck :> Vehicle {
        /* 'front' and 'rear' partition the 'wheels' set */
        part frontWheels[2] subsets wheels;
        part rearWheels[2] subsets wheels;
    }

    /* --- 3. Redefinition Example --- */
    part def ElectricMotor :> Engine;
    
    part def ElectricCar :> Vehicle {
        /* Replace generic Engine with ElectricMotor */
        part redefines engine : ElectricMotor;
    }

    /* --- 4. Feature Chaining & Redeclaration Example --- */
    part def SportsCar :> Vehicle {
        /* Feature Chaining: reaching into 'engine' */
        /* Redeclaration (:>>) shorthand for 'redefines' or 'subsets' */
        
        attribute :>> engine.horsepower = 500000 [W];
        
        /* This is structurally equivalent to: */
        /* part :>> engine { */
        /* attribute :>> horsepower = 500000 [W]; */
        /* } */
    }
}
```



<div style='page-break-before: always;'></div>

# Filters Tutorial

# Filters

*Refining View Content*

## 1. Filters

Filters refine what is shown in a view. They are crucial for creating manageable diagrams from complex models.

## 2. Syntax

- **hastype <Def>**: Checks if an element is a usage of `<Def>`.
- **@<Meta>**: Checks if an element has specific metadata applied.
- **and, or, not**: Standard boolean logic.

## 3. Filtering Example

```sysml
package Filters_Tutorial {
    private import DS_Views::SymbolicViews;
    private import Metaobjects::SemanticMetadata;
    
    part def HardwareComponent;
    part def SoftwareComponent;
    
    metadata def Critical;
    
    part system {
        part cpu : HardwareComponent;
        
        part os : SoftwareComponent {
            @Critical;
        }
        
        part driver : SoftwareComponent;
    }
    
    /* --- 1. Filtering by Type --- */
    view hardwareView : SymbolicViews::gv {
        expose system::**;
        
        /* Only show HardwareComponents */
        filter hastype HardwareComponent;
    }
    
    /* --- 2. Filtering by Metadata (Stereotypes) --- */
    view criticalView : SymbolicViews::gv {
        expose system::**;
        
        /* Only show elements tagged as @Critical */
        filter @Critical;
    }
    
    /* --- 3. Complex Logic --- */
    view complexView : SymbolicViews::gv {
        expose system::**;
        
        /* Show elements that are either Hardware or Software */
        filter hastype SoftwareComponent or hastype HardwareComponent;
    }
}
```



<div style='page-break-before: always;'></div>

# Flows Tutorial

# Flows

*Moving Items and Data*

## 1. Item Flows

Item flows specify the movement of matter, energy, or data between parts.

## 2. Syntax

```sysml
flow of <item> from <source> to <target>;
```

## 3. Fuel Flow Example

```sysml
package Flows_Tutorial {
    private import ScalarValues::*;
    
    item def Fuel;
    
    part def Tank;
    part def Engine;
    
    part def FuelSystem {
        part t : Tank;
        part e : Engine;
        
        /* --- Explicit Item Flow --- */
        /* Declaring that Fuel moves from Tank to Engine */
        /* This implies a connection exists or is abstractly represented */
        flow of Fuel from t to e;
        
        /* --- Connector with Flow --- */
        connect t to e {
            /* Optional property on the flow */
            flow of Fuel from t to e {
                attribute rate : Real = 5.0;
            }
        }
    }
}
```



<div style='page-break-before: always;'></div>

# Multiplicity Tutorial

# Multiplicity

*Cardinality, Collections, and Ordering*

## 1. Basic Multiplicity

Multiplicity constraints specify cardinality.
• **[1]**: Exactly one.
• **[0..1]**: Optional.
• **[*]**: Unbounded.

## 2. Default Multiplicity Rules

Defaults depend on context:
1. **In Definition**: [1] (Required).
2. **In Package**: [0..*] (Optional).
3. **Inheritance**: `subsets` inherits parent constraint.

## 3. Collection Types

• **unique**: Set (Default).
• **ordered**: Sequence.
• **nonunique**: Bag.

## 4. Multiplicity Example

```sysml
package Multiplicity_Tutorial {
    
    part def Person;
    part def Wheel;
    
    /* --- 1. Package Context --- */
    /* Usage directly in package defaults to [0..*] */
    part looseWheels : Wheel; 

    part def Car {
        /* --- 2. Definition Context --- */
        /* Usage in a definition (part/attr/port) defaults to [1] */
        part engine : Person; /* [1..1] Required */
        
        /* --- Explicit Constraints --- */
        part wheels : Wheel [4]; /* Exactly 4 */
        
        /* --- 3. Inheritance --- */
        /* subsets: inherits parent multiplicity (here [1]) */
        /* We can constrain it further, or leave it. */
        part driver subsets engine; 
        
        /* --- 4. Collections --- */
        /* unique (Default): Set */
        part passengers : Person [0..4]; 
        
        /* ordered nonunique: Sequence */
        attribute lapTimes : ScalarValues::Real [*] ordered nonunique;
    }
    
    action def Drive {
        /* Default parameter multiplicity is [1] */
        in distance : ScalarValues::Integer; 
    }
}
```



<div style='page-break-before: always;'></div>

# Naming Tutorial

# Names & Imports

*Identifiers, Conventions, and Package Management*

## 1. Identifiers

Standard identifiers in SysML v2 are alphanumeric and can include underscores. They must start with a letter or underscore. You can use 'single quotes' to escape any character sequence. Exception: Units in brackets `[ ]` don't need quotes (e.g., `[km/h]`).

## 2. Naming Conventions

- **Definitions (PascalCase)**: CamelCase starting with Uppercase. Used for: part defs, action defs, packages.
- **Usages (camelCase)**: CamelCase starting with lowercase. Used for: parts, actions, attributes.

## 3. Imports

Imports bring elements from other packages into scope.
• standard import: Transitive (publicly exposes imported elements). Example: `SI` libraries publicly import `ISQ` so you get both units and quantities.
• private import: Only visible within the current package.

## 4. Wildcards (* vs **)

• *: Shallow import (imports direct children).
• **: Recursive import (imports everything deeply).
Warning: Avoid ** in production to prevent namespace pollution!

## 5. Aliasing

Use `alias` to create short names for long qualified names. Sytnax: `alias <NewName> for <OldName>;`.

## 6. Comprehensive Example

```sysml
package Naming_Tutorial {
    private import ScalarValues::*;
    private import SI::*;
    private import ISQ::*;
    
    /* --- Library Definitions --- */
    package StandardLibrary {
        part def Widget;
        part def Gadget;
        attribute def Status;
    }
    
    package SpecializedLibrary {
        /* Name collision with StandardLibrary */
        part def Widget; 
    }

    /* --- Imports & Aliasing --- */
    /* Public import: 'StandardLibrary' is visible to users of 'Naming_Tutorial' */
    /* Real-world example: The 'SI' library has 'public import ISQ::*;' */
    public import StandardLibrary::*;
    
    /* Private import to bring it into scope, though we can also just use alias directly */
    private import SpecializedLibrary::Widget;
    
    /* Alias to resolve collision or create short names */
    alias SpecialWidget for SpecializedLibrary::Widget;

    /* --- Definitions & Usages --- */
    part def SystemContext {
        /* Usage of standard import */
        part standardPart : Widget;
        
        /* Usage of aliased element */
        part specialPart : SpecialWidget;
        
        /* Using the alias defined in the package */
        alias SW for SpecialWidget;
        part anotherPart : SW;
        
        /* Escaped identifier for spaces */
        attribute 'System ID' : String;
        
        /* Correct Convention: camelCase usage */
        part mainGadget : Gadget;
        
        /* Unit reference uses brackets after a value, no quotes needed for special chars */
        attribute speed : Real = 100.0 [km/h];
    }
}
```



<div style='page-break-before: always;'></div>

# Partsattributes Tutorial

# Parts & Attributes

*Defining Structure and Values*

## 1. Definitions vs Usages

SysML v2 clearly separates definitions (types) from usages (instances).
• **part def**: Defines the blueprint of a structural element.
• **part**: A specific usage of that blueprint within another structure.

## 2. Attributes and Values

Attributes capture data properties like mass, power, or status. You typically use the standard ISQ library for physical quantities.
• **attribute def**: Defines a new value type.
• **attribute**: Holds the actual value.

## 3. Decomposition

Structure is built by nesting parts inside other parts (Composite Structure).

## 4. Spacecraft Example

```sysml
package PartsAndAttributes_Tutorial {
    private import ISQ::*; /* Import standard quantities */
    private import ScalarValues::*;
    
    attribute kN;
    attribute kg;
    
    /* --- Definitions --- */
    part def Engine {
        attribute maxThrust :> ISQ::force;
        attribute mass :> ISQ::mass;
    }
    
    part def FuelTank {
        attribute capacity : VolumeValue;
    }
    
    /* --- Composite Definition --- */
    part def Spacecraft {
        /* Attributes of the spacecraft itself */
        attribute totalMass :> ISQ::mass;
        attribute callSign : String;
        
        /* Parts (Usages) */
        /* Decomposing Spacecraft into subsystems */
        part mainEngine : Engine {
            /* Assigning values to attributes */
            attribute :>> maxThrust = 500 [kN];
            attribute :>> mass = 1000 [kg];
        }
        
        part reserveEngine : Engine; /* Uses defaults if any */
        
        part fuelSystem {
            part loxTank : FuelTank;
            part rp1Tank : FuelTank;
        }
    }
    
    /* --- Concrete Instance --- */
    part myShip : Spacecraft {
        attribute :>> callSign = "Voyager-1";
    }
}
```



<div style='page-break-before: always;'></div>

# Portsinterfaces Tutorial

# Ports & Interfaces

*Defining Interactions Points*

## 1. Ports

Ports define distinct interaction points on the boundary of a part. They allow you to encapsulate internal structure and only expose specific interfaces.

- **port name : Type**: Basic port declaration.
- **directed port (in, out, inout)**: Specifies data flow direction.

## 2. Interface Definitions

- **interface def**: Reusable definition of ports/flows.
- **Conjugation (~)**: Flips the direction of flows (e.g., Plug vs Socket). If an interface has `out pwr`, the conjugated version has `in pwr`.
- **Rule**: The `end` properties inside an interface must be ports (or untyped), never parts.
- **Rule**: Define internal flows using `flow source to target;` without `from` or `of` keywords.

## 3. Power & Data Example

```sysml
package PortsInterfaces_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Interface Definitions --- */
    /* Physical connection interface */
    port def PowerInterface {
        /* 'out' means power leaves this port locally */
        out attribute powerLevel : Real;
    }
    
    /* Logical data interface */
    port def DataLink {
        /* end definitions MUST be typed by a port (if complex) or left untyped */
        end source;
        end target;
        /* flow of messages inside the interface */
        flow source to target;
        /* CRITICAL: do not use 'from' or 'of' inside interface flows */
    }

    /* --- 2. Component Definitions --- */
    part def Battery {
        /* Provides power (Source) */
        port pwrPort : PowerInterface;
    }

    part def Computer {
        /* Consumes power (Sink) */
        /* Normally we use '~' to conjugate the interface, but avoiding due to validator resolution bug */
        port pwrIn : PowerInterface;
        
        /* Data port */
        port eth0 : DataLink;
    }
}
```



<div style='page-break-before: always;'></div>

# Requirements Tutorial

# Requirements

*Specifying and Verifying Needs*

## 1. Defining Requirements

Requirements capture the needs of the system. Note: Always use requirement usages for actual project requirements, and doc /* ... */ for shall statements.

```sysml
requirement <'REQ-ID'> 'Name' : RequirementType { doc /* Description */; }
```

## 2. Traceability

- **satisfy**: Asserting that a design element (part) meets a requirement.
- **verify**: Asserting that a test case proves a requirement (inside an objective block).
- **assert constraint { ... }**: Adding formal constraints inside requirements. **CRITICAL**: Do NOT place a semicolon at the end of the constraint block.

## 3. Requirements Example

```sysml
package Requirements_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Requirements --- */
    requirement def PerformanceReq {
        doc /* The system shall operate within performance limits. */
    }
    
    requirement <'REQ-101'> 'Breaking Distance' : PerformanceReq {
        doc /* The vehicle must stop within 50 meters from 100km/h. */
        /* Formal attributes */
        attribute maxDistance : Real = 50.0;
        attribute actualDistance : Real;
        /* Formal constraint (CRITICAL: no semicolon after constraint block) */
        assert constraint {
            actualDistance <= maxDistance
        }
    }

    /* --- 2. Satisfaction (Design) --- */
    part def BrakeSystem;
    
    part brakes : BrakeSystem {
        /* Asserting that this part satisfies the requirement */
        satisfy 'Breaking Distance';
    }
    
    /* --- 3. Verification (Testing) --- */
    /* A case to test the requirement */
    verification def BrakeTest {
        /* The requirement being verified */
        subject req : PerformanceReq;
        
        /* The logic (action) of the test */
        action executeTest {
            /* ... test steps ... */
        }
    }
    
    /* Usage of validation */
    verification test1 : BrakeTest {
        objective {
            verify 'Breaking Distance';
        }
    }
}
```



<div style='page-break-before: always;'></div>

# Semanticmetadata Tutorial

# Semantic Metadata

*Domain Specific Language (DSL) Extension*

## 1. Extending SysML with Metadata

Semantic Metadata allows you to define a Domain Specific Language (DSL) on top of SysML. You map your domain vocabulary (e.g., 'Drone', 'Sensor') to standard SysML concepts.

## 2. Mechanics

- **Define Domain Library**: Standard SysML definitions (parts, ports).
- **Define Metadata**: Mappings using `metadata def` and `specializes SemanticMetadata`.
- **Use DSL**: Apply metadata with `#metadataName`.

## 3. Drone DSL Example

```sysml
package DroneDSLinSysML {
    
    /* --- 1. Domain Library (Vocabulary) --- */
    library package Drone_Library {
        part def Sensor;
        part def ImageSensor :> Sensor;
        part def CollisionSensor :> Sensor;
        
        part def Rotor;
        
        part def Drone {
           part rotors : Rotor [1..*];
           part sensors : Sensor [0..*];
        }
    }
    
    /* --- 2. Metadata Definitions (The Mapping) --- */
    package Drone_Metadata {
        private import Drone_Library::*;
        private import Metaobjects::SemanticMetadata;
        
        metadata def drone :> SemanticMetadata {
            :>> baseType = Drone meta SysML::Definition;
            :> annotatedElement : SysML::Definition;
        }
        
        metadata def rotor :> SemanticMetadata {
            :>> baseType = Rotor meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
        
        metadata def cam :> SemanticMetadata {
            :>> baseType = ImageSensor meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
        
        metadata def lidar :> SemanticMetadata {
            :>> baseType = CollisionSensor meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
    }
    
    /* --- 3. DSL Usage (The Result) --- */
    package Mission_Model {
        private import Drone_Metadata::*;
        
        #drone part def SurveillanceDrone {
            /* Using the DSL vocabulary: */
            #rotor part frontRotors[2];
            #rotor part rearRotors[2];
            
            /* Defining sensors using shorthand */
            #cam part mainCamera;
            #lidar part obstacleAvoider;
        }
    }
}
```



<div style='page-break-before: always;'></div>

# Statemachine Tutorial

# State Machines

*States, Transitions, and Events*

## 1. State Machine Concepts

State machines define event-driven behavior. A system exists in a 'state' until an event triggers a 'transition'.

## 2. Key Syntax

- **state def**: Defines the state machine structure.
- **entry/do/exit**: Actions associated with a state.
- **transition first <source> accept <trigger> if <guard> do <action> then <target>**: Full transition syntax.
- **Rule**: Guards must use `if`, not `where`.
- **Rule**: A transition can only have ONE source state. You cannot use `or` in the `first` clause.
- **Rule**: Actions used inside a state machine (e.g. `do action`) should be defined in the surrounding part so they can access the part's attributes.

## 3. Traffic Light Example

```sysml
package StateMachine_Tutorial {
    private import SI::s;
    
    /* Define the component containing the machine */
    part def TrafficLight {
        /* Local actions defined in part scope can access part attributes */
        action def LogStatus;
        
        /* The machine behavior */
        state def LightLogic {
            /* Initial entry point */
            entry;
            then Red;
            
            state Red;
            state Yellow;
            state Green;
            
            transition redToGreen first Red accept after 20 [SI::s] then Green;
            transition greenToYellow first Green accept after 5 [SI::s] then Yellow;
            /* Using if-guard and do-action */
            transition yellowToRed first Yellow accept after 30 [SI::s] if true do action log : LogStatus then Red;
        }
        /* Usage of the machine */
        state logic : LightLogic;
    }
    view StateMachine_Tutorial : DS_Views::SymbolicViews::gv;
}
```



<div style='page-break-before: always;'></div>

# Usecase Tutorial

# Use Case Tutorial

*A Conceptual Overview & Example*

In SysML v2, a Use Case is a specialized type of case used to specify the required behavior of a system from the perspective of its external users (actors). It represents a coherent unit of functionality that provides something of value to an actor.

## Key Concepts

- **Use Case Definition (use case def)**: Defines the interaction type, subject, actors, and goal.
- **Actor**: External entity (person, system) interacting with the subject.
- **Subject**: The system under design providing the functionality.
- **Use Case Usage (use case)**: A specific occurrence of a use case definition.
- **Relationships**: Interaction, Include (reuse), Extend (optional/exceptional behavior).

## Example: Automated Pickleball Server (APS)

```sysml
package AutomatedPickleballServerModel {


    /* --- Definitions --- */
    part def ActorPart;
    use case def TrackPlayerState;
    use case def DetermineNextShot;
    use case def ServeBall;

    /* --- 1. Define the Actors --- */
    part def Player :> ActorPart;
    part def CourtEnvironment :> ActorPart;

    /* --- 2. Define the Subject System --- */
    part def AutomatedPickleballServer {
      part aiController;
      part ballLauncher;
      part sensorSuite;
    }

    /* --- 3. Define the Use Cases --- */
    use case def PlayPracticeSession {
      subject aps : AutomatedPickleballServer;
      actor player : Player;

      doc /* The player engages in a practice session where the server
             serves balls tailored to their skill level. */

      /* This use case INCLUDES other core behaviors */
      include use case trackPlayer : TrackPlayerState;
      include use case determineShot : DetermineNextShot;
      include use case serveBall : ServeBall;
    }
}

```



<div style='page-break-before: always;'></div>

# Variants Tutorial

# Variants

*Product Line Engineering*

## 1. Variation Points

Variation points allow you to define configurable elements in a product line.

## 2. Variants

Variants are the concrete options that can fill a variation point.

## 3. Engine Options Example

```sysml
package Variants_Tutorial {
    
    /* abstract definition */
    part def Engine;
    
    /* --- 1. Variants --- */
    part def V6Engine :> Engine;
    part def V8Engine :> Engine;
    part def ElectricMotor :> Engine;
    
    /* --- 2. Variation Point --- */
    part def Car {
        /* 'variation' declares this must be chosen */
        variation part engine : Engine;
    }
    
    /* --- 3. Configuration (Binding) --- */
    /* A specific configuration of the Car */
    part def SportCar :> Car {
        /* Binding the variation point to a specific type */
        variant part redefines engine : V8Engine;
    }
    
    part def EcoCar :> Car {
        variant part redefines engine : ElectricMotor;
    }
}
```



<div style='page-break-before: always;'></div>

# Viewpoints Tutorial

# Viewpoints & Views

*Presenting the Model*

## 1. Viewpoints and Views

Views present a subset of the model for a specific purpose (the Viewpoint).

## 2. Expose and Filter

- **expose**: Explicitly includes elements in the view.
- **filter**: Conditionally excludes elements.

## 3. Mass Report Example

```sysml
package Viewpoint_Tutorial {
    private import ScalarValues::*;
    
    /* The subject */
    part def Car {
        attribute mass : Real;
        part engine;
        part wheels;
    }
    
    /* --- 1. Viewpoint Definition --- */
    viewpoint def MassReport {
        doc /* A report focusing only on mass properties. */
    }
    
    /* --- 2. Viewpoint Usage --- */
    viewpoint <'VP-002'> 'mass report viewpoint' : MassReport {
        doc /* Focuses on mass properties of the vehicle */
    }
    
    /* --- 3. View Definition --- */
    view def MassView {
        /* The subject being viewed */
        in part car : Car;
    }
        
    /* --- 4. View Usage and Exposing Elements --- */
    part myCar : Car;
    
    view report : MassView {
        in part car = myCar;
        satisfy 'mass report viewpoint';
        
        /* Show the car itself */
        expose myCar;
        
        /* Show sub-parts using :: */
        expose myCar::engine;
    }
}
```



<div style='page-break-before: always;'></div>

# Views Tutorial

# Views

*Visualizing the Model*

## 1. Views Concept

Views provide a way to visualize and present the model. They do not change the model structure but 'expose' parts of it in specific formats (Diagrams, Tables).

## 2. Common View Types

- **SymbolicViews::gv**: Graphical View (Diagram).
- **TabularViews::gt**: Generic Table.
- **TabularViews::rt**: Requirements Table.
- **CRITICAL**: When filtering for allocations or satisfies, filter by the usage (e.g., `@AllocationUsage`), not the definition (e.g., `@Allocation`).

## 3. Views Example

```sysml
package Views_Tutorial {
    /* Standard sysml library imports */
    private import SysML::*;
    
    /* Mock Cameo View elements for standard validation */
    package SymbolicViews { view def gv; }
    package TabularViews { view def gt; }
    view def TreeView;
    view def rt;
    action def EssentialElementsFilter;
    action def NonStandardLibraryElementFilter;
    
    package <BV> BaseViews {
        view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
            /* filter elements */
        }
        view allocationTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
            /* filter elements */
        }
    }

    part def Car;
    part def Engine;
    part def Wheel;
    
    part myCar : Car {
        part engine : Engine;
        part wheels [4] : Wheel;
    }
    
    /* --- 1. Graphical View (Diagram) --- */
    view carDiagram : SymbolicViews::gv, EssentialElementsFilter, NonStandardLibraryElementFilter {
        /* Show the entire car structure */
        expose myCar;
        
        /* You can filter or refine what is shown here */
        /* (See Filters Tutorial) */
    }
    
    /* --- 2. Tabular View (Table) --- */
    /* Defining a reusable table structure */
    view def PartTable :> TabularViews::gt {
        /* Define columns */
        render rendering asTable {
            /* table columns definition goes here */
        }
    }
    
    /* Using the table */
    view myTable : PartTable {
        /* Show everything under myCar recursively */
        expose myCar::**;
    }
}
```



<div style='page-break-before: always;'></div>

# Cameo Features Tutorial

# Cameo-Specific SysMLv2 Features

*Creating Custom Tables, Style Sheets, Palettes, and Dialogs in Cameo (CATIA Magic)*

## 1. Overview

While standard SysMLv2 provides robust modeling capabilities, Cameo (CATIA Magic) extends it with domain-specific features for creating custom diagrams (Symbolic Views), tables (Tabular Views), style sheets, and custom UI components (Dialogs, Palettes).

These features are accessed by importing specific Dassault Systèmes (DS) packages, such as `DS_Views`, `DS_Styles`, and `DS_UIComponents`.

---

## 2. Custom Style Sheets

Style sheets allow you to conditionally format elements in a view (e.g., coloring requirements based on metadata status).

```sysml
package StyleSheets {
    private import DS_Styles::CoreStylesComponents::Predicates::*;
    private import DS_Styles::CoreStylesComponents::KerMLStyles::*;

    part def StatusStyle :> DS_Styles::CoreStylesComponents::StyleSheet {
        
        part approvedRule :> rule {
            /* Condition for when the rule applies */
            part :>> condition : FreeFormCondition {
                calc :>> test {
                    GetValueOfMetadataFeature(element, Profile::info::status.metadata) == Profile::Status::approved.metadata
                }
            }
            /* Style applied when condition is true */
            part :>> style : SymbolStyle {
                attribute :>> penColor : Color = "#006400"; /* Dark Green */
                attribute :>> lineWidth = 2;
            }
        }
    }
}
```

**Applying the Style Sheet to a View:**
```sysml
view 'colored requirements diagram' : DS_Views::SymbolicViews::gv {
    /* Explicitly apply the style sheet */
    part : StyleSheets::StatusStyle :> explicitlyAppliedStyleSheets;
}
```

---

## 3. Custom Tabular Views (Tables)

You can define custom requirements tables (`rt`) or generic tables (`gt`) with specific scopes (expose), element filters, and dynamically calculated columns.

```sysml
private import DS_Views::*;

/* A Requirements Table */
view 'requirements table' : TabularViews::rt {
    expose DroneStakeholderRequirements::**; /* Scope */
    render rendering :>> asTable {
        view :>> 'Declared Name';
        view :>> 'Req Id';
        view :>> Documentation;
    }
}

/* A Generic Table with Custom Calculated Columns */
view 'variant table' : CoreViews::bt {
    filter @PartDefinition or @PartUsage;
    expose Drone::DroneVariants::**;
    
    render rendering :>> asTable {
        view : CoreViews::ColumnByFeatureView :> column {
            ref item :>> columnFeature = declaredName meta Feature;
        }
        
        /* Custom expression column */
        view 'Net Price' : CoreViews::ColumnByExpressionView :> column {
            render rendering : CoreViews::RealCellRendering :>> asTableCell {
                calc :>> getValue {
                    in :>> rowElement : Element;
                    (getNetPrice(rowElement) as LiteralInteger).value ?? 0
                }
                /* Custom calculation function */
                calc getNetPrice {
                    in e : Element;
                    /* ... extraction logic ... */
                }
            }
        }
    }
}
```

---

## 4. Custom Palettes and Symbolic Views

You can customize the creation palette (sidebar tools) for a specific symbolic view to provide a tailored modeling environment.

```sysml
private import DS_UIComponents::CoreUIComponents::Palette::*;

view def 'Requirements View' :> DS_Views::CoreViews::bsv {
    part :>> baseViewPalette {
        
        part requirementsCategory :> buttonCategories {
            attribute :>> label default "Requirements";
            
            /* Adding a button that creates an element via Code Action */
            part reqButton : Button :> abstractButtons {
                perform action : DS_UIComponents::CoreUIComponents::Operations::OperationFromCode :> operation {
                    in ref = DS_Views::ViewPalettes::CodeActionIdentifiers::requirementAction;
                }
            }
            
            /* Adding a button that creates an element from a Template */
            part softwareButton : Button :> abstractButtons {
                attribute :>> label = "Software Requirement";
                perform action : DS_UIComponents::CoreUIComponents::Operations::OperationFromTemplate :> operation {
                    in ref = softwareReqTemplate::softwareRequirement.metadata;
                }
            }
        }
    }
}
```

---

## 5. Custom View Creation Dialogs

You can inject your custom views and tables into the Cameo "Create View" or "Create Diagram" dialogs.

```sysml
package CustomViewCreationDialogs {
    /* 1. Wrap the view in a package acting as a template */
    package customRequirementsViewTemplate {
        view : CustomRequirementsView::'Requirements View';
    }

    /* 2. Specialize the Creation Dialog */
    part def CustomViewCreationDialog :> DS_UIComponents::UIComponents::SysMLViewCreationDialog {
        
        part :>> sysMLViewsMenu {
            part reqViewItem : DS_UIComponents::CoreUIComponents::Dialogs::DialogItem :> abstractItems {
                attribute :>> label default "Custom Requirements View";
                perform action : DS_UIComponents::CoreUIComponents::Operations::OperationFromTemplate :>> operation {
                    in ref = (customRequirementsViewTemplate meta KerML::Kernel::Package).ownedElement;
                }
            }
        }
    }
}
```



