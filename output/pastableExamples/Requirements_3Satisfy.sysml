package Requirements_3Satisfy {
    private import ScalarValues::*;
    private import SysML::*;
    requirement def Performance;
    requirement req1 : Performance;
    part server {
      satisfy req1;
    }
    /* satisfy req1 by server; */
}