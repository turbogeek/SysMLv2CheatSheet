package Symbols_1SpecializationAndSubsetting {
    private import ScalarValues::*;
    private import SysML::*;

    part def Vehicle;
    /* Definition Specialization */
    part def Car :> Vehicle;

    part def Garage {
        /* Usage Subsetting */
        part vehicles [*];
        part cars :> vehicles;
    }

    part myGarage : Garage {
        /* Usage Redefinition */
        part :>> cars [2..4];
    }
}