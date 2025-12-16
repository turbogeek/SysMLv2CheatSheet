# State Machines

*States, Transitions, and Events*

## 1. State Machine Concepts

State machines define event-driven behavior. A system exists in a 'state' until an event triggers a 'transition'.

## 2. Key Syntax

- **state def**: Defines the state machine structure.
- **entry/do/exit**: Actions associated with a state.
- **transition to <state>**: Defines the next state.
- **accept <event>** / **after <time>**: Triggers for transitions.

## 3. Traffic Light Example

```sysml
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
```

