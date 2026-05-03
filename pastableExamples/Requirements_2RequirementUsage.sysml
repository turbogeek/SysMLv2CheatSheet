package Requirements_2RequirementUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Time;
    attribute ms;
    requirement def Performance { attribute maxResponse : Time; }
    requirement <'REQ-001'> 'Fast' : Performance {
      doc /* Response < 10ms */
      attribute maxResponse = 10 [ms];
    }
}