package DroneDSLinSysML {
    
    /* --- 1. Domain Library (Vocabulary) --- */
    library package Drone_Library {
        part def Sensor;
        part def ImageSensor :> Sensor;
        part def CollisionSensor :> Sensor;
        
        part def Rotor;
        
        part def Drone {
           part rotors : Rotor [1..*];
           part sensors : Sensor [0..*];
        }
    }
    
    /* --- 2. Metadata Definitions (The Mapping) --- */
    package Drone_Metadata {
        private import Drone_Library::*;
        private import Metaobjects::SemanticMetadata;
        
        metadata def drone :> SemanticMetadata {
            :>> baseType = Drone meta SysML::Definition;
            :> annotatedElement : SysML::Definition;
        }
        
        metadata def rotor :> SemanticMetadata {
            :>> baseType = Rotor meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
        
        metadata def cam :> SemanticMetadata {
            :>> baseType = ImageSensor meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
        
        metadata def lidar :> SemanticMetadata {
            :>> baseType = CollisionSensor meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
    }
    
    /* --- 3. DSL Usage (The Result) --- */
    package Mission_Model {
        private import Drone_Metadata::*;
        
        #drone part def SurveillanceDrone {
            /* Using the DSL vocabulary: */
            #rotor part frontRotors[2];
            #rotor part rearRotors[2];
            
            /* Defining sensors using shorthand */
            #cam part mainCamera;
            #lidar part obstacleAvoider;
        }
    }
}