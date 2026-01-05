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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: STRUCTURE", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Part Definition ---
    lines = [
        [("part", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Vehicle", theme.c_type), (" {", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" massOfVehicle", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  part", theme.c_keyword), (" engine", theme.c_normal), (" :", theme.c_normal), (" Engine", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    md_blocks = []
    
    code_1 = """package Structure_1PartDefinition {
    private import ScalarValues::*;
    attribute def Mass;
    part def Engine;
    part def Vehicle {
      attribute massOfVehicle : Mass;
      part engine : Engine;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Part Definition", lines, "Defining structural blocks.", theme, full_code=code_1, sheet_name='Structure', wrapper_type='structure')
    md_blocks.append(("header", "1. Part Definition"))
    md_blocks.append(("text", "Defining structural blocks."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Part Usage & Multiplicity ---
    lines = [
        [("part", theme.c_keyword), (" car", theme.c_normal), (" :", theme.c_normal), (" Vehicle", theme.c_type), (" {", theme.c_normal)],
        [("  part", theme.c_keyword), (" wheels", theme.c_normal), (" [4]", theme.c_string), (" :", theme.c_normal), (" Wheel", theme.c_type), (";", theme.c_normal)],
        [("  part", theme.c_keyword), (" doors", theme.c_normal), (" [2..4]", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_2 = """package Structure_2PartUsage {
    private import ScalarValues::*;
    part def Vehicle;
    part def Wheel;
    part car : Vehicle {
      part wheels[4] : Wheel;
      part doors[2..4];
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Usage & Multiplicity", lines, "Instantiating parts with counts.", theme, full_code=code_2, sheet_name='Structure', wrapper_type='structure')
    md_blocks.append(("header", "2. Usage & Multiplicity"))
    md_blocks.append(("text", "Instantiating parts with counts."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Attributes & Values ---
    lines = [
        [("attribute", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Status", theme.c_type), (" {", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" code", theme.c_normal), (" :", theme.c_normal), (" Integer", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("part", theme.c_keyword), (" ecu", theme.c_normal), (" {", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" id", theme.c_normal), (" =", theme.c_normal), (" \"ECU-01\"", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_3 = """package Structure_3Attributes {
    private import ScalarValues::*;
    attribute def Status {
        attribute code : Integer;
    }
    part ecu {
        attribute id = "ECU-01";
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Attributes", lines, "Data properties of parts.", theme, full_code=code_3, sheet_name='Structure', wrapper_type='structure')
    md_blocks.append(("header", "3. Attributes"))
    md_blocks.append(("text", "Data properties of parts."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 5: Item Definition (Flows) ---
    lines = [
        [("item", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Fuel", theme.c_type), (";", theme.c_normal)],
        [("item", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Gasoline", theme.c_type), (" :>", theme.c_normal), (" Fuel", theme.c_type), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Items flow through ports */", theme.c_comment)]
    ]
    code_5 = """package Structure_5Items {
    private import ScalarValues::*;
    item def Fuel;
    item def Gasoline :> Fuel;
    doc /* Items flow through ports */
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Items", lines, "Things that flow.", theme, full_code=code_5, sheet_name='Structure', wrapper_type='structure')
    md_blocks.append(("header", "5. Items"))
    md_blocks.append(("text", "Things that flow."))
    md_blocks.append(("code", code_5))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 6: Packages ---
    lines = [
        [("package", theme.c_keyword), (" VehicleModel", theme.c_normal), (" {", theme.c_normal)],
        [("  import", theme.c_keyword), (" ScalarValues::*", theme.c_type), (";", theme.c_normal)],
        [("  part", theme.c_keyword), (" // ...", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_6 = """package Structure_6Packages {
    package VehicleModel {
        private import ScalarValues::*;
        part car;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Packages & Imports", lines, "Organizing model elements.", theme, full_code=code_6, sheet_name='Structure', wrapper_type='structure')
    md_blocks.append(("header", "6. Packages & Imports"))
    md_blocks.append(("text", "Organizing model elements."))
    md_blocks.append(("code", code_6))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 7: Inheritance (Generalization) ---
    lines = [
        [("part", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" ElectricCar", theme.c_type)],
        [("  :>", theme.c_normal), (" Vehicle", theme.c_type), (" {", theme.c_normal)],
        [("  part", theme.c_keyword), (" battery", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_7 = """package Structure_7Inheritance {
    private import ScalarValues::*;
    part def Vehicle;
    part def ElectricCar :> Vehicle {
        part battery;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "7. Inheritance (:>)", lines, "Specialization of definitions.", theme, full_code=code_7, sheet_name='Structure', wrapper_type='structure')
    md_blocks.append(("header", "7. Inheritance (:>)"))
    md_blocks.append(("text", "Specialization of definitions."))
    md_blocks.append(("code", code_7))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 8: Enumerations ---
    lines = [
        [("enum", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Color", theme.c_type), (" {", theme.c_normal)],
        [("  Red; Green; Blue;", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_8 = """package Structure_8Enumerations {
    private import ScalarValues::*;
    enum def Color {
        Red; Green; Blue;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "8. Enumerations", lines, "Predefined sets of values.", theme, full_code=code_8, sheet_name='Structure', wrapper_type='structure')
    md_blocks.append(("header", "8. Enumerations"))
    md_blocks.append(("text", "Predefined sets of values."))
    md_blocks.append(("code", code_8))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("structure_sheet.md", "Structure Cheat Sheet", "Parts, Attributes, Packages", md_blocks, subfolder="cheatsheets")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "structure.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
