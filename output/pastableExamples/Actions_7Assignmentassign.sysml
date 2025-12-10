package Actions_7Assignmentassign {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        assign x := 42;
        assign y := x + 1;
        doc /* Value assignment */
    }

    view ExposeExample {
        expose Main;
    }
}