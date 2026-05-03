package MessageTests;

// Test message passing and accept clauses

item def Message {
    attribute payload : String;
}

part def Sender {
    out item msg : Message;
}

part def Receiver {
    in item received : Message;
}

action def CommunicationProtocol {
    action send {
        out message : Message;
    }

    action receive {
        accept msg : Message via channel;

        then processMessage;
    }

    action processMessage;

    first send then receive;
}

part system {
    part sender : Sender;
    part receiver : Receiver;
    
    message msg from sender.msg to receiver.received;
}
