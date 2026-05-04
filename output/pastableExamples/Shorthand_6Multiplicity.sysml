package Shorthand_6Multiplicity {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    part  many [*] ;  /* 0..* */
    part  one ;  /* 1..1 (Default) */
    part  opt [0..1] ;  /* 0..1 */
}