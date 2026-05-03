/**
 * POSITIVE TEST: Part specialization (inheritance)
 * EXPECTED: No errors
 * CATEGORY: Specialization
 */
package PositiveTests {
    private import ScalarValues::*;

    part def Vehicle {
        attribute mass : Real;
        attribute wheelCount : Integer;
    }

    part def Car :> Vehicle {
        attribute :>> wheelCount = 4;
        attribute doors : Integer;
    }

    part def Truck :> Vehicle {
        attribute :>> wheelCount = 18;
        attribute cargoCapacity : Real;
    }
}
