# Use Case Tutorial

*A Conceptual Overview & Example*

In SysML v2, a Use Case is a specialized type of case used to specify the required behavior of a system from the perspective of its external users (actors). It represents a coherent unit of functionality that provides something of value to an actor.

## Key Concepts

- **Use Case Definition (use case def)**: Defines the interaction type, subject, actors, and goal.
- **Actor**: External entity (person, system) interacting with the subject.
- **Subject**: The system under design providing the functionality.
- **Use Case Usage (use case)**: A specific occurrence of a use case definition.
- **Relationships**: Interaction, Include (reuse), Extend (optional/exceptional behavior).

## Example: Automated Pickleball Server (APS)

```sysml
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

```

