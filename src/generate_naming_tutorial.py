import utils
import themes
import os
import uuid
import base64
import html
from themes import THEMES

# --- Configuration ---
WIDTH = 1400
HEIGHT = 1300
MARGIN = 30
COL_GAP = 20
ROW_GAP = 20
COL_WIDTH = (WIDTH - (2 * MARGIN) - COL_GAP) / 2

def generate_for_theme(theme_key, theme):
    svg = utils.svg_start(WIDTH, HEIGHT, theme)
    
    # Header
    title_text = "SysML v2 Cheat Sheet: NAMES & IMPORTS"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Naming & Identifiers ---
    lines = [
        [("Standard", theme.c_keyword), (" : alphanumeric + _ (start with letter/_) ", theme.c_normal)],
        [("Escaped", theme.c_keyword), ("  : 'Single Quoted' (allows spaces/symbols)", theme.c_normal)],
        [("SysML", theme.c_normal), (" is ", theme.c_normal), ("Case Sensitive", theme.c_keyword)],
        [("Conventions:", theme.c_comment)],
        [("  PartDef", theme.c_type), (" (PascalCase) - Definitions", theme.c_normal)],
        [("  myPart", theme.c_string), ("  (camelCase)  - Usages", theme.c_normal)],
        [("Recommendation:", theme.c_keyword), (" Avoid reserved words (type, id, etc.)", theme.c_normal)]
    ]
    code_1 = """package Naming_1Identifiers {
    part def VehiclePart;      // PascalCase for Definitions
    part myEngine : VehiclePart; // camelCase for Usages
    
    // Escaped identifiers for special chars or keywords
    part '123-Start'; 
    part 'Space Name';
    
    // Avoid name collisions with keywords
    // part type; // Error: 'type' is reserved
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Naming & Identifiers", lines, "Rules for naming elements.", theme, full_code=code_1, sheet_name='Naming', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Imports & Visibility ---
    lines = [
        [("import", theme.c_keyword), (" : Public import (transitive)", theme.c_normal)],
        [("private import", theme.c_keyword), (" : Private to this package", theme.c_normal)],
        [("Members of imported package become visible", theme.c_normal)],
        [("No 'include' - use import", theme.c_normal)]
    ]
    code_2 = """package Naming_2Imports {
    package Lib {
        part def Tool;
    }
    
    // Public Import: Visible to importers of Naming_2Imports
    import Lib::*;
    
    // Private Import: Only visible inside this package
    private import ScalarValues::Boolean;
    
    part t : Tool;
    attribute isReady : Boolean;
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Import Basics", lines, "Bringing elements into scope.", theme, full_code=code_2, sheet_name='Naming', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Import Scopes & Wildcards ---
    lines = [
        [("Specific", theme.c_keyword), (" : import Pkg::Item;", theme.c_normal)],
        [("Shallow *", theme.c_keyword), (" : import Pkg::*; (Direct contents)", theme.c_normal)],
        [("Recursive **", theme.c_keyword), (" : import Pkg::**; (All descendants)", theme.c_normal)],
        [("Warning:", theme.c_keyword), (" ** can import 1000s of names!", theme.c_normal)],
        [("Best Practice:", theme.c_keyword), (" Use specific imports to avoid pollution.", theme.c_normal)]
    ]
    code_3 = """package Naming_3Wildcards {
    package BigLibrary {
        package SubLib { part def InnerThing; }
        part def OuterThing;
    }
    
    // Imports only OuterThing, NOT InnerThing
    import BigLibrary::*; 
    
    // Imports OuterThing AND InnerThing (Recursive)
    // CAUTION: Can cause namespace pollution and conflicts
    // import BigLibrary::**; 
    
    part o : OuterThing;
    // part i : InnerThing; // Error if using *
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Wildcards & Scope", lines, "Controlling what you import.", theme, full_code=code_3, sheet_name='Naming', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Aliasing ---
    lines = [
        [("as", theme.c_keyword), (" : Rename imported element in local scope", theme.c_normal)],
        [("Resolves name conflicts between libraries", theme.c_normal)],
        [("Provides shorter names for deep paths", theme.c_normal)]
    ]
    code_4 = """package Naming_4Aliasing {
    package LibA { part def Widget; }
    package LibB { part def Widget; }
    
    // Conflict resolution
    import LibA::Widget as A_Widget;
    import LibB::Widget as B_Widget;
    
    part w1 : A_Widget;
    part w2 : B_Widget;
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Aliasing", lines, "Renaming for clarity or conflict resolution.", theme, full_code=code_4, sheet_name='Naming', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "naming_tutorial.svg")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
