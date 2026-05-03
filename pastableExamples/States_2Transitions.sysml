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