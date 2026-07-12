package Symbols_5EqualityAndAssignment {
    private import ScalarValues::*;
    private import SysML::*;

    attribute val1 = 5; /* Rigid value binding */
    attribute val2 := 10; /* Initial value (re-assignable) */

    action def Compare {
        in attribute a : Integer;
        in attribute b : Integer;
        out attribute isEqual : Boolean;
        out attribute isSame : Boolean;

        /* Value equality (==) vs Identity same (===) */
        isEqual = (a == b);
        isSame = (a === b);
    }
}