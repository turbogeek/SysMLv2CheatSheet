package ModifierTests;

part def Measurement {
    attribute rawValue : Real;
    
    // Readonly attribute
    readonly attribute timestamp : Real;
    
    // Derived attribute
    derived attribute calibratedValue : Real = rawValue * 1.05;
    
    // End feature
    end attribute finalValue : Real;
}

part def Container {
    // Ordered parts
    part ordered items[*];
    
    // Readonly part
    readonly part config;
}
