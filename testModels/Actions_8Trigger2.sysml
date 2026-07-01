package Actions_8Trigger2 {
    private import ScalarValues::*;
    private import SysML::*;
    part systemX {
        perform action MainAction {
            action def Tick;
            item def Foo;
            part clock {
                port clocky;
                attribute time : Real;
                attribute x : Real;
            }
            attribute t : Real;
            accept ticky : Foo via systemX;
            accept when t > 10.0;
            doc /* Event trigger with guard */
            view MainActionView : DS_Views::SymbolicViews::afv;
        }
    }
    view ExposeExample {
        expose Actions_8Trigger2;
    }
}
