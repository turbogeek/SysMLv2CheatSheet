# SysML v2.0 Language Reference

## Overview

Systems Modeling Language (SysML) v2.0 is an OMG standard for model-based systems engineering. It extends the Kernel Modeling Language (KerML) to provide comprehensive modeling capabilities for complex systems.

## Core Concepts

### Key things to remember

NEVER use single line comments `//` in the SysMLv2 language because these are not persisted to the model and are lost.
The only reason to use `public` is when the element is to be used everywhere because a `public` is part of the world view. It is better to use the default (no `public` or `private`) so that a user in another package is forced to import.
The only reason to use `private` is when the element is truly not usable or redefinable outside of a context of the package it lives, which in SysMLv2 is rare as we care less about this in engineering than is in software where we don't trust fellow programmers.
When importing, the import must be prefixed with `public` , `private` or `protected` with 'private' being the default import accessibility specified (for example `private import ScalarValues::*;`).

### Definition and Usage Pattern

The fundamental pattern in SysML v2 is the **definition-usage** relationship:

- **Definitions** classify things (types, templates)
- **Usages** apply definitions in specific contexts (instances, applications)

This pattern applies throughout the language for all major constructs.

---

## 1. STRUCTURAL MODELING

### 1.1 Packages (7.5)

Packages organize model elements into namespaces.

```sysml
package VehicleSystem {
    private import ScalarValues::*; // Or explicitly: private import ScalarValues::Real;
    // Package members
}
```

**Key Features:**

- Provide namespaces for organizing models
- Support imports. Always prefer `private import PackageName::*;` to avoid polluting the namespace of other packages that import yours.
- **CRITICAL RULE:** Any use of scalar values (like `Real`, `Integer`, `String`, `Boolean`) must be accompanied by an import, e.g., `private import ScalarValues::Real;` or `private import ScalarValues::*;`.
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

// Time slices
occurrence def Mission {
    timeslice planning[1];
    timeslice execution[1];
    timeslice review[1];
}

// Individuals
individual def Flight_248 :> Flight;

// Snapshots
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

