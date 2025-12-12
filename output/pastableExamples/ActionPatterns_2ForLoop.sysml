package ForLoopExample {
    private import ScalarValues::*;
    action def Main {
        action process { in i : Integer; }
        action loopAction {
            for i in 1..10 {
                perform process { in i = i; }
            }
        }
    }
    view LoopView {
        expose Main;
    }
}