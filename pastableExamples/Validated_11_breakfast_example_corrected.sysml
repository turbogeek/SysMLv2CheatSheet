/**
 * Breakfast Preparation Example - CORRECTED
 * Demonstrates CORRECT SysML v2 succession-based action flow
 *
 * CORRECTIONS MADE:
 * - Removed invalid action modifier keywords
 * - Added proper succession statements using 'first...then' pattern
 * - Used state machines for conditional logic
 * - All actions can execute in parallel unless succession constraints defined
 */

package BreakfastExample {
    private import ScalarValues::*;

    /**
     * Simple data type definitions
     */
    attribute def Ingredient {
        doc /* Represents a food ingredient */
    }

    attribute def Meal {
        doc /* Represents a complete prepared meal */
    }

    /**
     * Basic breakfast preparation with succession-based flow
     */
    action def MakeBreakfast {
        doc /* Prepare a complete breakfast with eggs, toast, and coffee */

        // Input items
        in eggs : Ingredient;
        in bread : Ingredient;
        in coffeeGrounds : Ingredient;
        in water : Ingredient;

        // Output
        out breakfast : Meal;

        // Sub-actions with compact flow notation
        action crackEggs {
            in rawEggs = eggs;
            out crackedEggs : Ingredient;
        }

        action cookEggs {
            in preparedEggs = crackEggs.crackedEggs;  // Compact flow
            out scrambledEggs : Ingredient;
        }

        action toastBread {
            in slicedBread = bread;
            out toast : Ingredient;
        }

        action brewCoffee {
            in grounds = coffeeGrounds;
            in hotWater = water;
            out coffee : Ingredient;
        }

        action plateFood {
            in eggs = cookEggs.scrambledEggs;
            in toastedBread = toastBread.toast;
            in brewedCoffee = brewCoffee.coffee;
            out completeMeal = breakfast;
        }

        // CORRECT: Define succession ordering
        first crackEggs then cookEggs;
        first cookEggs then plateFood;
        first toastBread then plateFood;
        first brewCoffee then plateFood;

        view 'MakeBreakfast action flow' : DS_Views::SymbolicViewsByExpression::ActionsNestedView {
            expose MakeBreakfast::**;
            render asDefault;
        }
    }

    /**
     * Parallel breakfast preparation
     * CORRECTED: Actions execute in parallel by default unless constrained by successions
     */
    action def MakeBreakfastParallel {
        doc /* Prepare breakfast - parallel tasks have no succession constraints between them */

        in ingredients : Ingredient[4];
        out meal : Meal;

        // These actions CAN execute in parallel (no succession constraints between them)
        action cookProtein {
            in eggs = ingredients#(0);
            out protein : Ingredient;
        }

        action cookCarbs {
            in bread = ingredients#(1);
            out carbs : Ingredient;
        }

        action makeBeverage {
            in coffee = ingredients#(2);
            in water = ingredients#(3);
            out beverage : Ingredient;
        }

        // Final action combines results
        action combine {
            in p = cookProtein.protein;
            in c = cookCarbs.carbs;
            in b = makeBeverage.beverage;
            out completeMeal = meal;
        }

        // CORRECT: Only define successions where ordering matters
        // The cooking actions can run in parallel
        // But combine must wait for all of them
        first cookProtein then combine;
        first cookCarbs then combine;
        first makeBeverage then combine;

        view 'MakeBreakfastParallel action flow' : DS_Views::SymbolicViewsByExpression::ActionsNestedView {
            expose MakeBreakfastParallel::**;
            render asDefault;
        }
    }

    /**
     * Breakfast with cooking choices based on preferences
     * CORRECTED: Use state machine for conditional logic
     */
    action def MakeBreakfastWithChoices {
        doc /* Breakfast with cooking choices using state-based logic */

        in preference : String;
        in ingredients : Ingredient[5];
        out meal : Meal;

        // First action
        action checkPreference {
            in pref = preference;
            out eggStyle : String;
            out breadType : String;
        }

        // CORRECT: Use state machine for decision logic
        state def EggCookingDecision {
            in style : String;

            state scramble {
                entry action scrambleEggs {
                    out cookedEggs : Ingredient;
                }
            }

            state fry {
                entry action fryEggs {
                    out cookedEggs : Ingredient;
                }
            }

            transition toScramble
                first start
                if (style == "scrambled")
                then scramble;

            transition toFry
                first start
                if (style == "fried")
                then fry;

            view 'EggCookingDecision state machine' : DS_Views::SymbolicViewsByExpression::StatesNestedView {
                expose EggCookingDecision::**;
                render asDefault;
            }
        }

        // Toast preparation
        action toastBread {
            in bread = ingredients#(1);
            in toastLevel = checkPreference.breadType;
            out toast : Ingredient;
        }

        // Combine results
        action serveMeal {
            in toast = toastBread.toast;
            out completeMeal = meal;
        }

        // Define successions
        first checkPreference then serveMeal;
        first toastBread then serveMeal;

        view 'MakeBreakfastWithChoices action flow' : DS_Views::SymbolicViewsByExpression::ActionsNestedView {
            expose MakeBreakfastWithChoices::**;
            render asDefault;
        }
    }

    /**
     * Ultra-compact example with minimal syntax
     */
    action def QuickBreakfast {
        doc /* Quick breakfast preparation with succession-based flow */

        in eggs : Ingredient;
        in bread : Ingredient;
        out meal : Meal;

        action crack {
            in e = eggs;
            out c : Ingredient;
        }

        action cook {
            in c = crack.c;
            out s : Ingredient;
        }

        action toast {
            in b = bread;
            out t : Ingredient;
        }

        action serve {
            in s = cook.s;
            in t = toast.t;
            out m = meal;
        }

        // CORRECT: Define succession ordering
        first crack then cook;
        first cook then serve;
        first toast then serve;

        view 'QuickBreakfast action flow' : DS_Views::SymbolicViewsByExpression::ActionsNestedView {
            expose QuickBreakfast::**;
            render asDefault;
        }
    }

    /**
     * Example usage of breakfast actions
     */
    package BreakfastUsageExamples {

        // Usage instance 1: Basic breakfast
        action basicBreakfast : MakeBreakfast {
            doc /* Prepare a standard breakfast */
            view 'basicBreakfast usage' : DS_Views::SymbolicViewsByExpression::ActionsNestedView {
                expose basicBreakfast::**;
                render asDefault;
            }
        }

        // Usage instance 2: Parallel cooking
        action parallelBreakfast : MakeBreakfastParallel {
            doc /* Prepare breakfast with parallel tasks */
            view 'parallelBreakfast usage' : DS_Views::SymbolicViewsByExpression::ActionsNestedView {
                expose parallelBreakfast::**;
                render asDefault;
            }
        }

        // Usage instance 3: Customized breakfast
        action customBreakfast : MakeBreakfastWithChoices {
            doc /* Prepare breakfast based on user preferences */
            view 'customBreakfast usage' : DS_Views::SymbolicViewsByExpression::ActionsNestedView {
                expose customBreakfast::**;
                render asDefault;
            }
        }

        // Usage instance 4: Quick breakfast
        action quickBreakfast : QuickBreakfast {
            doc /* Prepare a quick breakfast */
            view 'quickBreakfast usage' : DS_Views::SymbolicViewsByExpression::ActionsNestedView {
                expose quickBreakfast::**;
                render asDefault;
            }
        }

        view 'BreakfastUsageExamples overview' : DS_Views::SymbolicViewsByExpression::ActionsTreeView {
            expose BreakfastUsageExamples::**;
            render asDefault;
        }
    }

    view 'BreakfastExample package overview' : DS_Views::SymbolicViews::gv {
        expose BreakfastExample::**;
        render asDefault;
    }
}
