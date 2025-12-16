package Naming_Tutorial {
    // --- Library Definitions ---
    package StandardLibrary {
        part def Widget;
        part def Gadget;
        attribute def Status;
    }
    
    package SpecializedLibrary {
        // Name collision with StandardLibrary
        part def Widget; 
    }

    // --- Imports & Aliasing ---
    // Public import: 'StandardLibrary' is visible to users of 'Naming_Tutorial'
    import StandardLibrary::*;
    
    // Private import: Resolving collision with alias
    private import SpecializedLibrary::Widget as SpecialWidget;

    // --- Definitions & Usages ---
    part def SystemContext {
        // Usage of standard import
        part standardPart : Widget;
        
        // Usage of aliased import
        part specialPart : SpecialWidget;
        
        // Escaped identifier for spaces
        attribute 'System ID' : String;
        
        // Correct Convention: camelCase usage
        part mainGadget : Gadget;
    }
}