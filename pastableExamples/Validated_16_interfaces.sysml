package Interfaces {
    view 'power adapter to device' : DS_Views::SymbolicViews::gv;
    interface def 'TypeA to TypeC' {
        part converter {
            port a1;
            port a12;
            port b1;
            port b12;
            port pin1;
            port pin3;
            port pin2;
            port pin4;
            port a4;
            port b4;
            port a9;
            port b9;
            interface a1 to pin4;
            interface a12 to pin4;
            interface b1 to pin4;
            interface b12 to pin4;
            interface a4 to pin1;
            interface b4 to pin1;
            port a6;
            port a7;
            interface a6 to pin3;
            interface a7 to pin2;
        }
        end usbA : 'USB-A';
        end usbC : 'USB-C';
        interface converter.pin4 to usbA.pin4;
        interface converter.pin1 to usbA.pin1;
        interface converter.pin3 to usbA.pin3;
        interface converter.pin2 to usbA.pin2;
        view 'typeA to typeC interface definition' : DS_Views::SymbolicViews::gv;
        interface usbC.a1 to converter.a1;
        interface usbC.a12 to converter.a12;
        interface usbC.b1 to converter.b1;
        interface usbC.b12 to converter.b12;
        interface usbC.a4 to converter.a4;
        interface usbC.b4 to converter.b4;
        interface usbC.a9 to converter.a9;
        interface usbC.b9 to converter.b9;
        interface usbC.a6 to converter.a6;
        interface usbC.a7 to converter.a7;
    }
    part system {
        part 'power adapter' {
            port usbA : 'USB-A';
        }
        part device {
            port usbC : 'USB-C';
        }
        interface : 'TypeA to TypeC' connect 'power adapter'.usbA to device.usbC;
    }
    port def 'USB-A' {
        port pin4;
        port pin1;
        port pin2;
        port pin3;
    }
    port def 'USB-C' {
        port a1;
        port a12;
        port b1;
        port b12;
        port a4;
        port b4;
        port a9;
        port b9;
        port a6;
        port a7;
    }
    view interfaces : DS_Views::SymbolicViews::gv;
}
