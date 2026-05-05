package ToasterSystem {
    private import ScalarValues::*;
    private import ISQ::*;
    private import SI::*;
    private import Time::*;

    doc
    /*
     * This package defines the Toaster System model, including stakeholder concerns, 
     * use cases, requirements, and a black-box structural representation.
     */

    package <'RT'> RequirementTypes {
        requirement def PerformanceRequirement {
            doc /* A requirement specifying a measurable performance metric. */
        }
        requirement def SafetyRequirement {
            doc /* A requirement specifying a safety-critical constraint. */
        }
    }

    package StakeholderConcerns {
        requirement <'CONCERN-01'> 'User Safety' : RequirementTypes::SafetyRequirement {
            doc /* The stakeholder is concerned about preventing electrical shock and burns. */
        }
        requirement <'CONCERN-02'> 'Toast Quality' : RequirementTypes::PerformanceRequirement {
            doc /* The stakeholder is concerned with the consistency of the toast browning. */
        }
    }

    package UseCases {
        part def Person;
        part def Bread;

        use case def ToastBread {
            subject toaster : Toaster;
            actor user : Person;
            actor bread : Bread;
            objective {
                doc /* User successfully transforms bread into toast using the system. */
            }
        }
    }

    package Requirements {
        requirement <'REQ-SAFE-01'> 'Electrical Insulation' : RequirementTypes::SafetyRequirement {
            doc /* The toaster shall provide electrical insulation to prevent user contact with live parts. */
            frame concern StakeholderConcerns::'User Safety';
        }

        requirement <'REQ-PERF-01'> 'Browning Time' : RequirementTypes::PerformanceRequirement {
            doc /* The toaster shall complete a medium browning cycle within 180.0 seconds. */
            attribute actualTime : DurationValue;
            attribute targetTime : DurationValue = 180 [s];
            require constraint {
                language "Groovy"
                /* actualTime <= targetTime */
            }
            frame concern StakeholderConcerns::'Toast Quality';
        }
    }

    package BlackBoxModel {
        port def PowerPort {
            in inPower : ISQ::electricCurrent;
        }

        port def UserInterfacePort {
            in leverDepressed : Boolean;
            in browningLevel : Integer;
        }

        port def ThermalPort {
            out heatTransfer : ISQ::heat;
        }

        part def Toaster {
            doc /* Black-box representation of the Toaster system. */
            
            port powerIn : PowerPort;
            port userIn : UserInterfacePort;
            port toastOut : ThermalPort;

            attribute mass : ISQ::mass = 1.5 [kg];
            
            satisfy requirement Requirements::'Electrical Insulation';
            satisfy requirement Requirements::'Browning Time';
        }

        part myToaster : Toaster;
    }

    package <'BV'> BaseViews {
        private import DS_Views::SymbolicViewsByExpression::*;
        private import DS_Views::TabularViews::*;
        private import SysML::Systems::*;

        view toasterTree : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
            doc /* Hierarchical view of the Toaster System structure. */
            filter @PartDefinition;
            filter @PartUsage;
            expose ToasterSystem::*;
        }

        view requirementTable : rt, EssentialElementsFilter, NonStandardLibraryElementFilter {
            doc /* Tabular view of the system requirements. */
            filter @RequirementUsage;
            expose Requirements::*;
        }
    }
}