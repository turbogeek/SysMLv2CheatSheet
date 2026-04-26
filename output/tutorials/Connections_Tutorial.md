# Connections

*Wiring Parts Together*

## 1. Connection Basics

- **connect a to b**: Standard connection between two endpoints.
- **bind a = b**: Equivalence connection. Often used for **delegation** (exposing an internal part's port to the boundary of the container).
- **Rule**: Bindings must always use `=` instead of `to`.
- **Rule**: Bindings cannot contain array indices or multiplicity ranges (e.g. `bind a[1] = b[1]` is invalid). Bind parts individually or as a complete multi-part instead.

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
        
        /* 'bind' means internal eth0 IS the same interaction point as externalEth */
        /* MUST use '=' and NOT 'to' */
        bind externalEth = computer.eth0;
        
        /* --- Multiplicity Binding --- */
        /* Array indices are forbidden in bindings. */
        /* You can bind a single source to a multi-part target directly without indices: */
        /* bind battery.pwrOut = computers.pwrIn; */
    }
}
```

