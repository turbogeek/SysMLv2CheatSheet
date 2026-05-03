package AllocationTests;

// Test allocation definitions and allocate relationships

part def Server {
    attribute cpu : Real;
    attribute memory : Real;
}

part def SoftwareComponent {
    attribute memoryRequired : Real;
}

allocation def DeploymentAllocation {
    end source : SoftwareComponent;
    end target : Server;
}

part serverInstance : Server {
    attribute cpu = 2.4;
    attribute memory = 16.0;
}

part appComponent : SoftwareComponent {
    attribute memoryRequired = 4.0;
}

// Allocate software to hardware
allocate appComponent to serverInstance;

allocation deployment : DeploymentAllocation {
    end source = appComponent;
    end target = serverInstance;
}
