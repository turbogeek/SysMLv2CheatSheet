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