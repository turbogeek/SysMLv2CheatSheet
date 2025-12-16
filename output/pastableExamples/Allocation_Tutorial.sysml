package Allocation_Tutorial {
    
    // --- Behavioral / Logical View ---
    action def ComputePath;
    
    // --- Physical / Structural View ---
    part def FlightComputer;
    
    package Deployment {
        part ecu : FlightComputer;
        action plan : ComputePath;
        
        // Allocate the action (plan) to the hardware (ecu)
        // Meaning: "The ECU executes the planning action"
        allocate plan to ecu;
    }
}