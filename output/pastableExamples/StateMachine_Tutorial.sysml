package StateMachine_Tutorial {
    private import SI::s;
    
    /* Define the component containing the machine */
    part def TrafficLight {
        /* The machine behavior */
        state def LightLogic {
            /* Initial entry point */
            entry;
            then Red;
            
            state Red;
            state Yellow;
            state Green;
            
            transition Red accept after 20 [SI::s] then Green;
            transition Green accept after 5 [SI::s] then Yellow;
            transition Yellow accept after 30 [SI::s] then Red;
        }
        /* Usage of the machine */
        state logic : LightLogic;
    }
    view StateMachine_Tutorial : DS_Views::SymbolicViews::gv;
}