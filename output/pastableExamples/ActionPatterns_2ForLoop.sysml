package ForLoopExample {
    import ScalarValues::*;
    action def Main {
        action process { in i : Integer; }
        action loopAction {
            for i in 1..10 {
                perform process(i);
            }
        }
    }
    view LoopView {
        expose Main;
    }
}