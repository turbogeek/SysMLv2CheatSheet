package Connections_2BindingConnector {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    part system {
       part a : A;
       part b : B;
       bind a.p1 = b.p2;
    }
}