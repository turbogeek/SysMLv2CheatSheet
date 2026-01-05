# Filters

*Refining View Content*

## 1. Filters

Filters refine what is shown in a view. They are crucial for creating manageable diagrams from complex models.

## 2. Syntax

- **hastype <Def>**: Checks if an element is a usage of `<Def>`.
- **@<Meta>**: Checks if an element has specific metadata applied.
- **and, or, not**: Standard boolean logic.

## 3. Filtering Example

```sysml
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
```

