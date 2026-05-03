package Requirements_7TraceRefine {
    private import ScalarValues::*;
    private import SysML::*;
    requirement req1;
    requirement old_doc_item;
    requirement req2 {
      doc /* Using dependency to represent relationships */
      dependency from req2 to req1;
      dependency from req2 to old_doc_item;
    }
}