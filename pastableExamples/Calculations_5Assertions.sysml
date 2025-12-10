package Calculations_5Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        assert constraint {
           x > 0;
        }
        not assert constraint {
           y < 0;
        }
    }

    view ExposeExample {
        expose Main;
    }
}