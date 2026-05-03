/**
 * POSITIVE TEST: Multiple parallel actions (no succession between them)
 * EXPECTED: No errors
 * CATEGORY: Action & Succession
 */
package PositiveTests {
    private import ScalarValues::*;

    attribute def Ingredient;

    action def PrepareBreakfast {
        action cookEggs {
            out eggs : Ingredient;
        }

        action toastBread {
            out toast : Ingredient;
        }

        action brewCoffee {
            out coffee : Ingredient;
        }

        // CORRECT: These can execute in parallel (no succession constraints)
        // They are not forced to be sequential

        action serve {
            in e = cookEggs.eggs;
            in t = toastBread.toast;
            in c = brewCoffee.coffee;
            out meal;
        }

        // CORRECT: Serve must come after all others complete
        first cookEggs then serve;
        first toastBread then serve;
        first brewCoffee then serve;
    }
}
