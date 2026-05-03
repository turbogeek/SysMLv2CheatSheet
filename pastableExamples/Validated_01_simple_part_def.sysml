/**
 * POSITIVE TEST: Simple part definition
 * EXPECTED: No errors
 * CATEGORY: Basic Structure
 */
package PositiveTests {
    private import ScalarValues::*;

    part def Vehicle {
        attribute mass : Real;
        attribute length : Real;
    }
}
