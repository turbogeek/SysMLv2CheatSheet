/*
 * Alarm Clock — Reference SysMLv2 Model
 *
 * Companion files:
 *   01_alarm_clock_discovery.md      — INCOSE concept-stage discovery document
 *   02_alarm_clock_requirements.md   — StR-XX and SR-XX requirements
 *
 * Layout follows MagicGrid:
 *   ConceptExploration  — problem domain (stakeholders, needs, use cases, context)
 *   ConceptDefinition   — black-box solution domain (system boundary, system requirements)
 *   LogicalDesign       — white-box, technology-agnostic logical architecture
 *   PhysicalDesign      — white-box, technology-specific physical architecture
 *   AllocationsAndSatisfactions — cross-cutting allocations and satisfaction relationships
 *   Views               — base views and concrete views per package
 *
 * Coding-standards conformance:
 *   - All real requirements are usages with <'ID'> 'Short Name' and a doc /* shall ... */
 *   - No '//' comments anywhere
 *   - private imports throughout
 *   - ISQ quantity types used for engineering values
 *   - allocate / satisfy connect usages only
 *   - Definitions in library-style packages, usages in model-context packages
 */

package AlarmClockModel {

    /* ============================================================
     * Requirement type definitions (used as types for requirement usages)
     * ============================================================ */
    package <RT> RequirementTypes {
        doc /* Reusable requirement-type definitions for the alarm clock project. Real
             * project requirements are usages typed by these defs, never defs themselves.
             */

        requirement def StakeholderRequirement {
            doc /* A need expressed from the stakeholder's vantage. Technology-agnostic. */
        }

        requirement def FunctionalRequirement {
            doc /* What the system shall do, expressed from the system's vantage. */
        }

        requirement def PerformanceRequirement {
            doc /* A quantitative threshold on a functional behavior. */
        }

        requirement def InterfaceRequirement {
            doc /* A constraint on an external interface of the black-box system. */
        }

        requirement def EnvironmentalRequirement {
            doc /* A constraint on operating environment, form factor, or safety. */
        }
    }

    /* ============================================================
     * Project-local attribute definitions (small, deliberate)
     * ============================================================ */
    package AttributeDefs {
        private import ScalarValues::Integer;
        private import ScalarValues::Boolean;

        doc /* Small project-local attribute defs needed across the model. Physical
             * quantities use ISQ kinds directly and do not appear here.
             */

        attribute def TimeOfDay {
            doc /* Wall-clock time of day in 24-hour form. */
            attribute hour : Integer;
            attribute minute : Integer;
        }

        attribute def AlarmConfiguration {
            doc /* The current alarm configuration: target time and whether it is armed. */
            attribute alarmTime : TimeOfDay;
            attribute alarmEnabled : Boolean;
        }
    }

    /* ============================================================
     * MagicGrid: ConceptExploration  (problem domain)
     * ============================================================ */
    package <CE> ConceptExploration {
        private import RT::*;
        private import AttributeDefs::*;
        private import ScalarValues::*;

        doc /* Problem-domain content from the discovery document: actors, stakeholder
             * needs as requirement usages, top-level use cases, and the system context.
             */

        /* ----------------------------------------------------------
         * Actors (technology-agnostic types referenced by use cases
         * and by the system context).
         * ---------------------------------------------------------- */
        package Actors {
            doc /* External actor types for the alarm clock. Per skill, actor / stakeholder
                 * are usage keywords; their types are part defs. */

            part def User {
                doc /* The end user of the alarm clock. */
            }

            part def MainsAdapter {
                doc /* External Class II AC-DC adapter providing DC input to the clock. */
            }
        }

        /* ----------------------------------------------------------
         * Stakeholder requirements (StR-XX) — usages, never defs.
         * Mirrors §3 of the requirements document.
         * ---------------------------------------------------------- */
        package StakeholderNeeds {
            private import Actors::*;

            doc /* Stakeholder requirements traced from discovery-document needs. */

            requirement <'StR-01'> 'Read Time At A Glance' : StakeholderRequirement {
                doc /* The user shall be able to read the current time of day at a glance
                     * from across a bedroom. */
                stakeholder user : User;
            }

            requirement <'StR-02'> 'Set Current Time' : StakeholderRequirement {
                doc /* The user shall be able to set the system's current time. */
                stakeholder user : User;
            }

            requirement <'StR-03'> 'Set And Toggle Alarm' : StakeholderRequirement {
                doc /* The user shall be able to set the alarm time and enable or disable
                     * the alarm. */
                stakeholder user : User;
            }

            requirement <'StR-04'> 'Audible Alert At Alarm Time' : StakeholderRequirement {
                doc /* The system shall produce an audible alert at the set alarm time when
                     * the alarm is enabled. */
                stakeholder user : User;
            }

            requirement <'StR-05'> 'Silence Alarm' : StakeholderRequirement {
                doc /* The user shall be able to silence the audible alert until the next
                     * alarm time. */
                stakeholder user : User;
            }

            requirement <'StR-06'> 'Snooze Alarm' : StakeholderRequirement {
                doc /* The user shall be able to suspend (snooze) the audible alert for a
                     * fixed interval. */
                stakeholder user : User;
            }

            requirement <'StR-07'> 'Ride Through Power Loss' : StakeholderRequirement {
                doc /* The system shall preserve current time and alarm settings during brief
                     * power interruptions. */
                stakeholder user : User;
            }

            requirement <'StR-08'> 'Legible In Low Light' : StakeholderRequirement {
                doc /* The system display shall remain legible in low ambient light. */
                stakeholder user : User;
            }

            requirement <'StR-09'> 'Mains Safe Operation' : StakeholderRequirement {
                doc /* The system shall be safe to operate from standard mains power via an
                     * external adapter. */
                stakeholder user : User;
            }

            requirement <'StR-10'> 'Field Replaceable Backup Cell' : StakeholderRequirement {
                doc /* The system's backup cell shall be replaceable in the field without
                     * specialist tools. */
                stakeholder user : User;
            }
        }

        /* ----------------------------------------------------------
         * Top-level use cases — actor-driven scenarios.
         * ---------------------------------------------------------- */
        package UseCases {
            private import Actors::*;

            doc /* Top-level use cases. The subject of every use case is the alarm clock
                 * system; here it is forward-declared as a part def in ConceptDefinition
                 * and re-used via qualified reference. */

            use case def ReadTime {
                doc /* The user reads the current time of day from the display. */
                subject clock : ConceptDefinition::SystemBoundary::AlarmClockSystem;
                actor user : User;
                objective {
                    doc /* User obtains the current time of day. */
                }
            }

            use case def SetCurrentTime {
                doc /* The user adjusts the system's current time. */
                subject clock : ConceptDefinition::SystemBoundary::AlarmClockSystem;
                actor user : User;
                objective {
                    doc /* System now displays the user-specified time as current time. */
                }
            }

            use case def SetAlarmTime {
                doc /* The user sets the alarm time and enables the alarm. */
                subject clock : ConceptDefinition::SystemBoundary::AlarmClockSystem;
                actor user : User;
                objective {
                    doc /* Alarm is armed for the user-specified time. */
                }
            }

            use case def RespondToAlarm {
                doc /* The user silences or snoozes a sounding alarm. */
                subject clock : ConceptDefinition::SystemBoundary::AlarmClockSystem;
                actor user : User;
                objective {
                    doc /* The audible tone is stopped or suspended per user choice. */
                }
            }
        }

        /* ----------------------------------------------------------
         * System context (black box surrounded by external actors).
         * ---------------------------------------------------------- */
        package SystemContext {
            private import Actors::*;

            doc /* Black-box system context: the alarm clock plus its external actors. */

            part def AlarmClockContext {
                doc /* The operational context of the alarm clock. */
                ref part user : User;
                ref part mains : MainsAdapter;
                part clock : ConceptDefinition::SystemBoundary::AlarmClockSystem;
            }

            part alarmClockContext : AlarmClockContext {
                doc /* The deployed context instance used by views. */
            }
        }
    }

    /* ============================================================
     * MagicGrid: ConceptDefinition  (black-box solution domain)
     * ============================================================ */
    package <CD> ConceptDefinition {
        private import RT::*;
        private import AttributeDefs::*;
        private import ScalarValues::*;
        private import ISQ::*;
        private import SI::*;

        doc /* Black-box system: the AlarmClockSystem part def with external ports, plus
             * all SR-XX system requirements as usages. */

        /* ----------------------------------------------------------
         * External port and item definitions used at the system boundary.
         * ---------------------------------------------------------- */
        package BoundaryPortDefs {
            doc /* Port and item definitions for the four external interfaces of the
                 * alarm clock: button input, visual output, audible output, DC power. */

            item def ButtonPress {
                doc /* A discrete user-initiated button press event. */
            }

            item def VisualFrame {
                doc /* A frame of visual content rendered to the user. */
            }

            item def AudibleTone {
                doc /* An audible alarm tone delivered to the user. */
            }

            item def DcPower {
                doc /* DC electrical power delivered from the external adapter. */
            }

            port def UserInputPort {
                doc /* Port through which user button-press events enter the system. */
                in buttonPressIn : ButtonPress;
            }

            port def VisualOutputPort {
                doc /* Port through which visual frames leave the system. */
                out visualFrameOut : VisualFrame;
            }

            port def AudibleOutputPort {
                doc /* Port through which the alarm tone leaves the system. */
                out audibleToneOut : AudibleTone;
            }

            port def DcPowerInPort {
                doc /* Port through which DC power enters the system. */
                in dcPowerIn : DcPower;
            }
        }

        /* ----------------------------------------------------------
         * The AlarmClockSystem black-box part def.
         * ---------------------------------------------------------- */
        package SystemBoundary {
            private import BoundaryPortDefs::*;

            doc /* Black-box definition of the alarm clock system. The internal structure
                 * is intentionally absent here; that is what LogicalDesign elaborates. */

            part def AlarmClockSystem {
                doc /* The simple alarm clock as a black box. Its only externally visible
                     * features are the four boundary ports and the user-observable
                     * current-time and alarm-configuration attributes. */
                port userInput : UserInputPort;
                port visualOutput : VisualOutputPort;
                port audibleOutput : AudibleOutputPort;
                port dcPowerIn : DcPowerInPort;

                attribute currentTime : TimeOfDay;
                attribute alarmConfig : AlarmConfiguration;
            }
        }

        /* ----------------------------------------------------------
         * System requirements (SR-XX) — usages typed by RT defs.
         * Mirrors §§4–7 of the requirements document.
         * ---------------------------------------------------------- */
        package SystemRequirements {
            private import SystemBoundary::*;

            doc /* System-level requirements. Subject of every requirement is the
                 * AlarmClockSystem black box. */

            /* ---- Functional ---- */

            requirement <'SR-F-01'> 'Display Current Time' : FunctionalRequirement {
                doc /* The system shall continuously display the current time of day in
                     * hours and minutes. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-F-02'> 'Accept Set Current Time Input' : FunctionalRequirement {
                doc /* The system shall accept user input to set the current time in hours
                     * and minutes. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-F-03'> 'Accept Set Alarm Time Input' : FunctionalRequirement {
                doc /* The system shall accept user input to set the alarm time in hours
                     * and minutes. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-F-04'> 'Accept Alarm Enable Input' : FunctionalRequirement {
                doc /* The system shall accept user input to enable or disable the alarm. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-F-05'> 'Sound Alarm At Match' : FunctionalRequirement {
                doc /* The system shall, when the alarm is enabled and the current time
                     * equals the alarm time, produce an audible tone. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-F-06'> 'Silence Sounding Alarm' : FunctionalRequirement {
                doc /* The system shall accept user input to silence a sounding alarm
                     * until the next alarm time. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-F-07'> 'Snooze Sounding Alarm' : FunctionalRequirement {
                doc /* The system shall accept user input to snooze a sounding alarm,
                     * suspending the tone for a fixed interval and then resuming. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-F-08'> 'Display Alarm Enabled Indicator' : FunctionalRequirement {
                doc /* The system shall display an indicator showing whether the alarm is
                     * currently enabled. */
                subject clock : AlarmClockSystem;
            }

            /* ---- Performance ---- */

            requirement <'SR-P-01'> 'Time Accuracy' : PerformanceRequirement {
                doc /* The system shall maintain time-of-day accuracy of better than
                     * +/- 1 second per 24-hour period at 25 degrees Celsius. */
                subject clock : AlarmClockSystem;
                attribute maxDailyDrift : ISQ::time = 1 [s];
            }

            requirement <'SR-P-02'> 'Alarm Sound Pressure Level' : PerformanceRequirement {
                doc /* The system shall produce an audible alarm tone of at least 70 dB SPL
                     * measured at 1 metre on-axis. */
                subject clock : AlarmClockSystem;
                attribute minSplAtOneMeter : Real = 70.0;
            }

            requirement <'SR-P-03'> 'Backup Ride Through' : PerformanceRequirement {
                doc /* The system shall preserve current time and alarm settings on backup
                     * power for at least 24 hours. */
                subject clock : AlarmClockSystem;
                attribute minBackupDuration : ISQ::time = 24 [h];
            }

            requirement <'SR-P-04'> 'Snooze Interval' : PerformanceRequirement {
                doc /* The snooze interval shall be 9 minutes plus or minus 5 seconds. */
                subject clock : AlarmClockSystem;
                attribute snoozeNominal : ISQ::time = 9 [min];
                attribute snoozeTolerance : ISQ::time = 5 [s];
            }

            requirement <'SR-P-05'> 'Time To Set Alarm' : PerformanceRequirement {
                doc /* A first-time user shall be able to set a new alarm time within
                     * 15 seconds of starting the task. */
                subject clock : AlarmClockSystem;
                attribute maxSetAlarmTime : ISQ::time = 15 [s];
            }

            /* ---- Interface ---- */

            requirement <'SR-I-01'> 'Push Button Input' : InterfaceRequirement {
                doc /* The system shall provide push-button input for setting time, setting
                     * alarm, hour increment, minute increment, snooze, and off. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-I-02'> 'Digital Visual Display' : InterfaceRequirement {
                doc /* The system shall provide a digital visual display of the current
                     * time and an alarm-enabled indicator. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-I-03'> 'Electroacoustic Alarm Output' : InterfaceRequirement {
                doc /* The system shall provide an electroacoustic output that emits the
                     * alarm tone. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-I-04'> 'External DC Power Input' : InterfaceRequirement {
                doc /* The system shall accept DC input from a Class II external mains
                     * adapter. */
                subject clock : AlarmClockSystem;
            }

            /* ---- Environmental / Physical ---- */

            requirement <'SR-E-01'> 'Operating Temperature Range' : EnvironmentalRequirement {
                doc /* The system shall operate within an ambient temperature range of
                     * 5 to 40 degrees Celsius. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-E-02'> 'Form Factor Bounding Volume' : EnvironmentalRequirement {
                doc /* The system enclosure shall fit within a bounding volume of
                     * 150 mm by 100 mm by 80 mm. */
                subject clock : AlarmClockSystem;
                attribute maxLength : ISQ::length = 150 [mm];
                attribute maxWidth  : ISQ::length = 100 [mm];
                attribute maxHeight : ISQ::length = 80  [mm];
            }

            requirement <'SR-E-03'> 'Mains Safety Compliance' : EnvironmentalRequirement {
                doc /* The system shall comply with applicable mains-powered consumer-
                     * electronics safety standards in the target market. */
                subject clock : AlarmClockSystem;
            }

            requirement <'SR-E-04'> 'User Replaceable Backup Cell' : EnvironmentalRequirement {
                doc /* The backup cell shall be user-replaceable using only a coin or
                     * common screwdriver. */
                subject clock : AlarmClockSystem;
            }
        }
    }

    /* ============================================================
     * MagicGrid: LogicalDesign  (white-box, technology-agnostic)
     * ============================================================ */
    package <LD> LogicalDesign {
        private import AttributeDefs::*;
        private import ScalarValues::*;
        private import ISQ::*;
        private import SI::*;
        private import CD::BoundaryPortDefs::*;

        doc /* Technology-agnostic logical architecture. Each logical part def represents
             * a function the system must perform; no implementation choices are made
             * here. The composite LogicalAlarmClock instance in LogicalArchitecture is
             * what the system requirements are satisfied by, and what the physical
             * architecture is allocated to. */

        /* ----------------------------------------------------------
         * Logical ports between functional blocks.
         * ---------------------------------------------------------- */
        package LogicalPortDefs {
            doc /* Internal logical ports between functional blocks. */

            item def TimeTick {
                doc /* A periodic time-update signal from the time reference. */
            }

            item def UserCommand {
                doc /* An interpreted user command (e.g., set-time, enable-alarm, snooze). */
            }

            item def AlarmTrigger {
                doc /* An assertion that the alarm should be sounding now. */
            }

            port def TimeTickOutPort {
                doc /* Output port emitting time ticks. */
                out tick : TimeTick;
            }

            port def UserCommandOutPort {
                doc /* Output port emitting interpreted user commands. */
                out cmd : UserCommand;
            }

            port def AlarmTriggerOutPort {
                doc /* Output port asserting the alarm should sound. */
                out trigger : AlarmTrigger;
            }
        }

        /* ----------------------------------------------------------
         * Logical part definitions (functions / capabilities).
         * ---------------------------------------------------------- */
        package LogicalPartDefs {
            private import LogicalPortDefs::*;

            doc /* Logical functional units of the alarm clock. */

            part def TimeReferenceFunction {
                doc /* Maintains the current time-of-day and emits periodic time ticks.
                     * Technology-agnostic: a quartz crystal, an atomic reference, or a
                     * software counter all satisfy this. */
                attribute currentTime : TimeOfDay;
                port tickOut : TimeTickOutPort;
            }

            part def UserInputFunction {
                doc /* Receives raw button events and interprets them as user commands. */
                port rawInput : ~UserInputPort;
                port commandOut : UserCommandOutPort;
            }

            part def AlarmLogicFunction {
                doc /* Holds the alarm configuration, watches the time reference, and
                     * asserts the alarm trigger when current time equals alarm time and
                     * the alarm is enabled. Also handles silence and snooze logic. */
                attribute alarmConfig : AlarmConfiguration;
                attribute snoozeDuration : ISQ::time = 9 [min];
                port tickIn : ~TimeTickOutPort;
                port commandIn : ~UserCommandOutPort;
                port triggerOut : AlarmTriggerOutPort;
            }

            part def DisplayFunction {
                doc /* Renders the current time and alarm-enabled indicator to the visual
                     * output port. */
                port tickIn : ~TimeTickOutPort;
                port visualOut : VisualOutputPort;
            }

            part def AudibleAlertFunction {
                doc /* Produces an audible tone whenever the alarm trigger is asserted. */
                port triggerIn : ~AlarmTriggerOutPort;
                port audibleOut : AudibleOutputPort;
            }

            part def PowerSupplyFunction {
                doc /* Distributes DC power to all logical functions. */
                port dcIn : ~DcPowerInPort;
            }

            part def LogicalAlarmClock {
                doc /* The composite logical architecture: all six functional blocks plus
                     * the system's external boundary ports re-exposed. */
                port userInput : UserInputPort;
                port visualOutput : VisualOutputPort;
                port audibleOutput : AudibleOutputPort;
                port dcPowerIn : DcPowerInPort;

                part timeReference : TimeReferenceFunction;
                part userInputFn : UserInputFunction;
                part alarmLogic : AlarmLogicFunction;
                part display : DisplayFunction;
                part audibleAlert : AudibleAlertFunction;
                part powerSupply : PowerSupplyFunction;
            }
        }

        /* ----------------------------------------------------------
         * Logical state machine — alarm-clock operating modes.
         * ---------------------------------------------------------- */
        package LogicalStates {
            doc /* The alarm clock's high-level operating modes, owned by the alarm-logic
                 * function in the deployed architecture. */

            state def AlarmClockMode {
                doc /* Operating modes of the alarm clock. */
                entry; then idle;

                state idle {
                    doc /* Showing current time, alarm not currently sounding. */
                }
                state settingTime {
                    doc /* User is adjusting current time of day. */
                }
                state settingAlarm {
                    doc /* User is adjusting the alarm time and enable flag. */
                }
                state alarming {
                    doc /* The alarm trigger is asserted; tone is being produced. */
                }
                state snoozing {
                    doc /* The alarm has been temporarily suspended; will resume after the
                         * snooze interval. */
                }
            }
        }

        /* ----------------------------------------------------------
         * Logical architecture instance and internal connections.
         * ---------------------------------------------------------- */
        package LogicalArchitecture {
            private import LogicalPartDefs::*;

            doc /* The deployed logical-architecture instance. Internal port connections
                 * wire the functional blocks together. */

            part logicalAlarmClock : LogicalAlarmClock {
                doc /* Internal wiring of the logical functional blocks. */

                exhibit state operatingMode : LogicalStates::AlarmClockMode;

                connect userInput to userInputFn.rawInput;
                connect dcPowerIn to powerSupply.dcIn;

                connect timeReference.tickOut to alarmLogic.tickIn;
                connect timeReference.tickOut to display.tickIn;
                connect userInputFn.commandOut to alarmLogic.commandIn;
                connect alarmLogic.triggerOut to audibleAlert.triggerIn;

                connect display.visualOut to visualOutput;
                connect audibleAlert.audibleOut to audibleOutput;
            }
        }
    }

    /* ============================================================
     * MagicGrid: PhysicalDesign  (white-box, technology-specific)
     * ============================================================ */
    package <PD> PhysicalDesign {
        private import AttributeDefs::*;
        private import ScalarValues::*;
        private import ISQ::*;
        private import SI::*;
        private import CD::BoundaryPortDefs::*;
        private import LD::LogicalPortDefs::*;

        doc /* Technology-specific physical architecture. Every physical part is later
             * allocated to one or more logical parts in AllocationsAndSatisfactions. */

        /* ----------------------------------------------------------
         * Physical part definitions (concrete components).
         * ---------------------------------------------------------- */
        package PhysicalPartDefs {
            doc /* Concrete components implementing the alarm clock. */

            part def RealTimeClockIc {
                doc /* A temperature-compensated real-time clock IC (e.g., DS3231-class)
                     * with battery-backed timekeeping. */
                attribute partNumber : String;
                attribute drift : ISQ::time = 1 [s];
                port tickOut : TimeTickOutPort;
            }

            part def Microcontroller {
                doc /* An 8- or 32-bit microcontroller running the alarm-clock firmware. */
                attribute partNumber : String;
                port tickIn : ~TimeTickOutPort;
                port commandIn : ~UserCommandOutPort;
                port triggerOut : AlarmTriggerOutPort;
                port displayOut : VisualOutputPort;
            }

            part def LcdDisplayModule {
                doc /* A backlit segment LCD module rendering the time and indicators. */
                attribute partNumber : String;
                port displayIn : ~VisualOutputPort;
                port visualOut : VisualOutputPort;
            }

            part def PushButton {
                doc /* A single tactile push button. */
                attribute label : String;
            }

            part def ButtonPanel {
                doc /* The collection of push buttons exposed to the user. */
                part setTimeBtn : PushButton;
                part setAlarmBtn : PushButton;
                part hourBtn : PushButton;
                part minuteBtn : PushButton;
                part snoozeBtn : PushButton;
                part offBtn : PushButton;
                port userInput : UserInputPort;
                port commandOut : UserCommandOutPort;
            }

            part def PiezoBuzzer {
                doc /* A piezoelectric buzzer producing the alarm tone. */
                attribute ratedSpl : Real;
                port triggerIn : ~AlarmTriggerOutPort;
                port audibleOut : AudibleOutputPort;
            }

            part def AcDcAdapterInput {
                doc /* The DC-input jack and downstream regulation feeding the board. */
                attribute nominalVoltage : ISQ::voltage = 5 [V];
                port dcIn : DcPowerInPort;
            }

            part def BackupCell {
                doc /* Coin-cell backup keeping the RTC alive during mains outages. */
                attribute capacity : ISQ::electricCharge;
                attribute rideThrough : ISQ::time = 24 [h];
            }

            part def Enclosure {
                doc /* The external plastic enclosure containing all components. */
                attribute lengthDim : ISQ::length = 140 [mm];
                attribute widthDim  : ISQ::length =  90 [mm];
                attribute heightDim : ISQ::length =  70 [mm];
            }

            part def PhysicalAlarmClock {
                doc /* The composite physical assembly. External ports match the system
                     * boundary ports from ConceptDefinition. */
                port userInput : UserInputPort;
                port visualOutput : VisualOutputPort;
                port audibleOutput : AudibleOutputPort;
                port dcPowerIn : DcPowerInPort;

                part rtc : RealTimeClockIc;
                part mcu : Microcontroller;
                part lcd : LcdDisplayModule;
                part buttons : ButtonPanel;
                part buzzer : PiezoBuzzer;
                part adapterInput : AcDcAdapterInput;
                part backupCell : BackupCell;
                part enclosure : Enclosure;
            }
        }

        /* ----------------------------------------------------------
         * Physical architecture instance and internal wiring.
         * ---------------------------------------------------------- */
        package PhysicalArchitecture {
            private import PhysicalPartDefs::*;

            doc /* The deployed physical-architecture instance. */

            part physicalAlarmClock : PhysicalAlarmClock {
                doc /* Internal wiring of the physical components. */

                connect userInput to buttons.userInput;
                connect dcPowerIn to adapterInput.dcIn;

                connect rtc.tickOut to mcu.tickIn;
                connect buttons.commandOut to mcu.commandIn;
                connect mcu.triggerOut to buzzer.triggerIn;
                connect mcu.displayOut to lcd.displayIn;

                connect lcd.visualOut to visualOutput;
                connect buzzer.audibleOut to audibleOutput;
            }
        }
    }

    /* ============================================================
     * Cross-cutting allocations and satisfactions
     * ============================================================ */
    package AllocationsAndSatisfactions {
        private import LD::LogicalArchitecture::logicalAlarmClock;
        private import PD::PhysicalArchitecture::physicalAlarmClock;
        private import CD::SystemRequirements::*;

        doc /* Physical-to-logical allocations and requirement satisfactions. Per the
             * skill rules, allocate / satisfy connect usages only — never definitions —
             * and live in a model-context (non-library) package. */

        /* ----------------------------------------------------------
         * Physical -> Logical allocations.
         * ---------------------------------------------------------- */
        package PhysicalToLogicalAllocations {
            doc /* Each physical component realizes one logical function. */

            allocate physicalAlarmClock.rtc          to logicalAlarmClock.timeReference;
            allocate physicalAlarmClock.mcu          to logicalAlarmClock.alarmLogic;
            allocate physicalAlarmClock.lcd          to logicalAlarmClock.display;
            allocate physicalAlarmClock.buttons      to logicalAlarmClock.userInputFn;
            allocate physicalAlarmClock.buzzer       to logicalAlarmClock.audibleAlert;
            allocate physicalAlarmClock.adapterInput to logicalAlarmClock.powerSupply;
        }

        /* ----------------------------------------------------------
         * Satisfactions: which logical or physical usage satisfies each SR.
         * ---------------------------------------------------------- */
        package Satisfactions {
            doc /* Requirement satisfactions. Functional/performance/interface SRs are
                 * satisfied by logical-architecture usages where possible; physical-only
                 * concerns (form factor, replaceable cell) are satisfied by physical
                 * usages. */

            satisfy 'SR-F-01' by logicalAlarmClock.display;
            satisfy 'SR-F-02' by logicalAlarmClock.userInputFn;
            satisfy 'SR-F-03' by logicalAlarmClock.userInputFn;
            satisfy 'SR-F-04' by logicalAlarmClock.userInputFn;
            satisfy 'SR-F-05' by logicalAlarmClock.alarmLogic;
            satisfy 'SR-F-06' by logicalAlarmClock.alarmLogic;
            satisfy 'SR-F-07' by logicalAlarmClock.alarmLogic;
            satisfy 'SR-F-08' by logicalAlarmClock.display;

            satisfy 'SR-P-01' by physicalAlarmClock.rtc;
            satisfy 'SR-P-02' by physicalAlarmClock.buzzer;
            satisfy 'SR-P-03' by physicalAlarmClock.backupCell;
            satisfy 'SR-P-04' by logicalAlarmClock.alarmLogic;

            satisfy 'SR-I-01' by physicalAlarmClock.buttons;
            satisfy 'SR-I-02' by physicalAlarmClock.lcd;
            satisfy 'SR-I-03' by physicalAlarmClock.buzzer;
            satisfy 'SR-I-04' by physicalAlarmClock.adapterInput;

            satisfy 'SR-E-02' by physicalAlarmClock.enclosure;
            satisfy 'SR-E-04' by physicalAlarmClock.backupCell;
        }
    }

    /* ============================================================
     * Views — tables and tree views per skill BaseViews pattern
     * ============================================================ */
    package Views {
        private import DS_Views::SymbolicViewsByExpression::*;
        private import DS_Views::SymbolicViews::*;
        private import DS_Views::TabularViews::*;
        private import SysML::Systems::*;

        doc /* Reusable base views and concrete views exposing each MagicGrid package. */

        /* ----------------------------------------------------------
         * Base views — reusable view templates.
         * ---------------------------------------------------------- */
        package <BV> BaseViews {
            doc /* Reusable base views. Concrete views derive from these via :>. */

            view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @PartDefinition;
                filter @PartUsage;
            }

            view partsNestedView : UsagesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;

            view partsTableView : gt, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @PartUsage;
            }

            view partDefTableView : gt, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @PartDefinition;
            }

            view requirementsTreeView : RequirementsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;

            view requirementsTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @RequirementUsage;
            }

            view allocationsTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @AllocationUsage;
            }

            view statesNestedView : StatesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;

            view useCaseTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @UseCaseDefinition;
                filter @UseCaseUsage;
            }

            view symbolicView : gv, EssentialElementsFilter, NonStandardLibraryElementFilter;
        }

        /* ----------------------------------------------------------
         * Concrete views.
         * ---------------------------------------------------------- */
        package ConcreteViews {
            doc /* Concrete views exposing each MagicGrid package and the cross-cutting
                 * relationships. */

            /* ---- Concept Exploration ---- */

            view stakeholderRequirementsTable :> BV::requirementsTableView {
                doc /* Tabular view of all stakeholder requirements (StR-XX). */
                expose CE::StakeholderNeeds::**;
            }

            view stakeholderRequirementsTree :> BV::requirementsTreeView {
                doc /* Tree view of stakeholder requirements. */
                expose CE::StakeholderNeeds::**;
            }

            view useCasesTree :> BV::useCaseTreeView {
                doc /* Tree view of all use cases. */
                expose CE::UseCases::**;
            }

            view systemContextDiagram :> BV::symbolicView {
                doc /* Symbolic view of the system context (clock plus external actors). */
                expose CE::SystemContext::alarmClockContext;
            }

            /* ---- Concept Definition ---- */

            view systemRequirementsTable :> BV::requirementsTableView {
                doc /* Tabular view of all system requirements (SR-XX). */
                expose CD::SystemRequirements::**;
            }

            view systemRequirementsTree :> BV::requirementsTreeView {
                doc /* Tree view of system requirements organized by RT type. */
                expose CD::SystemRequirements::**;
            }

            view systemBoundaryDiagram :> BV::symbolicView {
                doc /* Black-box view of the alarm clock with its four boundary ports. */
                expose CD::SystemBoundary::AlarmClockSystem;
            }

            /* ---- Logical Design ---- */

            view logicalPartsTree :> BV::partsTreeView {
                doc /* Tree view of all logical part defs and usages. */
                expose LD::LogicalPartDefs::**;
            }

            view logicalArchitectureNested :> BV::partsNestedView {
                doc /* Internal nested view of the deployed logical alarm clock. */
                expose LD::LogicalArchitecture::logicalAlarmClock;
            }

            view logicalStatesView :> BV::statesNestedView {
                doc /* Nested view of the alarm-clock operating-mode state machine. */
                expose LD::LogicalStates::AlarmClockMode;
            }

            /* ---- Physical Design ---- */

            view physicalPartsTree :> BV::partsTreeView {
                doc /* Tree view of all physical part defs and usages. */
                expose PD::PhysicalPartDefs::**;
            }

            view physicalArchitectureNested :> BV::partsNestedView {
                doc /* Internal nested view of the deployed physical alarm clock. */
                expose PD::PhysicalArchitecture::physicalAlarmClock;
            }

            view physicalPartsTable :> BV::partsTableView {
                doc /* Tabular view of all physical part usages. */
                expose PD::PhysicalArchitecture::physicalAlarmClock::**;
            }

            /* ---- Cross-cutting ---- */

            view allocationsTable :> BV::allocationsTableView {
                doc /* Tabular view of all physical-to-logical allocations. */
                expose AllocationsAndSatisfactions::PhysicalToLogicalAllocations::**;
            }

            view satisfactionsTable :> BV::allocationsTableView {
                doc /* Tabular view of all requirement satisfactions. */
                expose AllocationsAndSatisfactions::Satisfactions::**;
            }
        }
    }
}
