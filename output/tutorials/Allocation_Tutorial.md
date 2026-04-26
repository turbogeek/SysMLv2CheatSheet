# Allocation

*Mapping Behavior to Structure*

## 1. Allocation Concept

Allocation maps one model element to another, typically to show realization (e.g., Logical functionality allocated to Physical hardware). **CRITICAL**: Allocations must happen between usages (instances), NOT definitions. Use a dedicated `AllocationContext` package to hold the instances and their allocations.

## 2. Syntax

```sysml
allocate <source> to <target>;
```

## 3. Deployment Example

```sysml
package Allocation_Tutorial {
    
    /* --- Behavioral / Logical View --- */
    action def ComputePath;
    
    /* --- Physical / Structural View --- */
    part def FlightComputer;
    
    /* Create a dedicated package for allocations between usages */
    package AllocationContext {
        part ecu : FlightComputer;
        action plan : ComputePath;
        
        /* Allocate the action usage (plan) to the hardware usage (ecu) */
        /* Meaning: "The ECU executes the planning action" */
        allocate plan to ecu;
    }
}
```

