package Behavior_3GuardsEffects {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        transition t2 {
           first Green
           if traffic == 0
           do action resetTimer
           then Red;
        }
    }

    view ExposeExample {
        expose Main;
    }
}