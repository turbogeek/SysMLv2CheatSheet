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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: STATE PATTERNS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Entry/Do/Exit ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Active", theme.c_type), (" {", theme.c_normal)],
        [("   entry", theme.c_keyword), (" action", theme.c_keyword), (" :", theme.c_normal), (" logStart", theme.c_normal), (";", theme.c_normal)],
        [("   do", theme.c_keyword), (" action", theme.c_keyword), (" :", theme.c_normal), (" maintain", theme.c_normal), (";", theme.c_normal)],
        [("   exit", theme.c_keyword), (" action", theme.c_keyword), (" :", theme.c_normal), (" logEnd", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Entry/Do/Exit", lines, "State lifecycle actions.", theme, sheet_name="StatePatterns", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP
    # --- Card 2: Composite State ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Composite", theme.c_type), (" {", theme.c_normal)],
        [("   entry", theme.c_keyword), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Sub1", theme.c_type), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Sub2", theme.c_type), (";", theme.c_normal)],
        [("   transition", theme.c_keyword), (" t1", theme.c_normal)],
        [("      first", theme.c_keyword), (" Sub1", theme.c_type)],
        [("      then", theme.c_keyword), (" Sub2", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Composite State", lines, "States within states.", theme, sheet_name="StatePatterns", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Exhibit State ---
    lines = [
        [("part", theme.c_keyword), (" def", theme.c_keyword), (" Vehicle", theme.c_type), (" {", theme.c_normal)],
        [("   exhibit", theme.c_keyword), (" state", theme.c_keyword), (" opState", theme.c_normal)],
        [("      references", theme.c_keyword), (" VehicleStates::operating", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Exhibit State", lines, "Part exhibiting a state.", theme, sheet_name="StatePatterns", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Internal Transition ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Monitoring", theme.c_type), (" {", theme.c_normal)],
        [("   transition", theme.c_keyword), (" selfCheck", theme.c_normal)],
        [("      accept", theme.c_keyword), (" tick", theme.c_normal)],
        [("      do", theme.c_keyword), (" action", theme.c_keyword), (" check", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Internal Transition", lines, "Transition without state change.", theme, sheet_name="StatePatterns", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "state_patterns.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
