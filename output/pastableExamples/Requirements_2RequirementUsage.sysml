package Requirements_2RequirementUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Time;
    attribute ms;
    requirement def Performance { attribute maxResponse : Time; }
    requirement req1 : Performance {
      doc /* Response < 10ms */
      attribute id = "REQ-001";
      attribute maxResponse = 10 [ms];
    }
}