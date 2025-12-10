import utils
import themes
import os

def generate_for_theme(theme_key, theme):
    # SVG Dimensions
    w, h = 1400, 2000 # Taller for tutorial
    svg = utils.svg_start(w, h, theme)
    
    # Title
    svg += utils.text(50, 60, "SysML v2 Use Case Tutorial", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "A Conceptual Overview & Example", 24, theme.text_sec, "italic", font_family=theme.title_font)

    # --- Content ---
    y = 150
    
    # Section 1: Introduction
    svg += utils.text(50, y, "1. What is a Use Case?", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "In SysML v2, a Use Case is a specialized type of case used to specify the required behavior",
        "of a system from the perspective of its external users (actors). It represents a coherent",
        "unit of functionality that provides something of value to an actor."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # Section 2: Key Concepts
    svg += utils.text(50, y, "2. Key Concepts", 24, theme.c_keyword, "bold")
    y += 30
    concepts = [
        ("Use Case Definition (use case def)", "Defines the interaction type, subject, actors, and goal."),
        ("Actor", "External entity (person, system) interacting with the subject."),
        ("Subject", "The system under design providing the functionality."),
        ("Use Case Usage (use case)", "A specific occurrence of a use case definition."),
        ("Relationships", "Interaction, Include (reuse), Extend (optional/exceptional behavior).")
    ]
    for title, desc in concepts:
        svg += utils.text(50, y, f"• {title}:", 18, theme.c_type, "bold")
        svg += utils.text(400, y, desc, 18, theme.text_main)
        y += 25
    y += 20
    
    # Section 3: Example Code
    svg += utils.text(50, y, "3. Example: Automated Pickleball Server (APS)", 24, theme.c_keyword, "bold")
    y += 30
    
    code_lines = [
        [("package", theme.c_keyword), (" AutomatedPickleballServerModel", theme.c_type), (" {", theme.c_normal)],
        [],
        [("  ", theme.c_normal), ("/* --- 1. Define the Actors --- */", theme.c_comment)],
        [("  ", theme.c_normal), ("/* Actors are external parts that interact with the system. */", theme.c_comment)],
        [("  ", theme.c_normal), ("part", theme.c_keyword), (" def", theme.c_keyword), (" Player", theme.c_type), (" :>", theme.c_normal), (" ActorPart", theme.c_type), (";", theme.c_normal)],
        [("  ", theme.c_normal), ("part", theme.c_keyword), (" def", theme.c_keyword), (" CourtEnvironment", theme.c_type), (" :>", theme.c_normal), (" ActorPart", theme.c_type), (";", theme.c_normal), (" /* Physical boundaries */", theme.c_comment)],
        [],
        [("  ", theme.c_normal), ("/* --- 2. Define the Subject System --- */", theme.c_comment)],
        [("  ", theme.c_normal), ("part", theme.c_keyword), (" def", theme.c_keyword), (" AutomatedPickleballServer", theme.c_type), (" {", theme.c_normal)],
        [("    ", theme.c_normal), ("part", theme.c_keyword), (" aiController", theme.c_normal), (";", theme.c_normal)],
        [("    ", theme.c_normal), ("part", theme.c_keyword), (" ballLauncher", theme.c_normal), (";", theme.c_normal)],
        [("    ", theme.c_normal), ("part", theme.c_keyword), (" sensorSuite", theme.c_normal), (";", theme.c_normal)],
        [("  ", theme.c_normal), ("}", theme.c_normal)],
        [],
        [("  ", theme.c_normal), ("/* --- 3. Define the Use Cases --- */", theme.c_comment)],
        [("  ", theme.c_normal), ("use", theme.c_keyword), (" case", theme.c_keyword), (" def", theme.c_keyword), (" PlayPracticeSession", theme.c_type), (" {", theme.c_normal)],
        [("    ", theme.c_normal), ("subject", theme.c_keyword), (" aps", theme.c_normal), (" :", theme.c_normal), (" AutomatedPickleballServer", theme.c_type), (";", theme.c_normal)],
        [("    ", theme.c_normal), ("actor", theme.c_keyword), (" player", theme.c_normal), (" :", theme.c_normal), (" Player", theme.c_type), (";", theme.c_normal)],
        [],
        [("    ", theme.c_normal), ("doc", theme.c_keyword), (" /* The player engages in a practice session where the server", theme.c_comment)],
        [("           ", theme.c_normal), ("* serves balls tailored to their skill level. */", theme.c_comment)],
        [],
        [("    ", theme.c_normal), ("/* This use case INCLUDES other core behaviors */", theme.c_comment)],
        [("    ", theme.c_normal), ("include", theme.c_keyword), (" use", theme.c_keyword), (" case", theme.c_keyword), (" trackPlayer", theme.c_normal), (" :", theme.c_normal), (" TrackPlayerState", theme.c_type), (";", theme.c_normal)],
        [("    ", theme.c_normal), ("include", theme.c_keyword), (" use", theme.c_keyword), (" case", theme.c_keyword), (" determineShot", theme.c_normal), (" :", theme.c_normal), (" DetermineNextShot", theme.c_type), (";", theme.c_normal)],
        [("    ", theme.c_normal), ("include", theme.c_keyword), (" use", theme.c_keyword), (" case", theme.c_keyword), (" serveBall", theme.c_normal), (" :", theme.c_normal), (" ServeBall", theme.c_type), (";", theme.c_normal)],
        [("  ", theme.c_normal), ("}", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    
    # Save Example
    raw_code = utils.reconstruct_code(code_lines)
    utils.save_example("UseCaseTutorial_APS.sysml", raw_code)
    
    # Draw Code Box
    code_h = len(code_lines) * 25 + 40
    svg += utils.rect(50, y, 1300, code_h, theme.card_bg, stroke=theme.c_type, stroke_width=1)
    cy = y + 30
    for line in code_lines:
        svg += utils.colored_code_line(70, cy, line, 16, theme)
        cy += 25
    y += code_h + 30

    # Cartoon
    svg += utils.text(50, y, "4. Illustration", 24, theme.c_keyword, "bold")
    y += 30
    
    # Path to cartoon
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cartoon_path = os.path.join(base_dir, "assets", "cartoon.png")
    
    if os.path.exists(cartoon_path):
        # Embed image
        svg += utils.image(50, y, 600, 400, cartoon_path)
        svg += utils.text(50, y + 420, "Figure 1: Automated Pickleball Server Concept", 14, theme.text_sec, "italic")
    else:
        svg += utils.text(50, y, "(Image not found)", 16, theme.c_string)
    
    svg += utils.svg_end()
    
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "use_case_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in themes.THEMES.items():
        generate_for_theme(key, theme)
