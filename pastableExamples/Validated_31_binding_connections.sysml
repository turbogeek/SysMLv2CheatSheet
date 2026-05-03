package BindingTests;

port def DataPort {
    in item dataIn;
    out item dataOut;
}

part def Module {
    port dataPort : DataPort;
}

part system {
    part module1 : Module;
    part module2 : Module;
    
    // Bind ports
    bind module1.dataPort.dataOut = module2.dataPort.dataIn;
    
    // Connect ports
    connect module1.dataPort to module2.dataPort;
}
