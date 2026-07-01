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

