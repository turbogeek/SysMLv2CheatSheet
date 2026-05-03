package States {
    private import ScalarValues::**;
    private import SI::**;
    item def increaseSpeed;
    item def decreaseSpeed;
    item def increaseHeat;
    item def decreaseHeat;
    item def switchedOn;
    item def pressOff;
    item def errorSignal;
    part hairDryer {
        attribute deviceTemperature : Real;
        exhibit state hairDryerStateMachine {
            state off;
            state error {
                do action fastBlinkInRed;
            }
            state on parallel {
                entry action turnOnMotor;
                exit action turnOffMotor;
                state speed {
                    state slow;
                    state average;
                    state fast;
                    transition avarageToFast first average accept increaseSpeed then fast;
                    transition fastToAvarage first fast accept decreaseSpeed then average;
                    transition avarageToSlow first average accept decreaseSpeed then slow;
                    transition slowToAvarage first slow accept increaseSpeed then average;
                    transition start then average;
                }
                state heat {
                    state cold;
                    state warm;
                    state hot;
                    transition warmToHot first warm accept increaseHeat if deviceTemperature < 50 then hot;
                    transition hotToWarm first hot accept decreaseHeat then warm;
                    transition warmToCold first warm accept decreaseHeat then cold;
                    transition coldToWarm first cold accept increaseHeat then warm;
                    transition start then warm;
                }
            }
            transition off_on first off accept switchedOn do action turnOnIndicator then on;
            transition exitToOff first error accept after 5 [s] then off;
            transition onToOff first on accept pressOff then off;
            transition onToError first on accept errorSignal then error;
            transition start then off;
        }
    }
    view states : DS_Views::SymbolicViews::gv;
}
