package Calculations_4ConstraintUsage {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        constraint checkMass : MassLimit {
           in m = self.mass;
           in limit = 1000.0;
        }
    }

    view ExposeExample {
        expose Main;
    }
}