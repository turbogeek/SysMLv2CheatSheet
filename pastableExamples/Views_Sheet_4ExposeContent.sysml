package Views {
    part def Car { part engine; part wheels[4]; }
    part myCar : Car;
    
    view myView {
        /* Expose specific element */
        expose myCar;
        
        /* Expose element and all children recursively */
        expose myCar::**; 
    }
}