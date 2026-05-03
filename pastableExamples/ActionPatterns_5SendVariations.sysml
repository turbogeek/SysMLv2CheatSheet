package ActionPatterns_5SendVariations {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        action def StartSignal;
        part p1;
        attribute sig : StartSignal;
        action sendA { send sig via p1; }
        send sig via p1;
        doc /* Named vs Unnamed */
    }
    view ExposeExample { expose Main; }
}