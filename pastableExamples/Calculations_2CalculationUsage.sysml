package Calculations_2CalculationUsage {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        calc p_motor : PowerCalc {
           in v = 12.0;
           in i = 5.0;
        }
    }

    view ExposeExample {
        expose Main;
    }
}