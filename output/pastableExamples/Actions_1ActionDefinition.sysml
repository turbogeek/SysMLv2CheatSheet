package Actions_1ActionDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        action def Serve {
           in speed : Speed;
           out result : Result;
           first toss;
           then strike;
        }
    }

    view ExposeExample {
        expose Main;
    }
}