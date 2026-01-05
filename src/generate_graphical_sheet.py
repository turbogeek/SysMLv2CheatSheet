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
    
    # --- Helper to save symbol SVG ---
    def save_symbol_svg(name, draw_func, theme):
        # Create a small canvas for the symbol
        w, h = 200, 100
        svg = utils.svg_start(w, h, theme, include_script=False)
        svg += draw_func(w/2, h/2, theme)
        svg += utils.svg_end()
        
        # Save to output/cheatsheets/assets/symbols/theme/name.svg
        # This keeps it relative to the graphical_sheet.md which is in output/cheatsheets/
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # output/cheatsheets/assets/symbols/light/
        output_dir = os.path.join(base_dir, "..", "output", "cheatsheets", "assets", "symbols", theme_key)
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{name}.svg"
        output_path = os.path.join(output_dir, filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(svg)
        
        # Return relative path for Markdown 
        # From cheatsheets/graphical_sheet.md to cheatsheets/assets/symbols/theme/file.svg
        # Path: assets/symbols/theme/file.svg
        return f"assets/symbols/{theme_key}/{filename}"

    # --- Helper to draw a graphical box ---
    def draw_graphical_card(x, y, title, draw_func, explanation, syntax, example, theme):
        h = 240 # Increased height
        svg = utils.rect(x, y, COL_WIDTH, h, theme.card_bg)
        svg += utils.text(x + 20, y + 35, title, 24, theme.c_type, "bold", font_family=theme.title_font)
        
        # Draw the graphical element on the LEFT
        cx = x + 100 
        cy = y + 120
        svg += draw_func(cx, cy, theme)
        
        # Separator line
        svg += f'<line x1="{x+200}" y1="{y+60}" x2="{x+200}" y2="{y+h-20}" stroke="{theme.c_normal}" stroke-width="1" stroke-dasharray="4" />'
        
        # Draw Text/Example on the RIGHT
        tx = x + 220
        ty = y + 70
        
        # Syntax
        svg += utils.text(tx, ty, "Syntax:", 14, theme.c_keyword, "bold")
        svg += utils.text(tx, ty + 20, syntax, 14, theme.c_normal, "normal", font_family="Consolas, monospace")
        
        # Example
        ty += 50
        svg += utils.text(tx, ty, "Example:", 14, theme.c_keyword, "bold")
        
        # Handle multi-line examples
        ex_lines = example.split('\n')
        ey = ty + 20
        for el in ex_lines:
            svg += utils.text(tx, ey, el, 14, theme.c_comment, "italic", font_family="Consolas, monospace")
            ey += 18

        # Explanation at bottom left? or just left side below graphic?
        # Let's put explanation below graphic
        svg += utils.text(x + 20, y + h - 20, explanation, 12, theme.text_sec, "italic")
        
        return svg, h

    # --- Graphical Draw Functions (SysML v2) ---
    # Definition: Rectangle
    # Usage: Rounded Rectangle
    
    def draw_def_box(cx, cy, theme, keyword, name):
        w, h = 140, 60
        s = f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" fill="none" stroke="{theme.c_normal}" stroke-width="2"/>'
        s += utils.text(cx, cy-10, keyword, 12, theme.c_normal, "normal", "middle")
        s += utils.text(cx, cy+10, name, 14, theme.c_normal, "bold", "middle")
        return s

    def draw_usage_box(cx, cy, theme, keyword, name):
        w, h = 140, 60
        s = f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" fill="none" stroke="{theme.c_normal}" stroke-width="2" rx="15" ry="15"/>'
        s += utils.text(cx, cy-10, keyword, 12, theme.c_normal, "normal", "middle")
        s += utils.text(cx, cy+10, name, 14, theme.c_normal, "bold", "middle")
        return s

    # --- Relationships ---
    def draw_specialization(cx, cy, theme):
        x1, y1 = cx - 50, cy
        x2, y2 = cx + 50, cy
        s = f'<line x1="{x1}" y1="{y1}" x2="{x2-12}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="2" />'
        s += f'<polygon points="{x2},{y2} {x2-12},{y2-6} {x2-12},{y2+6}" fill="{theme.bg_color}" stroke="{theme.c_normal}" stroke-width="2" />'
        return s

    def draw_composition(cx, cy, theme):
        x1, y1 = cx - 50, cy
        x2, y2 = cx + 50, cy
        s = f'<line x1="{x1+12}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="2" />'
        s += f'<polygon points="{x1},{y1} {x1+8},{y1-4} {x1+16},{y1} {x1+8},{y1+4}" fill="{theme.c_normal}" stroke="{theme.c_normal}" stroke-width="2" />'
        return s
        
    def draw_reference(cx, cy, theme):
        x1, y1 = cx - 50, cy
        x2, y2 = cx + 50, cy
        s = f'<line x1="{x1+12}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="2" />'
        s += f'<polygon points="{x1},{y1} {x1+8},{y1-4} {x1+16},{y1} {x1+8},{y1+4}" fill="{theme.bg_color}" stroke="{theme.c_normal}" stroke-width="2" />'
        return s

    def draw_import(cx, cy, theme):
        x1, y1 = cx - 50, cy
        x2, y2 = cx + 50, cy
        s = f'<line x1="{x1}" y1="{y1}" x2="{x2-2}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="2" stroke-dasharray="5,5" />'
        s += f'<line x1="{x2-8}" y1="{y2-5}" x2="{x2}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="2" />'
        s += f'<line x1="{x2-8}" y1="{y2+5}" x2="{x2}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="2" />'
        s += utils.text(cx, cy - 15, "«import»", 12, theme.c_normal, "normal", "middle")
        return s
        
    def draw_binding(cx, cy, theme):
        x1, y1 = cx - 50, cy
        x2, y2 = cx + 50, cy
        s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="3" />' 
        s += utils.text(cx, cy - 15, "«bind»", 12, theme.c_normal, "normal", "middle")
        return s

    def draw_succession(cx, cy, theme):
        x1, y1 = cx - 50, cy
        x2, y2 = cx + 50, cy
        s = f'<line x1="{x1}" y1="{y1}" x2="{x2-2}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="2" stroke-dasharray="5,5" />'
        s += f'<line x1="{x2-8}" y1="{y2-5}" x2="{x2}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="2" />'
        s += f'<line x1="{x2-8}" y1="{y2+5}" x2="{x2}" y2="{y2}" stroke="{theme.c_normal}" stroke-width="2" />'
        return s

    # Wrappers for Nodes
    def draw_part_def(cx, cy, theme): return draw_def_box(cx, cy, theme, "«part def»", "Vehicle")
    def draw_part_usage(cx, cy, theme): return draw_usage_box(cx, cy, theme, "«part»", "engine")
    def draw_action_def(cx, cy, theme): return draw_def_box(cx, cy, theme, "«action def»", "Drive")
    def draw_action_usage(cx, cy, theme): return draw_usage_box(cx, cy, theme, "«action»", "drive")
    def draw_req_def(cx, cy, theme): return draw_def_box(cx, cy, theme, "«requirement def»", "Perf")
    def draw_req_usage(cx, cy, theme): return draw_usage_box(cx, cy, theme, "«requirement»", "req1")
    def draw_state_def(cx, cy, theme): return draw_def_box(cx, cy, theme, "«state def»", "Idle")
    def draw_state_usage(cx, cy, theme): return draw_usage_box(cx, cy, theme, "«state»", "off")

    # --- Cards List ---
    # Format: (Title, DrawFunc, Explanation, Syntax, Example)
    
    nodes = [
        ("Part Definition", draw_part_def, "Rectangle: 'part def'", "part def Name;", "part def Vehicle;"),
        ("Part Usage", draw_part_usage, "Rounded Rect: 'part'", "part name : Type;", "part engine : Engine;"),
        ("Action Definition", draw_action_def, "Rectangle: 'action def'", "action def Name;", "action def Drive;"),
        ("Action Usage", draw_action_usage, "Rounded Rect: 'action'", "action name : Type;", "action drive : Drive;"),
        ("Requirement Def", draw_req_def, "Rectangle: 'requirement def'", "requirement def Name;", "requirement def Perf;"),
        ("Requirement Usage", draw_req_usage, "Rounded Rect: 'requirement'", "requirement name : Type;", "requirement req1 : Perf;"),
        ("State Definition", draw_state_def, "Rectangle: 'state def'", "state def Name;", "state def Idle;"),
        ("State Usage", draw_state_usage, "Rounded Rect: 'state'", "state name;", "state off;")
    ]
    
    relations = [
        ("Specialization", draw_specialization, "Solid line, hollow triangle", "def A :> B;", "part def Car :> Vehicle;"),
        ("Composition", draw_composition, "Solid line, filled diamond", "part name : Type;", "part wheel : Wheel;"),
        ("Reference", draw_reference, "Solid line, hollow diamond", "ref part name : Type;", "ref part driver : Person;"),
        ("Import", draw_import, "Dashed line, open arrow", "import Package::*;", "import SI::*;"),
        ("Binding", draw_binding, "Solid line, «bind»", "bind a = b;", "bind p1 = p2;"),
        ("Succession", draw_succession, "Dashed line, open arrow", "first a then b;", "first start then stop;")
    ]

    all_items = nodes + relations
    md_blocks = [] # For markdown generation

    # Layout Logic
    # Col 1: Nodes (8)
    # Col 2: Relationships (6)
    
    # Draw Nodes (Column 1)
    card_h_fixed = 180
    
    md_blocks.append(("header", "1. Nodes"))
    
    cur_y = 150
    for title, func, expl, syn, ex in nodes:
        # 1. Main Sheet Drawing
        card, h = draw_graphical_card(col1_x, cur_y, title, func, expl, syn, ex, theme)
        svg += card
        cur_y += h + ROW_GAP
        
        # 2. Markdown Asset Generation
        if theme_key == 'light':
            img_path = save_symbol_svg(utils.sanitize_name(title), func, theme)
            md_blocks.append(("header", title))
            md_blocks.append(("image", (img_path, title)))
            md_blocks.append(("text", f"**Notation**: {expl}\n\n**Syntax**: `{syn}`\n\n**Example**: `{ex}`"))

    # Draw Relations (Column 2)
    md_blocks.append(("header", "2. Relationships"))
    
    cur_y = 150
    for title, func, expl, syn, ex in relations:
        card, h = draw_graphical_card(col2_x, cur_y, title, func, expl, syn, ex, theme)
        svg += card
        cur_y += h + ROW_GAP
        
        if theme_key == 'light':
            img_path = save_symbol_svg(utils.sanitize_name(title), func, theme)
            md_blocks.append(("header", title))
            md_blocks.append(("image", (img_path, title)))
            md_blocks.append(("text", f"**Notation**: {expl}\n\n**Syntax**: `{syn}`\n\n**Example**: `{ex}`"))

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)
    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("graphical_sheet.md", "Graphical Cheat Sheet", "Standard Graphical Notation", md_blocks, subfolder="cheatsheets")
    
    output_dir = os.path.join("..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "graphical.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
