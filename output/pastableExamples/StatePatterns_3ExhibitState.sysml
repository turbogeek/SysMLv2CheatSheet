package StatePatterns_3ExhibitState {
    private import ScalarValues::*;
    private import SysML::*;
    package VehicleStates { state operating; }
    part def Vehicle {
       exhibit state opState
          references VehicleStates::operating;
    }
}