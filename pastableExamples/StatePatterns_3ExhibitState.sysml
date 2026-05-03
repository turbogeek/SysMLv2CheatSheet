package StatePatterns_3ExhibitState {
    private import ScalarValues::*;
    private import SysML::*;
    state def VehicleStates { state operating; }
    part def Vehicle {
       exhibit state opState : VehicleStates;
    }
}