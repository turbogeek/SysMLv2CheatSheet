package Views {
    part def System;
    part mySystem : System; 
    view def ReportView { in subject : System; }
    
    /* View Usage */
    view report : ReportView {
        in subject = mySystem;
    }
}