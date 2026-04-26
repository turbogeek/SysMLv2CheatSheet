package Requirements_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Requirements --- */
    requirement def PerformanceReq {
        doc /* Textual description */
            "The system shall operate within performance limits.";
    }
    
    requirement <'REQ-101'> 'Breaking Distance' : PerformanceReq {
        doc /* The vehicle must stop within 50 meters from 100km/h. */
        /* Formal constraint */
        attribute maxDistance : Real = 50.0;
    }

    /* --- 2. Satisfaction (Design) --- */
    part def BrakeSystem;
    
    part brakes : BrakeSystem {
        /* Asserting that this part satisfies the requirement */
        satisfy 'Breaking Distance';
    }
    
    /* --- 3. Verification (Testing) --- */
    /* A case to test the requirement */
    verification def BrakeTest {
        /* The requirement being verified */
        subject req : PerformanceReq;
        
        /* The logic (action) of the test */
        action executeTest {
            /* ... test steps ... */
        }
    }
    
    /* Usage of validation */
    verification case test1 : BrakeTest {
        verify 'Breaking Distance';
    }
}