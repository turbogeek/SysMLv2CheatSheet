package StateMachine_Tutorial {
    private import SI::s;
    
    /* Define the component containing the machine */
    part def TrafficLight {
        /* Local actions defined in part scope can access part attributes */
        action def LogStatus;
        
        /* The machine behavior */
        state def LightLogic {
            /* Initial entry point */
            entry;
            then Red;
            
            state Red;
            state Yellow;
            state Green;
            
            transition redToGreen first Red accept after 20 [SI::s] then Green;
            transition greenToYellow first Green accept after 5 [SI::s] then Yellow;
            /* Using if-guard and do-action */
            transition yellowToRed first Yellow accept after 30 [SI::s] if true do action log : LogStatus then Red;
        }
        /* Usage of the machine */
        state logic : LightLogic;
    }
    view StateMachine_Tutorial : DS_Views::SymbolicViews::gv;
}