# System Views

*Views, Viewpoints, and Filtering*

## 1. View Definition

```sysml
view def ReportView {
    in subject : System;
}
```

Defines a reusable view structure.

## 2. View Usage

```sysml
view report : ReportView {
    in subject = mySystem;
}
```

Uses a definition to create a specific view.

## 3. Viewpoint

```sysml
viewpoint def SafetyAnalysis { doc "Focus on hazards"; }
view def SafetyView { satisfies SafetyAnalysis; }
```

Connects a view to its stakeholder concern.

## 4. Expose Content

```sysml
view myView {
    expose myCar;      // Single element
    expose myCar::**;  // Recursive import
}
```

## 5. Filter

```sysml
filter @Part; // Keep only parts
```

## 6. Rendering

```sysml
render asTable { ... }
style color = "red";
```

