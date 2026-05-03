package ConjugateTests;

interface def DataInterface {
    in item request;
    out item response;
}

// Conjugate interface (reverses in/out)
interface def ~DataInterface;

part def Client {
    port clientPort : DataInterface;
}

part def Server {
    port serverPort : ~DataInterface;
}

part system {
    part client : Client;
    part server : Server;
    
    connect client.clientPort to server.serverPort;
}
