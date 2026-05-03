/**
 * POSITIVE TEST: Requirement with constraint
 * EXPECTED: No errors
 * CATEGORY: Requirements
 */
package PositiveTests {
    private import ScalarValues::*;

    part def Vehicle {
        attribute maxSpeed : Real;
    }

    requirement def SpeedLimit {
        subject vehicle : Vehicle;

        require constraint {
            vehicle.maxSpeed <= 120.0
        }
    }

    part myCar : Vehicle {
        attribute :>> maxSpeed = 100.0;
        satisfy SpeedLimit by myCar;
    }
}
