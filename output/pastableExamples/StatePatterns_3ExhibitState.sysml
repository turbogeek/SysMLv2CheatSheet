package StatePatterns_3ExhibitState {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    part def Vehicle {
       exhibit state opState
          references VehicleStates::operating;
    }
}