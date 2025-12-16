package StateMachine_Tutorial {
    import ScalarValues::*;
    
    // Define the component containing the machine
    part def TrafficLight {
        // The machine behavior
        state def LightLogic {
             // Initial entry point
             entry; then Red;
             
             state Red {
                 // Transition after time
                 transition to Green after 20 [ISQ::s];
             }
             
             state Green {
                 transition to Yellow after 30 [ISQ::s];
             }
             
             state Yellow {
                 transition to Red after 5 [ISQ::s];
             }
        }
        
        // Usage of the machine
        state logic : LightLogic;
    }
}