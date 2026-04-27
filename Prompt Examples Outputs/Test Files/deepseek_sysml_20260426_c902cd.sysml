package ToasterSystem {
    private import ScalarValues::*;
    private import SI::*;
    private import ISQ::*;
    private import ISQElectromagnetism::electricPower;
    private import Time::*;
    private import DS_Views::SymbolicViewsByExpression::*;
    private import DS_Views::TabularViews::*;
    private import SysML::Systems::*;

    /* ---- Base Views (filtered, reusable) ---- */
    package BaseViews {
        view partsView : UsagesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
        view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @PartDefinition;
            filter @PartUsage;
        }
        view requirementsTreeView : RequirementsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;
        view statesNestedView : StatesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
        view partsTableView : gt, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @PartUsage;
        }
        view partDefTableView : gt, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @PartDefinition;
        }
        view requirementTableTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @RequirementUsage;
        }
        view allocationTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @AllocationUsage;
        }
    }

    /* ---- Package of signals (items for events, and actions) ---- */
    package Signals {
        item def TimerExpired;
        item def CancelActivated;
        item def OverTempDetected;
        item def StopHeating;                   /* signal item */
        action def StopHeatingAction;           /* action for state machine effect */
    }

    /* ==============================
       CONCEPT EXPLORATION
    ================================ */
    package ConceptExploration {
        private import ToasterSystem::Signals::*;

        /* -- System under design (subject for use cases) -- */
        part def ToasterSystemRoot;

        /* -- Actors -- */
        part def Person;

        /* -- Use Cases -- */
        use case def ToastBread {
            subject toaster : ToasterSystemRoot;
            actor user : Person;
            objective {
                doc /* User toasts two slices of bread to desired darkness. */
            }
        }
        use case def ToastBagel {
            subject toaster : ToasterSystemRoot;
            actor user : Person;
            objective {
                doc /* User toasts a bagel half with only cut side heated. */
            }
        }
        use case def CancelCycle {
            subject toaster : ToasterSystemRoot;
            actor user : Person;
            objective {
                doc /* User cancels ongoing toasting at any time. */
            }
        }

        /* -- Viewpoint -- */
        viewpoint def ToasterUserViewpoint {
            doc /* Stakeholder concerns: safe, easy toast/bagel preparation. */
        }

        /* -- Requirements -- */
        package Requirements {
            requirement def PerformanceRequirement;
            requirement def SafetyRequirement;
            requirement def FunctionalRequirement;

            requirement <'REQ-FUNC-01'> 'Two Slot Toasting' : FunctionalRequirement {
                doc /* The system shall toast two slices of bread placed in the two slots. */
            }
            requirement <'REQ-FUNC-02'> 'Bagel Mode' : FunctionalRequirement {
                doc /* The system shall provide a bagel mode where only the inner heating elements activate. */
            }
            requirement <'REQ-FUNC-03'> 'Browning Control' : FunctionalRequirement {
                doc /* The system shall allow the user to adjust the browning level. */
            }
            requirement <'REQ-FUNC-04'> 'Auto Pop-Up' : FunctionalRequirement {
                doc /* The system shall automatically release the carriage and stop heating when the toast cycle completes. */
            }
            requirement <'REQ-FUNC-05'> 'Manual Cancel' : FunctionalRequirement {
                doc /* The system shall provide a manual cancel function that stops heating and raises the carriage. */
            }

            requirement <'REQ-PERF-01'> 'Cycle Time' : PerformanceRequirement {
                doc /* Toast cycle time shall not exceed 3 minutes at medium browning setting. */
                attribute cycleTime : DurationValue = 3 [min];
            }
            requirement <'REQ-PERF-02'> 'Browning Consistency' : PerformanceRequirement {
                doc /* Browning level shall not deviate more than 10% across identical settings and repeated cycles. */
                attribute consistencyTolerance : Real = 0.1;
            }

            requirement <'REQ-SAF-01'> 'Exterior Temperature' : SafetyRequirement {
                doc /* No accessible external surface shall exceed 45°C during operation. */
                attribute maxSurfaceTemp : ISQ::thermodynamicTemperature = 45 ['°C'];
            }
            requirement <'REQ-SAF-02'> 'Auto Shut-Off' : SafetyRequirement {
                doc /* The system shall automatically disconnect heating elements if a thermal runaway condition is detected. */
            }
            requirement <'REQ-SAF-03'> 'Electrical Safety' : SafetyRequirement {
                doc /* The system shall comply with UL 1026 standard. */
            }

            requirement <'REQ-DIM-01'> 'Size' : PerformanceRequirement {
                doc /* Overall dimensions shall not exceed 30 cm × 20 cm × 20 cm. */
                attribute maxLength : LengthValue = 30 [cm];
                attribute maxWidth  : LengthValue = 20 [cm];
                attribute maxHeight : LengthValue = 20 [cm];
            }
        }

        view UseCaseDiagram : BaseViews::partsView {
            expose ToastBread;
            expose ToastBagel;
            expose CancelCycle;
        }
        view RequirementsTree : BaseViews::requirementsTreeView {
            expose Requirements::**;
        }
    }

    /* ==============================
       LOGICAL DESIGN
    ================================ */
    package LogicalDesign {
        private import ScalarValues::*;
        private import SI::*;
        private import ISQElectromagnetism::electricPower;
        private import ToasterSystem::Signals::*;
        private import ConceptExploration::Requirements::*;

        /* -- Logical Part Definitions -- */
        part def HeatingSubsystem;
        part def TimingControlSubsystem;
        part def CarriageMechanism;
        part def UserInterfaceSubsystem;
        part def SafetySubsystem;

        /* -- Port Definitions (no conjugation here) -- */
        port def PowerPort {
            out power : electricPower;
        }
        port def ControlSignal {
            out activate : Boolean;
        }
        port def CarriageStatus {
            out isDown : Boolean;
            out isUp : Boolean;
        }
        port def UserSettings {
            out darknessLevel : Integer;
            out bagelMode : Boolean;
            out cancelPressed : Boolean;
        }

        /* -- Interfaces (all ends are port usages) -- */
        interface def PowerToHeater {
            end source : PowerPort;
            end sink : ~PowerPort;   /* conjugated usage */
        }
        interface def ControlToHeater {
            end ctrl : ControlSignal;
            end receiver : ~ControlSignal;
        }
        interface def CarriageToControl {
            end carriage : CarriageStatus;
            end controller : ~CarriageStatus;
        }
        interface def UserToControl {
            end ui : UserSettings;
            end ctrl : ~UserSettings;
        }

        /* -- State Machine for the toaster behaviour -- */
        state def ToasterStates {
            attribute leverDown : ScalarValues::Boolean;
            attribute errorDetected : ScalarValues::Boolean;

            entry;
            then Idle;

            state Idle;
            state Toasting;
            state Cancelled;
            state Error;

            transition idle_to_toasting
                first Idle
                accept when leverDown and not errorDetected
                then Toasting;

            transition toasting_to_cancelled
                first Toasting
                accept cancelActivated : CancelActivated
                then Cancelled;

            transition cancelled_to_idle
                first Cancelled
                do action stopHeating : StopHeatingAction
                then Idle;

            transition toasting_to_idle
                first Toasting
                accept timerExpired : TimerExpired
                do action stopHeating : StopHeatingAction
                then Idle;

            transition idle_to_error
                first Idle
                accept overTempDetected : OverTempDetected
                then Error;
            transition toasting_to_error
                first Toasting
                accept overTempDetected : OverTempDetected
                then Error;
            transition cancelled_to_error
                first Cancelled
                accept overTempDetected : OverTempDetected
                then Error;
        }

        /* -- Logical System Composite Definition -- */
        part def LogicalToaster {
            port wallPlug : PowerPort;

            part heating : HeatingSubsystem {
                port powerIn : ~PowerPort;
                port ctrlIn : ~ControlSignal;
            }
            part timing : TimingControlSubsystem {
                port uiIn : ~UserSettings;
                port carriageIn : ~CarriageStatus;
                port ctrlOut : ControlSignal;
            }
            part carriage : CarriageMechanism {
                port statusOut : CarriageStatus;
            }
            part ui : UserInterfaceSubsystem {
                port settingsOut : UserSettings;
            }
            part safety : SafetySubsystem;

            exhibit state operatingState : ToasterStates {
                bind leverDown = externalLeverDown;
                bind errorDetected = externalErrorDetected;
            }

            interface powerConn : PowerToHeater
                connect wallPlug to heating.powerIn;
            interface ctrlConn : ControlToHeater
                connect timing.ctrlOut to heating.ctrlIn;
            interface carriageConn : CarriageToControl
                connect carriage.statusOut to timing.carriageIn;
            interface uiConn : UserToControl
                connect ui.settingsOut to timing.uiIn;
        }

        attribute externalLeverDown : ScalarValues::Boolean;
        attribute externalErrorDetected : ScalarValues::Boolean;

        /* -- Logical System Usage with satisfy relationships -- */
        part logicalToaster : LogicalToaster {
            satisfy 'Two Slot Toasting'   by heating;
            satisfy 'Bagel Mode'          by ui;
            satisfy 'Browning Control'    by timing;
            satisfy 'Auto Pop-Up'         by carriage;
            satisfy 'Manual Cancel'       by ui;
            satisfy 'Cycle Time'          by timing;
            satisfy 'Exterior Temperature' by safety;
            satisfy 'Auto Shut-Off'       by safety;
            satisfy 'Electrical Safety'   by safety;
            satisfy 'Size'                by heating;
        }

        view LogicalPartsTree : BaseViews::partsTreeView {
            expose LogicalToaster::**;
        }
        view LogicalStates : BaseViews::statesNestedView {
            expose ToasterStates::**;
        }
    }

    /* ==============================
       PHYSICAL DESIGN
    ================================ */
    package PhysicalDesign {
        private import SI::*;
        private import ScalarValues::*;
        private import LogicalDesign::PowerPort;
        private import LogicalDesign::ControlSignal;
        private import LogicalDesign::CarriageStatus;
        private import LogicalDesign::UserSettings;

        /* -- Physical Part Definitions -- */
        part def NichromeHeatingElement {
            port powerIn : ~PowerPort;
        }
        part def BimetallicTimer {
            port inputContacts : ~PowerPort;
            port outputContacts : PowerPort;
        }
        part def ElectromagnetLatch;
        part def ReturnSpring;
        part def PushButton;
        part def RotaryKnob;
        part def ThermalFuse {
            port inPower  : ~PowerPort;
            port outPower : PowerPort;
        }
        part def SteelHousing;
        part def PowerCord {
            port plug : PowerPort;
            port wire : ~PowerPort;
        }

        /* -- Physical Toaster Definition -- */
        part def PhysicalToaster {
            port wallSupply : PowerPort;

            part outerElements[2] : NichromeHeatingElement;
            part innerElements[2] : NichromeHeatingElement;
            part timer : BimetallicTimer;
            part latch : ElectromagnetLatch;
            part spring : ReturnSpring;
            part bagelButton : PushButton;
            part cancelButton : PushButton;
            part darknessKnob : RotaryKnob;
            part fuse : ThermalFuse;
            part housing : SteelHousing;
            part cord : PowerCord;

            connect cord.plug to wallSupply;
            connect cord.wire to fuse.inPower;
            connect fuse.outPower to timer.inputContacts;
            connect timer.outputContacts to innerElements.powerIn;
            connect timer.outputContacts to outerElements.powerIn;
        }

        /* -- Physical System Usage -- */
        part physicalToaster : PhysicalToaster;

        /* -- Allocation (logical to physical) -- */
        package Allocation {
            private import LogicalDesign::logicalToaster;
            private import PhysicalDesign::physicalToaster;

            allocate physicalToaster.outerElements  to logicalToaster.heating;
            allocate physicalToaster.innerElements  to logicalToaster.heating;
            allocate physicalToaster.timer          to logicalToaster.timing;
            allocate physicalToaster.bagelButton    to logicalToaster.ui;
            allocate physicalToaster.cancelButton   to logicalToaster.ui;
            allocate physicalToaster.darknessKnob   to logicalToaster.ui;
            allocate physicalToaster.latch          to logicalToaster.carriage;
            allocate physicalToaster.spring         to logicalToaster.carriage;
            allocate physicalToaster.fuse           to logicalToaster.safety;
            allocate physicalToaster.housing        to logicalToaster.ui;
            allocate physicalToaster.cord           to logicalToaster.heating;
        }

        view PhysicalPartsTree : BaseViews::partsTreeView {
            expose PhysicalToaster::**;
        }
        view AllocationTable : BaseViews::allocationTableView {
            expose Allocation::**;
        }
    }

    /* ==============================
       TRACEABILITY (cross‑cutting)
    ================================ */
    package Traceability {
        private import ConceptExploration::Requirements::*;
        private import LogicalDesign::logicalToaster;
        private import PhysicalDesign::physicalToaster;

        satisfy 'Two Slot Toasting'   by physicalToaster.outerElements;
        satisfy 'Bagel Mode'          by physicalToaster.bagelButton;
        satisfy 'Browning Control'    by physicalToaster.darknessKnob;
        satisfy 'Auto Pop-Up'         by physicalToaster.spring;
        satisfy 'Manual Cancel'       by physicalToaster.cancelButton;
        satisfy 'Auto Shut-Off'       by physicalToaster.fuse;
        satisfy 'Electrical Safety'   by physicalToaster.fuse;
        satisfy 'Exterior Temperature' by physicalToaster.housing;
    }

    /* ==============================
       GLOBAL SYSTEM VIEWS
    ================================ */
    view SystemPartsOverview : BaseViews::partsView {
        expose LogicalDesign::logicalToaster::**;
        expose PhysicalDesign::physicalToaster::**;
    }
    view AllRequirementsTree : BaseViews::requirementsTreeView {
        expose ConceptExploration::Requirements::**;
        expose Traceability::**;
    }
}