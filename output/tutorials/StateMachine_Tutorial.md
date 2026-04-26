# State Machines

*States, Transitions, and Events*

## 1. State Machine Concepts

State machines define event-driven behavior. A system exists in a 'state' until an event triggers a 'transition'.

## 2. Key Syntax

- **state def**: Defines the state machine structure.
- **entry/do/exit**: Actions associated with a state.
- **transition <source> accept <trigger> then <target>**: Defines a transition between states.
- **accept <event>** / **after <time>**: Triggers for transitions.

## 3. Traffic Light Example

```sysml
package StateMachine_Tutorial {
    private import SI::s;
    
    /* Define the component containing the machine */
    part def TrafficLight {
        /* The machine behavior */
        state def LightLogic {
            /* Initial entry point */
            entry;
            then Red;
            
            state Red;
            state Yellow;
            state Green;
            
            transition Red accept after 20 [SI::s] then Green;
            transition Green accept after 5 [SI::s] then Yellow;
            transition Yellow accept after 30 [SI::s] then Red;
        }
        /* Usage of the machine */
        state logic : LightLogic;
    }
    view StateMachine_Tutorial : DS_Views::SymbolicViews::gv;
}
```

