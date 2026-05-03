/**
 * POSITIVE TEST: Action with proper succession syntax
 * EXPECTED: No errors
 * CATEGORY: Action & Succession
 */
package PositiveTests {
    private import ScalarValues::*;

    action def DriveVehicle {
        action start {
            out ignitionOn : Boolean;
        }

        action accelerate {
            in ready;
            out speed : Real;
        }

        // CORRECT: Use 'first...then' for succession
        first start then accelerate;
    }
}
