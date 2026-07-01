# System Views

*Views, Viewpoints, and Filtering*

## 1. View Definition

```sysml
view def ReportView {
    in part target_sys : System;
}
```

Defines a reusable view structure.

## 2. View Usage

```sysml
view report : ReportView {
    in part target_sys = mySystem;
}
```

Uses a definition to create a specific view.

## 3. Viewpoint

```sysml
viewpoint def SafetyAnalysis { doc "Focus on hazards"; }
viewpoint <'vp1'> 'sa' : SafetyAnalysis;
view mySafetyView { satisfy 'sa'; }
```

Connects a view to its stakeholder concern.

## 4. Expose Content

```sysml
view myView {
    expose myCar;      /* Single element */
    expose myCar::**;  /* Recursive import */
}
```

## 5. Filter

```sysml
filter @PartUsage; /* Keep only parts */
filter @AllocationUsage; /* Keep allocations */
```

**CRITICAL**: Always filter by Usage (e.g. `@PartUsage`, `@AllocationUsage`), not by Definition.

## 6. Rendering

```sysml
render asTable { ... }
style color = "red";
```

