package ItemFlowTests;

// Test item definitions and flow

item def DataPacket {
    attribute size : Integer;
    attribute timestamp : Real;
}

item def Signal {
    attribute frequency : Real;
    attribute amplitude : Real;
}

part def Sensor {
    out item signal : Signal;
}

part def Processor {
    in item inputSignal : Signal;
    out item data : DataPacket;
}

part def Display {
    in item displayData : DataPacket;
}

part system {
    part sensor : Sensor;
    part processor : Processor;
    part display : Display;

    // Item flows
    flow signal from sensor.signal to processor.inputSignal;
    flow data from processor.data to display.displayData;
}
