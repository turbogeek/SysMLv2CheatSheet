/**
 * POSITIVE TEST: Ports and connections
 * EXPECTED: No errors
 * CATEGORY: Ports & Connections
 */
package PositiveTests {
    private import ScalarValues::*;

    port def DataPort {
        attribute value : Real;
    }

    port def ~DataPort;  // Conjugated port

    part def Sensor {
        port output : DataPort;
    }

    part def Display {
        port input : ~DataPort;
    }

    part def System {
        part sensor : Sensor;
        part display : Display;

        connect sensor.output to display.input;
    }
}
