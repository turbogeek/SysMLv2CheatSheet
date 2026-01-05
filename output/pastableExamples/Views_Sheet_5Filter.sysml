package Views {
    import ScalarValues::*;
    part def Car;
    part myCar : Car;
    
    view myView {
        expose myCar::**;
        
        /* Keep only Parts */
        filter @Part;
        
        /* Or exclude specific things (logic depends on library) */
    }
}