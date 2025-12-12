package Constraints_4CalculationUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute def Speed;
    attribute def Energy;
    attribute kg;
    attribute m;
    attribute s;
    calc def calcKineticEnergy { in m : Mass; in v : Speed; return ke : Energy; }
    action def Main {
        attribute kEnergy : Energy = calcKineticEnergy(m = 100 [kg], v = 20 [m/s]);
    }
    view ExposeExample { expose Main; }
}