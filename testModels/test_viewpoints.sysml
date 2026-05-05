package TestViewpoints {
    part def Car { part engine; }
    
    viewpoint def MassReport {
        doc /* A report focusing only on mass properties. */
    }
    
    viewpoint <'VP-002'> 'mass report viewpoint' : MassReport {
        doc /* Focuses on mass properties of the vehicle */
    }
    
    view def MassView {
        in car : Car;
        expose car;
        expose car.engine;
    }
}
