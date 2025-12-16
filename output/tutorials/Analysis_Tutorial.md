# Analysis & Constraints

*Parametrics and Evaluation*

## 1. Constraints (Parametrics)

Constraints define mathematical equations that govern system properties.

```sysml
constraint def OhmLaw { in v; in i; in r; v == i * r }
```

## 2. Analysis Cases

Analysis cases specify the logic for evaluating system performance, often involving solving constraints or running simulations.

## 3. Mass Analysis Example

```sysml
package Analysis_Tutorial {
    import ScalarValues::*;
    
    // --- 1. Constraint Definition ---
    constraint def MassEquation {
        in total : Real;
        in p1 : Real;
        in p2 : Real;
        
        // The math
        total == p1 + p2
    }
    
    part def System {
        attribute mass : Real;
        attribute part1Mass : Real;
        attribute part2Mass : Real;
        
        // --- 2. Constraint Usage (Parametrics) ---
        // Binding properties to the equation parameters
        constraint massCheck : MassEquation {
            in total = mass;
            in p1 = part1Mass;
            in p2 = part2Mass;
        }
    }
    
    // --- 3. Analysis Case ---
    analysis def WeightCheck {
        subject system : System;
        
        // Determining if mass is within limits
        return result : Boolean = system.mass < 100.0;
    }
}
```

