package Vehicle_Library {
    port def DrivePort {
        out attribute torque : ISQ::TorqueValue;
    }
    part def Engine {
        port enginePort : DrivePort;
    }
    part engines : Engine [0..*];
    part def Wheel {
        port wheelPort : ~DrivePort;
    }
    part wheels : Wheel [0..*];
    interface def DriveTrain {
        end [0..1] port drivePort : DrivePort;
        end [0..*] port drivenPort : ~DrivePort;
    }
    abstract interface driveTrains : DriveTrain [0..*];
    
    part def Vehicle {
        part :>> engines;
        part :>> wheels;
        part :>> driveTrains;
    }
}