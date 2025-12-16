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
    title_text = "SysML v2 Cheat Sheet: SEMANTIC METADATA (DSL)"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Domain Concept Library ---
    lines = [
        [("Pre-requisite:", theme.c_comment), (" Define your domain concepts first.", theme.c_normal)],
        [("These are standard SysML definitions.", theme.c_normal)],
        [("Metadata will map to these concepts.", theme.c_normal)]
    ]
    code_1 = """package Vehicle_Library {
    port def DrivePort {
        out attribute torque : ISQ::TorqueValue;
    }
    part def Engine {
        port enginePort : DrivePort;
    }
    part engines : Engine [0..*];
    part def Wheel {
        port wheelPort : ~DrivePort;
    }
    part wheels : Wheel [0..*];
    interface def DriveTrain {
        end [0..1] port drivePort : DrivePort;
        end [0..*] port drivenPort : ~DrivePort;
    }
    abstract interface driveTrains : DriveTrain [0..*];
    
    part def Vehicle {
        part :>> engines;
        part :>> wheels;
        part :>> driveTrains;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Domain Library", lines, "The vocabulary we want to use.", theme, full_code=code_1, sheet_name='SemanticMetadata', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Defining Metadata ---
    lines = [
        [("metadata def", theme.c_keyword), (" : Defines a new annotation type.", theme.c_normal)],
        [("specializes SemanticMetadata", theme.c_keyword), (" : Required for semantic mapping.", theme.c_normal)],
        [("baseType", theme.c_keyword), (" : The Domain Concept this metadata represents.", theme.c_normal)],
        [("annotatedElement", theme.c_keyword), (" : Where this metadata can be applied.", theme.c_normal)]
    ]
    code_2 = """package Vehicle_Metadata {
    private import Vehicle_Library::*;
    private import Metaobjects::SemanticMetadata;

    metadata def drive :> SemanticMetadata {
        :>> baseType = driveTrains meta SysML::Usage;
        :> annotatedElement : SysML::InterfaceUsage;
    }
    metadata def engine :> SemanticMetadata {
        :>> baseType = engines meta SysML::Usage;
        :> annotatedElement : SysML::Usage;
    }
    metadata def wheel :> SemanticMetadata {
        :>> baseType = wheels meta SysML::Usage;
        :> annotatedElement : SysML::Usage;
    }
    metadata def vehicle :> SemanticMetadata {
        :>> baseType = Vehicle meta SysML::Definition;
        :> annotatedElement : SysML::Definition;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Defining Metadata", lines, "Mapping keywords to concepts.", theme, full_code=code_2, sheet_name='SemanticMetadata', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Using the DSL (The 'Magic') ---
    lines = [
        [("#hash", theme.c_keyword), (" syntax applies the metadata.", theme.c_normal)],
        [("The parser treats:", theme.c_normal)],
        [("  #vehicle def Car", theme.c_string)],
        [("as equivalent to:", theme.c_normal)],
        [("  part def Car :> Vehicle", theme.c_string)],
        [("(plus semantic tagging)", theme.c_comment)]
    ]
    code_3 = """package Car_Example {
    private import Vehicle_Metadata::*;
    
    #vehicle def Car {
        #engine carEngine [1];
        #wheel carWheels [4];
        
        #drive interface [1] carEngine.enginePort to [2] carWheels.wheelPort;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Using the DSL", lines, "Writing concise, domain-specific code.", theme, full_code=code_3, sheet_name='SemanticMetadata', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Key Concepts ---
    lines = [
        [("meta", theme.c_keyword), (" keyword: explicit reference to a metaclass.", theme.c_normal)],
        [("  e.g., meta SysML::Usage", theme.c_normal)],
        [("Benefits:", theme.c_keyword)],
        [("  1. Concise syntax (#engine vs part :> engine)", theme.c_normal)],
        [("  2. Semantic Validation (only engines here)", theme.c_normal)],
        [("  3. Tooling (custom views/generators)", theme.c_normal)]
    ]
    code_4 = """// Conceptual view of what happens under the hood
// When you write:
// #engine myEngine;

// It effectively becomes:
// @engine
// part myEngine :> engines;

// Where @engine links back to the metadata definition
// allowing tools to know "This part IS an engine"
// regardless of inheritance hierarchy complexities."""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Behind the Scenes", lines, "Why do this?", theme, full_code=code_4, sheet_name='SemanticMetadata', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "semantic_metadata_tutorial.svg")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
