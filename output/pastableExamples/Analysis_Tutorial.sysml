package Analysis_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Constraint Definition --- */
    constraint def MassEquation {
        in total : Real;
        in p1 : Real;
        in p2 : Real;
        
        /* The math */
        total == p1 + p2
    }
    
    part def System {
        attribute mass : Real;
        attribute part1Mass : Real;
        attribute part2Mass : Real;
        
        /* --- 2. Constraint Usage (Parametrics) --- */
        /* Binding properties to the equation parameters */
        constraint massCheck : MassEquation {
            in total = mass;
            in p1 = part1Mass;
            in p2 = part2Mass;
        }
    }
    
    /* --- 3. Analysis Case --- */
    analysis def WeightCheck {
        subject system : System;
        
        /* Determining if mass is within limits */
        return result : Boolean = system.mass < 100.0;
    }
}