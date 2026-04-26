# Requirements

*Specifying and Verifying Needs*

## 1. Defining Requirements

Requirements capture the needs of the system. Note: Always use requirement usages for actual project requirements, and doc /* ... */ for shall statements.

```sysml
requirement <'REQ-ID'> 'Name' : RequirementType { doc /* Description */; }
```

## 2. Traceability

- **satisfy**: Asserting that a design element (part) meets a requirement.
- **verify**: Asserting that a test case (verification case) proves a requirement.
- **require constraint { ... }**: Adding formal constraints inside requirements. **CRITICAL**: Do NOT place a semicolon at the end of the constraint block.

## 3. Requirements Example

```sysml
package Requirements_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Requirements --- */
    requirement def PerformanceReq {
        doc /* Textual description */
            "The system shall operate within performance limits.";
    }
    
    requirement <'REQ-101'> 'Breaking Distance' : PerformanceReq {
        doc /* The vehicle must stop within 50 meters from 100km/h. */
        /* Formal attributes */
        attribute maxDistance : Real = 50.0;
        attribute actualDistance : Real;
        /* Formal constraint (CRITICAL: no semicolon after constraint block) */
        require constraint {
            actualDistance <= maxDistance
        }
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
```

