package Cases_2TestCaseVerification {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Vehicle;
    attribute def Person;
    attribute def VerdictKind;
    /* Wrapped Snippet (Structure Context) */
    requirement brakeReq;
    requirement stoppingDistance;
    verification   def  TestBrakes  {
       objective {
           verify  brakeReq ;
           verify  stoppingDistance ;
       }
       return  verdict  :  VerdictKind ;
    }
}