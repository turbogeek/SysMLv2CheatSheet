package ActionPatterns_6ControlNodes {
    private import ScalarValues::*;
    private import SysML::*;
    
    action def Main {
        /* 1. Fork: Outgoing target mult 1..1 */
        fork f1;
        
        /* 2. Join: Incoming source mult 1..1 */
        join j1;
        
        /* 3. Decide: Outgoing target mult 0..1 (Optional) */
        decide d1;
        
        /* 4. Merge: Incoming source mult 0..1 (Optional) */
        merge m1;
    }

    view ExposeExample {
        expose Main;
    }
}