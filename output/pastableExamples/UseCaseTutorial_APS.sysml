package AutomatedPickleballServerModel {
    private import ScalarValues::*;
    private import SysML::*;

    // --- Definitions ---
    part def ActorPart;
    use case def TrackPlayerState;
    use case def DetermineNextShot;
    use case def ServeBall;

    /* --- 1. Define the Actors --- */
    part def Player :> ActorPart;
    part def CourtEnvironment :> ActorPart;

    /* --- 2. Define the Subject System --- */
    part def AutomatedPickleballServer {
      part aiController;
      part ballLauncher;
      part sensorSuite;
    }

    /* --- 3. Define the Use Cases --- */
    use case def PlayPracticeSession {
      subject aps : AutomatedPickleballServer;
      actor player : Player;

      doc /* The player engages in a practice session where the server
             serves balls tailored to their skill level. */

      /* This use case INCLUDES other core behaviors */
      include use case trackPlayer : TrackPlayerState;
      include use case determineShot : DetermineNextShot;
      include use case serveBall : ServeBall;
    }
}
