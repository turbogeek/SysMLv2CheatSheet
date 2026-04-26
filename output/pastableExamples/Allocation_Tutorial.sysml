package Allocation_Tutorial {
    
    /* --- Behavioral / Logical View --- */
    action def ComputePath;
    
    /* --- Physical / Structural View --- */
    part def FlightComputer;
    
    /* Create a dedicated package for allocations between usages */
    package AllocationContext {
        part ecu : FlightComputer;
        action plan : ComputePath;
        
        /* Allocate the action usage (plan) to the hardware usage (ecu) */
        /* Meaning: "The ECU executes the planning action" */
        allocate plan to ecu;
    }
}