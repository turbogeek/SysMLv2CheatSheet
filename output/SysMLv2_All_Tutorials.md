# SysML v2 Tutorials: Complete Collection

**Generated on:** 2026-05-05 14:11:03

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

