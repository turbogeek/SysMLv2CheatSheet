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
    title_text = "Howdy Kitty SysMLv2 Cheat Sheet" if theme_key == "howdy_kitty" else "SysML v2 Cheat Sheet: GRAPHICAL NOTATION"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Helper to draw a graphical box ---
    def draw_graphical_card(x, y, title, draw_func, explanation, theme):
        h = 200 # Fixed height for graphical cards
        svg = utils.rect(x, y, COL_WIDTH, h, theme.card_bg)
        svg += utils.text(x + 20, y + 35, title, 24, theme.c_type, "bold", font_family=theme.title_font)
        
        # Draw the graphical element in the center
        cx = x + COL_WIDTH / 2
        cy = y + 100
        svg += draw_func(cx, cy, theme)
        
        svg += utils.text(x + 20, y + h - 20, explanation, 16, theme.text_sec, "italic")
        return svg, h

    # --- Graphical Draw Functions (SysML v2) ---
    # Definition: Rectangle
    # Usage: Rounded Rectangle
    
    def draw_def_box(cx, cy, theme, keyword, name):
        w, h = 140, 80
        # Sharp rectangle for definition
        s = f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" fill="none" stroke="{theme.c_normal}" stroke-width="2"/>'
        # Keyword
        s += utils.text(cx, cy-15, keyword, 12, theme.c_normal, "normal", "middle")
        # Name
        s += utils.text(cx, cy+5, name, 14, theme.c_normal, "bold", "middle")
        return s

    def draw_usage_box(cx, cy, theme, keyword, name):
        w, h = 140, 80
        # Rounded rectangle for usage
        s = f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" fill="none" stroke="{theme.c_normal}" stroke-width="2" rx="15" ry="15"/>'
        # Keyword
        s += utils.text(cx, cy-15, keyword, 12, theme.c_normal, "normal", "middle")
        # Name
        s += utils.text(cx, cy+5, name, 14, theme.c_normal, "bold", "middle")
        return s

    def draw_part_def(cx, cy, theme):
        return draw_def_box(cx, cy, theme, "part def", "Vehicle")

    def draw_part_usage(cx, cy, theme):
        return draw_usage_box(cx, cy, theme, "part", "engine")

    def draw_action_def(cx, cy, theme):
        return draw_def_box(cx, cy, theme, "action def", "Drive")

    def draw_action_usage(cx, cy, theme):
        return draw_usage_box(cx, cy, theme, "action", "drive")

    def draw_requirement_def(cx, cy, theme):
        return draw_def_box(cx, cy, theme, "requirement def", "Performance")
        
    def draw_requirement_usage(cx, cy, theme):
        return draw_usage_box(cx, cy, theme, "requirement", "req1")

    def draw_state_def(cx, cy, theme):
        return draw_def_box(cx, cy, theme, "state def", "Operating")

    def draw_state_usage(cx, cy, theme):
        return draw_usage_box(cx, cy, theme, "state", "on")

    def draw_use_case_def(cx, cy, theme):
        return draw_def_box(cx, cy, theme, "use case def", "DriveCar")

    def draw_actor_def(cx, cy, theme):
        return draw_def_box(cx, cy, theme, "actor def", "Driver")

    def draw_actor_usage(cx, cy, theme):
        return draw_usage_box(cx, cy, theme, "actor", "driver")

    # --- Cards ---
    # Column 1: Definitions (Rectangles)
    card, h = draw_graphical_card(col1_x, cur_y_c1, "1. Part Definition", draw_part_def, "Rectangle: 'part def'", theme)
    svg += card
    cur_y_c1 += h + ROW_GAP

    card, h = draw_graphical_card(col1_x, cur_y_c1, "2. Action Definition", draw_action_def, "Rectangle: 'action def'", theme)
    svg += card
    cur_y_c1 += h + ROW_GAP

    card, h = draw_graphical_card(col1_x, cur_y_c1, "3. Requirement Definition", draw_requirement_def, "Rectangle: 'requirement def'", theme)
    svg += card
    cur_y_c1 += h + ROW_GAP

    card, h = draw_graphical_card(col1_x, cur_y_c1, "4. State Definition", draw_state_def, "Rectangle: 'state def'", theme)
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    card, h = draw_graphical_card(col1_x, cur_y_c1, "5. Use Case Definition", draw_use_case_def, "Rectangle: 'use case def'", theme)
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    card, h = draw_graphical_card(col1_x, cur_y_c1, "6. Actor Definition", draw_actor_def, "Rectangle: 'actor def'", theme)
    svg += card
    cur_y_c1 += h + ROW_GAP

    # Column 2: Usages (Rounded Rectangles)
    card, h = draw_graphical_card(col2_x, cur_y_c2, "7. Part Usage", draw_part_usage, "Rounded Rect: 'part'", theme)
    svg += card
    cur_y_c2 += h + ROW_GAP

    card, h = draw_graphical_card(col2_x, cur_y_c2, "8. Action Usage", draw_action_usage, "Rounded Rect: 'action'", theme)
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    card, h = draw_graphical_card(col2_x, cur_y_c2, "9. Requirement Usage", draw_requirement_usage, "Rounded Rect: 'requirement'", theme)
    svg += card
    cur_y_c2 += h + ROW_GAP

    card, h = draw_graphical_card(col2_x, cur_y_c2, "10. State Usage", draw_state_usage, "Rounded Rect: 'state'", theme)
    svg += card
    cur_y_c2 += h + ROW_GAP

    card, h = draw_graphical_card(col2_x, cur_y_c2, "11. Actor Usage", draw_actor_usage, "Rounded Rect: 'actor'", theme)
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    output_dir = os.path.join("..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "graphical.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
