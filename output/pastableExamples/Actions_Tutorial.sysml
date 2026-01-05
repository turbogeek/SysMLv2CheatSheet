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