package StatePatterns_4InternalTransition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    state def Monitoring {
       transition selfCheck
          accept tick
          do action check;
    }
}