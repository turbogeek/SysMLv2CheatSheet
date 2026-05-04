package Views {
    part def System;
    part mySystem : System; 
    view def ReportView { in part target_sys : System; }
    
    /* View Usage */
    view report : ReportView {
        in part target_sys = mySystem;
    }
}