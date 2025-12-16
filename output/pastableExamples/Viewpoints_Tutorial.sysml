package Viewpoint_Tutorial {
    import ScalarValues::*;
    
    // The subject
    part def Car {
        attribute mass : Real;
        part engine;
        part wheels;
    }
    
    // --- 1. Viewpoint Definition ---
    viewpoint def MassReport {
        doc "A report focusing only on mass properties.";
    }
    
    // --- 2. View Definition ---
    view def MassView {
        // The subject being viewed
        in car : Car;
        
        // --- 3. Exposing Elements ---
        // Show the car itself
        expose car;
        
        // Show sub-parts
        expose car.engine;
        
        // Filter: Only show attributes ending in 'Mass' (conceptual)
        // filter @Attribute ==> name.endsWith("sw")
    }
    
    // --- 4. View Usage ---
    part myCar : Car;
    
    view report : MassView {
        in car = myCar;
    }
}