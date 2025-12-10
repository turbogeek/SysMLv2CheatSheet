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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: SHORTHAND & ALTERNATIVES", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Specialization ---
    lines = [
        [("part", theme.c_keyword), (" def", theme.c_keyword), (" Car", theme.c_type), (" :>", theme.c_keyword), (" Vehicle", theme.c_type), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Equivalent to: */", theme.c_comment)],
        [("part", theme.c_keyword), (" def", theme.c_keyword), (" Car", theme.c_type), (" specializes", theme.c_keyword), (" Vehicle", theme.c_type), (";", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Specialization (:>)", lines, "Shorthand for 'specializes'.", theme, sheet_name="Shorthand", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Subsetting ---
    lines = [
        [("part", theme.c_keyword), (" engine", theme.c_normal), (" :>", theme.c_keyword), (" parts", theme.c_normal), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Equivalent to: */", theme.c_comment)],
        [("part", theme.c_keyword), (" engine", theme.c_normal), (" subsets", theme.c_keyword), (" parts", theme.c_normal), (";", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Subsetting (:>)", lines, "Shorthand for 'subsets'.", theme, sheet_name="Shorthand", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Redefinition ---
    lines = [
        [("attribute", theme.c_keyword), (" :>>", theme.c_keyword), (" mass", theme.c_normal), (" =", theme.c_normal), (" 100", theme.c_string), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Equivalent to: */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" redefines", theme.c_keyword), (" mass", theme.c_normal), (" =", theme.c_normal), (" 100", theme.c_string), (";", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Redefinition (:>>)", lines, "Shorthand for 'redefines'.", theme, sheet_name="Shorthand", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Conjugation ---
    lines = [
        [("port", theme.c_keyword), (" p", theme.c_normal), (" :", theme.c_normal), (" ~", theme.c_keyword), ("Interface", theme.c_type), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Equivalent to: */", theme.c_comment)],
        [("port", theme.c_keyword), (" p", theme.c_normal), (" :", theme.c_normal), (" conjugated", theme.c_keyword), (" Interface", theme.c_type), (";", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Conjugation (~)", lines, "Shorthand for 'conjugated'.", theme, sheet_name="Shorthand", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Feature Values ---
    lines = [
        [("attribute", theme.c_keyword), (" x", theme.c_normal), (" =", theme.c_normal), (" 1", theme.c_string), (";", theme.c_normal), (" /* Binding (Equality) */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" y", theme.c_normal), (" :=", theme.c_normal), (" 2", theme.c_string), (";", theme.c_normal), (" /* Initial Value */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" z", theme.c_normal), (" default", theme.c_keyword), (" =", theme.c_normal), (" 3", theme.c_string), (";", theme.c_normal), (" /* Default Value */", theme.c_comment)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Feature Values", lines, "Assignment variations.", theme, sheet_name="Shorthand", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Multiplicity ---
    lines = [
        [("part", theme.c_keyword), (" many", theme.c_normal), ("[*]", theme.c_keyword), (";", theme.c_normal), (" /* 0..* */", theme.c_comment)],
        [("part", theme.c_keyword), (" one", theme.c_normal), (";", theme.c_normal), (" /* 1..1 (Default) */", theme.c_comment)],
        [("part", theme.c_keyword), (" opt", theme.c_normal), ("[0..1]", theme.c_keyword), (";", theme.c_normal), (" /* 0..1 */", theme.c_comment)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Multiplicity", lines, "Common shorthands.", theme, sheet_name="Shorthand", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "shorthand.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
