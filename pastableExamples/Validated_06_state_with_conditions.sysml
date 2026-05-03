/**
 * POSITIVE TEST: State transitions with conditional guards
 * EXPECTED: No errors
 * CATEGORY: State Machines
 */
package PositiveTests {
    private import ScalarValues::*;

    state def Engine {
        in fuelLevel : Real;

        state off;
        state running;

        transition start
            first off
            if (fuelLevel > 0)  // CORRECT: 'if' in transition, not in 'action if'
            then running;

        transition stop
            first running
            then off;
    }
}