// Conjugated port (reversed directions)
part def Engine {
    port fuelInPort : ~FuelingPort;  // Conjugated
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

// Binding connection
bind part2.feature = part3.feature;

// Succession
first action1 then action2;
```

**Key Features:**

- Binary relationships with ends
- Support binding (equality)
- Support succession (ordering)
- Can have attributes and constraints

### 1.9 Interfaces (7.14)

Interfaces are connections where all ends are ports.

```sysml
interface def FuelingInterface {
    end port tankPort : FuelingPort;
    end port vehiclePort : ~FuelingPort;
}
```

**Key Features:**

- All ends must be ports
- Define interaction protocols
- Often use conjugated ports

### 1.10 Allocations (7.15)

Allocations map elements across system structures. **Crucially, allocation only works between usages, not definitions.**

```sysml
allocation def Deployment {
    end source : Function;
    end target : Component;
}

// Ensure you allocate between specific usages (e.g., parts), not defs:
part def LogicalSystem {
    part func : Function;
}
part def PhysicalSystem {
    part comp : Component;
}

part logicalUsage : LogicalSystem;
part physicalUsage : PhysicalSystem;

allocate physicalUsage.comp to logicalUsage.func;
```

**Key Features:**

- Assert target realizes source intent
- Support traceability
- Map across abstraction levels
- **Must be applied between usages, not definitions**

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
// While loop
while t < endTime {
    assign y := 2*x;
    then assign x := x + increment;
} until x >= 10;

// For loop
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
        first off /* transitioning from state*/
        accept TurnOn via commPort/* event */
        if isEnabled /* guard */
        do action powerUp : PowerUp; /* do action aka effect */
        then on /* transition to state*/; 
}

// State with actions
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

// Calculation usage
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

// Constraint usage
constraint vehicleMassLimit : MassLimit {
    in mass = vehicle.mass;
    in limit = 2000[kg];
}
```

**Assert Constraints:**

```sysml
assert constraint positiveValue {
    value > 0;
}

// Negated assertion
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
// Define requirement types (Defs)
package <RT> RequirementTypes {
    requirement def PerformanceRequirement {
        doc /* A requirement that requires a specific metric to be met. */
    }
    requirement def SafetyRequirement {
        doc /* A requirement that mandates a safety condition. */
    }
}

// Instantiate actual system requirements (Usages)
package Requirements {
    // Use the <'ID'> shortcut syntax for the ID and provide a short name
    requirement <'REQ-PERF-01'> 'Minimum System MTBF' : RT::PerformanceRequirement {
        doc /* The system shall have a mean time between failures of greater than 5 years. */
        attribute MTBF : Time::Iso8601DateTimeStructure; 
        attribute MTBF_target : Time::Iso8601DateTimeStructure = 5[Time::Iso8601DateTimeStructure::year];

        require constraint {
            MTBF >= MTBF_target
        }
    }
    
    requirement <'REQ-SAFE-01'> 'Max Temperature' : RT::SafetyRequirement {
        doc /* The external chassis temperature shall not exceed 45°C. */
    }
}
```

**Subjects, Actors, Stakeholders:**

```sysml
// NOTE: `actor` and `stakeholder` are USAGE keywords, not definition keywords.
// The types they reference must be defined as `part def` or `item def` (e.g., `part def Person;`).
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

// In context
part vehicle1 : Vehicle {
    satisfy rqts : VehicleRequirementsGroup;
}

// Negated
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

    // Case actions
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

    // Analysis actions
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

    // Verification actions
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
package BV BaseViews {
    doc /* A set of reusable views. These form the base of the zoo of views and are intended to be the starting point for the creation of new views. For example, the partDefTableView is a filtered and constrained table of parts. It inherits from the generic table and adds a default filter of parts.  */
    private import DS_Views::SymbolicViewsByExpression::*;
    private import DS_Views::TabularViews::*;
    private import SysML::Systems::*;
    
 /* A set of reusable views. These form the base of the zoo. This also serves as training and laboratory for the views */
    
    view partsView : UsagesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
    view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
        filter @PartDefinition;
        filter @PartUsage;
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
// Bind (equality)
attribute count : Integer = 12;

// Initial value
attribute counter : Integer := 0;

// Default value
attribute cutoff : Real default = 0.75 * average;
```

### Multiplicities

```sysml
part wheels[4] : Wheel;           // Exactly 4
part driver[0..1] : Person;       // Optional
part passengers[*] : Person;      // Any number
part engines[1..*] : Engine;      // At least 1
```

### Ordered and Unique

```sysml
part orderedList[*] ordered nonunique;
part uniqueSet[*] unordered unique;
```

### Specialization

```sysml
part def SportsCar specializes Vehicle;
part def SportsCar :> Vehicle;  // Shorthand
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
// Single line comment
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
import ScalarValues::*;
import ISQ::*;
import SI::*;
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
    port in : ~DataPort;  // Conjugated
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

1. **Textual First**: SysML v2 is primarily textual (v1 was graphical first)
2. **No Blocks**: Parts replace blocks as the primary structural element
3. **Unified Actions/Activities**: Integrated action model (v1 had separate concepts)
4. **Calculations**: New concept for side-effect-free computations
5. **Analysis/Verification Cases**: Formalized case concepts
6. **Stronger Typing**: More rigorous type system based on KerML
7. **Feature-Based**: Everything is a feature with consistent semantics
8. **Occurrence Semantics**: Explicit temporal and spatial extent modeling
9. **Conjugated Ports**: Built-in support for direction reversal
10. **Metadata Framework**: Standardized metadata annotations

---

## 10. METAMODEL CONCEPTS (Section 8)

The SysML v2 metamodel defines:

- **Abstract Syntax**: The structure of model elements
- **Concrete Syntax**: Textual and graphical notation
- **Semantics**: Meaning and behavior of elements
- **Well-Formedness Rules**: Validity constraints

Key metamodel concepts:

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
