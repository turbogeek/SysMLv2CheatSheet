package Naming_3Wildcards {
    package BigLibrary {
        package SubLib { part def InnerThing; }
        part def OuterThing;
    }
    
    // Imports only OuterThing, NOT InnerThing
    import BigLibrary::*; 
    
    // Imports OuterThing AND InnerThing (Recursive)
    // CAUTION: Can cause namespace pollution and conflicts
    // import BigLibrary::**; 
    
    part o : OuterThing;
    // part i : InnerThing; // Error if using *
}