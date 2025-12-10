package Calculations_6Requirements {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    requirement def Safety {
       assume constraint { temp < 100 }
       require constraint { pressure < 50 }
    }
}