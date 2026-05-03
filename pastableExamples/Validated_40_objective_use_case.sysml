package ObjectiveUseCaseTests;

// Test objective and use case definitions

requirement def MissionObjective {
    doc /* High-level mission objective */

    subject mission : MissionSystem;

    require constraint {
        mission.reliability > 0.99
    }
}

use case def UserAuthentication {
    doc /* User login use case */

    subject user : User;
    actor system : AuthenticationSystem;

    objective {
        doc /* Successfully authenticate user */
    }

    include use case ValidateCredentials;
}

use case def ValidateCredentials {
    doc /* Validate user credentials */
}

part def MissionSystem {
    attribute reliability : Real;
}

part def User;
part def AuthenticationSystem;

objective missionSuccess : MissionObjective;
