package Constraints_3CalculationDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    calc def calcKineticEnergy {
      in m : Mass;
      in v : Speed;
      return ke : Energy;
      0.5 * m * v^2
    }
}