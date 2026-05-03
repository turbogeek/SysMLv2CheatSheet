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