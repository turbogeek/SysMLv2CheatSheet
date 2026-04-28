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
        
        use case def StopAlarm {
            subject system : AlarmClock;
            actor user : User;
        }
        
        use case def SnoozeAlarm {
            subject system : AlarmClock;
            actor user : User;
        }
        
        use case def SetTime {
            subject system : AlarmClock;
            actor user : User;
        }
        
        use case def SetDate {
            subject system : AlarmClock;
            actor user : User;
        }
        
        use case def SetTimezone {
            subject system : AlarmClock;
            actor user : User;
        }
        
        use case def FireAlarm {
            subject system : AlarmClock;
            actor user : User;
        }
    }
    
    package ConceptDefinition {
        private import AlarmClockSystem::ConceptExploration::*;
        
        requirement def FunctionalRequirement;
        requirement def NonFunctionalRequirement;
        requirement def ConstraintRequirement;
        
        requirement REQ_FUNC_01 : FunctionalRequirement {
            doc /* The system shall display the current time continuously. */
        }
        
        requirement REQ_FUNC_02 : FunctionalRequirement {
            doc /* The system shall allow the user to set an alarm time. */
        }
        
        requirement REQ_FUNC_03 : FunctionalRequirement {
            doc /* The system shall sound an alarm when the current time matches the alarm time. */
        }
        
        requirement REQ_FUNC_04 : FunctionalRequirement {
            doc /* The system shall allow the user to stop an active alarm. */
        }
        
        requirement REQ_FUNC_05 : FunctionalRequirement {
            doc /* The system shall allow the user to snooze an active alarm, temporarily silencing it. */
        }
        
        requirement REQ_FUNC_06 : FunctionalRequirement {
            doc /* The system shall allow the user to set the current time, date, and timezone. */
        }
        
        requirement REQ_FUNC_07 : FunctionalRequirement {
            doc /* The system shall monitor the environment for smoke or fire. */
        }
        
        requirement REQ_FUNC_08 : FunctionalRequirement {
            doc /* The system shall trigger a distinct, high-priority alarm when fire is detected. */
        }
        
        requirement REQ_NF_01 : NonFunctionalRequirement {
            doc /* The alarm shall be at least 70 dB to ensure it is heard. */
        }
        
        requirement REQ_NF_02 : NonFunctionalRequirement {
            doc /* The system shall trigger the alarm accurately when the set time arrives. */
        }
        
        requirement REQ_NF_03 : NonFunctionalRequirement {
            doc /* The fire detection system must operate with high reliability and minimal false positives. */
        }
        
        requirement REQ_CON_01 : ConstraintRequirement {
            doc /* The system must operate on standard household power (or battery backup). */
        }
    }
    
    package LogicalDesign {
        private import AlarmClockSystem::ConceptDefinition::*;
        
        port def TimePort {
            out currentTime : Real;
            out currentDate : String;
            out currentTimezone : String;
        }
        
        port def TriggerPort {
            out triggerSignal : Boolean;
            out isFireAlarm : Boolean;
        }
        
        port def InputPort {
            out userInput : Real;
            out stopCommand : Boolean;
            out snoozeCommand : Boolean;
        }
        
        port def FireSensorPort {
            out fireDetected : Boolean;
        }
        
        part def TimekeepingSubsystem {
            port timeOut : TimePort;
        }
        
        part def DisplaySubsystem {
            port timeIn : ~TimePort;
        }
        
        part def EnvironmentalMonitoringSubsystem {
            port fireOut : FireSensorPort;
        }
        
        part def AlarmSubsystem {
            port timeIn : ~TimePort;
            port fireIn : ~FireSensorPort;
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
            part envMonitor : EnvironmentalMonitoringSubsystem;
            
            bind timekeeper.timeOut = display.timeIn;
            bind timekeeper.timeOut = alarm.timeIn;
            bind ui.userInputOut = alarm.userInputIn;
            bind envMonitor.fireOut = alarm.fireIn;
            bind alarm.alarmTriggerOut = sound.triggerIn;
            
            satisfy REQ_FUNC_01 by display;
            satisfy REQ_FUNC_02 by ui;
            satisfy REQ_FUNC_03 by alarm;
            satisfy REQ_FUNC_04 by ui;
            satisfy REQ_FUNC_05 by ui;
            satisfy REQ_FUNC_06 by ui;
            satisfy REQ_FUNC_07 by envMonitor;
            satisfy REQ_FUNC_08 by alarm;
            satisfy REQ_NF_01 by sound;
            satisfy REQ_NF_03 by envMonitor;
        }
        
        state def AlarmClockStates {
            entry;
            then normalState;
            
            state normalState;
            state settingState;
            state alarmingState;
            state snoozingState;
            state fireAlarmingState;
            
            transition normal_to_setting
                first normalState
                if true
                then settingState;
                
            transition setting_to_normal
                first settingState
                if true
                then normalState;
                
            transition normal_to_alarming
                first normalState
                if true
                then alarmingState;
                
            transition alarming_to_normal
                first alarmingState
                if true
                then normalState;
                
            transition alarming_to_snoozing
                first alarmingState
                if true
                then snoozingState;
                
            transition snoozing_to_alarming
                first snoozingState
                if true
                then alarmingState;
                
            transition to_fire_alarm
                first normalState
                if true
                then fireAlarmingState;
                
            transition fire_to_normal
                first fireAlarmingState
                if true
                then normalState;
        }
    }
    
    package PhysicalDesign {
        private import AlarmClockSystem::LogicalDesign::*;
        
        part def Microcontroller;
        part def LCDDisplay;
        part def Speaker;
        part def Buttons;
        part def PowerSupply;
        part def SmokeDetector;
        
        // Down-selected specific components
        part def ESP32_Microcontroller :> Microcontroller;
        part def Philips_LEDDisplay :> LCDDisplay;
        part def Murata_PiezoBuzzer :> Speaker;
        part def Omron_TactileSwitches :> Buttons;
        part def MeanWell_PowerSupply :> PowerSupply;
        part def FirstAlert_PhotoelectricSensor :> SmokeDetector;
        
        part def AlarmClockPhysical {
            part mcu : ESP32_Microcontroller;
            part screen : Philips_LEDDisplay;
            part spkr : Murata_PiezoBuzzer;
            part btns : Omron_TactileSwitches;
            part power : MeanWell_PowerSupply;
            part smokeSensor : FirstAlert_PhotoelectricSensor;
        }
        
        part logicalClock : AlarmClockLogical;
        part physicalClock : AlarmClockPhysical;
        
        allocate physicalClock.mcu to logicalClock.timekeeper;
        allocate physicalClock.mcu to logicalClock.alarm;
        allocate physicalClock.screen to logicalClock.display;
        allocate physicalClock.spkr to logicalClock.sound;
        allocate physicalClock.btns to logicalClock.ui;
        allocate physicalClock.smokeSensor to logicalClock.envMonitor;
    }
    
    package Views {
        private import AlarmClockSystem::LogicalDesign::*;
        
        view def LogicalArchitectureView {
            expose AlarmClockLogical;
            filter EssentialElementsFilter;
            filter NonStandardLibraryElementFilter;
        }
        
        view logicalView : LogicalArchitectureView;
    }
}
