
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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: ACTIONS - CONTROL", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: If / Else ---
    lines = [
        [("if", theme.c_keyword), (" condition", theme.c_normal), (" {", theme.c_normal)],
        [("   perform", theme.c_keyword), (" A", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal), (" else", theme.c_keyword), (" {", theme.c_normal)],
        [("   perform", theme.c_keyword), (" B", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Conditional (If/Else)", lines, "Branching logic.", theme, sheet_name='ActionsControl', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Loops ---
    lines = [
        [("while", theme.c_keyword), (" x < 10", theme.c_normal), (" {", theme.c_normal)],
        [("   perform", theme.c_keyword), (" A", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("for", theme.c_keyword), (" i", theme.c_normal), (" in", theme.c_keyword), (" 1..5", theme.c_string), (" {", theme.c_normal)],
        [("   perform", theme.c_keyword), (" B", theme.c_type), ("(i)", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Loops", lines, "Iteration.", theme, sheet_name='ActionsControl', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Assignments ---
    lines = [
        [("action", theme.c_keyword), (" Defs", theme.c_normal), (" {", theme.c_normal)],
        [("   attribute", theme.c_keyword), (" x", theme.c_normal), (" :", theme.c_normal), (" Integer", theme.c_type), (";", theme.c_normal)],
        [("   assign", theme.c_keyword), (" x", theme.c_normal), (" :=", theme.c_normal), (" 42", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Assignments", lines, "Setting values.", theme, sheet_name='ActionsControl', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Control Nodes (Decision) ---
    lines = [
        [("action", theme.c_keyword), (" DecisionFlow", theme.c_normal), (" {", theme.c_normal)],
        [("   decide", theme.c_keyword), (" d1", theme.c_normal), (";", theme.c_normal)],
        [("   merge", theme.c_keyword), (" m1", theme.c_normal), (";", theme.c_normal)],
        [("   first", theme.c_keyword), (" start", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" d1", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" m1", theme.c_normal), (" if", theme.c_keyword), (" condition", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Decision / Merge", lines, "Control nodes for branching.", theme, sheet_name='ActionsControl', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Parallel (Fork/Join) ---
    lines = [
        [("action", theme.c_keyword), (" ParallelFlow", theme.c_normal), (" {", theme.c_normal)],
        [("   fork", theme.c_keyword), (" f1", theme.c_normal), (";", theme.c_normal)],
        [("   join", theme.c_keyword), (" j1", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" f1", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" a", theme.c_normal), (" from", theme.c_keyword), (" f1", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" b", theme.c_normal), (" from", theme.c_keyword), (" f1", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" j1", theme.c_normal), (" from", theme.c_keyword), (" a", theme.c_normal), (",", theme.c_normal), (" b", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Fork / Join", lines, "Parallel execution.", theme, sheet_name='ActionsControl', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Structured Groups ---
    lines = [
        [("group", theme.c_keyword), (" {", theme.c_normal)],
        [("   perform", theme.c_keyword), (" A", theme.c_type), (";", theme.c_normal)],
        [("   perform", theme.c_keyword), (" B", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Group Action", lines, "Block grouping.", theme, sheet_name='ActionsControl', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "actions_control.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
