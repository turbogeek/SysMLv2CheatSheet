# Actions & Behavior

*Modeling Activity Diagrams*

## 1. Action Basics

Actions represent distinct steps of behavior.
• **action def**: A reusable definition.
• **action**: A usage (step).

## 2. Flows and Control

- **first**: Marks the starting action.
- **flow**: Explicit succession (`flow from a to b`).
- **then**: Shorthand succession (`a then b`).
- **fork/join**: Implicit when multiple flows leave or enter an action.

## 3. Processing Pipeline Example

```sysml
package Actions_Tutorial {
    private import ScalarValues::*;
    
    /* reusable action */
    action def LogStatus { in msg : String; }

    action def ProcessData {
        /* Defining steps */
        action step1;
        action step2;
        action step3;
        
        /* --- Control Flow --- */
        /* 'first' implies the entry point */
        first step1;
        
        /* 'then' implies succession (step1 completes before step2 starts) */
        flow from step1 to step2; /* explicit */
        
        /* Shorthand for flow: */
        /* step2 then step3;  */ 
        
        /* --- Parallelism --- */
        action branchA;
        action branchB;
        
        /* Forking: step3 triggers both branches */
        flow from step3 to branchA;
        flow from step3 to branchB;
        
        /* --- Using Definitions --- */
        action logger : LogStatus {
            in msg = "Processing Complete";
        }
        
        /* Joining: both must finish before logger runs */
        flow from branchA to logger;
        flow from branchB to logger;
    }
}
```

