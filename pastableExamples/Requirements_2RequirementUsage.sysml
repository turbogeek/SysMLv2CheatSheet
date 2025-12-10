package Requirements_2RequirementUsage {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    requirement req1 : Performance {
      doc /* Response < 10ms */
      id "REQ-001";
      maxResponse = 10 [ms];
    }
}