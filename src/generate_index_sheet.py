import html
import os
from themes import THEMES

# --- Configuration ---
WIDTH = 1200
HEIGHT = 1600
MARGIN = 30
COL_GAP = 20
ROW_GAP = 20
COL_WIDTH = (WIDTH - (2 * MARGIN) - COL_GAP) / 2

# --- SVG Helpers ---
def svg_start(w, h, theme):
    svg = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="font-family: {theme.font_family}; background-color: {theme.bg_color};">'
    if theme.branding_svg:
        svg += theme.branding_svg
    return svg

def svg_end():
    return '</svg>'

def rect(x, y, w, h, fill, r=10):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" rx="{r}" ry="{r}" />'

def text(x, y, content, size, color, weight="normal", anchor="start", font_family=None):
    font_attr = f'font-family="{font_family}"' if font_family else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" {font_attr}>{html.escape(content)}</text>'

def draw_section(x, y, title, items, theme):
    # items is a list of (keyword, sheet_name)
    h = 60 + (len(items) * 25) + 40
    svg = rect(x, y, COL_WIDTH, h, theme.card_bg)
    svg += text(x + 20, y + 35, title, 24, theme.c_type, "bold", font_family=theme.title_font)
    
    cy = y + 70
    for keyword, sheet in items:
        svg += text(x + 20, cy, keyword, 18, theme.c_keyword, "bold")
        svg += text(x + 200, cy, sheet, 18, theme.c_normal)
        cy += 25
    return svg, h

# --- Content ---
def generate_for_theme(theme_key, theme):
    svg = svg_start(WIDTH, HEIGHT, theme)
    
    # Header
    title_text = "Howdy Kitty SysMLv2 Cheat Sheet" if theme_key == "howdy_kitty" else "SysML v2 Cheat Sheet: INDEX"
    svg += text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Column 1 ---
    
    # A-E
    items = [
        ("abstract", "Reference"),
        ("accept", "Actions"),
        ("action", "Actions"),
        ("actor", "Cases"),
        ("alias", "Reference"),
        ("analysis", "Cases"),
        ("assert", "Requirements"),
        ("assign", "Actions"),
        ("attribute", "Structure"),
        ("bind", "Relationships"),
        ("case", "Cases"),
        ("connect", "Relationships"),
        ("connection", "Relationships"),
        ("constraint", "Requirements"),
        ("decision", "Actions"),
        ("def", "Structure"),
        ("doc", "Requirements"),
        ("do", "States"),
        ("else", "Actions"),
        ("end", "Connections"),
        ("entry", "States"),
        ("enum", "Structure"),
        ("exit", "States"),
    ]
    card, h = draw_section(col1_x, cur_y_c1, "Keywords A-E", items, theme)
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # F-O
    items = [
        ("first", "Actions"),
        ("flow", "Relationships"),
        ("for", "Actions"),
        ("id", "Requirements"),
        ("if", "Actions"),
        ("import", "Structure"),
        ("in", "Actions"),
        ("inout", "Actions"),
        ("interface", "Relationships"),
        ("item", "Structure"),
        ("loop", "Actions"),
        ("merge", "Actions"),
        ("objective", "Cases"),
        ("out", "Actions"),
    ]
    card, h = draw_section(col1_x, cur_y_c1, "Keywords F-O", items, theme)
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Column 2 ---
    
    # P-R
    items = [
        ("package", "Structure"),
        ("parallel", "States"),
        ("part", "Structure"),
        ("perform", "Actions"),
        ("port", "Structure"),
        ("redefine", "Relationships"),
        ("refine", "Relationships"),
        ("requirement", "Requirements"),
        ("return", "Actions"),
    ]
    card, h = draw_section(col2_x, cur_y_c2, "Keywords P-R", items, theme)
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # S-Z
    items = [
        ("satisfy", "Relationships"),
        ("send", "Actions"),
        ("specialize", "Relationships"),
        ("state", "States"),
        ("subject", "Cases"),
        ("subsets", "Relationships"),
        ("succession", "Relationships"),
        ("then", "Actions"),
        ("to", "States"),
        ("trace", "Relationships"),
        ("transition", "States"),
        ("use case", "Cases"),
        ("verification", "Cases"),
        ("verify", "Relationships"),
        ("while", "Actions"),
    ]
    card, h = draw_section(col2_x, cur_y_c2, "Keywords S-Z", items, theme)
    svg += card
    cur_y_c2 += h + ROW_GAP

    # Symbols
    items = [
        (":>", "Inheritance / Subsetting"),
        (":>>", "Usage Redefinition"),
        ("::", "Namespace Scope"),
        ("~", "Conjugation / Operator"),
        ("=", "Constraint / Binding"),
        (":=", "Assignment / Init Value"),
        ("== / ===", "Value/Identity Equality"),
        ("* / **", "Multiplicity / Wildcards"),
        ("@ / @@", "Metadata / Type Test"),
        ("' / \" / \\", "Escapes & Literals")
    ]
    card, h = draw_section(col2_x, cur_y_c2, "Symbols", items, theme)
    svg += card
    cur_y_c2 += h + ROW_GAP

    svg += svg_end()
    
    output_dir = os.path.join("..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "index.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
