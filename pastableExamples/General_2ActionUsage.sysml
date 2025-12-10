package General_2ActionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        action playPoint {
           action serve : Serve;
           perform serve { ... }
           action serve2 : Serve;
           perform action serve2;
        }
    }

    view ExposeExample {
        expose Main;
    }
}