package Constraints_3CalculationDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute def Speed;
    attribute def Energy;
    calc def calcKineticEnergy {
      in m : Mass;
      in v : Speed;
      return ke : Energy = 0.5 * m * v^2;
    }
}