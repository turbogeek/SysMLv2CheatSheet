# Allocation

*Mapping Behavior to Structure*

## 1. Allocation Concept

Allocation maps one model element to another, typically to show realization (e.g., Logical functionality allocated to Physical hardware).

## 2. Syntax

```sysml
allocate <source> to <target>;
```

## 3. Deployment Example

```sysml
package Allocation_Tutorial {
    
    // --- Behavioral / Logical View ---
    action def ComputePath;
    
    // --- Physical / Structural View ---
    part def FlightComputer;
    
    package Deployment {
        part ecu : FlightComputer;
        action plan : ComputePath;
        
        // Allocate the action (plan) to the hardware (ecu)
        // Meaning: "The ECU executes the planning action"
        allocate plan to ecu;
    }
}
```

