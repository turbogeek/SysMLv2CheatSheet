import html
import os
from themes import THEMES
import utils

# --- Configuration ---
WIDTH = 1200
HEIGHT = 1600
MARGIN = 30
COL_GAP = 20
ROW_GAP = 20
COL_WIDTH = (WIDTH - (2 * MARGIN) - COL_GAP) / 2

# --- Content ---
def generate_for_theme(theme_key, theme):
    svg = utils.svg_start(WIDTH, HEIGHT, theme)
    
    # Header
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: PATTERNS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Metadata Definition ---
    lines = [
        [("metadata", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Status", theme.c_type), (" {", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" priority", theme.c_normal), (" :", theme.c_normal), (" Integer", theme.c_type), (";", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" approved", theme.c_normal), (" :", theme.c_normal), (" Boolean", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("part", theme.c_keyword), (" myPart", theme.c_normal), (" {", theme.c_normal)],
        [("  metadata", theme.c_keyword), (" Status", theme.c_type), (" {", theme.c_normal)],
        [("    priority", theme.c_normal), (" =", theme.c_normal), (" 1", theme.c_string), (";", theme.c_normal)],
        [("  }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    md_blocks = []
    
    code_1 = """package Patterns_1MetadataAnnotations {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    metadata   def  Status  {
      attribute  priority  :  Integer ;
      attribute  approved  :  Boolean ;
    }
    part  myPart  {
      metadata  Status  {
        priority  =  1 ;
      }
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Metadata (Annotations)", lines, "Tagging elements with data.", theme, full_code=code_1, sheet_name="Patterns", wrapper_type="structure")
    md_blocks.append(("header", "1. Metadata (Annotations)"))
    md_blocks.append(("text", "Tagging elements with data."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Views & Viewpoints ---
    lines = [
        [("view", theme.c_keyword), (" MyView", theme.c_normal), (" :", theme.c_normal), (" GeneralDiagram", theme.c_type), (" {", theme.c_normal)],
        [("/* filter Status; */", theme.c_comment)],
        [("}", theme.c_normal)],
        [("/* Rendering specific subsets */", theme.c_comment)]
    ]
    code_2 = """package Patterns_2Views {
    private import ScalarValues::*;
    private import SysML::*;
    part def GeneralDiagram;
    /* Wrapped Snippet (Structure Context) */
    view  MyView  :  GeneralDiagram  {
    /* filter Status; */
    }
    /* Rendering specific subsets */
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Views", lines, "Visualizing the model.", theme, full_code=code_2, sheet_name="Patterns", wrapper_type="structure")
    md_blocks.append(("header", "2. Views"))
    md_blocks.append(("text", "Visualizing the model."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Custom Units (Nano Banana) ---
    lines = [
        [("package", theme.c_keyword), (" BananaUnits", theme.c_type), (" {", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" <nB>", theme.c_type), (" nanoBanana", theme.c_normal), (" :", theme.c_normal), (" LengthUnit", theme.c_type), (" {", theme.c_normal)],
        [("    attribute", theme.c_keyword), (" unitConversion", theme.c_normal), (";", theme.c_normal)],
        [("      :>>", theme.c_keyword), (" prefix", theme.c_normal), (" =", theme.c_normal), (" nano", theme.c_string), (";", theme.c_normal)],
        [("      :>>", theme.c_keyword), (" referenceUnit", theme.c_normal), (" =", theme.c_normal), (" 'Standard Banana'", theme.c_string), (";", theme.c_normal)],
        [("    }", theme.c_normal)],
        [("  }", theme.c_normal)]
    ]
    code_3 = """package BananaUnits {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def LengthUnit {
        attribute prefix;
        attribute referenceUnit;
    }
    attribute nano;
    attribute <nB> nanoBanana : LengthUnit {
        attribute unitConversion;
        :>> prefix = nano;
        :>> referenceUnit = "Standard Banana";
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Custom Units (Nano Banana)", lines, "Defining domain-specific units.", theme, full_code=code_3, sheet_name="Patterns", wrapper_type="structure")
    md_blocks.append(("header", "3. Custom Units (Nano Banana)"))
    md_blocks.append(("text", "Defining domain-specific units."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 4: Abstract vs Individual ---
    lines = [
        [("abstract", theme.c_keyword), (" part", theme.c_keyword), (" def", theme.c_keyword), (" Wheel", theme.c_type), (";", theme.c_normal)],
        [("part", theme.c_keyword), (" def", theme.c_keyword), (" Bus", theme.c_type), (" {", theme.c_normal)],
        [("  abstract", theme.c_keyword), (" part", theme.c_keyword), (" wheel", theme.c_normal), (" [4]", theme.c_string), (" :", theme.c_normal), (" Wheel", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("individual", theme.c_keyword), (" part", theme.c_keyword), (" myBus", theme.c_normal), (" :", theme.c_normal), (" Bus", theme.c_type), (" {", theme.c_normal)],
        [("  part", theme.c_keyword), (" frontLeft", theme.c_normal), (" :>", theme.c_keyword), (" wheel", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package Patterns_4AbstractvsIndividual {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    abstract  part  def  Wheel ;
    part  def  Bus  {
      abstract  part  wheel  [4]  :  Wheel ;
    }
    individual  part  myBus  :  Bus  {
      part  frontLeft  :>  wheel ;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Abstract vs Individual", lines, "Templates vs Concrete instances.", theme, full_code=code_4, sheet_name="Patterns", wrapper_type="structure")
    md_blocks.append(("header", "4. Abstract vs Individual"))
    md_blocks.append(("text", "Templates vs Concrete instances."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP

    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("patterns_sheet.md", "Patterns Cheat Sheet", "Reusable Modeling Patterns", md_blocks, subfolder="cheatsheets")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "patterns.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
