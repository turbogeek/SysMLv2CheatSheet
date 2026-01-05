package Flows_Tutorial {
    private import ScalarValues::*;
    
    item def Fuel;
    
    part def Tank;
    part def Engine;
    
    part def FuelSystem {
        part t : Tank;
        part e : Engine;
        
        /* --- Explicit Item Flow --- */
        /* Declaring that Fuel moves from Tank to Engine */
        /* This implies a connection exists or is abstractly represented */
        flow of Fuel from t to e;
        
        /* --- Connector with Flow --- */
        connect t to e {
            /* Optional property on the flow */
            flow of Fuel from t to e {
                attribute rate : Real = 5.0;
            }
        }
    }
}