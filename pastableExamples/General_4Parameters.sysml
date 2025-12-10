package General_4Parameters {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        action def ComputeValues {
           in x : Real;
           inout y : Real;
           return z : Real;
        }
    }

    view ExposeExample {
        expose Main;
    }
}