package ActionPatterns_7AdvancedSend {
    private import ScalarValues::*;
    private import ScalarValues::*;
    private import SysML::*;
    private import Base::*;
    action def Main {
        attribute val : Anything;
        part monitor;
        action sendReading send {
           in payload;
           in sender = monitor;
        }
        flow val to sendReading.payload;
    }
    view ExposeExample { expose Main; }
}