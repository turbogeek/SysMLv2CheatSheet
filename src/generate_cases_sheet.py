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
    title_text = "Howdy Kitty SysMLv2 Cheat Sheet" if theme_key == "howdy_kitty" else "SysML v2 Cheat Sheet: CASES"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Use Case Definition ---
    lines = [
        [("use", theme.c_keyword), (" ", theme.c_normal), ("case", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" DriveCar", theme.c_type), (" {", theme.c_normal)],
        [("   subject", theme.c_keyword), (" vehicle", theme.c_normal), (" :", theme.c_normal), (" Vehicle", theme.c_type), (";", theme.c_normal)],
        [("   actor", theme.c_keyword), (" driver", theme.c_normal), (" :", theme.c_normal), (" Person", theme.c_type), (";", theme.c_normal)],
        [("   objective", theme.c_keyword), (" {", theme.c_normal)],
        [("      doc", theme.c_keyword), (" /* Transport safely */", theme.c_comment)],
        [("   }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Use Case Definition", lines, "Functional goals.", theme, sheet_name='Cases', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Test Case Definition ---
    lines = [
        [("verification", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" TestBrakes", theme.c_type), (" {", theme.c_normal)],
        [("   verify", theme.c_keyword), (" brakeReq", theme.c_normal), (";", theme.c_normal)],
        [("   objective", theme.c_keyword), (" {", theme.c_normal)],
        [("      verify", theme.c_keyword), (" stoppingDistance", theme.c_normal), (";", theme.c_normal)],
        [("   }", theme.c_normal)],
        [("   return", theme.c_keyword), (" verdict", theme.c_normal), (" :", theme.c_normal), (" VerdictKind", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Test Case (Verification)", lines, "Verifying requirements.", theme, sheet_name='Cases', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Analysis Case Definition ---
    lines = [
        [("analysis", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" FuelEconomy", theme.c_type), (" {", theme.c_normal)],
        [("   subject", theme.c_keyword), (" vehicle", theme.c_normal), (" :", theme.c_normal), (" Vehicle", theme.c_type), (";", theme.c_normal)],
        [("   objective", theme.c_keyword), (" {", theme.c_normal)],
        [("      doc", theme.c_keyword), (" /* Estimate MPG */", theme.c_comment)],
        [("   }", theme.c_normal)],
        [("   return", theme.c_keyword), (" mpg", theme.c_normal), (" :", theme.c_normal), (" Real", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Analysis Case", lines, "Evaluating properties.", theme, sheet_name='Cases', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Case Usage ---
    lines = [
        [("use", theme.c_keyword), (" ", theme.c_normal), ("case", theme.c_keyword), (" driveToWork", theme.c_normal), (" :", theme.c_normal), (" DriveCar", theme.c_type), (" {", theme.c_normal)],
        [("   actor", theme.c_keyword), (" driver", theme.c_normal), (" =", theme.c_normal), (" me", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Case Usage", lines, "Instantiating a case.", theme, sheet_name='Cases', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    output_dir = os.path.join("..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "cases.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
