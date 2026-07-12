package Symbols_7AnnotationsAndClassification {
    private import ScalarValues::*;
    private import SysML::*;

    /* Declaring metadata annotation type */
    metadata def SafetyLevel {
        attribute level : Integer;
    }

    /* '@' applied as annotation */
    @SafetyLevel { level = 1; }
    part safePart;

    attribute isSafeType = safePart @ Part; /* '@' used for Type test */
    attribute isSafeMeta = safePart @@ Part; /* '@@' used for Metaclass test */
}