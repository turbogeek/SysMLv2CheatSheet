package Viewpoint_Tutorial {
    private import ScalarValues::*;
    
    /* The subject */
    part def Car {
        attribute mass : Real;
        part engine;
        part wheels;
    }
    
    /* --- 1. Viewpoint Definition --- */
    viewpoint def MassReport {
        doc /* A report focusing only on mass properties. */
    }
    
    /* --- 2. Viewpoint Usage --- */
    viewpoint <'VP-002'> 'mass report viewpoint' : MassReport {
        doc /* Focuses on mass properties of the vehicle */
    }
    
    /* --- 3. View Definition --- */
    view def MassView {
        /* The subject being viewed */
        in part car : Car;
    }
        
    /* --- 4. View Usage and Exposing Elements --- */
    part myCar : Car;
    
    view report : MassView {
        in part car = myCar;
        satisfy 'mass report viewpoint';
        
        /* Show the car itself */
        expose myCar;
        
        /* Show sub-parts using :: */
        expose myCar::engine;
    }
}