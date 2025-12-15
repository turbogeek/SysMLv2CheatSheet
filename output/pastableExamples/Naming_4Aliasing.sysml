package Naming_4Aliasing {
    package LibA { part def Widget; }
    package LibB { part def Widget; }
    
    // Conflict resolution
    import LibA::Widget as A_Widget;
    import LibB::Widget as B_Widget;
    
    part w1 : A_Widget;
    part w2 : B_Widget;
}