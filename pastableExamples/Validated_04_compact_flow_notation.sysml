/**
 * POSITIVE TEST: Compact flow notation (binding expressions)
 * EXPECTED: No errors
 * CATEGORY: Action & Flow
 */
package PositiveTests {
    private import ScalarValues::*;

    attribute def Data;

    action def ProcessData {
        action collect {
            out rawData : Data;
        }

        action transform {
            in input = collect.rawData;  // CORRECT: Compact flow notation
            out processed : Data;
        }

        action store {
            in data = transform.processed;  // CORRECT: Compact flow notation
        }

        first collect then transform;
        first transform then store;
    }
}
