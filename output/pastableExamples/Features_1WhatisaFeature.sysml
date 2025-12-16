package Feature_Basics {
    part def Car {
        // Structural Features
        attribute vin : String;
        part engine : Engine;
        
        // Behavioral Features
        action drive;
    }
}