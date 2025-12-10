package Cases_3AnalysisCase {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    analysis def FuelEconomy {
       subject vehicle : Vehicle;
       objective {
          doc /* Estimate MPG */
       }
       return mpg : Real;
    }
}