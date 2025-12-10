package States_3GuardsEffects {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    transition t2
       first Green
       if traffic == 0
       do action resetTimer
       then Red;
}