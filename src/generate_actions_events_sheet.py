
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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: ACTIONS - EVENTS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Signal Trigger ---
    lines = [
        [("accept", theme.c_keyword), (" start", theme.c_normal), (" :", theme.c_normal), (" StartSignal", theme.c_type), (";", theme.c_normal)],
        [("accept", theme.c_keyword), (" msg", theme.c_normal), (" :", theme.c_normal), (" Message", theme.c_type), (" via", theme.c_keyword), (" p1", theme.c_normal), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Wait for signal */", theme.c_comment)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Signal Triggers", lines, "Waiting for signals.", theme, sheet_name='ActionsEvents', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Change Trigger ---
    lines = [
        [("accept", theme.c_keyword), (" when", theme.c_keyword), (" temperature > 100", theme.c_normal), (";", theme.c_normal)],
        [("accept", theme.c_keyword), (" when", theme.c_keyword), (" tank.full", theme.c_normal), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Wait for condition */", theme.c_comment)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Change Triggers", lines, "Waiting for state/value change.", theme, sheet_name='ActionsEvents', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Time Trigger ---
    lines = [
        [("accept", theme.c_keyword), (" at", theme.c_keyword), (" '12:00:00'", theme.c_string), (";", theme.c_normal)],
        [("accept", theme.c_keyword), (" after", theme.c_keyword), (" 10 [s]", theme.c_string), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Absolute/Relative time */", theme.c_comment)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Time Triggers", lines, "Waiting for time events.", theme, sheet_name='ActionsEvents', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Send Signal ---
    lines = [
        [("send", theme.c_keyword), (" StartSignal", theme.c_type), ("(", theme.c_normal), (")", theme.c_normal), (";", theme.c_normal)],
        [("send", theme.c_keyword), (" Cmd", theme.c_type), ("(", theme.c_normal), ("val", theme.c_normal), ("=", theme.c_normal), ("42", theme.c_string), (")", theme.c_normal), (" to", theme.c_keyword), (" server", theme.c_normal), (";", theme.c_normal)],
        [("send", theme.c_keyword), (" msg", theme.c_normal), (" via", theme.c_keyword), (" pOut", theme.c_normal), (";", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Send Action", lines, "Sending signals.", theme, sheet_name='ActionsEvents', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Advanced Send ---
    lines = [
        [("action", theme.c_keyword), (" prepareAndSend", theme.c_normal), (" {", theme.c_normal)],
        [("   action", theme.c_keyword), (" s", theme.c_normal), (" :", theme.c_normal), (" SendAction", theme.c_type), (" {", theme.c_normal)],
        [("      in", theme.c_keyword), (" payload", theme.c_normal), (" =", theme.c_normal), (" 42", theme.c_string), (";", theme.c_normal)],
        [("      out", theme.c_keyword), (" result", theme.c_normal), (";", theme.c_normal)],
        [("   }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Advanced Send", lines, "Send with complex data.", theme, sheet_name='ActionsEvents', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "actions_events.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
