package Calculations_3ConstraintDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    constraint def MassLimit {
       in m : Mass;
       in limit : Mass;
       m <= limit;
    }
}