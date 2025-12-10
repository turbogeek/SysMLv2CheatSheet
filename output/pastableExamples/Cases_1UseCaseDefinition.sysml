package Cases_1UseCaseDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    use case def DriveCar {
       subject vehicle : Vehicle;
       actor driver : Person;
       objective {
          doc /* Transport safely */
       }
    }
}