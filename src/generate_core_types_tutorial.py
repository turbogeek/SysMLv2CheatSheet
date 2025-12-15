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
    title_text = "SysML v2 Cheat Sheet: CORE TYPES"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Part vs Item ---
    lines = [
        [("Part", theme.c_keyword), (" : Physical/Logical entity (Space/Time)", theme.c_normal)],
        [("Item", theme.c_keyword), (" : Pure Information/Logical flow", theme.c_normal)],
        [("Rule:", theme.c_keyword), (" Parts have mass/energy, Items do not.", theme.c_normal)],
        [("Usage:", theme.c_comment)],
        [("  part eng : Engine;", theme.c_normal)],
        [("  item cmd : TorqueCommand;", theme.c_normal)]
    ]
    code_1 = """package CoreTypes_1PartItems {
    // A Part occupies space and time
    part def Engine {
        // Parts can contain other parts
        part cylinder;
    }
    
    // An Item is information or substance flow (no structure)
    item def TorqueCommand;
    
    part car {
        part myEngine : Engine;
        // Items often flow between parts
        item currentCmd : TorqueCommand;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Part vs. Item", lines, "Physical Structure vs. Information.", theme, full_code=code_1, sheet_name='CoreTypes', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Attributes & Scalars ---
    lines = [
        [("attribute", theme.c_keyword), (" : Carries a value (No independent identity)", theme.c_normal)],
        [("scalar", theme.c_keyword), ("    : Defines the raw type (Real, String...)", theme.c_normal)],
        [("Structure:", theme.c_normal)],
        [("  scalar def -> attribute def -> usage", theme.c_comment)]
    ]
    code_2 = """package CoreTypes_2Attributes {
    // 1. Define the Scalar (Primitive Type)
    scalar def Kilogram;
    
    // 2. Define the Attribute Concept (Property)
    attribute def Mass {
        attribute val : Kilogram;
    }
    
    part def Rocket;
    
    part myRocket : Rocket {
        // 3. Use the Attribute
        attribute dryMass : Mass = 5000;
        
        // Or simple usage with standard types
        attribute name : String = "Falcon";
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Attributes & Scalars", lines, "Defining and using data values.", theme, full_code=code_2, sheet_name='CoreTypes', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Enumerations ---
    lines = [
        [("enum def", theme.c_keyword), (" : Define a set of valid literals", theme.c_normal)],
        [("Useful for states, modes, options", theme.c_normal)],
        [("Example:", theme.c_normal), (" Red, Yellow, Green", theme.c_string)]
    ]
    code_3 = """package CoreTypes_3Enums {
    enum def TrafficColor {
        enum Red;
        enum Yellow;
        enum Green;
    }
    
    part trafficLight {
        attribute state : TrafficColor;
    }
    
    // Assigning an enum value
    part intersection {
        part light1 : trafficLight {
             attribute :>> state = TrafficColor::Red;
        }
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Enumerations", lines, "Predefined sets of values.", theme, full_code=code_3, sheet_name='CoreTypes', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Putting it Together ---
    lines = [
        [("Composition:", theme.c_keyword), (" Parts composed of attributes (vals)", theme.c_normal)],
        [("Flows:", theme.c_keyword), (" Items flow, Parts execute", theme.c_normal)],
        [("The Core:", theme.c_keyword), (" Almost everything in SysML v2 extends", theme.c_normal)],
        [("from these core types.", theme.c_normal)]
    ]
    code_4 = """package CoreTypes_4Integrated {
    import ScalarValues::Real;
    
    scalar def Percent;
    
    item def Fuel;
    
    part def Tank {
        attribute level : Percent; 
        attribute capacity : Real;
    }
    
    part fuelSystem {
        part mainTank : Tank {
            attribute :>> level = 85.5;
            attribute :>> capacity = 50.0;
        }
        
        // Item existing within component
        item currentFuel : Fuel;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Integrated Example", lines, "Combining Structural Concepts.", theme, full_code=code_4, sheet_name='CoreTypes', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "core_types_tutorial.svg")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
