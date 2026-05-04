package Patterns_1MetadataAnnotations {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    metadata   def  Status  {
      attribute  priority  :  Integer ;
      attribute  approved  :  Boolean ;
    }
    part  myPart  {
      metadata  Status  {
        priority  =  1 ;
      }
    }
}