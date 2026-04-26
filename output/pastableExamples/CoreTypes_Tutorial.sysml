package CoreTypes_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Enumerations --- */
    enum def Status {
        enum Active;
        enum Idle;
        enum Error;
    }

    /* --- 2. Attributes & Scalars --- */
    attribute def MassValue :> Real;
    
    /* --- 3. Parts (Structure) --- */
    part def StorageTank {
        attribute capacity : MassValue = 1000.0;
        attribute currentStatus : Status = Status::Idle;
    }

    /* --- 4. Items (Flow/Substance) --- */
    item def Water;
    
    part def WaterSystem {
        part tank1 : StorageTank;
        part tank2 : StorageTank;
        
        /* Items flow or are stored */
        item storedWater : Water;
    }
}