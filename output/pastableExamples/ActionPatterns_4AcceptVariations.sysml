package ActionPatterns_4AcceptVariations {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        accept startSignal : StartSignal;
        comment about startSignal ...
        accept when temp > 100;
        accept at schedule;
        accept after 10 [s];
    }

    view ExposeExample {
        expose Main;
    }
}