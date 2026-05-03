package BananaUnits {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def LengthUnit {
        attribute prefix;
        attribute referenceUnit;
    }
    attribute nano;
    attribute <nB> nanoBanana : LengthUnit {
        attribute unitConversion;
        :>> prefix = nano;
        :>> referenceUnit = "Standard Banana";
    }
}