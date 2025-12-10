package ActionPatterns_3IfElse {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        if x > 0 {
           assign y := 1;
        } else {
           assign y := 0;
        }
    }

    view ExposeExample {
        expose Main;
    }
}