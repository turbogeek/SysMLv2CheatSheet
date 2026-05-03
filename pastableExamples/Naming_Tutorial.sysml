package Naming_Tutorial {
    private import ScalarValues::*;
    
    /* --- Library Definitions --- */
    package StandardLibrary {
        part def Widget;
        part def Gadget;
        attribute def Status;
    }
    
    package SpecializedLibrary {
        /* Name collision with StandardLibrary */
        part def Widget; 
    }

    /* --- Imports & Aliasing --- */
    /* Public import: 'StandardLibrary' is visible to users of 'Naming_Tutorial' */
    /* Real-world example: The 'SI' library has 'public import ISQ::*;' */
    public import StandardLibrary::*;
    
    /* Private import: Resolving collision with alias */
    private import SpecializedLibrary::Widget as SpecialWidget;

    /* --- Definitions & Usages --- */
    part def SystemContext {
        /* Usage of standard import */
        part standardPart : Widget;
        
        /* Usage of aliased element */
        part specialPart : SpecialWidget;
        
        /* Using the alias defined in the package */
        alias SW for SpecialWidget;
        part anotherPart : SW;
        
        /* Escaped identifier for spaces */
        attribute 'System ID' : String;
        
        /* Correct Convention: camelCase usage */
        part mainGadget : Gadget;
        
        /* Unit reference uses brackets, no quotes needed for special chars */
        attribute speed : Real [km/h];
    }
}