package AutomatedPickleballServerModel {

  /* --- 1. Define the Actors --- */
  /* Actors are external parts that interact with the system. */
  part def Player :> ActorPart;
  part def CourtEnvironment :> ActorPart; /* Physical boundaries */

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
           * serves balls tailored to their skill level. */

    /* This use case INCLUDES other core behaviors */
    include use case trackPlayer : TrackPlayerState;
    include use case determineShot : DetermineNextShot;
    include use case serveBall : ServeBall;
  }
}