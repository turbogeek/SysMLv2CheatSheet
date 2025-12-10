package Behavior_1StateDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        state def PracticeSession {
           entry; exit;
           state Idle;
           state Serving;
        }
    }

    view ExposeExample {
        expose Main;
    }
}