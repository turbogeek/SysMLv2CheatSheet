package States_1StateDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    state def TrafficLight {
       entry perform logStart;
       exit perform logEnd;
       state Red;
       state Green;
    }
}