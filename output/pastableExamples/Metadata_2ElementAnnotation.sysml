package Metadata_2ElementAnnotation {
    private import ScalarValues::*;
    private import SysML::*;
    metadata def Risk { attribute level : Integer; attribute desc : String = ""; }
    
    doc /* Usage within element */
    part engine {
        metadata Risk {
            :>> level = 5;
            :>> desc = "Overheat potential";
        }
    }
    
    doc /* Shorthand annotation nested in definition */
    part wheel {
        @Risk { :>> level = 1; }
    }
}