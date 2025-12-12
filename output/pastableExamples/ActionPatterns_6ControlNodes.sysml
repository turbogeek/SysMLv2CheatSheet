package ActionPatterns_6ControlNodes {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        fork  f1 ;
        join  j1 ;
        decide  d1 ;
        merge  m1 ;
    }

    view ExposeExample {
        expose Main;
    }
}