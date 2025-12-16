# Requirements

*Specifying and Verifying Needs*

## 1. Defining Requirements

Requirements capture the needs of the system.

```sysml
requirement <id> 'Name' { doc "Description"; }
```

## 2. Traceability

- **satisfy**: Asserting that a design element (part) meets a requirement.
- **verify**: Asserting that a test case (verification case) proves a requirement.
- **refine**: Decomposing a requirement into lower-level details.

## 3. Requirements Example

```sysml
package Requirements_Tutorial {
    import ScalarValues::*;
    
    // --- 1. Requirements ---
    requirement def PerformanceReq {
        doc /* Textual description */
            "The system shall operate within performance limits.";
    }
    
    requirement <101> 'Breaking Distance' : PerformanceReq {
        doc "The vehicle must stop within 50 meters from 100km/h.";
        // Formal constraint
        attribute maxDistance : Real = 50.0;
    }

    // --- 2. Satisfaction (Design) ---
    part def BrakeSystem;
    
    part brakes : BrakeSystem {
        // Asserting that this part satisfies the requirement
        satisfy 'Breaking Distance';
    }
    
    // --- 3. Verification (Testing) ---
    // A case to test the requirement
    verification def BrakeTest {
        // The requirement being verified
        subject req : PerformanceReq;
        
        // The logic (action) of the test
        action executeTest {
            // ... test steps ...
        }
    }
    
    // Usage of validation
    verification case test1 : BrakeTest {
        verify 'Breaking Distance';
    }
}
```

