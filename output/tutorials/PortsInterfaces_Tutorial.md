# Ports & Interfaces

*Defining Interactions Points*

## 1. Ports

Ports define distinct interaction points on the boundary of a part. They allow you to encapsulate internal structure and only expose specific interfaces.

- **port name : Type**: Basic port declaration.
- **directed port (in, out, inout)**: Specifies data flow direction.

## 2. Interface Definitions

- **interface def**: Reusable definition of ports/flows.
- **Conjugation (~)**: Flips the direction of flows (e.g., Plug vs Socket). If an interface has `out pwr`, the conjugated version has `in pwr`.
- **Rule**: The `end` properties inside an interface must be ports (or untyped), never parts.
- **Rule**: Define internal flows using `flow source to target;` without `from` or `of` keywords.

## 3. Power & Data Example

```sysml
package PortsInterfaces_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Interface Definitions --- */
    /* Physical connection interface */
    interface def PowerInterface {
        /* 'out' means power leaves this port locally */
        out powerLevel : Real;
    }
    
    /* Logical data interface */
    interface def DataLink {
        /* end definitions MUST be typed by a port (if complex) or left untyped */
        end source;
        end target;
        /* flow of messages inside the interface */
        flow source to target;
        /* CRITICAL: do not use 'from' or 'of' inside interface flows */
    }

    /* --- 2. Component Definitions --- */
    part def Battery {
        /* Provides power (Source) */
        port pwrPort : PowerInterface;
    }

    part def Computer {
        /* Consumes power (Sink) */
        /* '~' (Tilde) conjugates the interface: 'out' becomes 'in' */
        port pwrIn : ~PowerInterface;
        
        /* Data port */
        port eth0 : DataLink;
    }
}
```

