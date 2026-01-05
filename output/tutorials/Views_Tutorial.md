# Views

*Visualizing the Model*

## 1. Views Concept

Views provide a way to visualize and present the model. They do not change the model structure but 'expose' parts of it in specific formats (Diagrams, Tables).

## 2. Common View Types

- **SymbolicViews::gv**: Graphical View (Diagram).
- **TabularViews::gt**: Generic Table.
- **TabularViews::rt**: Requirements Table.

## 3. Views Example

```sysml
package Views_Tutorial {
    /* Import Cameo View Libraries */
    private import DS_Views::SymbolicViews;
    private import CustomTabularViews::*;
    
    part def Car;
    part def Engine;
    part def Wheel;
    
    part myCar : Car {
        part engine : Engine;
        part wheels [4] : Wheel;
    }
    
    /* --- 1. Graphical View (Diagram) --- */
    view carDiagram : SymbolicViews::gv {
        /* Show the entire car structure */
        expose myCar;
        
        /* You can filter or refine what is shown here */
        /* (See Filters Tutorial) */
    }
    
    /* --- 2. Tabular View (Table) --- */
    /* Defining a reusable table structure */
    view def PartTable :> TabularViews::gt {
        /* Define columns */
        render rendering :>> asTable {
            view :>> 'Declared Name';
            view :>> 'Owner';
        }
    }
    
    /* Using the table */
    view myTable : PartTable {
        /* Show everything under myCar recursively */
        expose myCar::**;
    }
}
```

