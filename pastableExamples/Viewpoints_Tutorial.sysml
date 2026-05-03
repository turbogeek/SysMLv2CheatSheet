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
        doc "A report focusing only on mass properties.";
    }
    
    /* --- 2. Viewpoint Usage --- */
    viewpoint <'VP-002'> 'mass report viewpoint' : MassReport {
        doc "Focuses on mass properties of the vehicle";
    }
    
    /* --- 3. View Definition --- */
    view def MassView {
        /* The subject being viewed */
        in car : Car;
        
        /* --- 4. Exposing Elements --- */
        /* Show the car itself */
        expose car;
        
        /* Show sub-parts */
        expose car.engine;
        
        /* Filter: Only show attributes ending in 'Mass' (conceptual) */
        /* filter @Attribute ==> name.endsWith("sw") */
    }
    
    /* --- 5. View Usage --- */
    part myCar : Car;
    
    view report : MassView {
        in car = myCar;
        satisfy 'mass report viewpoint';
    }
}