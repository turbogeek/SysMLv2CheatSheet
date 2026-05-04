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
    md_blocks = []
    
    code_1 = """package Shorthand_1Specialization {
    private import ScalarValues::*;
    private import SysML::*;
    part def Vehicle;
    /* Wrapped Snippet (Structure Context) */
    part  def  Car  :>  Vehicle ;
    doc  /* Equivalent to: 
            part  def  Car  specializes  Vehicle ; */
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Specialization (:>)", lines, "Shorthand for 'specializes'.", theme, full_code=code_1, sheet_name="Shorthand", wrapper_type="structure")
    md_blocks.append(("header", "1. Specialization (:>)"))
    md_blocks.append(("text", "Shorthand for 'specializes'."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Subsetting ---
    lines = [
        [("part", theme.c_keyword), (" engine", theme.c_normal), (" :>", theme.c_keyword), (" parts", theme.c_normal), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Equivalent to: */", theme.c_comment)],
        [("part", theme.c_keyword), (" engine", theme.c_normal), (" subsets", theme.c_keyword), (" parts", theme.c_normal), (";", theme.c_normal)]
    ]
    code_2 = """package Shorthand_2Subsetting {
    private import ScalarValues::*;
    private import SysML::*;
    part parts;
    /* Wrapped Snippet (Structure Context) */
    part  engine  :>  parts ;
    doc  /* Equivalent to: 
            part  engine  subsets  parts ; */
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Subsetting (:>)", lines, "Shorthand for 'subsets'.", theme, full_code=code_2, sheet_name="Shorthand", wrapper_type="structure")
    md_blocks.append(("header", "2. Subsetting (:>)"))
    md_blocks.append(("text", "Shorthand for 'subsets'."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Redefinition ---
    lines = [
        [("attribute", theme.c_keyword), (" :>>", theme.c_keyword), (" mass", theme.c_normal), (" =", theme.c_normal), (" 100", theme.c_string), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Equivalent to: */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" redefines", theme.c_keyword), (" mass", theme.c_normal), (" =", theme.c_normal), (" 100", theme.c_string), (";", theme.c_normal)]
    ]
    code_3 = """comment about Shorthand_3Redefinition /* Source: Shorthand_3Redefinition.sysml */
package Shorthand_3Redefinition {
    private import ISQ::*;
    comment /* Wrapped Snippet (Structure Context)
    attribute partMass : ISQBase::mass  =  100.0 ;
    attribute partMass1 :>> partMass  =  101.0 ;   
    attribute  partMass2 redefines  partMass  =  101.0 ;
    comment about partMass1, partMass2 /* :>> and redefines are equivelnt */
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Redefinition (:>>)", lines, "Shorthand for 'redefines'.", theme, full_code=code_3, sheet_name="Shorthand", wrapper_type="structure")
    md_blocks.append(("header", "3. Redefinition (:>>)"))
    md_blocks.append(("text", "Shorthand for 'redefines'."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Conjugation ---
    lines = [
        [("port", theme.c_keyword), (" p", theme.c_normal), (" :", theme.c_normal), (" ~", theme.c_keyword), ("Interface", theme.c_type), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Equivalent to: */", theme.c_comment)],
        [("port", theme.c_keyword), (" p", theme.c_normal), (" :", theme.c_normal), (" conjugated", theme.c_keyword), (" Interface", theme.c_type), (";", theme.c_normal)]
    ]
    code_4 = """package Shorthand_4Conjugation {
    private import ScalarValues::*;
    private import SysML::*;
    port def Interface;
    /* Wrapped Snippet (Structure Context) */
    port  p  :  ~ Interface ;
    doc  /* Equivalent to: 
            port  p  :  conjugated  Interface ; */
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Conjugation (~)", lines, "Shorthand for 'conjugated'.", theme, full_code=code_4, sheet_name="Shorthand", wrapper_type="structure")
    md_blocks.append(("header", "4. Conjugation (~)"))
    md_blocks.append(("text", "Shorthand for 'conjugated'."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Feature Values ---
    lines = [
        [("attribute", theme.c_keyword), (" x", theme.c_normal), (" =", theme.c_normal), (" 1", theme.c_string), (";", theme.c_normal), (" /* Binding (Equality) */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" y", theme.c_normal), (" :=", theme.c_normal), (" 2", theme.c_string), (";", theme.c_normal), (" /* Initial Value */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" z", theme.c_normal), (" default", theme.c_keyword), (" =", theme.c_normal), (" 3", theme.c_string), (";", theme.c_normal), (" /* Default Value */", theme.c_comment)]
    ]
    code_5 = """package Shorthand_5FeatureValues {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    attribute  x  =  1 ;  /* Binding (Equality) */
    attribute  y  :=  2 ;  /* Initial Value */
    attribute  z  default  =  3 ;  /* Default Value */
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Feature Values", lines, "Assignment variations.", theme, full_code=code_5, sheet_name="Shorthand", wrapper_type="structure")
    md_blocks.append(("header", "5. Feature Values"))
    md_blocks.append(("text", "Assignment variations."))
    md_blocks.append(("code", code_5))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Multiplicity ---
    lines = [
        [("part", theme.c_keyword), (" many", theme.c_normal), ("[*]", theme.c_keyword), (";", theme.c_normal), (" /* 0..* */", theme.c_comment)],
        [("part", theme.c_keyword), (" one", theme.c_normal), (";", theme.c_normal), (" /* 1..1 (Default) */", theme.c_comment)],
        [("part", theme.c_keyword), (" opt", theme.c_normal), ("[0..1]", theme.c_keyword), (";", theme.c_normal), (" /* 0..1 */", theme.c_comment)],
        [("Note:", theme.c_keyword), (" Modifiers after [*], no {}", theme.c_normal)]
    ]
    code_6 = """package Shorthand_6Multiplicity {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    part  many [*] ;  /* 0..* */
    part  one ;  /* 1..1 (Default) */
    part  opt [0..1] ;  /* 0..1 */
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Multiplicity", lines, "Common shorthands.", theme, full_code=code_6, sheet_name="Shorthand", wrapper_type="structure")
    md_blocks.append(("header", "6. Multiplicity"))
    md_blocks.append(("text", "Common shorthands."))
    md_blocks.append(("code", code_6))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("shorthand_sheet.md", "Shorthand Cheat Sheet", "Syntax Shortcuts", md_blocks, subfolder="cheatsheets")
    
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
