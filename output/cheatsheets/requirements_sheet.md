# Requirements Cheat Sheet

*Requirements and Verification*

## 1. Requirement Definition

Defining requirement types.

```sysml
package Requirements_1RequirementDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Time;
    requirement def Performance {
      doc /* The system shall be fast. */
      attribute maxResponse : Time;
    }
}
```

## 2. Requirement Usage

Specific requirement instances.

```sysml
package Requirements_2RequirementUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Time;
    attribute ms;
    requirement def Performance { attribute maxResponse : Time; }
    requirement req1 : Performance {
      doc /* Response < 10ms */
      attribute id = "REQ-001";
      attribute maxResponse = 10 [ms];
    }
}
```

## 3. Satisfy

Design meets requirement.

```sysml
package Requirements_3Satisfy {
    private import ScalarValues::*;
    private import SysML::*;
    requirement def Performance;
    requirement req1 : Performance;
    part server {
      satisfy req1;
    }
    /* satisfy req1 by server; // Alternative syntax */
}
```

## 4. Verify

Test case for requirement.

```sysml
package Requirements_4Verify {
    private import ScalarValues::*;
    private import SysML::*;
    requirement req1;
    verification def TestLatency {
      objective {
          verify req1;
      }
    }
}
```

## 5. Constraint Definition

Mathematical rules.

```sysml
package Requirements_5ConstraintDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute kg;
    constraint def CheckMass {
      in m : Mass;
      m <= 1000 [kg]
    }
}
```

## 6. Assertions

Applying constraints.

```sysml
package Requirements_6Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute kg;
    constraint def CheckMass { in m : Mass; m <= 1000[kg] }
    part car {
      attribute mass : Mass;
      assert constraint CheckMass {
        in m = mass;
      }
    }
}
```

## 7. Trace & Refine

Requirement relationships.

```sysml
package Requirements_7TraceRefine {
    private import ScalarValues::*;
    private import SysML::*;
    requirement req1;
    requirement old_doc_item;
    requirement req2 {
      doc /* Using dependency to represent relationships */
      dependency from req2 to req1;
      dependency from req2 to old_doc_item;
    }
}
```

