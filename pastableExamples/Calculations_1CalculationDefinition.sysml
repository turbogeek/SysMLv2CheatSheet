package Calculations_1CalculationDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Voltage;
    attribute def Current;
    attribute def Power;
    calc def PowerCalc {
       in v : Voltage;
       in i : Current;
       return p : Power = v * i;
    }
}