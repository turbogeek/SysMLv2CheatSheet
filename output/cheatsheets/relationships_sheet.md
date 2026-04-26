# Relationships Cheat Sheet

*Structural and Behavioral Relationships*

## 1. Taxonomy (Def vs Usage)

Specialization matches Definitions.

```sysml
package 'Example: Taxonomy (Def vs Usage)' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Taxonomy (Def vs Usage)' {
        part def Vehicle {
            doc /* Definitions use specialize */
        }
        part def Car :> Vehicle {
            part wheel;
        }
        part sedan : Car {
            doc /* Usages use redefines/subsets */
            part betterWheel :>> wheel;
        }
    }
    view 'View: 1. Taxonomy (Def vs Usage)' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Taxonomy (Def vs Usage)'::'Taxonomy (Def vs Usage)'::*;
    }
}
```

## 2. Structural Links

Connecting and Binding usages.

```sysml
package 'Example: Structural Links' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Structural Links' {
        part def 'Connection Examples' {
            part p1;
            part p2;
            connect p1 to p2;
            bind p1 = p2;
        }
    }
    view 'View: 2. Structural Links' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Structural Links'::'Structural Links'::*;
    }
}
```

## 3. Behavioral Flow

Successions (Time) vs Flows (Data).

```sysml
package 'Example: Behavioral Flow' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Behavioral Flow' {
        action def Process {
            action step1;
            action step2;
            first step1 then step2;
            attribute x : Integer;
            flow x from step1 to step2;
            view Process : DS_Views::SymbolicViews::afv;
            action __unnamed84 terminate;
            first start then step1;
            first step2 then __unnamed84;
        }
    }
    view 'View: 3. Behavioral Flow' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Behavioral Flow'::'Behavioral Flow'::**;
    }
}
```

## 4. Cross-Cutting

Traceability and Assertions.

```sysml
package 'Example: Cross-Cutting' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Cross-Cutting' {
        requirement r1;
        part p satisfy r1;
        
        part abstractPart;
        part concretePart;
        
        refine abstractPart to concretePart;
        
        verification def Test;
        verification v1 : Test {
            subject p;
            objective {
                verify r1;
            }
        }
    }
    view 'View: 4. Cross-Cutting' {
        expose 'Example: Cross-Cutting'::'Cross-Cutting'::*;
    }
}
```

## 5. Import & Exposure

Managing namespace visibility.

```sysml
package 'Example: Import & Exposure' {
    private import ScalarValues::*;
    private import SysML::*;
    package P1 {
        part def A;
        part def B;
    }
    package P2 {
        private import P1::A;
        public import P1::B;
        alias MyA for A;
        part thing : A;
        part otherThing : B;
    }
    view 'View: 5. Import & Exposure' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Import & Exposure'::**;
    }
}
```

