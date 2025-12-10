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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: REQUIREMENTS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Requirement Definition ---
    lines = [
        [("requirement", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Performance", theme.c_type), (" {", theme.c_normal)],
        [("  doc", theme.c_keyword), (" /* The system shall be fast. */", theme.c_comment)],
        [("  attribute", theme.c_keyword), (" maxResponse", theme.c_normal), (" :", theme.c_normal), (" Time", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Requirement Definition", lines, "Defining requirement types.", theme, sheet_name="Requirements", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Requirement Usage ---
    lines = [
        [("requirement", theme.c_keyword), (" req1", theme.c_normal), (" :", theme.c_normal), (" Performance", theme.c_type), (" {", theme.c_normal)],
        [("  doc", theme.c_keyword), (" /* Response < 10ms */", theme.c_comment)],
        [("  id", theme.c_keyword), (" \"REQ-001\"", theme.c_string), (";", theme.c_normal)],
        [("  maxResponse", theme.c_normal), (" =", theme.c_normal), (" 10", theme.c_string), (" [ms]", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Requirement Usage", lines, "Specific requirement instances.", theme, sheet_name="Requirements", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Satisfy Relationship ---
    lines = [
        [("part", theme.c_keyword), (" server", theme.c_normal), (" {", theme.c_normal)],
        [("  satisfy", theme.c_keyword), (" req1", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Or external: */", theme.c_comment)],
        [("satisfy", theme.c_keyword), (" server", theme.c_normal), (" by", theme.c_keyword), (" req1", theme.c_normal), (";", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Satisfy", lines, "Design meets requirement.", theme, sheet_name="Requirements", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 4: Verify Relationship ---
    lines = [
        [("verification", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" TestLatency", theme.c_type), (" {", theme.c_normal)],
        [("  verify", theme.c_keyword), (" req1", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Verify", lines, "Test case for requirement.", theme, sheet_name="Requirements", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 5: Constraint Blocks ---
    lines = [
        [("constraint", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" CheckMass", theme.c_type), (" {", theme.c_normal)],
        [("  in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  m <= 1000 [kg]", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Constraint Definition", lines, "Mathematical rules.", theme, sheet_name="Requirements", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 6: Assertions ---
    lines = [
        [("part", theme.c_keyword), (" car", theme.c_normal), (" {", theme.c_normal)],
        [("  assert", theme.c_keyword), (" constraint", theme.c_keyword), (" CheckMass", theme.c_type), (" {", theme.c_normal)],
        [("    in", theme.c_keyword), (" m", theme.c_normal), (" =", theme.c_normal), (" mass", theme.c_normal), (";", theme.c_normal)],
        [("  }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Assertions", lines, "Applying constraints.", theme, sheet_name="Requirements", wrapper_type="structure")
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 7: Trace & Refine ---
    lines = [
        [("requirement", theme.c_keyword), (" req2", theme.c_normal), (" {", theme.c_normal)],
        [("  refine", theme.c_keyword), (" req1", theme.c_normal), (";", theme.c_normal)],
        [("  trace", theme.c_keyword), (" old_doc_item", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "7. Trace & Refine", lines, "Requirement relationships.", theme, sheet_name="Requirements", wrapper_type="structure")
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "requirements.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
