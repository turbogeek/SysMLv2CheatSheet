package Views {
    /* 1. Define specific concern/perspective */
    viewpoint def SafetyAnalysis {
        doc "Focus on hazards.";
    }
    
    /* 2. Link view to viewpoint */
    view def SafetyView {
        satisfies SafetyAnalysis;
    }
}