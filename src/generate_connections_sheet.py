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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: CONNECTIONS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: PickleBot Networking ({theme.name})", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Connection Def ---
    lines = [
        [("connection", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" DeviceConn", theme.c_type), (" {", theme.c_normal)],
        [("   end", theme.c_keyword), (" hub", theme.c_normal), (" :", theme.c_normal), (" Hub", theme.c_type), (";", theme.c_normal)],
        [("   end", theme.c_keyword), (" device", theme.c_normal), (" :", theme.c_normal), (" Device", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Connection Definition", lines, "Defining connection types.", theme, sheet_name='Connections', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 1b: Connection Usage ---
    lines = [
        [("part", theme.c_keyword), (" context", theme.c_normal), (" {", theme.c_normal)],
        [("   connection", theme.c_keyword), (" c1", theme.c_normal), (" :", theme.c_normal), (" DeviceConn", theme.c_type)],
        [("      connect", theme.c_keyword), (" hub", theme.c_normal), (" to", theme.c_keyword), (" device", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1b. Connection Usage", lines, "Connecting parts.", theme, sheet_name='Connections', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Binding Connector ---
    lines = [
        [("part", theme.c_keyword), (" system", theme.c_normal), (" {", theme.c_normal)],
        [("   part", theme.c_keyword), (" a", theme.c_normal), (" :", theme.c_normal), (" A", theme.c_type), (";", theme.c_normal)],
        [("   part", theme.c_keyword), (" b", theme.c_normal), (" :", theme.c_normal), (" B", theme.c_type), (";", theme.c_normal)],
        [("   bind", theme.c_keyword), (" a.p1", theme.c_normal), (" =", theme.c_normal), (" b.p2", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Binding Connector (=)", lines, "Equating two elements.", theme, sheet_name='Connections', wrapper_type='structure')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Interface Connection ---
    lines = [
        [("interface", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" IData", theme.c_type), (" {", theme.c_normal)],
        [("   end", theme.c_keyword), (" source", theme.c_normal), (";", theme.c_normal)],
        [("   end", theme.c_keyword), (" target", theme.c_normal), (";", theme.c_normal)],
        [("   flow", theme.c_keyword), (" source", theme.c_normal), (" to", theme.c_keyword), (" target", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Interface Connection", lines, "Flows within interfaces.", theme, sheet_name='Connections', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Succession Flow ---
    lines = [
        [("action", theme.c_keyword), (" process", theme.c_normal), (" {", theme.c_normal)],
        [("   step1", theme.c_normal), (" then", theme.c_keyword), (" step2", theme.c_normal), (";", theme.c_normal)],
        [("   doc", theme.c_keyword), (" /* Equivalent to: */", theme.c_comment)],
        [("   flow", theme.c_keyword), (" from", theme.c_keyword), (" step1", theme.c_normal), (" to", theme.c_keyword), (" step2", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Succession Flow", lines, "Control/Data flow.", theme, sheet_name='Connections', wrapper_type='structure')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    output_dir = os.path.join("..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "connections.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
