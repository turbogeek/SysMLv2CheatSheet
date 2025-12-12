package Metadata_4Standard {
    private import ScalarValues::*;
    private import SysML::*;
    
    doc /* Deprecation */
    part oldPart {
        @Deprecated;
    }
    
    metadata def FIXME;
    
    action check {
        @FIXME {
            doc /* Needs update */
        }
    }
}