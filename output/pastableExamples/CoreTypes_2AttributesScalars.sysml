package CoreTypes_2Attributes {
    // 1. Define the Scalar (Primitive Type)
    scalar def Kilogram;
    
    // 2. Define the Attribute Concept (Property)
    attribute def Mass {
        attribute val : Kilogram;
    }
    
    part def Rocket;
    
    part myRocket : Rocket {
        // 3. Use the Attribute
        attribute dryMass : Mass = 5000;
        
        // Or simple usage with standard types
        attribute name : String = "Falcon";
    }
}