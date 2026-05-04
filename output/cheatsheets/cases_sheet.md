# Cases Cheat Sheet

*Use Cases, Analysis, Verification*

## 1. Use Case Definition

Functional goals.

```sysml
package Cases_1UseCaseDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Vehicle;
    attribute def Person;
    /* Wrapped Snippet (Structure Context) */
    use   case   def  DriveCar  {
        subject  vehicle  :  Vehicle ;
        actor  driver  :  Person ;
        objective  {
           doc  /* Transport safely */
        }
    }
}
```

## 2. Test Case (Verification)

Verifying requirements.

```sysml
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
```

## 3. Analysis Case

Evaluating properties.

```sysml
package Cases_3AnalysisCase {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Vehicle;
    /* Wrapped Snippet (Structure Context) */
    analysis   def  FuelEconomy  {
       subject  vehicle  :  Vehicle ;
       objective  {
          doc  /* Estimate MPG */
       }
       return  mpg  :  Real ;
    }
}
```

## 4. Case Usage

Instantiating a case.

```sysml
package Cases_4CaseUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Vehicle; attribute def Person;
    use case def DriveCar { subject vehicle : Vehicle; actor driver : Person; }
    part me : Person;
    /* Wrapped Snippet (Structure Context) */
    use   case  driveToWork  :  DriveCar  {
       actor  driver  =  me ;
    }
}
```

