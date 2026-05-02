package ToasterSystem {
    private import ScalarValues::*;
    private import SI::*;
    private import ISQ::*;
    private import Time::*;
    private import DS_Views::SymbolicViewsByExpression::*;
    private import DS_Views::TabularViews::*;
    private import SysML::Systems::*;

    /* =======================================================
       BASE VIEWS – reusable filtered views for the whole model
    ========================================================= */
    package BaseViews {
        view partsView : UsagesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
        view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @PartDefinition;
            filter @PartUsage;
        }
        view actionsTreeView : ActionsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;
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

    /* ==============================
       CONCEPT EXPLORATION
    ================================ */
    package ConceptExploration {
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
                doc /* User toasts a bagel halve with only cut side heated. */
            }
        }
        use case def CancelCycle {
            subject toaster : ToasterSystemRoot;
            actor user : Person;
            objective {
                doc /* User cancels ongoing toasting at any time. */
            }
        }

        /* -- Stakeholder & Actor Definitions -- */
        part def Person;

        /* -- Viewpoint -- */
        viewpoint def ToasterUserViewpoint {
            doc /* Stakeholder concerns: safe, easy toast/bagel preparation. */
        }

        /* -- Requirements (all as usages) -- */
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
                attribute maxSurfaceTemp : ThermodynamicTemperatureValue = 45 [°C];
            }
            requirement <'REQ-SAF-02'> 'Auto Shut-Off' : SafetyRequirement {
                doc /* The system shall automatically disconnect heating elements if a thermal runaway condition is detected. */
            }
            requirement <'REQ-SAF-03'> 'Electrical Safety' : SafetyRequirement {
                doc /* The system shall comply with UL 1026 standard. */
            }

            requirement <'REQ-DIM-01'> 'Size' : PerformanceRequirement {
                doc /* Overall dimensions shall not exceed 30 cm × 20 cm × 20 cm. */
                attribute maxLength : LengthValue = 30 [cm];
                attribute maxWidth : LengthValue = 20 [cm];
                attribute maxHeight : LengthValue = 20 [cm];
            }
        }

        /* -- Views for Concept Exploration -- */
        view UseCaseDiagram : BaseViews::partsView {
            expose ConceptExploration::ToastBread;
            expose ConceptExploration::ToastBagel;
            expose ConceptExploration::CancelCycle;
        }
        view RequirementsTree : BaseViews::requirementsTreeView {
            expose ConceptExploration::Requirements::**;
        }
    }

    /* ==============================
       LOGICAL DESIGN
    ================================ */
    package LogicalDesign {
        private import ConceptExploration::Requirements::*;
        private import ScalarValues::*;
        private import SI::*;

        /* -- Logical Part Definitions (technology‑agnostic) -- */
        part def HeatingSubsystem;
        part def TimingControlSubsystem;
        part def CarriageMechanism;
        part def UserInterfaceSubsystem;
        part def SafetySubsystem;

        /* -- Logical Port Definitions -- */
        port def PowerPort {
            out power : ElectricPower;
        }
        port def ~PowerPort {
            in power : ElectricPower;
        }
        port def ControlSignal {
            out activate : Boolean;
        }
        port def ~ControlSignal {
            in activate : Boolean;
        }
        port def CarriageStatus {
            out isDown : Boolean;
            out isUp : Boolean;
        }
        port def ~CarriageStatus {
            in isDown : Boolean;
            in isUp : Boolean;
        }
        port def UserSettings {
            out darknessLevel : Integer;
            out bagelMode : Boolean;
            out cancelPressed : Boolean;
        }
        port def ~UserSettings {
            in darknessLevel : Integer;
            in bagelMode : Boolean;
            in cancelPressed : Boolean;
        }

        /* -- Logical Interfaces -- */
        interface def PowerToHeater {
            end source : PowerPort;
            end sink : ~PowerPort;
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

        /* -- Logical System Composite -- */
        part def LogicalToaster {
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

            /* internal connections */
            interface powerConn : PowerToHeater {
                end source = wallPlug;   /* to be allocated later */
                end sink = heating.powerIn;
            }
            interface ctrlConn : ControlToHeater connect timing.ctrlOut to heating.ctrlIn;
            interface carriageConn : CarriageToControl connect carriage.statusOut to timing.carriageIn;
            interface uiConn : UserToControl connect ui.settingsOut to timing.uiIn;
        }

        /* -- Logical State Machine -- */
        state def ToasterStates {
            entry;
            then Idle;

            state Idle;
            state Toasting;
            state Cancelled;
            state Error;

            transition idle_to_toasting
                first Idle
                accept when leverDown && !errorDetected
                then Toasting;

            transition toasting_to_cancelled
                first Toasting
                accept cancelActivated
                then Cancelled;

            transition cancelled_to_idle
                first Cancelled
                do action stopHeating
                then Idle;

            transition toasting_to_idle
                first Toasting
                accept timerExpired
                do action stopHeating
                then Idle;

            transition any_to_error
                first Idle, Toasting, Cancelled
                accept overTempDetected
                then Error;
        }

        /* -- Logical System Root Usage -- */
        part logicalToaster : LogicalToaster {
            satisfy all Requirement usages by parts;
            /* Specific satisfies (mapped later via allocation) */
        }

        /* -- Views for Logical Design -- */
        view LogicalPartsTree : BaseViews::partsTreeView {
            expose LogicalDesign::LogicalToaster::**;
        }
        view LogicalStates : BaseViews::statesNestedView {
            expose LogicalDesign::ToasterStates::**;
        }
    }

    /* ==============================
       PHYSICAL DESIGN
    ================================ */
    package PhysicalDesign {
        private import SI::*;
        private import ScalarValues::*;

        part def NichromeHeatingElement;
        part def BimetallicTimer;
        part def ElectromagnetLatch;
        part def ReturnSpring;
        part def PushButton;
        part def RotaryKnob;
        part def ThermalFuse;
        part def SteelHousing;
        part def PowerCord;

        port def MainsPlug : PowerPort;
        port def Terminals : ~PowerPort;

        part def PhysicalToaster {
            part outerElements[2] : NichromeHeatingElement {
                port powerIn : Terminals;
            }
            part innerElements[2] : NichromeHeatingElement {
                port powerIn : Terminals;
            }
            part timer : BimetallicTimer {
                port inputContacts : Terminals;
                port outputContacts : PowerPort;
            }
            part latch : ElectromagnetLatch;
            part spring : ReturnSpring;
            part bagelButton : PushButton;
            part cancelButton : PushButton;
            part darknessKnob : RotaryKnob;
            part fuse : ThermalFuse {
                port in : Terminals;
                port out : PowerPort;
            }
            part housing : SteelHousing;
            part cord : PowerCord {
                port plug : MainsPlug;
                port wire : Terminals;
            }
            /* internal wiring and assembly connections */
            connect cord.wire to fuse.in;
            connect fuse.out to timer.inputContacts;
            connect timer.outputContacts to outerElements.powerIn;
            /* Bagel mode wiring: only inner elements activated via separate switch */
            /* (abstracted) */
        }

        part physicalToaster : PhysicalToaster;

        /* -- Allocation from Logical to Physical -- */
        package Allocation {
            private import LogicalDesign::LogicalToaster::*;
            private import PhysicalDesign::PhysicalToaster::*;

            allocate physicalToaster.outerElements to logicalToaster.heating;
            allocate physicalToaster.innerElements to logicalToaster.heating;
            allocate physicalToaster.timer to logicalToaster.timing;
            allocate physicalToaster.bagelButton to logicalToaster.ui;
            allocate physicalToaster.cancelButton to logicalToaster.ui;
            allocate physicalToaster.darknessKnob to logicalToaster.ui;
            allocate physicalToaster.latch to logicalToaster.carriage;
            allocate physicalToaster.spring to logicalToaster.carriage;
            allocate physicalToaster.fuse to logicalToaster.safety;
            allocate physicalToaster.housing to logicalToaster.ui; /* housing provides mounting for UI */
            allocate physicalToaster.cord to logicalToaster.heating;
        }

        /* -- Views for Physical Design -- */
        view PhysicalPartsTree : BaseViews::partsTreeView {
            expose PhysicalDesign::PhysicalToaster::**;
        }
        view AllocationTable : BaseViews::allocationTableView {
            expose PhysicalDesign::Allocation::**;
        }
    }

    /* ==============================
       TRACEABILITY & SATISFACTION
    ================================ */
    package Traceability {
        private import ConceptExploration::Requirements::*;
        private import LogicalDesign::LogicalToaster::*;
        private import PhysicalDesign::PhysicalToaster::*;

        /* Satisfy requirements from logical parts */
        satisfy 'Two Slot Toasting' by logicalToaster.heating;
        satisfy 'Bagel Mode' by logicalToaster.ui;
        satisfy 'Browning Control' by logicalToaster.timing;
        satisfy 'Auto Pop-Up' by logicalToaster.carriage;
        satisfy 'Manual Cancel' by logicalToaster.ui;
        satisfy 'Cycle Time' by logicalToaster.timing;
        satisfy 'Exterior Temperature' by logicalToaster.safety;
        satisfy 'Auto Shut-Off' by logicalToaster.safety;
        satisfy 'Electrical Safety' by logicalToaster.safety;
        satisfy 'Size' by logicalToaster.heating;  /* housing dimensions constrain heating size */

        /* Re‑satisfy some requirements from physical components to illustrate full trace */
        satisfy 'Two Slot Toasting' by physicalToaster.outerElements;
        satisfy 'Bagel Mode' by physicalToaster.bagelButton;
        satisfy 'Browning Control' by physicalToaster.darknessKnob;
        satisfy 'Auto Pop-Up' by physicalToaster.spring;
        satisfy 'Manual Cancel' by physicalToaster.cancelButton;
        satisfy 'Auto Shut-Off' by physicalToaster.fuse;
        satisfy 'Electrical Safety' by physicalToaster.fuse;
        satisfy 'Exterior Temperature' by physicalToaster.housing;
    }

    /* ==============================
       GLOBAL VIEWS FOR THE SYSTEM
    ================================ */
    view SystemPartsOverview : BaseViews::partsView {
        expose LogicalDesign::LogicalToaster::**;
        expose PhysicalDesign::PhysicalToaster::**;
    }

    view AllRequirementsTree : BaseViews::requirementsTreeView {
        expose ConceptExploration::Requirements::**;
        expose Traceability::**;
    }
}