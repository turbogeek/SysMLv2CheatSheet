package Vehicle_Library {
    part def Vehicle;
    part def engines;
    part def wheels;
    interface def driveTrains;
    
    // Standard Ports for connections
    part def EnginePart :> engines { port enginePort; }
    part def WheelPart :> wheels { port wheelPort; }
}