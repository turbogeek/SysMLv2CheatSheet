package Cases_2TestCaseVerification {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    verification def TestBrakes {
       verify brakeReq;
       objective {
          verify stoppingDistance;
       }
       return verdict : VerdictKind;
    }
}