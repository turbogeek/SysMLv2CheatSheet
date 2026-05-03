package AnalysisTests;

// Test analysis definitions and calculations

public import ScalarValues::*;

part def Vehicle {
    attribute mass : Real;
    attribute velocity : Real;

    // Calculated attribute
    attribute kineticEnergy : Real;

    calc :>> kineticEnergy {
        0.5 * mass * velocity * velocity
    }
}

analysis def MassAnalysis {
    subject vehicle : Vehicle;

    return totalMass : Real;

    calc :>> totalMass {
        vehicle.mass
    }
}

// Analysis case
analysis massCheck : MassAnalysis {
    subject vehicleInstance;
}

part vehicleInstance : Vehicle {
    attribute mass = 1500.0;
    attribute velocity = 25.0;
}
