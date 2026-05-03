package TradeStudyTests;

// Test trade studies and concerns

concern 'Performance vs Cost' {
    doc /* Need to balance performance requirements with budget constraints */
}

concern 'Reliability vs Weight' {
    doc /* Higher reliability often requires more redundancy, increasing weight */
}

part def Engine {
    attribute power : Real;
    attribute weight : Real;
    attribute cost : Real;
}

variation part def EngineVariant :> Engine {
    variant engineA : Engine {
        attribute power = 150.0;
        attribute weight = 200.0;
        attribute cost = 5000.0;
    }

    variant engineB : Engine {
        attribute power = 200.0;
        attribute weight = 250.0;
        attribute cost = 7000.0;
    }

    variant engineC : Engine {
        attribute power = 180.0;
        attribute weight = 220.0;
        attribute cost = 6000.0;
    }
}

analysis def TradeAnalysis {
    subject engines : EngineVariant;

    objective {
        doc /* Select optimal engine variant */
    }
}
