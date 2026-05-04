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