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
    title_text = "Howdy Kitty SysMLv2 Cheat Sheet" if theme_key == "howdy_kitty" else "SysML v2 Cheat Sheet: METADATA"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Metadata Definition ---
    lines = [
        [("metadata", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Risk", theme.c_type), (" {", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" level", theme.c_normal), (" :", theme.c_normal), (" Integer", theme.c_type), (";", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" desc", theme.c_normal), (" :", theme.c_normal), (" String", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Defining custom", theme.c_comment)],
        [("       tags/annotations */", theme.c_comment)]
    ]
    code_1 = """package Metadata_1Definition {
    private import ScalarValues::*;
    private import SysML::*;
    doc /* Define custom metadata (like a Stereotype) */
    metadata def Risk {
        attribute level : Integer;
        attribute desc : String;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Metadata Definition", lines, "Defining custom annotations.", theme, full_code=code_1, sheet_name="Metadata", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Element Annotation ---
    lines = [
        [("part", theme.c_keyword), (" Engine", theme.c_type), (" {", theme.c_normal)],
        [("  metadata", theme.c_keyword), (" Risk", theme.c_type), (" {", theme.c_normal)],
        [("    :>>", theme.c_keyword), (" level", theme.c_normal), (" =", theme.c_normal), (" 5", theme.c_string), (";", theme.c_normal)],
        [("    :>>", theme.c_keyword), (" desc", theme.c_normal), (" =", theme.c_normal), (" \"Overheat\"", theme.c_string), (";", theme.c_normal)],
        [("  }", theme.c_normal)],
        [("}", theme.c_normal)],
        [(" ", theme.c_normal)],
        [("part", theme.c_keyword), (" Wheel", theme.c_type), (" {", theme.c_normal)],
        [("  @Risk", theme.c_type), (" {", theme.c_normal)],
        [("     :>>", theme.c_keyword), (" level", theme.c_normal), (" =", theme.c_normal), (" 1", theme.c_string), (";", theme.c_normal)],
        [("  }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_2 = """package Metadata_2ElementAnnotation {
    private import ScalarValues::*;
    private import SysML::*;
    metadata def Risk { attribute level : Integer; attribute desc : String = ""; }
    
    doc /* Usage within element */
    part engine {
        metadata Risk {
            :>> level = 5;
            :>> desc = "Overheat potential";
        }
    }
    
    doc /* Shorthand annotation nested in definition */
    part wheel {
        @Risk { :>> level = 1; }
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Element Annotation", lines, "Tagging parts and actions.", theme, full_code=code_2, sheet_name="Metadata", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Relationship Annotation ---
    lines = [
        [("dependency", theme.c_keyword), (" from", theme.c_keyword), (" req2", theme.c_normal), (" to", theme.c_keyword), (" req1", theme.c_normal), (" {", theme.c_normal)],
        [("  metadata", theme.c_keyword), (" RefineData", theme.c_type), (" {", theme.c_normal)],
        [("    :>>", theme.c_keyword), (" isRefine", theme.c_normal), (" =", theme.c_normal), (" true", theme.c_string), (";", theme.c_normal)],
        [("  }", theme.c_normal)],
        [("}", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Tagging dependencies", theme.c_comment)],
        [("       for transformers */", theme.c_comment)]
    ]
    code_3 = """package Metadata_3RelationshipAnnotation {
    private import ScalarValues::*;
    private import SysML::*;
    metadata def RefineData { attribute isRefine : Boolean; }
    requirement req1;
    requirement req2;
    
    doc /* Annotating a dependency */
    dependency from req2 to req1 {
        metadata RefineData {
            :>> isRefine = true;
        }
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Relationship Annotation", lines, "Annotating relationships.", theme, full_code=code_3, sheet_name="Metadata", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Standard Metadata ---
    lines = [
        [("part", theme.c_keyword), (" OldPart", theme.c_type), (" {", theme.c_normal)],
        [("  @Deprecated", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [(" ", theme.c_normal)],
        [("action", theme.c_keyword), (" check", theme.c_normal), (" {", theme.c_normal)],
        [("  @FIXME", theme.c_type), (" {", theme.c_normal)],
        [("    doc", theme.c_keyword), (" /* Needs update */", theme.c_comment)],
        [("  }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package Metadata_4Standard {
    private import ScalarValues::*;
    private import SysML::*;
    
    metadata def Deprecated;
    
    doc /* Deprecation */
    part oldPart {
        @Deprecated;
    }
    
    metadata def FIXME;
    
    action check {
        @FIXME {
            doc /* Needs update */
        }
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Standard Metadata", lines, "Common annotations.", theme, full_code=code_4, sheet_name="Metadata", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Metadata Extension ---
    lines = [
        [("metadata", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" TestPlan", theme.c_type), (" {", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" tool", theme.c_normal), (" :", theme.c_normal), (" String", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("@LabTest", theme.c_type), (" {", theme.c_normal)],
        [("  :>>", theme.c_keyword), (" tool", theme.c_normal), (" =", theme.c_normal), (" \"JUnit\"", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("action", theme.c_keyword), (" runTest", theme.c_normal), (";", theme.c_normal)]
    ]
    code_5 = """package Metadata_5Extension {
    private import ScalarValues::*;
    private import SysML::*;
    
    doc /* Base metadata */
    metadata def TestPlan {
        attribute tool : String;
    }
    
    doc /* Extended metadata (Inheritance) */
    metadata def LabTest :> TestPlan {
        attribute labId : String;
    }
    
    metadata def VRTest :> TestPlan {
        attribute headsetModel : String;
    }
    
    doc /* Usage with values */
    action runUnitTests {
        @LabTest {
            :>> tool = "JUnit";
            :>> labId = "Lab-101";
        }
    }
    
    action runSimTest {
        @VRTest {
            :>> tool = "Unity";
            :>> headsetModel = "Quest 3";
        }
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "5. Metadata Extension", lines, "Inheriting and specializing metadata.", theme, full_code=code_5, sheet_name="Metadata", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 6: Hashtag Syntax ---
    lines = [
        [("/* Definition Package */", theme.c_comment)],
        [("metadata", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Vehicle", theme.c_type), (";", theme.c_normal)],
        [("metadata", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Engine", theme.c_type), (";", theme.c_normal)],
        [(" ", theme.c_normal)],
        [("/* Usage Package */", theme.c_comment)],
        [("#Vehicle", theme.c_type), (" ", theme.c_normal), ("def", theme.c_keyword), (" Car", theme.c_type), (" {", theme.c_normal)],
        [("  #Engine", theme.c_type), (" ", theme.c_normal), ("part", theme.c_keyword), (" carEngine", theme.c_normal), (" [1];", theme.c_string)],
        [("}", theme.c_normal)]
    ]
    code_6 = """package Metadata_6Hashtags {
    private import ScalarValues::*;
    private import SysML::*;
    
    package Vehicle_Metadata {
        metadata def Vehicle;
        metadata def Engine;
        metadata def Wheel;
    }
    package Car_Example {
        private import Vehicle_Metadata::*;
        
        #Vehicle def Car {
            #Engine part carEngine [1];
            #Wheel part carWheels [4];
        }
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Short Annotation (#)", lines, "Using hashtags for metadata.", theme, full_code=code_6, sheet_name="Metadata", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    output_dir = os.path.join("..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "metadata.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
