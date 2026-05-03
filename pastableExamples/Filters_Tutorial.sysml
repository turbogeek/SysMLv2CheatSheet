package Filters_Tutorial {
    private import DS_Views::SymbolicViews;
    private import Metaobjects::SemanticMetadata;
    
    part def HardwareComponent;
    part def SoftwareComponent;
    
    metadata def Critical;
    
    part system {
        part cpu : HardwareComponent;
        
        @Critical
        part os : SoftwareComponent;
        
        part driver : SoftwareComponent;
    }
    
    /* --- 1. Filtering by Type --- */
    view hardwareView : SymbolicViews::gv {
        expose system::**;
        
        /* Only show HardwareComponents */
        filter hastype HardwareComponent;
    }
    
    /* --- 2. Filtering by Metadata (Stereotypes) --- */
    view criticalView : SymbolicViews::gv {
        expose system::**;
        
        /* Only show elements tagged as @Critical */
        filter @Critical;
    }
    
    /* --- 3. Complex Logic --- */
    view complexView : SymbolicViews::gv {
        expose system::**;
        
        /* Show Software that is NOT Critical */
        filter hastype SoftwareComponent and not @Critical;
    }
}