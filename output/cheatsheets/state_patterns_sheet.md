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

