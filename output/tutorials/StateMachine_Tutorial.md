# State Machines

*States, Transitions, and Events*

## 1. State Machine Concepts

State machines define event-driven behavior. A system exists in a 'state' until an event triggers a 'transition'.

## 2. Key Syntax

- **state def**: Defines the state machine structure.
- **entry/do/exit**: Actions associated with a state.
- **transition first <source> accept <trigger> if <guard> do <action> then <target>**: Full transition syntax.
- **Rule**: Guards must use `if`, not `where`.
- **Rule**: A transition can only have ONE source state. You cannot use `or` in the `first` clause.
- **Rule**: Actions used inside a state machine (e.g. `do action`) should be defined in the surrounding part so they can access the part's attributes.

## 3. Traffic Light Example

```sysml
package StateMachine_Tutorial {
    private import SI::s;
    
    /* Define the component containing the machine */
    part def TrafficLight {
        /* Local actions defined in part scope can access part attributes */
        action def LogStatus;
        
        /* The machine behavior */
        state def LightLogic {
            /* Initial entry point */
            entry;
            then Red;
            
            state Red;
            state Yellow;
            state Green;
            
            transition redToGreen first Red accept after 20 [SI::s] then Green;
            transition greenToYellow first Green accept after 5 [SI::s] then Yellow;
            /* Using if-guard and do-action */
            transition yellowToRed first Yellow accept after 30 [SI::s] if true do action log : LogStatus then Red;
        }
        /* Usage of the machine */
        state logic : LightLogic;
    }
    view StateMachine_Tutorial : DS_Views::SymbolicViews::gv;
}
```

