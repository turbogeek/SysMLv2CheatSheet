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

