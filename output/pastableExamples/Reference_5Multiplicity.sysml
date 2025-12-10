package Reference_5Multiplicity {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    [1] Exactly one
    [*] Zero or more
    [0..1] Optional
    ordered /* Sequence (indexed) */
    nonunique /* Allow duplicates */
    /* Defaults: */
    Part/Attr -> [1]
    Other -> [0..*]
}