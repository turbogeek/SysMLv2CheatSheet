package Views_Tutorial {
    /* Import Cameo View Libraries */
    private import DS_Views::SymbolicViews;
    private import DS_Views::TabularViews;
    private import SysML::Systems::*;
    
    package <BV> BaseViews {
        view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @PartDefinition;
            filter @PartUsage;
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