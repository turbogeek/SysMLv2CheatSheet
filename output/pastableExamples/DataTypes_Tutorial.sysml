package DataTypes_Tutorial {
    import ScalarValues::*;
    import ISQ::*; 

    // --- 1. Custom Value Definitions ---
    // Specializing a primitive
    attribute def IDString :> String;
    
    // Struct for composite data (Kernel level concept often used)
    attribute def Coordinates {
        attribute x : Real;
        attribute y : Real;
        attribute z : Real;
    }

    part def SensorSystem {
        // --- 2. Using Primitives ---
        attribute isActive : Boolean = true;
        attribute firmwareVersion : String = "v1.2.4";
        attribute cycleCount : Integer = 0;
        
        // --- 3. Using ISQ Units ---
        // Type checking ensures you can't assign Mass to Length
        attribute weight : MassValue = 5.5 [kg];
        attribute scanRange : LengthValue = 150 [m];
        
        // Unit conversion is handled by checks (e.g. [km] -> [m])
        attribute speed : SpeedValue = 120 [km/h]; 
        
        // --- 4. Using Custom Types ---
        attribute sensorID : IDString = "SENS-001";
        attribute location : Coordinates {
             :>> x = 10.0;
             :>> y = 20.0;
             :>> z = 0.0;
        }
    }
}