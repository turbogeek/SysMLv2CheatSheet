package PartsAndAttributes_Tutorial {
    private import ISQ::*; /* Import standard quantities */
    private import ScalarValues::*;
    
    attribute kN;
    attribute kg;
    
    /* --- Definitions --- */
    part def Engine {
        attribute maxThrust :> ISQ::force;
        attribute mass :> ISQ::mass;
    }
    
    part def FuelTank {
        attribute capacity : VolumeValue;
    }
    
    /* --- Composite Definition --- */
    part def Spacecraft {
        /* Attributes of the spacecraft itself */
        attribute totalMass :> ISQ::mass;
        attribute callSign : String;
        
        /* Parts (Usages) */
        /* Decomposing Spacecraft into subsystems */
        part mainEngine : Engine {
            /* Assigning values to attributes */
            attribute :>> maxThrust = 500 [kN];
            attribute :>> mass = 1000 [kg];
        }
        
        part reserveEngine : Engine; /* Uses defaults if any */
        
        part fuelSystem {
            part loxTank : FuelTank;
            part rp1Tank : FuelTank;
        }
    }
    
    /* --- Concrete Instance --- */
    part myShip : Spacecraft {
        attribute :>> callSign = "Voyager-1";
    }
}