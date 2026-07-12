package Symbols_2TypingAndNamespace {
    private import ScalarValues::*;
    private import SysML::*;

    /* Namespace qualification using '::' */
    attribute x : ISQ::mass;

    action def ProcessEvent {
        /* Trigger parameter binding using ':' */
        accept e : Event;
    }
}