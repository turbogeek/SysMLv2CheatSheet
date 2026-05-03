package Requirements_6Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute kg;
    part car {
      attribute mass : Mass;
      require constraint {
        mass <= 1000 [kg]
      }
    }
}