package Naming_2Imports {
    package Lib {
        part def Tool;
    }
    
    // Public Import: Visible to importers of Naming_2Imports
    import Lib::*;
    
    // Private Import: Only visible inside this package
    private import ScalarValues::Boolean;
    
    part t : Tool;
    attribute isReady : Boolean;
}