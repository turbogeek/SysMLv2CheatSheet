package DroneProject {
    private import ScalarValues::*;
    private import ISQ::*;
    private import SI::*;
    
    // Project Specific Units
    package ProjectUnits {
        private import SI::*;
        private import MeasurementReferences::ConversionByPrefix;

        attribute <ms> millisecond : DurationUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = milli;
                :>> referenceUnit = s;
            }
        }
    }

    library package BaseViews {
        private import DS_Views::SymbolicViewsByExpression::*;
        private import DS_Views::TabularViews::*;
        private import SysML::Systems::*;
        
        view partsView : UsagesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
        private import DS_Views::**;
        view partsTreeView : gv, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @PartDefinition;
            filter @PartUsage;
        }
        view requirementTableTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @RequirementUsage;
        }
    }

    library package RequirementTypes {
        requirement def FunctionalRequirement {
            doc /* A requirement that specifies a function that a system or system component must be able to perform. */
        }
        requirement def PerformanceRequirement {
            doc /* A requirement that requires a specific metric to be met. */
        }
        requirement def CostRequirement {
            doc /* A requirement that specifies cost constraints. */
        }
        requirement def ConstraintRequirement {
            doc /* A requirement that specifies a design constraint. */
        }
    }

    library package ConceptLibrary {
        part def Stakeholder;
        use case def DroneUseCase;
    }

    package Concept {
        part pilot : ConceptLibrary::Stakeholder {
            doc /* Hobbyist Pilot (End User) */
        }
        part generalPublic : ConceptLibrary::Stakeholder {
            doc /* General Public (Safety and Privacy concerns) */
        }
        part regulators : ConceptLibrary::Stakeholder {
            doc /* Regulatory Bodies (e.g., FAA for weight limits and airspace) */
        }

        use case takeoff : ConceptLibrary::DroneUseCase {
            subject droneSystem : LogicalArchitecture::logicalDrone;
            actor user = pilot;
            objective { doc /* User commands the drone to take off, and it ascends to a stable hover height. */ }
        }
        
        use case recordVideo : ConceptLibrary::DroneUseCase {
            subject droneSystem : LogicalArchitecture::logicalDrone;
            actor user = pilot;
            objective { doc /* User starts and stops video recording; video is saved or streamed. */ }
        }
        
        use case followMe : ConceptLibrary::DroneUseCase {
            subject droneSystem : LogicalArchitecture::logicalDrone;
            actor user = pilot;
            objective { doc /* User commands the drone to follow them using visual tracking. */ }
        }
        
        use case returnToHome : ConceptLibrary::DroneUseCase {
            subject droneSystem : LogicalArchitecture::logicalDrone;
            actor user = pilot;
            objective { doc /* User commands the drone to return to the takeoff position. */ }
        }
    }

    package Requirements {
        requirement <'REQ-FUN-01'> 'Flight Control' : RequirementTypes::FunctionalRequirement {
            doc /* The system shall accept directional inputs (pitch, roll, yaw, altitude) from the smartphone app. */
        }
        requirement <'REQ-FUN-02'> 'Takeoff and Landing' : RequirementTypes::FunctionalRequirement {
            doc /* The system shall provide automated takeoff and landing functions. */
        }
        requirement <'REQ-FUN-03'> Hovering : RequirementTypes::FunctionalRequirement {
            doc /* The system shall automatically maintain a stable hover when user inputs are neutral. */
        }
        requirement <'REQ-FUN-04'> 'Video Capture' : RequirementTypes::FunctionalRequirement {
            doc /* The system shall record and stream video to the connected app. */
        }
        requirement <'REQ-FUN-05'> 'Follow Me' : RequirementTypes::FunctionalRequirement {
            doc /* The system shall track and follow the user using visual tracking. */
        }
        requirement <'REQ-FUN-06'> 'Return to Home' : RequirementTypes::FunctionalRequirement {
            doc /* The system shall autonomously return to its takeoff position when commanded. */
        }
        requirement <'REQ-PRF-01'> Endurance : RequirementTypes::PerformanceRequirement {
            doc /* The drone shall have a maximum flight time of at least 15 minutes. */
            attribute flightTime : DurationValue;
            attribute minFlightTime : DurationValue = 15 [min];
            require constraint { flightTime >= minFlightTime }
        }
        requirement <'REQ-PRF-02'> 'Video Quality' : RequirementTypes::PerformanceRequirement {
            doc /* The camera shall capture video at a minimum resolution of 1080p. */
        }
        requirement <'REQ-CST-01'> Cost : RequirementTypes::CostRequirement {
            doc /* The total unit retail price shall not exceed $500. */
        }
        requirement <'REQ-CON-01'> Weight : RequirementTypes::ConstraintRequirement {
            doc /* The drone takeoff weight shall be under 250 grams to avoid FAA registration requirements. */
            attribute weight : MassValue;
            attribute maxWeight : MassValue = 250 [g];
            require constraint { weight < maxWeight }
        }

        package Views {
            view requirementsTable :> BaseViews::requirementTableTableView {
                expose Requirements::**;
            }
        }
    }

    library package LogicalLibrary {
        port def CommPort;
        port def VideoPort;
        port def MotorControlPort;
        port def PowerPort;
        port def TrackingDataPort;
        port def NavCommandPort;

        interface def CommInterface {
            end port source : CommPort;
            end port target : ~CommPort;
        }
        interface def VideoInterface {
            end port source : VideoPort;
            end port target : ~VideoPort;
        }
        interface def MotorControlInterface {
            end port source : MotorControlPort;
            end port target : ~MotorControlPort;
        }
        interface def PowerInterface {
            end port source : PowerPort;
            end port target : ~PowerPort;
        }
        interface def TrackingDataInterface {
            end port source : TrackingDataPort;
            end port target : ~TrackingDataPort;
        }
        interface def NavCommandInterface {
            end port source : NavCommandPort;
            end port target : ~NavCommandPort;
        }

        part def FlightController;
        part def CommunicationSubsystem;
        part def PowerSubsystem;
        part def PayloadSubsystem;
        part def PropulsionSubsystem;
        part def NavigationSubsystem;
        
        part def DroneSystem {
            part flightController : FlightController {
                port commIn : ~CommPort;
                port motorOut : MotorControlPort;
                port navCmdIn : ~NavCommandPort;
                port powerIn : ~PowerPort;
            }
            part navigationSubsystem : NavigationSubsystem {
                port trackingDataIn : ~TrackingDataPort;
                port navCmdOut : NavCommandPort;
                port powerIn : ~PowerPort;
            }
            part commSubsystem : CommunicationSubsystem {
                port commOut : CommPort;
                port videoIn : ~VideoPort;
                port powerIn : ~PowerPort;
            }
            part powerSubsystem : PowerSubsystem {
                port powerOut : PowerPort;
            }
            part payloadSubsystem : PayloadSubsystem {
                port videoOut : VideoPort;
                port trackingDataOut : TrackingDataPort;
                port powerIn : ~PowerPort;
            }
            part propulsionSubsystem : PropulsionSubsystem {
                port motorIn : ~MotorControlPort;
                port powerIn : ~PowerPort;
            }

            interface commToFlightCtrl : CommInterface {
                end port source = commSubsystem.commOut;
                end port target = flightController.commIn;
            }
            interface flightCtrlToPropulsion : MotorControlInterface {
                end port source = flightController.motorOut;
                end port target = propulsionSubsystem.motorIn;
            }
            interface payloadToComm : VideoInterface {
                end port source = payloadSubsystem.videoOut;
                end port target = commSubsystem.videoIn;
            }
            interface payloadToNav : TrackingDataInterface {
                end port source = payloadSubsystem.trackingDataOut;
                end port target = navigationSubsystem.trackingDataIn;
            }
            interface navToFlightCtrl : NavCommandInterface {
                end port source = navigationSubsystem.navCmdOut;
                end port target = flightController.navCmdIn;
            }
            
            satisfy Requirements::'REQ-FUN-01' by flightController;
            satisfy Requirements::'REQ-FUN-02' by flightController;
            satisfy Requirements::'REQ-FUN-03' by flightController;
            satisfy Requirements::'REQ-FUN-04' by payloadSubsystem;
            satisfy Requirements::'REQ-FUN-05' by navigationSubsystem;
            satisfy Requirements::'REQ-FUN-06' by navigationSubsystem;
        }
    }

    package LogicalArchitecture {
        part logicalDrone : LogicalLibrary::DroneSystem;

        package Views {
            view logicalPartsTree :> BaseViews::partsTreeView {
                expose LogicalArchitecture::**;
            }
        }
    }

    library package PhysicalLibrary {
        part def MCU;
        part def WiFiModule;
        part def LiPoBattery {
            attribute mass : MassValue;
        }
        part def CameraModule;
        part def BrushlessMotor;
        part def Smartphone;
        part def GPSModule;
        part def VPU;
        
        part def PhysicalDrone {
            part mcu : MCU;
            part wifiModule : WiFiModule;
            part lipoBattery : LiPoBattery;
            part cameraModule : CameraModule;
            part gpsModule : GPSModule;
            part vpu : VPU;
            part motors [4] : BrushlessMotor;
            
            attribute totalMass : MassValue;
            
            satisfy Requirements::'REQ-CON-01' by totalMass;
            satisfy Requirements::'REQ-PRF-01' by lipoBattery;
            satisfy Requirements::'REQ-PRF-02' by cameraModule;
        }
    }

    package PhysicalArchitecture {
        part physicalDrone : PhysicalLibrary::PhysicalDrone;

        package Views {
            view physicalPartsTree :> BaseViews::partsTreeView {
                expose PhysicalArchitecture::**;
            }
        }
    }

    package Allocations {
        allocate PhysicalArchitecture::physicalDrone.mcu to LogicalArchitecture::logicalDrone.flightController;
        allocate PhysicalArchitecture::physicalDrone.wifiModule to LogicalArchitecture::logicalDrone.commSubsystem;
        allocate PhysicalArchitecture::physicalDrone.cameraModule to LogicalArchitecture::logicalDrone.payloadSubsystem;
        allocate PhysicalArchitecture::physicalDrone.lipoBattery to LogicalArchitecture::logicalDrone.powerSubsystem;
        allocate PhysicalArchitecture::physicalDrone.gpsModule to LogicalArchitecture::logicalDrone.navigationSubsystem;
        allocate PhysicalArchitecture::physicalDrone.vpu to LogicalArchitecture::logicalDrone.navigationSubsystem;
        allocate PhysicalArchitecture::physicalDrone.motors to LogicalArchitecture::logicalDrone.propulsionSubsystem;
    }
}

