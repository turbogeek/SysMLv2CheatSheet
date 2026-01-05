# Connections

*Wiring Parts Together*

## 1. Connection Basics

- **connect a to b**: Standard connection between two endpoints.
- **binding a = b**: Equivalence connection. Often used for **delegation** (exposing an internal part's port to the boundary of the container).

## 2. Wiring Example

This example shows connecting a Battery to a Computer, and binding the internal Ethernet port to the outside.

```sysml
package Connections_Tutorial {
    private import PortsInterfaces_Tutorial::*; /* Import Battery, Computer */
    
    part def System;
    
    part def PowerSystem :> System {
        part battery : Battery;
        part computer : Computer;
        
        /* --- Connection --- */
        /* Connecting compatible ports (PowerInterface vs ~PowerInterface) */
        connect battery.pwrPort to computer.pwrIn;
        
        /* --- Binding (Delegation) --- */
        /* Exposing the computer's ethernet port to the outside world */
        port externalEth : DataLink;
        
        /* 'binding' means internal eth0 IS the same interaction point as externalEth */
        binding externalEth = computer.eth0;
    }
}
```

