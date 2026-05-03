package StateEntryExitTests;

// Test state entry, exit, and do actions

state def LifecycleState {
    entry action initialize {
        doc /* Entry action when entering state */
    }

    do action operate {
        doc /* Continuous action while in state */
    }

    exit action cleanup {
        doc /* Exit action when leaving state */
    }
}

part def Device {
    state deviceState {
        entry action powerOn;
        do action monitoring;
        exit action powerOff;

        state off;
        state on {
            entry action startSensors;

            state idle;
            state active {
                do action processing;
            }

            transition idle_to_active
                first idle
                accept StartSignal
                then active;

            transition active_to_idle
                first active
                accept StopSignal
                then idle;
        }

        transition off_to_on
            first off
            accept PowerButton
            then on;

        transition on_to_off
            first on
            accept PowerButton
            then off;
    }
}

signal StartSignal;
signal StopSignal;
signal PowerButton;
