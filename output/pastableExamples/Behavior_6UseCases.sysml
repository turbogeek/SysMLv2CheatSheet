package Behavior_6UseCases {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        use case def Practice {
           subject b : PickleBot;
           actor p : Player;
           objective {
              doc /* Improve skills */
           }
        }
    }

    view ExposeExample {
        expose Main;
    }
}