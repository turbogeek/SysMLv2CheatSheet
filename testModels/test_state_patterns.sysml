package TestStatePatterns {
    action def tick;
    action check;
    state def Monitoring {
       state Idle;
       transition t1 first Idle accept tick do check then Idle;
    }
}
