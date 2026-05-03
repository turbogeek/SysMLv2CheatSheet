package VerificationTests;

// Test verification definitions and verify relationships

requirement def SafetyRequirement {
    subject system;
    require constraint speed <= 100.0;
}

part def System {
    attribute speed : Real;
}

verification def SpeedTest {
    subject req : SafetyRequirement;

    objective {
        doc /* Verify speed constraint is satisfied */
    }

    // Test method
    method testSpeed {
        // Verification logic
    }
}

requirement safetyReq : SafetyRequirement {
    subject testSystem;
}

part testSystem : System {
    attribute speed = 85.0;
}

// Verification case
verify safetyReq by SpeedTest;

verification speedVerification : SpeedTest {
    subject safetyReq;
}
