package Connections_4SuccessionFlow {
    private import ScalarValues::*;
    private import SysML::*;
    action process {
       action step1;
       action step2;
       first step1;
       then step2;
       doc /* Equivalent to: */
       flow from step1 to step2;
    }
}