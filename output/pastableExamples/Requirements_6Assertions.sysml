package Requirements_6Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    part car {
      assert constraint CheckMass {
        in m = mass;
      }
    }
}