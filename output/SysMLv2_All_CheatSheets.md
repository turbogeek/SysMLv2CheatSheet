# SysML v2 Cheat Sheets: Complete Collection

**Generated on:** 2026-04-27 11:31:14

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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Action Context */)
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
    /* Wrapped Snippet (Action Context */)
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
    /* Wrapped Snippet (Action Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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

![Part Definition](assets/symbols/light/PartDefinition.svg)

**Notation**: Rectangle: 'part def'

**Syntax**: `part def Name;`

**Example**: `part def Vehicle;`

## Part Usage

![Part Usage](assets/symbols/light/PartUsage.svg)

**Notation**: Rounded Rect: 'part'

**Syntax**: `part name : Type;`

**Example**: `part engine : Engine;`

## Action Definition

![Action Definition](assets/symbols/light/ActionDefinition.svg)

**Notation**: Rectangle: 'action def'

**Syntax**: `action def Name;`

**Example**: `action def Drive;`

## Action Usage

![Action Usage](assets/symbols/light/ActionUsage.svg)

**Notation**: Rounded Rect: 'action'

**Syntax**: `action name : Type;`

**Example**: `action drive : Drive;`

## Requirement Def

![Requirement Def](assets/symbols/light/RequirementDef.svg)

**Notation**: Rectangle: 'requirement def'

**Syntax**: `requirement def Name;`

**Example**: `requirement def Perf;`

## Requirement Usage

![Requirement Usage](assets/symbols/light/RequirementUsage.svg)

**Notation**: Rounded Rect: 'requirement'

**Syntax**: `requirement name : Type;`

**Example**: `requirement req1 : Perf;`

## State Definition

![State Definition](assets/symbols/light/StateDefinition.svg)

**Notation**: Rectangle: 'state def'

**Syntax**: `state def Name;`

**Example**: `state def Idle;`

## State Usage

![State Usage](assets/symbols/light/StateUsage.svg)

**Notation**: Rounded Rect: 'state'

**Syntax**: `state name;`

**Example**: `state off;`

## 2. Relationships

## Specialization

![Specialization](assets/symbols/light/Specialization.svg)

**Notation**: Solid line, hollow triangle

**Syntax**: `def A :> B;`

**Example**: `part def Car :> Vehicle;`

## Composition

![Composition](assets/symbols/light/Composition.svg)

**Notation**: Solid line, filled diamond

**Syntax**: `part name : Type;`

**Example**: `part wheel : Wheel;`

## Reference

![Reference](assets/symbols/light/Reference.svg)

**Notation**: Solid line, hollow diamond

**Syntax**: `ref part name : Type;`

**Example**: `ref part driver : Person;`

## Import

![Import](assets/symbols/light/Import.svg)

**Notation**: Dashed line, open arrow

**Syntax**: `import Package::*;`

**Example**: `import SI::*;`

## Binding

![Binding](assets/symbols/light/Binding.svg)

**Notation**: Solid line, «bind»

**Syntax**: `bind a = b;`

**Example**: `bind p1 = p2;`

## Succession

![Succession](assets/symbols/light/Succession.svg)

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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    attribute n : Natural; /* 0, 1, * (UnlimitedNatural in v1 */)
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
    /* satisfy req1 by server; // Alternative syntax */
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
      require constraint {
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
       /* Internal behavior (Self-transition */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    /* Wrapped Snippet (Structure Context */)
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
    in subject : System;
}
```

Defines a reusable view structure.

## 2. View Usage

```sysml
view report : ReportView {
    in subject = mySystem;
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



