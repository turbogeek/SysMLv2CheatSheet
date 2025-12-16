package DomainLibs_Tutorial {
    import ISQ::*;
    import SI::*;
    import Time::*;
    
    // --- 1. Using ISQ Types ---
    part def MovingObject {
        attribute mass : MassValue;
        attribute velocity : SpeedValue;
        attribute startingTime : TimeInstantValue;
    }
    
    part car : MovingObject {
        // --- 2. Using Units ---
        attribute redefines mass = 1500 [kg];
        attribute redefines velocity = 120 [km/h];
        
        // --- 3. Time ISO 8601 ---
        attribute redefines startingTime = "2023-10-27T10:00:00Z";
    }
    
    // --- 4. Geometry (Shape Library) ---
    // (Requires Shape library import usually)
    // part wheel : Cylinder { 
    //    attribute radius = 30 [cm];
    // }
}