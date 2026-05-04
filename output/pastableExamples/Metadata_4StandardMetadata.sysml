package Metadata_4Standard {
    private import ScalarValues::*;
    private import SysML::*;
    
    metadata def Deprecated;
    
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