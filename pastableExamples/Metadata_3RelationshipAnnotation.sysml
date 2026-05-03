package Metadata_3RelationshipAnnotation {
    private import ScalarValues::*;
    private import SysML::*;
    metadata def RefineData { attribute isRefine : Boolean; }
    requirement req1;
    requirement req2;
    
    doc /* Annotating a dependency */
    dependency from req2 to req1 {
        metadata RefineData {
            :>> isRefine = true;
        }
    }
}