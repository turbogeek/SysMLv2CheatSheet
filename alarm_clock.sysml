package AlarmClockProject {
    private import ScalarValues::*;

    package ConceptExploration {
        part def User;
        part def SystemContext;
        
        use case def CheckTime {
            subject system : SystemContext;
            actor user : User;
        }
        
        use case def SetAlarm {
            subject system : SystemContext;
            actor user : User;
        }
        
        use case def WakeUp {
            subject system : SystemContext;
            actor user : User;
        }
    }

    package ConceptDefinition {
        requirement def FunctionalRequirement;
        requirement def PerformanceRequirement;
        
        requirement <'REQ-F-01'> 'Display Time' : FunctionalRequirement {
            doc /* The system shall display the current time. */
        }
        
        requirement <'REQ-F-02'> 'Set Alarm Time' : FunctionalRequirement {
            doc /* The system shall allow the user to set an alarm time. */
        }
        
        requirement <'REQ-F-03'> 'Sound Alarm Alert' : FunctionalRequirement {
            doc /* The system shall sound an alarm when the current time matches the alarm time. */
        }
        
        requirement <'REQ-P-01'> 'Alarm Volume' : PerformanceRequirement {
            doc /* The alarm volume shall be at least 70 dB. */
        }
    }

    package LogicalDesign {
        import ConceptDefinition::*;
        
        part def Timekeeper {
            satisfy 'Display Time';
            attribute currentTime : Real;
            action updateTime;
        }
        
        part def AlarmController {
            satisfy 'Set Alarm Time';
            satisfy 'Sound Alarm Alert';
            attribute alarmTime : Real;
            action compareTime;
        }
        
        part def AudioOutput {
            satisfy 'Alarm Volume';
            action emitSound;
        }
        
        part logicalAlarmClock {
            part clock : Timekeeper;
            part controller : AlarmController;
            part speaker : AudioOutput;
        }
    }

    package PhysicalDesign {
        import LogicalDesign::*;
        
        part def Microcontroller;
        part def LCDDisplay;
        part def PiezoBuzzer;
        part def Buttons;
        
        part physicalAlarmClock {
            part mcu : Microcontroller;
            part display : LCDDisplay;
            part buzzer : PiezoBuzzer;
            part controlButtons : Buttons;
        }
        
        allocate physicalAlarmClock.mcu to logicalAlarmClock.clock;
        allocate physicalAlarmClock.mcu to logicalAlarmClock.controller;
        allocate physicalAlarmClock.buzzer to logicalAlarmClock.speaker;
    }
    
    package Views {
        import ConceptDefinition::*;
        
        view def RequirementsTable {
            filter EssentialElementsFilter;
            filter NonStandardLibraryElementFilter;
        }
        
        view reqView : RequirementsTable {
            expose ConceptDefinition::*;
        }
    }
}
