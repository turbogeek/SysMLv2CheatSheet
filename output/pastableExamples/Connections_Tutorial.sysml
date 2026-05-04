package Connections_Tutorial {
    private import ScalarValues::*;
    
    /* --- Interface Definitions --- */
    port def PowerInterface {
        out attribute powerLevel : Real;
    }
    
    port def DataLink {
        end source;
        end target;
        flow source to target;
    }

    /* --- Component Definitions --- */
    part def Battery {
        port pwrPort : PowerInterface;
    }

    part def Computer {
        port pwrIn : PowerInterface;
        port eth0 : DataLink;
    }
    
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