package DroneSystem {
    doc /* A complete SysMLv2 model for a simple hobbyist drone following MagicGrid-like separation: Concept, Logical, Physical. */

    // =========================== IMPORTS ===========================
    private import ScalarValues::*;
    private import SI::*;
    private import ISQ::*;
    private import DS_Views::SymbolicViewsByExpression::*;
    private import DS_Views::TabularViews::*;
    private import SysML::Systems::*;
    private import MeasurementReferences::ConversionByPrefix;

    // =========================== REQUIREMENT TYPES (DEFINITIONS) ===========================
    library package RequirementTypes {
        doc /* Reusable definitions of requirement kinds. */
        requirement def PerformanceRequirement {
            doc /* A requirement that specifies a measurable performance criterion. */
        }
        requirement def SafetyRequirement {
            doc /* A requirement that specifies a safety condition or constraint. */
        }
        requirement def InterfaceRequirement {
            doc /* A requirement that defines external interaction protocols. */
        }
    }

    // =========================== CONCEPT DOMAIN (PROBLEM) ===========================
    package Concept {
        doc /* Problem domain: stakeholder needs, operational scenarios, system context, and high-level requirements. */

        // ----- Stakeholders and Actors -----
        part def Person {
            doc /* A human stakeholder. */
        }
        part def Hobbyist :> Person {
            doc /* The primary user of the drone. */
        }
        part def Smartphone {
            doc /* The mobile device running the control application. */
        }

        // ----- Stakeholder Concerns (expressed as requirements) -----
        package StakeholderConcerns {
            doc /* Concerns expressed by stakeholders that drive requirements. */
            concern def FlightStability {
                subject drone : DroneSystem::Concept::Drone;
                stakeholder pilot : Hobbyist;
                require constraint { /* drone maintains stable hover and controllable flight */ }
            }
            concern def VideoQuality {
                subject drone : DroneSystem::Concept::Drone;
                stakeholder pilot : Hobbyist;
                require constraint { /* recorded video meets resolution and framerate expectations */ }
            }
            concern def EaseOfUse {
                subject drone : DroneSystem::Concept::Drone;
                stakeholder pilot : Hobbyist;
                require constraint { /* intuitive controls via smartphone app */ }
            }
            concern def Safety {
                subject drone : DroneSystem::Concept::Drone;
                stakeholder pilot : Hobbyist;
                require constraint { /* emergency landing and low-battery protection */ }
            }
            concern def FlightTime {
                subject drone : DroneSystem::Concept::Drone;
                stakeholder pilot : Hobbyist;
                require constraint { /* sufficient endurance for typical recreational flights */ }
            }
        }

        // ----- System Context (Black-Box) -----
        part def Drone {
            doc /* The System of Interest: a hobbyist quadcopter with video recording capability. */
            attribute name : String default "HobbyDrone";
            // External interactions via ports (to be refined)
            port pilotCmd : ~ControlInterface;
            port videoStreamOut : VideoStreamInterface;
        }

        part def Environment {
            doc /* External environment including wind, temperature, obstacles. */
        }

        part def GroundControl {
            doc /* Smartphone application that sends commands and receives telemetry. */
            port cmdOut : ControlInterface;
            port videoIn : ~VideoStreamInterface;
        }

        interface def ControlInterface {
            doc /* Commands from smartphone to drone. */
            out takeoff : Signal;
            out land : Signal;
            out emergencyStop : Signal;
            out setpoint : VelocityVector;
            out arm : Signal;
            out disarm : Signal;
            out startRecording : Signal;
            out stopRecording : Signal;
        }

        interface def VideoStreamInterface {
            doc /* Transmission of video frames from drone to ground. */
            out videoFrame : VideoFrame;
        }

        action def Signal;  // Base signal type
        attribute def VelocityVector {
            attribute x : Real;
            attribute y : Real;
            attribute z : Real;
        }
        item def VideoFrame {
            attribute data : String;
            attribute timestamp : Real;
        }

        // ----- Use Cases -----
        use case def FlyDrone {
            subject drone : Drone;
            actor pilot : Hobbyist;
            actor phone : Smartphone;
            objective {
                doc /* The pilot successfully controls the drone for recreational flight, including takeoff, maneuvering, and landing. */
            }
            include use case Takeoff;
            include use case ControlInFlight;
            include use case Land;
        }
        use case def Takeoff {
            subject drone : Drone;
            objective {
                doc /* Drone ascends to a predefined hover altitude and maintains position. */
            }
        }
        use case def ControlInFlight {
            subject drone : Drone;
            objective {
                doc /* Drone responds to real‑time pitch, roll, yaw, and throttle commands from the pilot. */
            }
        }
        use case def Land {
            subject drone : Drone;
            objective {
                doc /* Drone descends and motors stop when ground contact is detected. */
            }
        }
        use case def RecordVideo {
            subject drone : Drone;
            objective {
                doc /* Drone records high‑definition video to onboard storage while transmitting a low‑latency preview to the pilot’s phone. */
            }
        }
        use case def ReturnToHome {
            subject drone : Drone;
            objective {
                doc /* Drone automatically returns to the takeoff point and lands, triggered by pilot command or low battery condition. */
            }
        }

        // ----- Stakeholder Needs & System Requirements (Verifiable usages) -----
        package Requirements {
            doc /* Verifiable system requirements derived from stakeholder needs. */

            // Performance requirements
            requirement <'REQ-FLIGHT-01'> 'Hover Accuracy' : RequirementTypes::PerformanceRequirement {
                doc /* The drone shall maintain horizontal position within 1.0 meter and altitude within 0.5 meter during hover in calm wind (< 5 m/s). */
                attribute posAccuracy : ISQ::length = 1.0 [m];
                attribute altAccuracy : ISQ::length = 0.5 [m];
                require constraint {
                    posAccuracy <= 1.0 [m] and altAccuracy <= 0.5 [m];
                }
            }
            requirement <'REQ-FLIGHT-02'> 'Flight Endurance' : RequirementTypes::PerformanceRequirement {
                doc /* The drone shall achieve a flight time of at least 15 minutes when hovering with a fully charged battery and no payload. */
                attribute minEndurance : DurationValue = 15 [min];
            }
            requirement <'REQ-FLIGHT-03'> 'Maximum Range' : RequirementTypes::PerformanceRequirement {
                doc /* The drone shall maintain control and video link up to a range of 1 kilometer in open outdoor conditions. */
                attribute maxRange : ISQ::length = 1000 [m];
            }
            requirement <'REQ-FLIGHT-04'> 'Wind Resistance' : RequirementTypes::PerformanceRequirement {
                doc /* The drone shall be capable of stable flight and controlled maneuvering in wind speeds up to 8 m/s. */
                attribute maxWindSpeed : ISQ::speed = 8 [m/s];
            }

            // Video requirements
            requirement <'REQ-VIDEO-01'> 'Video Resolution' : RequirementTypes::PerformanceRequirement {
                doc /* The recorded video shall be at least 1080p (1920x1080) at 30 frames per second. */
                attribute minResolution : String = "1920x1080";
                attribute minFramerate : Integer = 30;
            }
            requirement <'REQ-VIDEO-02'> 'Live Preview Latency' : RequirementTypes::PerformanceRequirement {
                doc /* The video preview on the pilot’s smartphone shall have end‑to‑end latency no greater than 200 milliseconds. */
                attribute maxLatency : DurationValue = 200 [ms];
            }

            // Safety requirements
            requirement <'REQ-SAFE-01'> 'Low Battery Auto‑Land' : RequirementTypes::SafetyRequirement {
                doc /* When battery voltage drops below the safe flight threshold, the drone shall automatically land within 30 seconds. */
                attribute voltageThreshold : ISQ::voltage = 10.5 [V];
            }
            requirement <'REQ-SAFE-02'> 'Emergency Stop' : RequirementTypes::SafetyRequirement {
                doc /* Upon receiving an emergency stop command from the pilot, all motors shall stop within 1 second. */
                attribute stopTime : DurationValue = 1 [s];
            }
            requirement <'REQ-SAFE-03'> 'Return to Home on Signal Loss' : RequirementTypes::SafetyRequirement {
                doc /* If the control link is lost for more than 3 seconds, the drone shall automatically execute Return to Home. */
                attribute linkLossTimeout : DurationValue = 3 [s];
            }

            // Interface requirements
            requirement <'REQ-INT-01'> 'Smartphone Compatibility' : RequirementTypes::InterfaceRequirement {
                doc /* The drone shall be controllable via a dedicated smartphone application running on iOS 13+ or Android 8+. */
            }
        }
    }

    // =========================== LOGICAL DOMAIN (SOLUTION) ===========================
    package Logical {
        doc /* Technology‑independent logical architecture: subsystems, behavior, and interfaces. */

        // ----- Logical Subsystems (part defs) -----
        part def FlightController {
            doc /* Computes motor commands, stabilizes the drone, executes high‑level control laws. */
            port sensorDataIn : SensorDataPort;
            port cmdIn : ~ControlInterface;          // from pilot
            port motorCmdsOut : MotorCommandPort;
            port telemetryOut : TelemetryPort;
            // Behaviors
            exhibit state flightControlState : FlightStateMachine;
            action computeControlLaw : ControlLaw;
        }

        part def PowerSystem {
            doc /* Manages battery, power distribution, and low‑voltage monitoring. */
            port powerOut : PowerInterface;
            port voltageSenseOut : VoltageSensePort;
            attribute capacity : CapacityValue;
            attribute currentVoltage : ISQ::voltage;
        }

        part def PropulsionSystem {
            doc /* Converts electrical power into thrust; comprises 4 motors and propellers. */
            port powerIn : ~PowerInterface;
            port motorCmdIn : ~MotorCommandPort;
            port rpmOut : RPMDataPort;
        }

        part def SensorSuite {
            doc /* Provides state estimation: GPS, IMU, barometer, magnetometer. */
            port gpsOut : GPSDataPort;
            port imuOut : IMUDataPort;
            port baroOut : BarometerDataPort;
        }

        part def VideoSystem {
            doc /* Captures video, encodes, and streams preview. */
            port videoOut : VideoStreamInterface;
            port recordCmdIn : RecordCommandPort;
            attribute resolution : String;
            attribute framerate : Integer;
        }

        // ----- Port and Interface Definitions (Logical) -----
        interface def SensorDataPort {
            in gps : GPSData;
            in imu : IMUData;
            in baro : BarometerData;
        }
        interface def MotorCommandPort {
            out motor1 : Real;
            out motor2 : Real;
            out motor3 : Real;
            out motor4 : Real;
        }
        interface def TelemetryPort {
            out altitude : ISQ::length;
            out groundSpeed : ISQ::speed;
            out batteryVoltage : ISQ::voltage;
            out position : LatLongAlt;
        }
        interface def PowerInterface {
            out voltage : ISQ::voltage;
            out current : ISQ::electricCurrent;
        }
        interface def VoltageSensePort {
            out voltage : ISQ::voltage;
        }
        interface def RPMDataPort {
            out rpm : Real;
        }
        interface def GPSDataPort {
            out lat : Real;
            out lon : Real;
            out alt : ISQ::length;
            out fixType : Integer;
        }
        interface def IMUDataPort {
            out accelX : Real;
            out accelY : Real;
            out accelZ : Real;
            out gyroX : Real;
            out gyroY : Real;
            out gyroZ : Real;
        }
        interface def BarometerDataPort {
            out pressure : ISQ::pressure;
            out altitude : ISQ::length;
        }
        interface def RecordCommandPort {
            in start : Signal;
            in stop : Signal;
        }

        attribute def LatLongAlt {
            attribute latitude : Real;
            attribute longitude : Real;
            attribute altitude : ISQ::length;
        }
        item def GPSData;
        item def IMUData;
        item def BarometerData;

        // ----- Logical Behavior: State Machine -----
        state def FlightStateMachine {
            doc /* Main flight state machine for the drone. */
            entry;
            then Disarmed;

            state Disarmed;
            state Armed;
            state TakingOff;
            state Flying;
            state Hovering;
            state Landing;
            state EmergencyLanding;

            // Armed transition
            transition armTransition
                first Disarmed
                accept arm via cmdIn
                if batteryVoltage > lowVoltageLimit
                do action armMotors
                then Armed;

            // Takeoff
            transition takeoffTransition
                first Armed
                accept takeoff via cmdIn
                do action ascendToHoverAltitude
                then TakingOff;
            transition afterTakeoff
                first TakingOff
                accept when altitude >= hoverAltitude
                then Hovering;

            // Flying / Hovering transitions
            transition startFlight
                first Hovering
                accept setpoint via cmdIn
                do action computeControlLaw
                then Flying;
            transition stopFlight
                first Flying
                accept setpoint where setpoint.x==0 and setpoint.y==0 and setpoint.z==0
                then Hovering;

            // Landing
            transition landTransition
                first Flying or Hovering
                accept land via cmdIn
                do action descendAndLand
                then Landing;
            transition afterLanding
                first Landing
                accept when altitude <= 0.1 [m]
                do action disarmMotors
                then Disarmed;

            // Emergency
            transition emergencyTrigger
                first Armed or TakingOff or Flying or Hovering
                accept emergencyStop via cmdIn
                do action cutMotors
                then EmergencyLanding;
            transition lowBatteryTrigger
                first Flying or Hovering
                accept when batteryVoltage <= lowVoltageLimit
                do action initiateAutoLand
                then EmergencyLanding;
        }

        // ----- Logical Actions -----
        action def ControlLaw {
            in setpoint : VelocityVector;
            in sensors : SensorData;
            out motorCommands : MotorCommand;
        }

        // ----- Logical Structure Composition -----
        part def DroneLogical {
            doc /* Logical decomposition of the drone into subsystems. */
            part flightController : FlightController;
            part powerSystem : PowerSystem;
            part propulsion : PropulsionSystem;
            part sensors : SensorSuite;
            part video : VideoSystem;

            // Internal connections
            connect flightController.motorCmdsOut to propulsion.motorCmdIn;
            connect powerSystem.powerOut to propulsion.powerIn;
            connect sensors.gpsOut to flightController.sensorDataIn.gps;
            connect sensors.imuOut to flightController.sensorDataIn.imu;
            connect sensors.baroOut to flightController.sensorDataIn.baro;
            connect powerSystem.voltageSenseOut to flightController.sensorDataIn.voltage;

            // Delegate external ports
            port cmdIn : ~ControlInterface;
            port videoStreamOut : VideoStreamInterface;
            binding cmdIn = flightController.cmdIn;
            binding videoStreamOut = video.videoOut;
        }
    }

    // =========================== PHYSICAL DOMAIN (IMPLEMENTATION) ===========================
    package Physical {
        doc /* Technology‑specific physical components, allocation to logical architecture, and verification. */

        // ----- Physical Components -----
        part def LipoBattery {
            doc /* 3S 1500mAh lithium‑polymer battery. */
            attribute nominalVoltage : ISQ::voltage = 11.1 [V];
            attribute capacity : CapacityValue = 1500 [mAh];
            attribute maxDischargeCurrent : ISQ::electricCurrent = 20 [A];
            port powerOut : PowerInterface;
            port senseOut : VoltageSensePort;
        }

        part def BrushlessMotor {
            doc /* 2300KV brushless DC motor. */
            attribute kV : Real = 2300.0;
            port powerIn : ~PowerInterface;
            port commandIn : PWMCommandPort;
        }

        part def ESC {
            doc /* Electronic Speed Controller for one motor. */
            port cmdIn : ~PWMCommandPort;
            port powerOut : PowerInterface;
        }

        part def Propeller {
            attr diameter : ISQ::length = 5 [inch];
            attr pitch : ISQ::length = 4.5 [inch];
        }

        part def FlightControllerBoard {
            doc /* STM32F405‑based flight controller running ArduPilot. */
            port sensorI2C : I2CPort;
            port pwmOuts : PWMCommandPort[4];
            port uartGPS : UARTPort;
            port radioRx : SBUSPort;
            port usbVideo : USBPort;
            // firmware
            item firmware : SoftwareBinary;
        }

        part def GPSModule {
            doc /* UBlox NEO‑M8N GPS/GLONASS receiver. */
            port uartOut : UARTPort;
        }

        part def IMUModule {
            doc /* MPU6000 inertial sensor. */
            port i2cOut : I2CPort;
        }

        part def BarometerModule {
            doc /* BMP280 pressure sensor. */
            port i2cOut : I2CPort;
        }

        part def CameraModule {
            doc /* 4K CMOS sensor with H.264 encoder. */
            port videoOut : VideoStreamInterface;
            port recordCmd : RecordCommandPort;
        }

        part def VideoTransmitter {
            doc /* 5.8 GHz analog or digital VTx. */
            port videoIn : ~VideoStreamInterface;
            port antenna : SMAport;
        }

        part def SmartphoneApp {
            doc /* Companion mobile application (Android/iOS). */
            port cmdOut : ControlInterface;
            port videoIn : ~VideoStreamInterface;
        }

        // Additional physical interface definitions
        interface def PWMCommandPort {
            out pwmDutyCycle : Real;
        }
        interface def I2CPort {
            inout scl : Boolean;
            inout sda : Boolean;
        }
        interface def UARTPort {
            out tx : Byte;
            in rx : Byte;
        }
        interface def SBUSPort {
            in chan : Integer[16];
        }
        interface def USBPort {
            inout data : Byte[*];
        }
        interface def SMAport {
            out rf : Real;
        }
        item def SoftwareBinary;

        // ----- Physical System Composition -----
        part def DronePhysical {
            doc /* Complete physical assembly of the drone. */
            part battery : LipoBattery;
            part flightCtrl : FlightControllerBoard;
            part gps : GPSModule;
            part imu : IMUModule;
            part baro : BarometerModule;
            part camera : CameraModule;
            part vtx : VideoTransmitter;
            part motors : BrushlessMotor[4];
            part escs : ESC[4];
            part props : Propeller[4];

            // Internal connections (simplified)
            connect flightCtrl.pwmOuts[1] to escs[1].cmdIn;
            connect escs[1].powerOut to motors[1].powerIn;
            connect battery.powerOut to flightCtrl.powerIn;
            connect battery.powerOut to escs[1..4].powerIn;
            connect gps.uartOut to flightCtrl.uartGPS;
            connect imu.i2cOut to flightCtrl.sensorI2C;
            connect baro.i2cOut to flightCtrl.sensorI2C;
            connect camera.videoOut to vtx.videoIn;

            // External ports
            port cmdWireless : ~ControlInterface;
            port videoAntenna : VideoStreamInterface;
            binding cmdWireless = flightCtrl.radioRx;   // simplified: telemetry/rc link
            binding videoAntenna = vtx.videoIn;
        }

        part def GroundPhysical {
            part phoneApp : SmartphoneApp;
            part rcReceiver : RadioReceiver;   // included in phone or external gamepad
            part videoReceiver : VideoReceiver;
            // links to drone
        }

        // ----- Allocation (Logical → Physical) -----
        package Allocation {
            doc /* Allocations between logical architecture elements and physical components. */
            allocate physical flightCtrl to logical flightController;
            allocate physical gps to logical sensors.gps;
            allocate physical imu to logical sensors.imu;
            allocate physical baro to logical sensors.baro;
            allocate physical camera to logical video;
            allocate physical vtx to logical video.videoOut;
            allocate physical battery to logical powerSystem;
            allocate physical motors + escs to logical propulsion;
            allocate physical phoneApp to logical cmdIn;
        }

        // ----- Verification: Satisfy Requirements -----
        // Each physical part or system satisfies specific requirements.
        part dronePhysicalInstance : DronePhysical {
            satisfy Concept::Requirements::<'REQ-FLIGHT-01'>;
            satisfy Concept::Requirements::<'REQ-FLIGHT-02'> by battery.capacity;
            satisfy Concept::Requirements::<'REQ-FLIGHT-03'> by flightCtrl.radioRx;
            satisfy Concept::Requirements::<'REQ-FLIGHT-04'> by flightCtrl.controlLaw;
            satisfy Concept::Requirements::<'REQ-VIDEO-01'> by camera.resolution;
            satisfy Concept::Requirements::<'REQ-VIDEO-02'> by vtx.latency;
            satisfy Concept::Requirements::<'REQ-SAFE-01'> by battery.voltageSense;
            satisfy Concept::Requirements::<'REQ-SAFE-02'> by flightCtrl.emergencyLogic;
            satisfy Concept::Requirements::<'REQ-SAFE-03'> by flightCtrl.linkLossHandler;
            satisfy Concept::Requirements::<'REQ-INT-01'> by GroundPhysical::phoneApp;
        }
    }

    // =========================== VIEWS ===========================
    package Views {
        doc /* Reusable and concrete views to visualize the drone model. */

        // Base Views pattern
        package BV BaseViews {
            private import DS_Views::SymbolicViewsByExpression::*;
            private import DS_Views::TabularViews::*;
            private import SysML::Systems::*;

            view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @PartDefinition;
                filter @PartUsage;
            }
            view requirementsTreeView : RequirementsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;
            view allocationTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @Allocation;
            }
            view stateMachineView : StatesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
            view useCaseView : UseCasesView, EssentialElementsFilter, NonStandardLibraryElementFilter;
        }

        // Concrete Views for Concept
        package ConceptViews {
            view conceptContextDiagram :> BV::partsTreeView {
                expose DroneSystem::Concept::Drone;
                expose DroneSystem::Concept::GroundControl;
                expose DroneSystem::Concept::Environment;
            }
            view useCases :> BV::useCaseView {
                expose DroneSystem::Concept::**;
            }
            view requirementsTable :> BV::requirementsTreeView {
                expose DroneSystem::Concept::Requirements::**;
            }
        }

        // Concrete Views for Logical
        package LogicalViews {
            view logicalStructure :> BV::partsTreeView {
                expose DroneSystem::Logical::DroneLogical;
                expose DroneSystem::Logical::**;
            }
            view flightStateMachine :> BV::stateMachineView {
                expose DroneSystem::Logical::FlightStateMachine;
            }
        }

        // Concrete Views for Physical
        package PhysicalViews {
            view physicalAssembly :> BV::partsTreeView {
                expose DroneSystem::Physical::DronePhysical;
                expose DroneSystem::Physical::**;
            }
            view allocationMatrix :> BV::allocationTableView {
                expose DroneSystem::Physical::Allocation::**;
            }
            view satisfactionTable : rt {
                expose DroneSystem::Physical::**;
                filter @SatisfyRequirementUsage;
            }
        }
    }
}