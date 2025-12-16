package PartsAndAttributes_Tutorial {
    import ISQ::*; // Import standard units
    
    // --- Definitions ---
    part def Engine {
        attribute maxThrust : ForceValue;
        attribute mass : MassValue;
    }
    
    part def FuelTank {
        attribute capacity : VolumeValue;
    }
    
    // --- Composite Definition ---
    part def Spacecraft {
        // Attributes of the spacecraft itself
        attribute totalMass : MassValue;
        attribute callSign : String;
        
        // Parts (Usages)
        // Decomposing Spacecraft into subsystems
        part mainEngine : Engine {
            // Assigning values to attributes
            attribute :>> maxThrust = 500 [kN];
            attribute :>> mass = 1000 [kg];
        }
        
        part reserveEngine : Engine; // Uses defaults if any
        
        part fuelSystem {
            part loxTank : FuelTank;
            part rp1Tank : FuelTank;
        }
    }
    
    // --- Concrete Instance ---
    part myShip : Spacecraft {
        attribute :>> callSign = "Voyager-1";
    }
}