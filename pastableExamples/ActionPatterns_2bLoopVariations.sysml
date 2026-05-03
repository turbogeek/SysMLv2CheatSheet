package LoopVariationsExample {
    private import ScalarValues::*;
    attribute def Power;
    attribute profile : Power[*];
    action def Main {
        attribute x : Integer = 0;
        attribute done : Boolean = false;
        
        action collectionLoop {
            for p : Power in profile {
                /* body */
            }
        }
        
        action whileUntilLoop {
            while x < 10 {
                assign x := x + 1;
            } until done;
        }
        
        action infiniteLoop {
            loop {
               assign x := x + 1;
            } until x > 100;
        }
    }
    view LoopView {
        expose Main;
    }
}