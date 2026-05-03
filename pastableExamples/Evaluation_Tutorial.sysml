package Evaluation_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Calculations --- */
    calc def PowerCalc {
        in force : Real;
        in velocity : Real;
        return power : Real = force * velocity;
    }

    package System {
        part engine {
            attribute force : Real = 1000.0;
            attribute maxPower : Real = 50000.0;
            
            /* Using the calculation */
            attribute currentPower : Real = PowerCalc(force, 25.0);
        }
    }

    /* --- 2. Requirements & Constraints --- */
    requirement def PowerLimit {
        attribute actualPower : Real;
        attribute limit : Real;
        
        /* Boolean check */
        require constraint {
            actualPower <= limit
        }
    }
    
    part myEngine : System::engine {
        /* Satisfaction */
        satisfy requirement checkPower : PowerLimit {
            attribute :>> actualPower = myEngine.currentPower;
            attribute :>> limit = myEngine.maxPower;
        }
    }

    /* --- 3. Verification Case --- */
    verification def PowerTest {
        subject system : System::engine;
        
        objective {
            /* Verify that the requirement is met */
            verify checkPower {
                subject = system;
            }
        }
    }

    /* --- 4. Analysis (Trade Study) --- */
    analysis def Optimization {
        subject candidates : System::engine [1..*];
        
        objective : MaximizeObjective {
            subject;
        }
        
        /* Define how we measure 'goodness' */
        calc :>> evaluationFunction {
            in part cand :> candidates :>> alternative;
            return :>> result = cand.currentPower;
        }
    }
}