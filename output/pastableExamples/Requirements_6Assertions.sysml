package Requirements_6Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute kg;
    constraint def CheckMass { in m : Mass; m <= 1000[kg] }
    part car {
      attribute mass : Mass;
      assert constraint CheckMass {
        in m = mass;
      }
    }
}