package Requirements_5ConstraintDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute kg;
    constraint def CheckMass {
      in m : Mass;
      m <= 1000 [kg]
    }
}