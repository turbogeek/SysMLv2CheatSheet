package SimpleAlarmClock_Model {
    private import SysML::*;
    private import SysML::Systems::*;
    private import ScalarValues::*;
    private import Time::*;

    package Concept_Exploration {
        part def User {
            doc /* The person using the alarm clock. */
        }
        
        part def Manufacturer {
            doc /* The organization that builds the clock. */
        }

        use case def ViewTime {
            actor user : User;
            objective { doc /* User observes current time. */ }
        }
        
        use case def SetAlarm {
            actor user : User;
            objective { doc /* User specifies wake-up time. */ }
        }
        
        use case def WakeUp {
            actor user : User;
            objective { doc /* System sounds alert when alarm time is reached. */ }
        }
        
        use case def DismissAlarm {
            actor user : User;
            objective { doc /* User turns off the sounding alarm. */ }
        }
    }

    package Concept_Definition {
        requirement def FunctionalRequirement;
        requirement def PerformanceRequirement;
        requirement def ConstraintRequirement;
        
        requirement <'REQ-FUNC-01'> 'Display Time' : FunctionalRequirement {
            doc /* The system shall continuously display the current time. */
        }
        
        requirement <'REQ-FUNC-02'> 'Set Alarm Time' : FunctionalRequirement {
            doc /* The system shall provide a mechanism for the user to set an alarm time. */
        }
        
        requirement <'REQ-FUNC-03'> 'Trigger Alarm' : FunctionalRequirement {
            doc /* The system shall trigger an audible alarm when the current time matches the set alarm time. */
        }
        
        requirement <'REQ-FUNC-04'> 'Dismiss Alarm' : FunctionalRequirement {
            doc /* The system shall provide a mechanism to stop the audible alarm once it is triggered. */
        }

        requirement <'REQ-PERF-01'> 'Volume' : PerformanceRequirement {
            doc /* The alarm volume shall be at least 70 dB. */
        }

        requirement <'REQ-PERF-02'> 'Accuracy' : PerformanceRequirement {
            doc /* The internal clock shall maintain time with an accuracy of +/- 1 minute per month. */
        }

        requirement <'CON-01'> 'Size' : ConstraintRequirement {
            doc /* The system footprint shall not exceed 15 cm x 15 cm. */
        }
    }

    package Logical_Design {
        private import Concept_Definition::*;
        private import Concept_Exploration::*;

        action def AlarmBehavior {
            in currentTime : Iso8601DateTimeStructure;
            in alarmTime : Iso8601DateTimeStructure;
            inout isAlarmActive : Boolean;

            state def OperationalStates {
                entry;
                then displayingTime;
                
                state displayingTime;
                state alarmSounding;
                
                transition triggerAlarm
                    first displayingTime
                    accept when currentTime == alarmTime
                    do action soundAlarm;
                    then alarmSounding;
                    
                transition stopAlarm
                    first alarmSounding
                    accept dismissSignal
                    then displayingTime;
            }
        }

        part def Timekeeper {
            attribute currentTime : Iso8601DateTimeStructure;
            attribute alarmTime : Iso8601DateTimeStructure;
        }

        part def UserInterface {
            port displayOut;
            port soundOut;
            port userInput;
        }

        part def AlarmTrigger {
            attribute isAlarmActive : Boolean;
        }

        part def LogicalAlarmClock {
            part timekeeper : Timekeeper;
            part userInterface : UserInterface;
            part alarmTrigger : AlarmTrigger;
            
            satisfy 'Display Time' by userInterface;
            satisfy 'Set Alarm Time' by userInterface;
            satisfy 'Trigger Alarm' by alarmTrigger;
            satisfy 'Dismiss Alarm' by userInterface;
            satisfy 'Volume' by userInterface;
            satisfy 'Accuracy' by timekeeper;
        }
    }

    package Physical_Design {
        private import Logical_Design::*;
        private import Concept_Definition::*;
        
        part def Microcontroller;
        part def LED_Display;
        part def Buzzer;
        part def Buttons;
        part def PowerSupply;

        part def PhysicalAlarmClock {
            part mcu : Microcontroller;
            part display : LED_Display;
            part buzzer : Buzzer;
            part buttons : Buttons;
            part power : PowerSupply;

            satisfy Concept_Definition::'Size' by PhysicalAlarmClock;
        }

        part logicalClockUsage : LogicalAlarmClock;
        part physicalClockUsage : PhysicalAlarmClock;

        allocate physicalClockUsage.mcu to logicalClockUsage.timekeeper;
        allocate physicalClockUsage.mcu to logicalClockUsage.alarmTrigger;
        allocate physicalClockUsage.display to logicalClockUsage.userInterface;
        allocate physicalClockUsage.buzzer to logicalClockUsage.userInterface;
        allocate physicalClockUsage.buttons to logicalClockUsage.userInterface;
    }

    package Views {
        private import DS_Views::TabularViews::*;
        private import SysML::Systems::*;
        
        view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
            filter @PartDefinition;
            filter @PartUsage;
        }

        view requirementsTreeView : RequirementsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;

        view alarmClockPartsView :> partsTreeView {
            expose Physical_Design::**;
            expose Logical_Design::**;
        }
        
        view alarmClockRequirementsView :> requirementsTreeView {
            expose Concept_Definition::**;
        }
    }
}
