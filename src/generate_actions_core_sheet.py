
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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: ACTIONS - CORE", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Action Definition ---
    lines = [
        [("action", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Calculate", theme.c_type), (" {", theme.c_normal)],
        [("   doc", theme.c_keyword), (" /* Reusable behavior */", theme.c_comment)],
        [("   in", theme.c_keyword), (" x", theme.c_normal), (" :", theme.c_normal), (" Real", theme.c_type), (";", theme.c_normal)],
        [("   out", theme.c_keyword), (" y", theme.c_normal), (" :", theme.c_normal), (" Real", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Action Definition", lines, "Defining behaviors.", theme, sheet_name='ActionsCore', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Action Usage ---
    lines = [
        [("action", theme.c_keyword), (" rootAction", theme.c_normal), (" {", theme.c_normal)],
        [("   action", theme.c_keyword), (" calc1", theme.c_normal), (" :", theme.c_normal), (" Calculate", theme.c_type), (";", theme.c_normal)],
        [("   perform", theme.c_keyword), (" action", theme.c_keyword), (" calc2", theme.c_normal), (" :", theme.c_normal), (" Calculate", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Action Usage", lines, "Using defined actions.", theme, sheet_name='ActionsCore', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Parameters ---
    lines = [
        [("action", theme.c_keyword), (" Process", theme.c_normal), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" input1", theme.c_normal), (";", theme.c_normal)],
        [("   out", theme.c_keyword), (" result", theme.c_normal), (";", theme.c_normal)],
        [("   inout", theme.c_keyword), (" state", theme.c_normal), (";", theme.c_normal)],
        [("   return", theme.c_keyword), (" status", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Parameters", lines, "Data inputs/outputs.", theme, sheet_name='ActionsCore', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Succession ---
    lines = [
        [("action", theme.c_keyword), (" Sequence", theme.c_normal), (" {", theme.c_normal)],
        [("   first", theme.c_keyword), (" start", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" step1", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" step2", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" done", theme.c_keyword), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Sequencing", lines, "Ordering execution.", theme, sheet_name='ActionsCore', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Flows ---
    lines = [
        [("action", theme.c_keyword), (" DataFlow", theme.c_normal), (" {", theme.c_normal)],
        [("   action", theme.c_keyword), (" generate", theme.c_normal), (" {", theme.c_normal), (" out", theme.c_keyword), (" val", theme.c_normal), (";", theme.c_normal), (" }", theme.c_normal)],
        [("   action", theme.c_keyword), (" consume", theme.c_normal), (" {", theme.c_normal), (" in", theme.c_keyword), (" val", theme.c_normal), (";", theme.c_normal), (" }", theme.c_normal)],
        [("   flow", theme.c_keyword), (" generate.val", theme.c_normal), (" to", theme.c_keyword), (" consume.val", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Item Flow", lines, "Passing data between actions.", theme, sheet_name='ActionsCore', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 6: Nested Parameters ---
    lines = [
        [("action", theme.c_keyword), (" ComplexParams", theme.c_normal), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" config", theme.c_normal), (" {", theme.c_normal)],
        [("      in", theme.c_keyword), (" mode", theme.c_normal), (";", theme.c_normal)],
        [("      in", theme.c_keyword), (" setting", theme.c_normal), (";", theme.c_normal)],
        [("   }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Nested Parameters", lines, "Grouping parameters.", theme, sheet_name='ActionsCore', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "actions_core.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
