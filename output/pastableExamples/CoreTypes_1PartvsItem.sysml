package CoreTypes_1PartItems {
    // A Part occupies space and time
    part def Engine {
        // Parts can contain other parts
        part cylinder;
    }
    
    // An Item is information or substance flow (no structure)
    item def TorqueCommand;
    
    part car {
        part myEngine : Engine;
        // Items often flow between parts
        item currentCmd : TorqueCommand;
    }
}