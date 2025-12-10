package Behavior_3bInternalTransition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        state def Monitoring {
           state selfCheck;
           transition selfCheck
              accept tick
              do action check then selfCheck;
        }
    }

    view ExposeExample {
        expose Main;
    }
}