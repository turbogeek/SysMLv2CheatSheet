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
    title_text = "Howdy Kitty SysMLv2 Cheat Sheet" if theme_key == "howdy_kitty" else "SysML v2 Cheat Sheet: STATES"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: State Definition ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" TrafficLight", theme.c_type), (" {", theme.c_normal)],
        [("   entry", theme.c_keyword), (" perform", theme.c_keyword), (" logStart", theme.c_normal), (";", theme.c_normal)],
        [("   exit", theme.c_keyword), (" perform", theme.c_keyword), (" logEnd", theme.c_normal), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Red", theme.c_type), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Green", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    md_blocks = []
    
    code_1 = """package States_1StateDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    action def logStart;
    action def logEnd;
    state   def  TrafficLight  {
       entry  action : logStart ;
       exit   action : logEnd ;
       state  Red ;
       state  Green ;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. State Definition", lines, "Defining states and lifecycle actions.", theme, full_code=code_1, sheet_name="States", wrapper_type="structure")
    md_blocks.append(("header", "1. State Definition"))
    md_blocks.append(("text", "Defining states and lifecycle actions."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Transitions ---
    lines = [
        [("transition", theme.c_keyword), (" t1", theme.c_normal)],
        [("   first", theme.c_keyword), (" Red", theme.c_type)],
        [("   accept", theme.c_keyword), (" TimeEvent", theme.c_type)],
        [("   then", theme.c_keyword), (" Green", theme.c_type), (";", theme.c_normal)]
    ]
    code_2 = """package States_2Transitions {
    private import ScalarValues::*;
    private import SysML::*;
    state def Main {
        state Red;
        state Green;
        action def TimeEvent;
        transition t1
           first Red
           accept TimeEvent
           then Green;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Transitions", lines, "Moving between states.", theme, full_code=code_2, sheet_name="States", wrapper_type="state")
    md_blocks.append(("header", "2. Transitions"))
    md_blocks.append(("text", "Moving between states."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Guards & Effects ---
    lines = [
        [("transition", theme.c_keyword), (" t2", theme.c_normal)],
        [("   first", theme.c_keyword), (" Green", theme.c_type)],
        [("   if", theme.c_keyword), (" traffic == 0", theme.c_normal)],
        [("   do", theme.c_keyword), (" action", theme.c_keyword), (" resetTimer", theme.c_normal)],
        [("   then", theme.c_keyword), (" Red", theme.c_type), (";", theme.c_normal)]
    ]
    code_3 = """package States_3GuardsEffects {
    private import ScalarValues::*;
    private import SysML::*;
    state def Main {
        state Green;
        state Red;
        attribute traffic : Integer;
        action resetTimer;
        transition t2
           first Green
           if traffic == 0
           do resetTimer
           then Red;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Guards & Effects", lines, "Conditions and actions on transition.", theme, full_code=code_3, sheet_name="States", wrapper_type="state")
    md_blocks.append(("header", "3. Guards & Effects"))
    md_blocks.append(("text", "Conditions and actions on transition."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Composite States ---
    lines = [
        [("state", theme.c_keyword), (" Operational", theme.c_type), (" {", theme.c_normal)],
        [("   entry", theme.c_keyword), (" /* ... */", theme.c_normal)],
        [("   state", theme.c_keyword), (" Normal", theme.c_type), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Maintenance", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package States_4CompositeStates {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    state Operational {
       entry;
       state Normal;
       state Maintenance;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Composite States", lines, "States within states.", theme, full_code=code_4, sheet_name="States", wrapper_type="structure")
    md_blocks.append(("header", "4. Composite States"))
    md_blocks.append(("text", "States within states."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Parallel States ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" System", theme.c_type), (" ", theme.c_normal), ("parallel", theme.c_keyword), (" {", theme.c_normal)],
        [("   state", theme.c_keyword), (" Power", theme.c_type), (" {", theme.c_normal), ("/* ... */", theme.c_comment), ("}", theme.c_normal)],
        [("   state", theme.c_keyword), (" Connectivity", theme.c_type), (" {", theme.c_normal), ("/* ... */", theme.c_comment), ("}", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_5 = """package States_5ParallelStates {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    state def System parallel {
       state Power;
       state Connectivity;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Parallel States", lines, "Concurrency.", theme, full_code=code_5, sheet_name="States", wrapper_type="structure")
    md_blocks.append(("header", "5. Parallel States"))
    md_blocks.append(("text", "Concurrency."))
    md_blocks.append(("code", code_5))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("states_sheet.md", "States Cheat Sheet", "State Machines", md_blocks, subfolder="cheatsheets")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "states.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
