package DroneSystem {
    doc /* A complete SysMLv2 model for a simple hobbyist drone following MagicGrid-like separation: Concept, Logical, Physical. */

    /* =========================== IMPORTS =========================== */
    private import ScalarValues::*;
    private import SI::*;
    private import ISQ::*;
    private import ISQInformation::*;
    private import DS_Views::SymbolicViewsByExpression::*;
    private import DS_Views::TabularViews::*;
    private import SysML::Systems::*;
    private import MeasurementReferences::ConversionByPrefix;

    /* =========================== PROJECT UNITS =========================== */
    package ProjectUnits {
        private import SI::*;
        private import MeasurementReferences::ConversionByPrefix;
        doc /* Project-specific units added where the standard SI library does not already provide the needed named unit. */

        attribute <ms> millisecond : DurationUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = milli;
                :>> referenceUnit = s;
            }
        }
        attribute <'mm/h'> 'millimetre per hour' : SpeedUnit = mm / h;
        attribute <kPa> kilopascal : PressureUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = kilo;
                :>> referenceUnit = Pa;
            }
        }
        attribute <MPa> megapascal : PressureUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = mega;
                :>> referenceUnit = Pa;
            }
        }
        attribute <GPa> gigapascal : PressureUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = giga;
                :>> referenceUnit = Pa;
            }
        }
        attribute <mPa> millipascal : PressureUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = milli;
                :>> referenceUnit = Pa;
            }
        }
        attribute <'µPa'> micropascal : PressureUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = micro;
                :>> referenceUnit = Pa;
            }
        }
        attribute <nPa> nanopascal : PressureUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = nano;
                :>> referenceUnit = Pa;
            }
        }
        attribute <pPa> picopascal : PressureUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = pico;
                :>> referenceUnit = Pa;
            }
        }
        attribute <TPa> terapascal : PressureUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = tera;
                :>> referenceUnit = Pa;
            }
        }
        attribute <mAh> milliampereHour : ElectricChargeUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = milli;
                :>> referenceUnit = A * h;
            }
        }
    }

    /* =========================== REQUIREMENT TYPES (DEFINITIONS) =========================== */
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

    /* =========================== CONCEPT DOMAIN (PROBLEM) =========================== */
    package Concept {
        doc /* Problem domain: stakeholder needs, operational scenarios, system context, and high-level requirements. */

        /* ----- Signal Item Definitions ----- */
        item def TakeoffSignal;
        item def LandSignal;
        item def EmergencyStopSignal;
        item def ArmSignal;
        item def DisarmSignal;
        item def StartRecordingSignal;
        item def StopRecordingSignal;

        /* ----- Stakeholders and Actors ----- */
        part def Person {
            doc /* A human stakeholder. */
        }
        part def Hobbyist :> Person {
            doc /* The primary user of the drone. */
        }
        part def Smartphone {
            doc /* The mobile device running the control application. */
        }

        /* ----- Stakeholder Concerns (expressed as requirements) ----- */
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

        /* ----- System Context (Black-Box) ----- */
        part def Drone {
            doc /* The System of Interest: a hobbyist quadcopter with video recording capability. */
            attribute name : String default "HobbyDrone";
            /* External interactions via ports */
            port pilotCmd : ~ControlPort;
            port videoStreamOut : VideoStreamPort;
        }

        part def Environment {
            doc /* External environment including wind, temperature, obstacles. */
        }

        part def GroundControl {
            doc /* Smartphone application that sends commands and receives telemetry. */
            port cmdOut : ControlPort;
            port videoIn : ~VideoStreamPort;
        }

        /* ----- Port Definitions (Interaction Points) ----- */
        port def ControlPort {
            doc /* Physical port specification for control commands. */
            out takeoff : TakeoffSignal;
            out land : LandSignal;
            out emergencyStop : EmergencyStopSignal;
            out setpoint : VelocityVector;
            out arm : ArmSignal;
            out disarm : DisarmSignal;
            out startRecording : StartRecordingSignal;
            out stopRecording : StopRecordingSignal;
        }

        port def VideoStreamPort {
            doc /* Physical port specification for video streaming. */
            out videoFrame : VideoFrame;
        }

        attribute def VelocityVector {
            attribute x : Real;
            attribute y : Real;
            attribute z : Real;
        }
        item def VideoFrame {
            attribute data : String;
            attribute timestamp : Real;
        }

        /* ----- Interface Definitions (Connect Ports) ----- */
        interface def ControlInterface {
            end port groundPort : ControlPort;
            end port dronePort : ~ControlPort;
        }

        interface def VideoStreamInterface {
            end port dronePort : VideoStreamPort;
            end port groundPort : ~VideoStreamPort;
        }

        /* ----- Use Cases ----- */
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

        /* ----- Stakeholder Needs & System Requirements (Verifiable usages) ----- */
        package Requirements {
            doc /* Verifiable system requirements derived from stakeholder needs. */

            /* Performance requirements */
            requirement <'REQ-FLIGHT-01'> 'Hover Accuracy' : RequirementTypes::PerformanceRequirement {
                doc /* The drone shall maintain horizontal position within 1.0 meter and altitude within 0.5 meter during hover in calm wind (< 5 m/s). */
                subject drone : Drone;
                attribute posAccuracyMeasured : ISQ::length;
                attribute posAccuracyTarget : ISQ::length = 1.0 [m];
                attribute altAccuracyMeasured : ISQ::length;
                attribute altAccuracyTarget : ISQ::length = 0.5 [m];
                require constraint {
                    posAccuracyMeasured <= posAccuracyTarget and altAccuracyMeasured <= altAccuracyTarget
                }
            }
            requirement <'REQ-FLIGHT-02'> 'Flight Endurance' : RequirementTypes::PerformanceRequirement {
                doc /* The drone shall achieve a flight time of at least 15 minutes when hovering with a fully charged battery and no payload. */
                subject drone : Drone;
                attribute enduranceMeasured : DurationValue;
                attribute enduranceTarget : DurationValue = 15 [min];
                require constraint {
                    enduranceMeasured >= enduranceTarget
                }
            }
            requirement <'REQ-FLIGHT-03'> 'Maximum Range' : RequirementTypes::PerformanceRequirement {
                doc /* The drone shall maintain control and video link up to a range of 1 kilometer in open outdoor conditions. */
                subject drone : Drone;
                attribute rangeMeasured : ISQ::length;
                attribute rangeTarget : ISQ::length = 1000 [m];
                require constraint {
                    rangeMeasured >= rangeTarget
                }
            }
            requirement <'REQ-FLIGHT-04'> 'Wind Resistance' : RequirementTypes::PerformanceRequirement {
                doc /* The drone shall be capable of stable flight and controlled maneuvering in wind speeds up to 8 m/s. */
                subject drone : Drone;
                attribute windSpeedMeasured : ISQ::speed;
                attribute windSpeedTarget : ISQ::speed = 8 [m/s];
                require constraint {
                    windSpeedMeasured >= windSpeedTarget
                }
            }

            /* Video requirements */
            requirement <'REQ-VIDEO-01'> 'Video Resolution' : RequirementTypes::PerformanceRequirement {
                doc /* The recorded video shall be at least 1080p (1920x1080) at 30 frames per second. */
                subject video : DroneSystem::Logical::VideoSystem;
                attribute resolutionMeasured : String;
                attribute resolutionTarget : String = "1920x1080";
                attribute framerateMeasured : Integer;
                attribute framerateTarget : Integer = 30;
                require constraint {
                    resolutionMeasured == resolutionTarget and framerateMeasured >= framerateTarget
                }
            }
            requirement <'REQ-VIDEO-02'> 'Live Preview Latency' : RequirementTypes::PerformanceRequirement {
                doc /* The video preview on the pilot’s smartphone shall have end‑to‑end latency no greater than 200 milliseconds. */
                subject drone : Drone;
                attribute latencyMeasured : DurationValue;
                attribute latencyTarget : DurationValue = 200 [ProjectUnits::ms];
                require constraint {
                    latencyMeasured <= latencyTarget
                }
            }

            /* Safety requirements */
            requirement <'REQ-SAFE-01'> 'Low Battery Auto‑Land' : RequirementTypes::SafetyRequirement {
                doc /* When battery voltage drops below the safe flight threshold, the drone shall automatically land within 30 seconds. */
                subject drone : Drone;
                attribute voltageMeasured : ISQ::voltage;
                attribute voltageThreshold : ISQ::voltage = 10.5 [V];
                attribute autoLandTriggered : Boolean;
                require constraint {
                    (voltageMeasured <= voltageThreshold) implies autoLandTriggered
                }
            }
            requirement <'REQ-SAFE-02'> 'Emergency Stop' : RequirementTypes::SafetyRequirement {
                doc /* Upon receiving an emergency stop command from the pilot, all motors shall stop within 1 second. */
                subject drone : Drone;
                attribute stopTimeMeasured : DurationValue;
                attribute stopTimeTarget : DurationValue = 1 [s];
                require constraint {
                    stopTimeMeasured <= stopTimeTarget
                }
            }
            requirement <'REQ-SAFE-03'> 'Return to Home on Signal Loss' : RequirementTypes::SafetyRequirement {
                doc /* If the control link is lost for more than 3 seconds, the drone shall automatically execute Return to Home. */
                subject drone : Drone;
                attribute lossTimeMeasured : DurationValue;
                attribute lossTimeoutTarget : DurationValue = 3 [s];
                attribute returnToHomeTriggered : Boolean;
                require constraint {
                    (lossTimeMeasured >= lossTimeoutTarget) implies returnToHomeTriggered
                }
            }

            /* Interface requirements */
            requirement <'REQ-INT-01'> 'Smartphone Compatibility' : RequirementTypes::InterfaceRequirement {
                doc /* The drone shall be controllable via a dedicated smartphone application running on iOS 13+ or Android 8+. */
                subject app : DroneSystem::Physical::SmartphoneApp;
            }
        }
    }

    /* =========================== LOGICAL DOMAIN (SOLUTION) =========================== */
    package Logical {
        doc /* Technology‑independent logical architecture: subsystems, behavior, and interfaces. */

        /* ----- Signal Items (reused from Concept) ----- */
        private import Concept::*;

        /* ----- Motor command item definition ----- */
        item def MotorCommand {
            attribute motor1 : Real;
            attribute motor2 : Real;
            attribute motor3 : Real;
            attribute motor4 : Real;
        }

        /* ----- Sensor data composite item ----- */
        item def SensorData {
            attribute gps : GPSData;
            attribute imu : IMUData;
            attribute baro : BarometerData;
        }

        /* ----- Logical Subsystems (part defs) ----- */
        part def FlightController {
            doc /* Computes motor commands, stabilizes the drone, executes high‑level control laws. */
            port sensorDataIn : SensorDataPort;
            port cmdIn : ~ControlPort;          /* from pilot */
            port motorCmdsOut : MotorCommandPort;
            port telemetryOut : TelemetryPort;

            /* Attributes for state machine */
            attribute batteryVoltage : ISQ::voltage;
            attribute lowVoltageLimit : ISQ::voltage = 10.5 [V];
            attribute hoverAltitude : ISQ::length = 10.0 [m];
            attribute currentAltitude : ISQ::length;

            /* Local action definitions */
            action def ArmMotors;
            action def AscendToHoverAltitude;
            action def ComputeControlLaw;
            action def DescendAndLand;
            action def DisarmMotors;
            action def CutMotors;
            action def InitiateAutoLand;

            /* State machine defined inside the part to have direct access to part features */
            state def FlightStateMachine {
                entry;
                then Disarmed;

                state Disarmed;
                state Armed;
                state TakingOff;
                state Flying;
                state Hovering;
                state Landing;
                state EmergencyLanding;

                transition armTransition
                    first Disarmed
                    accept armSignal : ArmSignal via cmdIn
                    if batteryVoltage > lowVoltageLimit
                    do action armMotors : ArmMotors
                    then Armed;

                transition takeoffTransition
                    first Armed
                    accept takeoffSignal : TakeoffSignal via cmdIn
                    do action ascend : AscendToHoverAltitude
                    then TakingOff;
                transition afterTakeoff
                    first TakingOff
                    accept when currentAltitude >= hoverAltitude
                    then Hovering;

                transition startFlight
                    first Hovering
                    accept setpoint : VelocityVector via cmdIn
                    do action controlLaw : ComputeControlLaw
                    then Flying;

                transition stopFlight
                    first Flying
                    accept setpoint : VelocityVector if setpoint.x==0 and setpoint.y==0 and setpoint.z==0
                    then Hovering;

                transition landFromHovering
                    first Hovering
                    accept landSignal : LandSignal via cmdIn
                    do action descend : DescendAndLand
                    then Landing;
                transition landFromFlying
                    first Flying
                    accept landSignal : LandSignal via cmdIn
                    do action descend : DescendAndLand
                    then Landing;

                transition afterLanding
                    first Landing
                    accept when currentAltitude <= 0.1 [m]
                    do action disarm : DisarmMotors
                    then Disarmed;

                transition emergencyFromArmed
                    first Armed
                    accept emergencySignal : EmergencyStopSignal via cmdIn
                    do action cut : CutMotors
                    then EmergencyLanding;
                transition emergencyFromTakingOff
                    first TakingOff
                    accept emergencySignal : EmergencyStopSignal via cmdIn
                    do action cut : CutMotors
                    then EmergencyLanding;
                transition emergencyFromFlying
                    first Flying
                    accept emergencySignal : EmergencyStopSignal via cmdIn
                    do action cut : CutMotors
                    then EmergencyLanding;
                transition emergencyFromHovering
                    first Hovering
                    accept emergencySignal : EmergencyStopSignal via cmdIn
                    do action cut : CutMotors
                    then EmergencyLanding;

                transition lowBatteryFromFlying
                    first Flying
                    accept when batteryVoltage <= lowVoltageLimit
                    do action autoLand : InitiateAutoLand
                    then EmergencyLanding;
                transition lowBatteryFromHovering
                    first Hovering
                    accept when batteryVoltage <= lowVoltageLimit
                    do action autoLand : InitiateAutoLand
                    then EmergencyLanding;
            }

            exhibit state flightControlState : FlightStateMachine;

            action def ControlLaw {
                in setpoint : VelocityVector;
                in sensors : SensorData;
                out motorCommands : MotorCommand;
            }
        }

        part def PowerSystem {
            doc /* Manages battery, power distribution, and low‑voltage monitoring. */
            port powerOut : PowerPort;
            port voltageSenseOut : VoltageSensePort;
            attribute chargeCapacity : ISQ::electricCharge = 1500 [ProjectUnits::mAh];
            attribute currentVoltage : ISQ::voltage;
        }

        part def PropulsionSystem {
            doc /* Converts electrical power into thrust; comprises 4 motors and propellers. */
            port powerIn : ~PowerPort;
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
            port videoOut : VideoStreamPort;
            port recordCmdIn : RecordCommandPort;
            attribute resolution : String;
            attribute framerate : Integer;
        }

        /* ----- Port Definitions (Logical) ----- */
        port def SensorDataPort {
            in sensorData : SensorData;
        }
        port def MotorCommandPort {
            out command : MotorCommand;
        }
        port def TelemetryPort {
            out altitude : ISQ::length;
            out groundSpeed : ISQ::speed;
            out batteryVoltage : ISQ::voltage;
            out position : LatLongAlt;
        }
        port def PowerPort {
            out voltage : ISQ::voltage;
            out current : ISQ::electricCurrent;
        }
        port def VoltageSensePort {
            out voltage : ISQ::voltage;
        }
        port def RPMDataPort {
            out rpm : Real;
        }
        port def GPSDataPort {
            out lat : Real;
            out lon : Real;
            out alt : ISQ::length;
            out fixType : Integer;
            out gpsData : GPSData;
        }
        port def IMUDataPort {
            out accelX : Real;
            out accelY : Real;
            out accelZ : Real;
            out gyroX : Real;
            out gyroY : Real;
            out gyroZ : Real;
            out imuData : IMUData;
        }
        port def BarometerDataPort {
            out pressure : ISQ::pressure;
            out altitude : ISQ::length;
            out baroData : BarometerData;
        }
        port def RecordCommandPort {
            in start : StartRecordingSignal;
            in stop : StopRecordingSignal;
        }

        attribute def LatLongAlt {
            attribute latitude : Real;
            attribute longitude : Real;
            attribute altitude : ISQ::length;
        }
        item def GPSData;
        item def IMUData;
        item def BarometerData;

        /* ----- Logical Interfaces (connect ports) ----- */
        interface def SensorDataInterface {
            end port fcPort : SensorDataPort;
            end port gpsPort : ~GPSDataPort;
            end port imuPort : ~IMUDataPort;
            end port baroPort : ~BarometerDataPort;
            /* Compose sensor data item from individual ports */
            flow gpsPort.gpsData to fcPort.sensorData.gps;
            flow imuPort.imuData to fcPort.sensorData.imu;
            flow baroPort.baroData to fcPort.sensorData.baro;
        }

        interface def PowerInterface {
            end port provider : PowerPort;
            end port consumer : ~PowerPort;
            flow provider.voltage to consumer.voltage;
            flow provider.current to consumer.current;
        }

        /* ----- Logical Structure Composition ----- */
        part def DroneLogical {
            doc /* Logical decomposition of the drone into subsystems. */
            part flightController : FlightController;
            part powerSystem : PowerSystem;
            part propulsion : PropulsionSystem;
            part sensors : SensorSuite;
            part video : VideoSystem;

            /* Internal connections using binding bind syntax */
            binding bind flightController.motorCmdsOut = propulsion.motorCmdIn;
            binding bind powerSystem.powerOut = propulsion.powerIn;
            binding bind sensors.gpsOut = flightController.sensorDataIn.sensorData.gps;
            binding bind sensors.imuOut = flightController.sensorDataIn.sensorData.imu;
            binding bind sensors.baroOut = flightController.sensorDataIn.sensorData.baro;

            /* Delegate external ports */
            port cmdIn : ~ControlPort;
            port videoStreamOut : VideoStreamPort;
            binding bind cmdIn = flightController.cmdIn;
            binding bind videoStreamOut = video.videoOut;
        }
    }

    /* =========================== PHYSICAL DOMAIN (IMPLEMENTATION) =========================== */
    package Physical {
        doc /* Technology‑specific physical components, allocation to logical architecture, and verification. */

        /* ----- Physical Port Definitions ----- */
        port def PowerConnector {
            out voltage : ISQ::voltage;
            out current : ISQ::electricCurrent;
        }
        port def ESCPWM {
            in pwm : Real;
        }
        port def I2CDataPort {
            inout scl : Boolean;
            inout sda : Boolean;
        }
        port def UARTDataPort {
            out tx : byte;
            in rx : byte;
        }
        port def RadioControlPort {
            in channels : Integer[16];
        }

        /* ----- Items ----- */
        item def BatteryCell;
        item def SoftwareFirmware;

        /* ----- Physical Components ----- */
        part def LipoBattery {
            doc /* 3S 1500mAh lithium‑polymer battery. */
            attribute nominalVoltage : ISQ::voltage = 11.1 [V];
            attribute chargeCapacity : ISQ::electricCharge = 1500 [ProjectUnits::mAh];
            attribute maxDischargeCurrent : ISQ::electricCurrent = 20 [A];
            port pwrOut : PowerConnector;
            port senseOut : Logical::VoltageSensePort;
        }

        part def BrushlessMotor {
            doc /* 2300KV brushless DC motor. */
            attribute kV : Real = 2300.0;
            port pwrIn : ~PowerConnector;
            port cmdIn : ESCPWM;
        }

        part def ESC {
            doc /* Electronic Speed Controller for one motor. */
            port pwmIn : ~ESCPWM;
            port pwrOut : PowerConnector;
            port pwrIn : ~PowerConnector;  /* added to receive power from battery */
        }

        part def Propeller {
            attribute diameter : ISQ::length = 0.127 [m];  /* 5 inches converted to meters */
            attribute pitch : ISQ::length = 0.1143 [m];    /* 4.5 inches to meters */
        }

        part def FlightControllerBoard {
            doc /* STM32F405‑based flight controller running ArduPilot. */
            port pwrIn : PowerConnector;  /* added to receive power from battery */
            port i2cBus : I2CDataPort;
            port pwmOut1 : ESCPWM;
            port pwmOut2 : ESCPWM;
            port pwmOut3 : ESCPWM;
            port pwmOut4 : ESCPWM;
            port uartGPS : UARTDataPort;
            port radioRx : RadioControlPort;
            item firmware : SoftwareFirmware;
        }

        part def GPSModule {
            doc /* UBlox NEO‑M8N GPS/GLONASS receiver. */
            port uartOut : ~UARTDataPort;
        }

        part def IMUModule {
            doc /* MPU6000 inertial sensor. */
            port i2cOut : ~I2CDataPort;
        }

        part def BarometerModule {
            doc /* BMP280 pressure sensor. */
            port i2cOut : ~I2CDataPort;
        }

        part def CameraModule {
            doc /* 4K CMOS sensor with H.264 encoder. */
            port videoOut : Concept::VideoStreamPort;
            port recordCmd : Logical::RecordCommandPort;
        }

        part def VideoTransmitter {
            doc /* 5.8 GHz analog or digital VTx. */
            port videoIn : ~Concept::VideoStreamPort;
        }

        part def SmartphoneApp {
            doc /* Companion mobile application (Android/iOS). */
            port cmdOut : Concept::ControlPort;
            port videoIn : ~Concept::VideoStreamPort;
        }

        /* ----- Physical Interfaces (with item flows) ----- */
        interface def PowerConnectionInterface {
            end port batteryPort : PowerConnector;
            end port escPort : ~PowerConnector;
            flow batteryPort.voltage to escPort.voltage;
            flow batteryPort.current to escPort.current;
        }

        interface def SensorI2CInterface {
            end port fcPort : I2CDataPort;
            end port sensorPort : ~I2CDataPort;
            flow fcPort.scl to sensorPort.scl;
            flow fcPort.sda to sensorPort.sda;
        }

        interface def GPSUARTInterface {
            end port fcPort : UARTDataPort;
            end port gpsPort : ~UARTDataPort;
            flow fcPort.tx to gpsPort.tx;
            flow gpsPort.rx to fcPort.rx;
        }

        /* ----- Physical System Composition ----- */
        part def DronePhysical {
            doc /* Complete physical assembly of the drone. */
            part battery : LipoBattery;
            part flightCtrl : FlightControllerBoard;
            part gps : GPSModule;
            part imu : IMUModule;
            part baro : BarometerModule;
            part camera : CameraModule;
            part vtx : VideoTransmitter;
            part motor1 : BrushlessMotor;
            part motor2 : BrushlessMotor;
            part motor3 : BrushlessMotor;
            part motor4 : BrushlessMotor;
            part esc1 : ESC;
            part esc2 : ESC;
            part esc3 : ESC;
            part esc4 : ESC;
            part prop1 : Propeller;
            part prop2 : Propeller;
            part prop3 : Propeller;
            part prop4 : Propeller;

            /* Internal connections using binding bind (no indices) */
            binding bind flightCtrl.pwmOut1 = esc1.pwmIn;
            binding bind flightCtrl.pwmOut2 = esc2.pwmIn;
            binding bind flightCtrl.pwmOut3 = esc3.pwmIn;
            binding bind flightCtrl.pwmOut4 = esc4.pwmIn;
            binding bind esc1.pwrOut = motor1.pwrIn;
            binding bind esc2.pwrOut = motor2.pwrIn;
            binding bind esc3.pwrOut = motor3.pwrIn;
            binding bind esc4.pwrOut = motor4.pwrIn;
            binding bind battery.pwrOut = flightCtrl.pwrIn;
            binding bind battery.pwrOut = esc1.pwrIn;
            binding bind battery.pwrOut = esc2.pwrIn;
            binding bind battery.pwrOut = esc3.pwrIn;
            binding bind battery.pwrOut = esc4.pwrIn;
            binding bind gps.uartOut = flightCtrl.uartGPS;
            binding bind imu.i2cOut = flightCtrl.i2cBus;
            binding bind baro.i2cOut = flightCtrl.i2cBus;
            binding bind camera.videoOut = vtx.videoIn;

            /* External ports */
            port cmdWireless : ~Concept::ControlPort;
            port videoAntenna : Concept::VideoStreamPort;
            binding bind cmdWireless = flightCtrl.radioRx;
            binding bind videoAntenna = vtx.videoIn;
        }

        part def GroundPhysical {
            part phoneApp : SmartphoneApp;
            part rcReceiver : RadioReceiver;
            part videoReceiver : VideoReceiver;
        }

        part def RadioReceiver;
        part def VideoReceiver;

        /* ----- Allocation (Logical → Physical) - must be between usages ----- */
        package AllocationContext {
            part myLogical : Logical::DroneLogical;
            part myPhysical : Physical::DronePhysical;

            allocate myPhysical.flightCtrl to myLogical.flightController;
            allocate myPhysical.gps to myLogical.sensors;
            allocate myPhysical.imu to myLogical.sensors;
            allocate myPhysical.baro to myLogical.sensors;
            allocate myPhysical.camera to myLogical.video;
            allocate myPhysical.vtx to myLogical.video;
            allocate myPhysical.battery to myLogical.powerSystem;
            allocate myPhysical.motor1 to myLogical.propulsion;
            allocate myPhysical.motor2 to myLogical.propulsion;
            allocate myPhysical.motor3 to myLogical.propulsion;
            allocate myPhysical.motor4 to myLogical.propulsion;
            allocate myPhysical.esc1 to myLogical.propulsion;
            allocate myPhysical.esc2 to myLogical.propulsion;
            allocate myPhysical.esc3 to myLogical.propulsion;
            allocate myPhysical.esc4 to myLogical.propulsion;
            /* phoneApp allocation would involve ground station, omitted here for simplicity */
        }
    }

    /* =========================== VIEWS =========================== */
    package Views {
        doc /* Reusable and concrete views to visualize the drone model. */

        /* Base Views pattern */
        package <BV> BaseViews {
            private import DS_Views::SymbolicViewsByExpression::*;
            private import DS_Views::TabularViews::*;
            private import SysML::Systems::*;

            view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @PartDefinition;
                filter @PartUsage;
            }
            view requirementsTreeView : RequirementsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;
            view allocationTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @AllocationUsage;
            }
            view stateMachineView : StatesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
            view graphicalView : DS_Views::SymbolicViews::gv, EssentialElementsFilter, NonStandardLibraryElementFilter;
        }

        /* Concrete Views for Concept */
        package ConceptViews {
            view conceptContextDiagram :> BV::partsTreeView {
                expose DroneSystem::Concept::Drone;
                expose DroneSystem::Concept::GroundControl;
                expose DroneSystem::Concept::Environment;
            }
            view useCases :> BV::graphicalView {
                expose DroneSystem::Concept::**;
            }
            view requirementsTable :> BV::requirementsTreeView {
                expose DroneSystem::Concept::Requirements::**;
            }
        }

        /* Concrete Views for Logical */
        package LogicalViews {
            view logicalStructure :> BV::partsTreeView {
                expose DroneSystem::Logical::DroneLogical;
                expose DroneSystem::Logical::**;
            }
            view flightStateMachine :> BV::stateMachineView {
                expose DroneSystem::Logical::FlightController::FlightStateMachine;
            }
        }

        /* Concrete Views for Physical */
        package PhysicalViews {
            view physicalAssembly :> BV::partsTreeView {
                expose DroneSystem::Physical::DronePhysical;
                expose DroneSystem::Physical::**;
            }
            view allocationMatrix :> BV::allocationTableView {
                expose DroneSystem::Physical::AllocationContext::**;
            }
            view satisfactionTable :> BV::graphicalView {
                expose DroneSystem::Physical::**;
                filter @SatisfyRequirementUsage;
            }
        }
    }
}