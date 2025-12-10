package Requirements_5ConstraintDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    constraint def CheckMass {
      in m : Mass;
      m <= 1000 [kg]
    }
}