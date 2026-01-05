# Behavior Cheat Sheet

*State Machines and Actions*

## 1. State Definition

States and lifecycle actions.

```sysml
package Behavior_1StateDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
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
    // Wrapped Snippet (Action Context)
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

