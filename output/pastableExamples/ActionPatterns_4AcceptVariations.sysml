package ActionPatterns_4AcceptVariations {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute temp : Real;
        attribute s : Real;
        part schedule;
        action def StartSignal;
        action acceptSomething {
            accept startSignal : StartSignal;
            doc /* about startSignal ... */
            accept when temp > 100;
            accept at schedule;
            accept after 10 [s];
        }
    }
    view ExposeExample { expose Main; }
}