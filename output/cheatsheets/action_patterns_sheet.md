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

