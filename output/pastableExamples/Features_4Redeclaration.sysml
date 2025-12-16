package Redeclaration_Example {
    part def Spacecraft {
        part module;
    }
    
    part def Lander :> Spacecraft {
        // Add details to the inherited 'module'
        // Equivalent to: part module :>> module { ... }
        part :>> module {
            attribute mass = 500 [ISQ::kg];
        }
    }
}