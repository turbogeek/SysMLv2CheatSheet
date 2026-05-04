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