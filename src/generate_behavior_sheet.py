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
    title_text = "Howdy Kitty SysMLv2 Cheat Sheet" if theme_key == "howdy_kitty" else "SysML v2 Cheat Sheet: BEHAVIOR"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: State Definition ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" PracticeSession", theme.c_type), (" {", theme.c_normal)],
        [("   entry", theme.c_keyword), (";", theme.c_normal), (" exit", theme.c_keyword), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Idle", theme.c_type), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Serving", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. State Definition", lines, "States and lifecycle actions.", theme, sheet_name="Behavior", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Transitions ---
    lines = [
        [("transition", theme.c_keyword), (" startServe", theme.c_normal)],
        [("   first", theme.c_keyword), (" Idle", theme.c_type)],
        [("   accept", theme.c_keyword), (" Remote.Start", theme.c_normal)],
        [("   do", theme.c_keyword), (" action", theme.c_keyword), (" log", theme.c_normal), (" :", theme.c_normal), (" Log", theme.c_type), ("(", theme.c_normal), ("'Serving'", theme.c_string), (");", theme.c_normal)],
        [("   then", theme.c_keyword), (" Serving", theme.c_type), (";", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Transitions", lines, "Move between states on triggers.", theme, sheet_name="Behavior", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Guards & Effects ---
    lines = [
        [("transition", theme.c_keyword), (" t2", theme.c_normal), (" {", theme.c_normal)],
        [("   first", theme.c_keyword), (" Green", theme.c_type)],
        [("   if", theme.c_keyword), (" traffic == 0", theme.c_normal)],
        [("   do", theme.c_keyword), (" action", theme.c_keyword), (" resetTimer", theme.c_normal)],
        [("   then", theme.c_keyword), (" Red", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Guards & Effects", lines, "Conditions and actions on transition.", theme, sheet_name="Behavior", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3b: Internal Transition ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Monitoring", theme.c_type), (" {", theme.c_normal)],
        [("   state", theme.c_keyword), (" selfCheck", theme.c_normal), (";", theme.c_normal)],
        [("   transition", theme.c_keyword), (" selfCheck", theme.c_normal)],
        [("      accept", theme.c_keyword), (" tick", theme.c_normal)],
        [("      do", theme.c_keyword), (" action", theme.c_keyword), (" check", theme.c_normal), (" then", theme.c_keyword), (" selfCheck", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3b. Internal Transition", lines, "Self-transition pattern.", theme, sheet_name="Behavior", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Action Definition ---
    lines = [
        [("action", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Serve", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" speed", theme.c_normal), (" :", theme.c_normal), (" Speed", theme.c_type), (";", theme.c_normal)],
        [("   out", theme.c_keyword), (" result", theme.c_normal), (" :", theme.c_normal), (" Result", theme.c_type), (";", theme.c_normal)],
        [("   first", theme.c_keyword), (" toss", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" strike", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Action Definition", lines, "Reusable behavior spec.", theme, sheet_name="Behavior", wrapper_type="action")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Action Usage ---
    lines = [
        [("action", theme.c_keyword), (" playPoint", theme.c_normal), (" {", theme.c_normal)],
        [("   action", theme.c_keyword), (" serve", theme.c_normal), (" :", theme.c_normal), (" Serve", theme.c_type), (";", theme.c_normal)],
        [("   perform", theme.c_keyword), (" serve", theme.c_normal), (" {", theme.c_normal)],
        [("      in", theme.c_keyword), (" speed", theme.c_normal), (" =", theme.c_normal), (" 60", theme.c_string), (";", theme.c_normal)],
        [("   }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Action Usage", lines, "Executing an action.", theme, sheet_name="Behavior", wrapper_type="action")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Use Cases ---
    lines = [
        [("use", theme.c_keyword), (" ", theme.c_normal), ("case", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Practice", theme.c_type), (" {", theme.c_normal)],
        [("   subject", theme.c_keyword), (" b", theme.c_normal), (" :", theme.c_normal), (" PickleBot", theme.c_type), (";", theme.c_normal)],
        [("   actor", theme.c_keyword), (" p", theme.c_normal), (" :", theme.c_normal), (" Player", theme.c_type), (";", theme.c_normal)],
        [("   objective", theme.c_keyword), (" {", theme.c_normal)],
        [("      doc", theme.c_keyword), (" /* Improve skills */", theme.c_comment)],
        [("   }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Use Cases", lines, "High-level user goals.", theme, sheet_name="Behavior", wrapper_type="action")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "behavior.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
