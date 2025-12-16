package DSLinSysML {
    doc /* https://www.omg.org/cgi-bin/doc?syseng/25-03-07.pdf */
    
    // --- 1. Domain Library (Vocabulary) ---
    library package Vehicle_Library {
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
    
    // --- 2. Metadata Definitions (The Mapping) ---
    package Vehicle_Metadata {
        private import Vehicle_Library::*;
        private import Metaobjects::SemanticMetadata;
        
        metadata def drive :> SemanticMetadata {
            :>> baseType = driveTrains meta SysML::Usage;
            :> annotatedElement : SysML::InterfaceUsage;
        }
        metadata def engine :> SemanticMetadata {
            :>> baseType = engines meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
        metadata def wheel :> SemanticMetadata {
            :>> baseType = wheels meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
        metadata def vehicle :> SemanticMetadata {
            :>> baseType = Vehicle meta SysML::Definition;
            :> annotatedElement : SysML::Definition;
        }
    }
    
    // --- 3. DSL Usage (The Result) ---
    package Car_Example {
        private import Vehicle_Metadata::*;
        
        #vehicle def Car {
            #engine carEngine [1];
            #wheel carWheels [4];
            #drive interface [1] carEngine.enginePort to [2] carWheels.wheelPort;
        }
    }
}