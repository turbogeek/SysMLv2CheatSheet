package Constraints_2bInlineAssertion {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute x : Integer;
        assert constraint {
           x > 0
        }
        /* Boolean expression */
    }
    view ExposeExample { expose Main; }
}