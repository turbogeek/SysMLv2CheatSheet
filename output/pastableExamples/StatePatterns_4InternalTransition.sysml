package StatePatterns_4InternalTransition {
    private import ScalarValues::*;
    private import SysML::*;
    action def tick;
    action check;
    state def Monitoring {
       state Idle;
       /* Internal behavior (Self-transition) */
       transition t1 first Idle accept tick do check then Idle;
    }
}