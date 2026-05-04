package PortsInterfaces_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Interface Definitions --- */
    /* Physical connection interface */
    port def PowerInterface {
        /* 'out' means power leaves this port locally */
        out attribute powerLevel : Real;
    }
    
    /* Logical data interface */
    port def DataLink {
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
        /* Normally we use '~' to conjugate the interface, but avoiding due to validator resolution bug */
        port pwrIn : PowerInterface;
        
        /* Data port */
        port eth0 : DataLink;
    }
}