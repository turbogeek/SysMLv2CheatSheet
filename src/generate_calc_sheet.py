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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: CONSTRAINTS & CALCS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Calculation Definition ---
    lines = [
        [("calc", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" PowerCalc", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" v", theme.c_normal), (" :", theme.c_normal), (" Voltage", theme.c_type), (";", theme.c_normal)],
        [("   in", theme.c_keyword), (" i", theme.c_normal), (" :", theme.c_normal), (" Current", theme.c_type), (";", theme.c_normal)],
        [("   return", theme.c_keyword), (" p", theme.c_normal), (" :", theme.c_normal), (" Power", theme.c_type), (" =", theme.c_normal), (" v * i", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Calculation Definition", lines, "Reusable math expressions.", theme, sheet_name="Calculations", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Calculation Usage ---
    lines = [
        [("calc", theme.c_keyword), (" p_motor", theme.c_normal), (" :", theme.c_normal), (" PowerCalc", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" v", theme.c_normal), (" =", theme.c_normal), (" 12.0", theme.c_string), (";", theme.c_normal)],
        [("   in", theme.c_keyword), (" i", theme.c_normal), (" =", theme.c_normal), (" 5.0", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Calculation Usage", lines, "Performing a calculation.", theme, sheet_name="Calculations", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Constraint Definition ---
    lines = [
        [("constraint", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" MassLimit", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("   in", theme.c_keyword), (" limit", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("   m <= limit", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Constraint Definition", lines, "Reusable boolean conditions.", theme, sheet_name="Calculations", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Constraint Usage ---
    lines = [
        [("constraint", theme.c_keyword), (" checkMass", theme.c_normal), (" :", theme.c_normal), (" MassLimit", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" m", theme.c_normal), (" =", theme.c_normal), (" self.mass", theme.c_normal), (";", theme.c_normal)],
        [("   in", theme.c_keyword), (" limit", theme.c_normal), (" =", theme.c_normal), (" 1000.0", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Constraint Usage", lines, "Applying a constraint.", theme, sheet_name="Calculations", wrapper_type="action")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Assertions ---
    lines = [
        [("assert", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal)],
        [("   x > 0", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("not", theme.c_keyword), (" assert", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal)],
        [("   y < 0", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Assertions", lines, "Enforcing truth.", theme, sheet_name="Calculations", wrapper_type="action")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Requirements ---
    lines = [
        [("requirement", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Safety", theme.c_type), (" {", theme.c_normal)],
        [("   assume", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal), (" temp < 100", theme.c_normal), (" }", theme.c_normal)],
        [("   require", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal), (" pressure < 50", theme.c_normal), (" }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Requirements", lines, "Assumptions and requirements.", theme, sheet_name="Calculations", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "calc.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
