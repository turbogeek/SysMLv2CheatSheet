package AlarmClockSystem {
    private import ScalarValues::*;
    package ConceptExploration {
        part def User;
        part def AlarmClock;
        use case def ViewTime {
            subject system : AlarmClock;
            actor user : User;
        }
        use case def SetAlarm {
            subject system : AlarmClock;
            actor user : User;
        }
        use case def SoundAlarm {
            subject system : AlarmClock;
            actor user : User;
        }
    }
    package ConceptDefinition {
        private import AlarmClockSystem::ConceptExploration::*;
        requirement def FunctionalRequirement;
        requirement def NonFunctionalRequirement;
        requirement def ConstraintRequirement;
        requirement <'REQ-FUNC-01'> 'Display Time' : FunctionalRequirement {
            doc /* The system shall display the current time continuously. */
        }
        requirement <'REQ-FUNC-02'> 'Set Alarm' : FunctionalRequirement {
            doc /* The system shall allow the user to set an alarm time. */
        }
        requirement <'REQ-FUNC-03'> 'Sound Alarm' : FunctionalRequirement {
            doc /* The system shall sound an alarm when the current time matches the alarm time. */
        }
        requirement <'REQ-NF-01'> Volume : NonFunctionalRequirement {
            doc /* The alarm shall be at least 70 dB to ensure it is heard. */
        }
        requirement <'REQ-CON-01'> Power : ConstraintRequirement {
            doc /* The system must operate on standard household power (or battery backup). */
        }
    }
    package LogicalDesign {
        private import AlarmClockSystem::ConceptDefinition::*;
        port def TimePort {
            out currentTime : Real;
        }
        port def TriggerPort {
            out triggerSignal : Boolean;
        }
        port def InputPort {
            out userInput : Real;
        }
        part def TimekeepingSubsystem {
            port currentTimeOut : TimePort;
        }
        part def DisplaySubsystem {
            port currentTimeIn : ~TimePort;
        }
        part def AlarmSubsystem {
            port currentTimeIn : ~TimePort;
            port alarmTriggerOut : TriggerPort;
            port userInputIn : ~InputPort;
        }
        part def UserInterfaceSubsystem {
            port userInputOut : InputPort;
        }
        part def SoundSubsystem {
            port triggerIn : ~TriggerPort;
        }
        part def AlarmClockLogical {
            part timekeeper : TimekeepingSubsystem;
            part display : DisplaySubsystem;
            part alarm : AlarmSubsystem;
            part ui : UserInterfaceSubsystem;
            part sound : SoundSubsystem;
            bind timekeeper.currentTimeOut = display.currentTimeIn;
            bind timekeeper.currentTimeOut = alarm.currentTimeIn;
            bind ui.userInputOut = alarm.userInputIn;
            bind alarm.alarmTriggerOut = sound.triggerIn;
            satisfy 'REQ-FUNC-01' by display;
            satisfy 'REQ-FUNC-02' by ui;
            satisfy 'REQ-FUNC-03' by alarm;
            satisfy 'REQ-NF-01' by sound;
        }
        state def AlarmClockStates {
            entry;
            then normalState;
            state normalState;
            state settingState;
            state alarmingState;
            transition normal_to_setting first normalState if true then settingState;
            transition setting_to_normal first settingState if true then normalState;
            transition normal_to_alarming first normalState if true then alarmingState;
            transition alarming_to_normal first alarmingState if true then normalState;
        }
    }
    package PhysicalDesign {
        private import AlarmClockSystem::LogicalDesign::*;
        part def Microcontroller;
        part def LCDDisplay;
        part def Speaker;
        part def Buttons;
        part def PowerSupply;
        part def AlarmClockPhysical {
            part mcu : Microcontroller;
            part screen : LCDDisplay;
            part spkr : Speaker;
            part btns : Buttons;
            part power : PowerSupply;
        }
        part logicalClock : AlarmClockLogical;
        part physicalClock : AlarmClockPhysical;
        allocate physicalClock.mcu to logicalClock.timekeeper;
        allocate physicalClock.mcu to logicalClock.alarm;
        allocate physicalClock.screen to logicalClock.display;
        allocate physicalClock.spkr to logicalClock.sound;
        allocate physicalClock.btns to logicalClock.ui;
    }
    library package BaseViews {
        private import DS_Views::SymbolicViewsByExpression::*;
        private import DS_Views::TabularViews::*;
        private import SysML::Systems::*;
        private import DS_Views::**;
        view partsView : UsagesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
        view partsTreeView : gv, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @PartDefinition;
            filter @PartUsage;
        }
        view requirementTableTableView : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @RequirementUsage;
        }
    }
    package Views {
        private import AlarmClockSystem::LogicalDesign::*;
        private import DS_Views::SymbolicViewsByExpression::*;
        private import DS_Views::TabularViews::*;
        private import SysML::Systems::*;
        private import DS_Views::**;
        view partsTreeView : gv, EssentialElementsFilter, NonStandardLibraryElementFilter {
            expose AlarmClockLogical::**;
            filter @PartUsage;
        }
    }
}
