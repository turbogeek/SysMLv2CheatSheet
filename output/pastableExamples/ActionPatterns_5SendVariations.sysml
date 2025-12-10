package ActionPatterns_5SendVariations {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        action sendA send startSignal via p1;
        send startSignal via p1;
        doc /* Named vs Unnamed */
    }

    view ExposeExample {
        expose Main;
    }
}