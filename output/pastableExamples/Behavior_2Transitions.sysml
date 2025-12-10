package Behavior_2Transitions {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        transition startServe
           first Idle
           accept Remote.Start
           do action log : Log('Serving');
           then Serving;
    }

    view ExposeExample {
        expose Main;
    }
}