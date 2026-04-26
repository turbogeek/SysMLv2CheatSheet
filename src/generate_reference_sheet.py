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
    title_text = "Howdy Kitty SysMLv2 Cheat Sheet" if theme_key == "howdy_kitty" else "SysML v2 Cheat Sheet: REFERENCE"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Keywords ---
    lines = [
        [("package", theme.c_keyword), (", ", theme.c_normal), ("part", theme.c_keyword), (", ", theme.c_normal), ("item", theme.c_keyword), (", ", theme.c_normal), ("port", theme.c_keyword)],
        [("attribute", theme.c_keyword), (", ", theme.c_normal), ("action", theme.c_keyword), (", ", theme.c_normal), ("state", theme.c_keyword)],
        [("transition", theme.c_keyword), (", ", theme.c_normal), ("constraint", theme.c_keyword)],
        [("requirement", theme.c_keyword), (", ", theme.c_normal), ("use case", theme.c_keyword)],
        [("import", theme.c_keyword), (", ", theme.c_normal), ("alias", theme.c_keyword), (", ", theme.c_normal), ("metadata", theme.c_keyword)]
    ]
    md_blocks = []
    
    code_1 = """package Reference_1CommonKeywords {
    doc /*
      package, import, private import
      attribute def, attribute
      part def, part
      action def, action
      item def, item
      state def, state
      interface def, port def, port
      connection def, connection
      requirement def, requirement
      constraint def, constraint, assert
      analysis def, analysis
      verification def, verification
      view def, view
      metadata def, metadata
    */
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Common Keywords", lines, "Core language definitions.", theme, full_code=code_1, sheet_name='Reference', wrapper_type='structure')
    md_blocks.append(("header", "1. Common Keywords"))
    md_blocks.append(("text", "Core language definitions."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Primitive Types ---
    lines = [
        [("Boolean", theme.c_type), (" /* true, false */", theme.c_comment)],
        [("Integer", theme.c_type), (" /* 1, -5, 0 */", theme.c_comment)],
        [("Real", theme.c_type), (" /* 3.14, 1.0 */", theme.c_comment)],
        [("String", theme.c_type), (" /* 'text\" */", theme.c_comment)],
        [("UnlimitedNatural", theme.c_type), (" /* 0, 1, * */", theme.c_comment)]
    ]
    code_2 = """package Reference_2PrimitiveTypes {
    private import ScalarValues::*;
    private import Base::*;
    private import SysML::*;
    attribute b : Boolean; /* true, false */
    attribute i : Integer; /* 1, -5, 0 */
    attribute r : Real; /* 3.14, 1.0 */
    attribute s : String; /* 'text' */
    attribute n : Natural; /* 0, 1, * (UnlimitedNatural in v1 */)
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Primitive Types", lines, "Basic data types.", theme, full_code=code_2, sheet_name='Reference', wrapper_type='structure')
    md_blocks.append(("header", "2. Primitive Types"))
    md_blocks.append(("text", "Basic data types."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Relationships ---
    lines = [
        [(":>", theme.c_keyword), (" Specialization (Inheritance)", theme.c_normal)],
        [(":", theme.c_keyword), (" Classification (Typing)", theme.c_normal)],
        [("=", theme.c_keyword), (" Binding / Equality", theme.c_normal)],
        [("connect", theme.c_keyword), (" Connection", theme.c_normal)],
        [("ref", theme.c_keyword), (" Reference (Pointer)", theme.c_normal)],
        [("import", theme.c_keyword), (" Import Namespace", theme.c_normal)]
    ]
    code_3 = """package Reference_3Relationships {
    doc /*
      Generalization ( :> ) - Inheritance
      Subsetting ( :> ) - Hierarchy
      Redefinition ( :>> ) - Specialized replacement
      Reference ( references ) - Pointer
      Conjugation ( ~ ) - Reverse port
      Binding ( = ) - Equality
      Assignment ( := ) - Value set
      Succession ( first..then ) - Ordering
    */
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Relationships", lines, "Connecting elements.", theme, full_code=code_3, sheet_name='Reference', wrapper_type='structure')
    md_blocks.append(("header", "3. Relationships"))
    md_blocks.append(("text", "Connecting elements."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Comments ---
    lines = [
        [("/* Single line */", theme.c_comment), (" (not persisted)", theme.text_sec)],
        [("/* Multi-line", theme.c_comment)],
        [("   comment */", theme.c_comment)],
        [("doc /* Documentation */", theme.c_comment)],
        [("comment", theme.c_keyword), (" about", theme.c_keyword), (" element", theme.c_normal), (" /* text */", theme.c_comment)]
    ]
    code_4 = """package Reference_4Comments {
    /* Single line */
    /* Multi-line
       comment */
    doc /* Documentation */
    /* Single line */
    /* Multi-line
       comment */
    doc /* Documentation */
    part element;
    comment about element /* text */
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Comments", lines, "Annotating code.", theme, full_code=code_4, sheet_name='Reference', wrapper_type='structure')
    md_blocks.append(("header", "4. Comments"))
    md_blocks.append(("text", "Annotating code."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 5: Multiplicity ---
    lines = [
        [("[1]", theme.c_normal), (" Exactly one", theme.c_normal)],
        [("[*]", theme.c_normal), (" Zero or more", theme.c_normal)],
        [("[0..1]", theme.c_normal), (" Optional", theme.c_normal)],
        [("ordered", theme.c_keyword), (" /* Sequence (indexed) */", theme.c_comment)],
        [("nonunique", theme.c_keyword), (" /* Allow duplicates */", theme.c_comment)],
        [("/* Defaults: */", theme.c_comment)],
        [("Part/Attr", theme.c_normal), (" -> [1]", theme.c_normal)],
        [("Other", theme.c_normal), (" -> [0..*]", theme.c_normal)]
    ]
    code_5 = """package Reference_5Multiplicity {
    doc /*
      [1]      - Exactly one (Default)
      [0..1]   - Optional
      [*]      - Zero or more
      [1..*]   - One or more
      [2..5]   - Specific range
    */
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Multiplicity", lines, "Cardinality & Ordering.", theme, full_code=code_5, sheet_name='Reference', wrapper_type='structure')
    md_blocks.append(("header", "5. Multiplicity"))
    md_blocks.append(("text", "Cardinality & Ordering."))
    md_blocks.append(("code", code_5))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Visibility ---
    lines = [
        [("public", theme.c_keyword), (" (default)", theme.c_normal)],
        [("private", theme.c_keyword), (" (internal only)", theme.c_normal)],
        [("protected", theme.c_keyword), (" (subtypes only)", theme.c_normal)]
    ]
    code_6 = """package Reference_6Visibility {
    doc /*
      public    (default) - Visible everywhere
      private   (private) - Visible only inside
      protected (protected) - Visible to children
    */
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Visibility", lines, "Access control.", theme, full_code=code_6, sheet_name='Reference', wrapper_type='structure')
    md_blocks.append(("header", "6. Visibility"))
    md_blocks.append(("text", "Access control."))
    md_blocks.append(("code", code_6))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("reference_sheet.md", "Reference Cheat Sheet", "Keywords and Types", md_blocks, subfolder="cheatsheets")
    
    output_dir = os.path.join("..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "reference.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
