/**
 * POSITIVE TEST: State machine with transitions
 * EXPECTED: No errors
 * CATEGORY: State Machines
 */
package PositiveTests {
    private import ScalarValues::*;

    state def TrafficLightStates {
        entry; then red;

        state red;
        state yellow;
        state green;

        transition red_to_green
            first red
            then green
            when after(30);

        transition green_to_yellow
            first green
            then yellow
            when after(45);

        transition yellow_to_red
            first yellow
            then red
            when after(5);
    }
}
