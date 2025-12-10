package Constraints_5Objective {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    objective def MinimizeMass {
      in m : Mass;
      minimize m;
    }
}