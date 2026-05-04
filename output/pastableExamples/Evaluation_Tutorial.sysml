package Evaluation_Tutorial {
    private import ScalarValues::*;
    private import AnalysisCases::*;
    
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
    
    /* Requirement Usage at package level to allow verification */
    requirement checkPower : PowerLimit;

    part myEngine : System::engine {
        /* Satisfaction */
        satisfy checkPower {
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
        
        objective maximizeObj {
            subject candidates = Optimization::candidates;
        }
        
        /* Define how we measure 'goodness' */
        calc evaluate {
            in part cand :> candidates;
            return result : Real = cand.currentPower;
        }
    }
}