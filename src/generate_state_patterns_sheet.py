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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: STATE PATTERNS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Entry/Do/Exit ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Active", theme.c_type), (" {", theme.c_normal)],
        [("   entry", theme.c_keyword), (" action", theme.c_keyword), (" :", theme.c_normal), (" logStart", theme.c_normal), (";", theme.c_normal)],
        [("   do", theme.c_keyword), (" action", theme.c_keyword), (" :", theme.c_normal), (" maintain", theme.c_normal), (";", theme.c_normal)],
        [("   exit", theme.c_keyword), (" action", theme.c_keyword), (" :", theme.c_normal), (" logEnd", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    md_blocks = []
    
    code_1 = """package StatePatterns_1EntryDoExit {
    private import ScalarValues::*;
    private import SysML::*;
    action def logStart;
    action def maintain;
    action def logEnd;
    state def Active {
       entry action : logStart;
       do action : maintain;
       exit action : logEnd;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Entry/Do/Exit", lines, "State lifecycle actions.", theme, full_code=code_1, sheet_name="StatePatterns", wrapper_type="structure")
    md_blocks.append(("header", "1. Entry/Do/Exit"))
    md_blocks.append(("text", "State lifecycle actions."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP
    # --- Card 2: Composite State ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Composite", theme.c_type), (" {", theme.c_normal)],
        [("   entry", theme.c_keyword), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Sub1", theme.c_type), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Sub2", theme.c_type), (";", theme.c_normal)],
        [("   transition", theme.c_keyword), (" t1", theme.c_normal)],
        [("      first", theme.c_keyword), (" Sub1", theme.c_type)],
        [("      then", theme.c_keyword), (" Sub2", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_2 = """package StatePatterns_2CompositeState {
    private import ScalarValues::*;
    private import SysML::*;
    state def Composite {
       entry;
       state Sub1;
       state Sub2;
       transition t1
          first Sub1
          then Sub2;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Composite State", lines, "States within states.", theme, full_code=code_2, sheet_name="StatePatterns", wrapper_type="structure")
    md_blocks.append(("header", "2. Composite State"))
    md_blocks.append(("text", "States within states."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Exhibit State ---
    lines = [
        [("part", theme.c_keyword), (" def", theme.c_keyword), (" Vehicle", theme.c_type), (" {", theme.c_normal)],
        [("   exhibit", theme.c_keyword), (" state", theme.c_keyword), (" opState", theme.c_normal)],
        [("      references", theme.c_keyword), (" VehicleStates::operating", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_3 = """package StatePatterns_3ExhibitState {
    private import ScalarValues::*;
    private import SysML::*;
    package VehicleStates { state operating; }
    part def Vehicle {
       exhibit state opState
          references VehicleStates::operating;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Exhibit State", lines, "Part exhibiting a state.", theme, full_code=code_3, sheet_name="StatePatterns", wrapper_type="structure")
    md_blocks.append(("header", "3. Exhibit State"))
    md_blocks.append(("text", "Part exhibiting a state."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Internal Transition ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Monitoring", theme.c_type), (" {", theme.c_normal)],
        [("   transition", theme.c_keyword), (" selfCheck", theme.c_normal)],
        [("      accept", theme.c_keyword), (" tick", theme.c_normal)],
        [("      do", theme.c_keyword), (" action", theme.c_keyword), (" check", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package StatePatterns_4InternalTransition {
    private import ScalarValues::*;
    private import SysML::*;
    action def tick;
    action check;
    state def Monitoring {
       state Idle;
       // Internal behavior (Self-transition)
       transition t1 first Idle accept tick do check then Idle;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Internal Transition", lines, "Transition without state change.", theme, full_code=code_4, sheet_name="StatePatterns", wrapper_type="structure")
    md_blocks.append(("header", "4. Internal Transition"))
    md_blocks.append(("text", "Transition without state change."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("state_patterns_sheet.md", "State Patterns Cheat Sheet", "Advanced State Patterns", md_blocks, subfolder="cheatsheets")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "state_patterns.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
