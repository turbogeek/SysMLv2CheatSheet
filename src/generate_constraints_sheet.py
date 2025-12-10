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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: CONSTRAINTS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Constraint Definition ---
    lines = [
        [("constraint", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" NewtonLaw", theme.c_type), (" {", theme.c_normal)],
        [("  in", theme.c_keyword), (" f", theme.c_normal), (" :", theme.c_normal), (" Force", theme.c_type), (";", theme.c_normal)],
        [("  in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  in", theme.c_keyword), (" a", theme.c_normal), (" :", theme.c_normal), (" Acceleration", theme.c_type), (";", theme.c_normal)],
        [("  ", theme.c_normal), ("f", theme.c_normal), (" =", theme.c_normal), (" m * a", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Constraint Definition", lines, "Defining mathematical relationships.", theme, sheet_name="Constraints", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Constraint Usage (Assert) ---
    lines = [
        [("part", theme.c_keyword), (" Car", theme.c_type), (" {", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" mass", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" accel", theme.c_normal), (" :", theme.c_normal), (" Acceleration", theme.c_type), (";", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" force", theme.c_normal), (" :", theme.c_normal), (" Force", theme.c_type), (";", theme.c_normal)],
        [("  assert", theme.c_keyword), (" constraint", theme.c_keyword), (" n1", theme.c_normal), (" :", theme.c_normal), (" NewtonLaw", theme.c_type), (" {", theme.c_normal)],
        [("    in", theme.c_keyword), (" f", theme.c_normal), (" =", theme.c_normal), (" force", theme.c_normal), (";", theme.c_normal)],
        [("    in", theme.c_keyword), (" m", theme.c_normal), (" =", theme.c_normal), (" mass", theme.c_normal), (";", theme.c_normal)],
        [("    in", theme.c_keyword), (" a", theme.c_normal), (" =", theme.c_normal), (" accel", theme.c_normal), (";", theme.c_normal)],
        [("  }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Constraint Usage (Assert)", lines, "Enforcing constraints on parts.", theme, sheet_name="Constraints", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2b: Inline Assertion ---
    lines = [
        [("assert", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal)],
        [("  x > 0", theme.c_normal)],
        [("}", theme.c_normal)],
        [("/* Boolean expression */", theme.c_comment)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2b. Inline Assertion", lines, "Simple boolean check.", theme, sheet_name="Constraints", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Calculation Definition ---
    lines = [
        [("calc", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" calcKineticEnergy", theme.c_type), (" {", theme.c_normal)],
        [("  in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  in", theme.c_keyword), (" v", theme.c_normal), (" :", theme.c_normal), (" Speed", theme.c_type), (";", theme.c_normal)],
        [("  return", theme.c_keyword), (" ke", theme.c_normal), (" :", theme.c_normal), (" Energy", theme.c_type), (";", theme.c_normal)],
        [("  ", theme.c_normal), ("0.5 * m * v^2", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Calculation Definition", lines, "Reusable computation logic.", theme, sheet_name="Constraints", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 4: Calculation Usage ---
    lines = [
        [("attribute", theme.c_keyword), (" kEnergy", theme.c_normal), (" =", theme.c_normal), (" calcKineticEnergy", theme.c_type), ("(", theme.c_normal)],
        [("  m", theme.c_normal), (" =", theme.c_normal), (" 100[kg]", theme.c_string), (",", theme.c_normal)],
        [("  v", theme.c_normal), (" =", theme.c_normal), (" 20[m/s]", theme.c_string)],
        [(")", theme.c_normal), (";", theme.c_normal)],
        [("/* Result assigned to attribute */", theme.c_comment)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Calculation Usage", lines, "Invoking calculations.", theme, sheet_name="Constraints", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 5: Objective (Optimization) ---
    lines = [
        [("objective", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" MinimizeMass", theme.c_type), (" {", theme.c_normal)],
        [("  in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  minimize", theme.c_keyword), (" m", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Objective", lines, "Optimization goals.", theme, sheet_name="Constraints", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "constraints.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
