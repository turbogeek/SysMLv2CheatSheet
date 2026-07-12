package Symbols_4RangeAndCoalescing {
    private import ScalarValues::*;
    private import SysML::*;

    /* '..' for multiplicity range */
    part sensors [1..5];

    attribute status : String[0..1];
    /* '??' and '..' in expressions */
    attribute currentStatus = status ?? "Unknown";
    attribute rangeList = 1..10;
}