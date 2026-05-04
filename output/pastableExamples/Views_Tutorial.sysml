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