package Actions_2ActionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    action def Serve;
    action def Main {
        action playPoint {
           action serve : Serve;
           perform serve { /* ... */ }
           action serve2 : Serve;
           perform serve2;
        }
    }
    view ExposeExample { expose Main; }
}