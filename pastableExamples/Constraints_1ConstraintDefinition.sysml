package Constraints_1ConstraintDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Force;
    attribute def Mass;
    attribute def Acceleration;
    constraint def NewtonLaw {
      in f : Force;
      in m : Mass;
      in a : Acceleration;
      f = m * a;
    }
}