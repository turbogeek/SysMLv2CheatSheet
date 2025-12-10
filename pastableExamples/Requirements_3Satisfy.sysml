package Requirements_3Satisfy {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    part server {
      satisfy req1;
    }
    doc /* Or external: */
    satisfy server by req1;
}