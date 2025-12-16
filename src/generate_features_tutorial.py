import utils
import themes
import os
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
    title_text = "SysML v2 Cheat Sheet: FEATURES & REDEFINITION"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Feature Typology ---
    lines = [
        [("Features", theme.c_keyword), (" are the structural and behavioral elements.", theme.c_normal)],
        [("Structure:", theme.c_keyword), (" attributes, parts, ports.", theme.c_normal)],
        [("Behavior:", theme.c_keyword), (" actions, steps.", theme.c_normal)],
        [("All features can be typed, valued, and related.", theme.c_normal)]
    ]
    code_1 = """package Feature_Basics {
    part def Car {
        // Structural Features
        attribute vin : String;
        part engine : Engine;
        
        // Behavioral Features
        action drive;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. What is a Feature?", lines, "The building blocks of definitions.", theme, full_code=code_1, sheet_name='Features', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Subsetting (Narrowing the Scope) ---
    lines = [
        [("subsets", theme.c_keyword), (" : Declares that a feature is a specific case of another.", theme.c_normal)],
        [("Usage:", theme.c_keyword), (" Grouping or classification.", theme.c_normal)],
        [("Constraint:", theme.c_keyword), (" The subset must be consistent with the superset.", theme.c_normal)]
    ]
    code_2 = """package Subsetting_Example {
    part def Vehicle {
        part wheels[4];
    }
    
    part def Car :> Vehicle {
        // 'frontWheels' is a specific subset of 'wheels'
        part frontWheels[2] subsets wheels;
        
        // 'rearWheels' is another subset
        part rearWheels[2] subsets wheels;
        
        // Total items in subsets cannot exceed superset multiplicity
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Subsetting", lines, "Classification and grouping.", theme, full_code=code_2, sheet_name='Features', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Redefinition (Replacing) ---
    lines = [
        [("redefines", theme.c_keyword), (" : Replaces an inherited feature with a new one.", theme.c_normal)],
        [("Usage:", theme.c_keyword), (" Changing types or multiplicity in subclasses.", theme.c_normal)],
        [("Result:", theme.c_keyword), (" The original feature is hidden/replaced.", theme.c_normal)]
    ]
    code_3 = """package Redefinition_Example {
    part def Vehicle {
        part engine : Engine;
    }
    
    part def ElectricCar :> Vehicle {
        // Replace the generic Engine with an ElectricMotor
        // Multiplicity or Type can change
        part redefines engine : ElectricMotor;
    }
    
    part def ElectricMotor :> Engine;
    part def Engine;
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Redefinition", lines, "Modifying inherited structure.", theme, full_code=code_3, sheet_name='Features', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Redeclaration Shorthand ---
    lines = [
        [(":>>", theme.c_keyword), (" : The 'redeclaration' operator.", theme.c_normal)],
        [("This is shorthand for ", theme.c_normal), ("subsets", theme.c_keyword), (" or ", theme.c_normal), ("redefines", theme.c_keyword)],
        [("depending on context (usually subsets by default).", theme.c_normal)],
        [("It allows adding Detail without restating keywords.", theme.c_normal)]
    ]
    code_4 = """package Redeclaration_Example {
    part def Spacecraft {
        part module;
    }
    
    part def Lander :> Spacecraft {
        // Add details to the inherited 'module'
        // Equivalent to: part module :>> module { ... }
        part :>> module {
            attribute mass = 500 [ISQ::kg];
        }
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Redeclaration (:>>)", lines, "Adding detail to inherited features.", theme, full_code=code_4, sheet_name='Features', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "features_tutorial.svg")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
