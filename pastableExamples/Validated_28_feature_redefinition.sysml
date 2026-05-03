package RedefinitionTests;

// Test feature redefinition, chains, and inverses

part def Vehicle {
    part engine;
    part wheels[4];
    attribute speed : Real;
}

part def Car :> Vehicle {
    // Redefine with more specific type
    part :>> engine : CarEngine;
    
    // Redefine with different multiplicity
    part :>> wheels[4];
    
    // Redefine attribute
    attribute :>> speed : Real = 120.0;
}

part def CarEngine {
    attribute horsepower : Real;
}

// Feature chains
connection def Connector {
    end source;
    end target;
}

connection def ChainedConnector :> Connector {
    end :>> source chains link1.output;
    end :>> target;
}

// Inverse relationships
connection def BidirectionalLink {
    end a;
    end b inverses a;
}
