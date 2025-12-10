package Connections_4SuccessionFlow {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    action process {
       step1 then step2;
       doc /* Equivalent to: */
       flow from step1 to step2;
    }
}