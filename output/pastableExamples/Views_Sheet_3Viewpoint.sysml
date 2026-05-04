package Views {
    /* 1. Define specific concern/perspective */
    viewpoint def SafetyAnalysis {
        doc /* Focus on hazards. */
    }
    
    /* 2. Create viewpoint usage */
    viewpoint <'vp1'> 'sa' : SafetyAnalysis;
    
    /* 3. Link view usage to viewpoint usage */
    view mySafetyView {
        satisfy 'sa';
    }
}