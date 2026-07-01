# Views

*Visualizing the Model*

## 1. Views Concept

Views provide a way to visualize and present the model. They do not change the model structure but 'expose' parts of it in specific formats (Diagrams, Tables).

## 2. Common View Types

- **SymbolicViews::gv**: Graphical View (Diagram).
- **TabularViews::gt**: Generic Table.
- **TabularViews::rt**: Requirements Table.
- **CRITICAL**: When filtering for allocations or satisfies, filter by the usage (e.g., `@AllocationUsage`), not the definition (e.g., `@Allocation`).

## 3. Views Example

```sysml
package Views_Tutorial {
    /* Standard sysml library imports */
    private import SysML::*;
    
    /* Mock Cameo View elements for standard validation */
    package SymbolicViews { view def gv; }
    package TabularViews { view def gt; }
    view def TreeView;
    view def rt;
    action def EssentialElementsFilter;
    action def NonStandardLibraryElementFilter;
    
    package <BV> BaseViews {
        view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
            /* filter elements */
        }
        view allocationTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
            /* filter elements */
        }
    }

    part def Car;
    part def Engine;
    part def Wheel;
    
    part myCar : Car {
        part engine : Engine;
        part wheels [4] : Wheel;
    }
    
    /* --- 1. Graphical View (Diagram) --- */
    view carDiagram : SymbolicViews::gv, EssentialElementsFilter, NonStandardLibraryElementFilter {
        /* Show the entire car structure */
        expose myCar;
        
        /* You can filter or refine what is shown here */
        /* (See Filters Tutorial) */
    }
    
    /* --- 2. Tabular View (Table) --- */
    /* Defining a reusable table structure */
    view def PartTable :> TabularViews::gt {
        /* Define columns */
        render rendering asTable {
            /* table columns definition goes here */
        }
    }
    
    /* Using the table */
    view myTable : PartTable {
        /* Show everything under myCar recursively */
        expose myCar::**;
    }
}
```

