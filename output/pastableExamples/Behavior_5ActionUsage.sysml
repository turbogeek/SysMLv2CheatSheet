package Behavior_5ActionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        action playPoint {
           action serve : Serve;
           perform serve {
              in speed = 60;
           }
        }
    }

    view ExposeExample {
        expose Main;
    }
}