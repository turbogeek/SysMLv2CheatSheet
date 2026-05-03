package Metadata_1Definition {
    private import ScalarValues::*;
    private import SysML::*;
    doc /* Define custom metadata (like a Stereotype) */
    metadata def Risk {
        attribute level : Integer;
        attribute desc : String;
    }
}