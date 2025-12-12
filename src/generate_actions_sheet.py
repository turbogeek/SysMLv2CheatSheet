import html
import os
from themes import THEMES
import utils

# --- Configuration ---
WIDTH = 1200
HEIGHT = 1600
MARGIN = 30 # Condensed from 50
COL_GAP = 20 # Condensed from 40
ROW_GAP = 20 # Condensed from 40
COL_WIDTH = (WIDTH - (2 * MARGIN) - COL_GAP) / 2

# --- Content ---
def generate_for_theme(theme_key, theme):
    svg = utils.svg_start(WIDTH, HEIGHT, theme)
    
    # Header
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: ACTIONS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: PickleBot Moves ({theme.name})", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Action Def ---
    lines = [
        [("action", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Serve", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" speed", theme.c_normal), (" :", theme.c_normal), (" Speed", theme.c_type), (";", theme.c_normal)],
        [("   out", theme.c_keyword), (" result", theme.c_normal), (" :", theme.c_normal), (" Result", theme.c_type), (";", theme.c_normal)],
        [("   first", theme.c_keyword), (" toss", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" strike", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_1 = """package Actions_1ActionDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Speed;
    attribute def Result;
    action def Serve {
       in speed : Speed;
       out result : Result;
       first toss;
       then strike;
       action toss;
       action strike;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Action Definition", lines, "Reusable behavior spec.", theme, full_code=code_1, sheet_name="Actions", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Action Usage ---
    lines = [
        [("action", theme.c_keyword), (" playPoint", theme.c_normal), (" {", theme.c_normal)],
        [("   action", theme.c_keyword), (" serve", theme.c_normal), (" :", theme.c_normal), (" Serve", theme.c_type), (";", theme.c_normal)],
        [("   perform", theme.c_keyword), (" serve", theme.c_normal), (" {", theme.c_normal), (" /* ... */", theme.c_comment), (" }", theme.c_normal)],
        [("   action", theme.c_keyword), (" serve2", theme.c_normal), (" :", theme.c_normal), (" Serve", theme.c_type), (";", theme.c_normal)],
        [("   perform", theme.c_keyword), (" action", theme.c_keyword), (" serve2", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]

    code_2 = """package Actions_2ActionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    action def Serve;
    action def Main {
        action playPoint {
           action serve : Serve;
           perform serve { /* ... */ }
           action serve2 : Serve;
           perform serve2;
        }
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Action Usage", lines, "Executing an action.", theme, full_code=code_2, sheet_name='Actions', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 4: Parameters ---
    lines = [
        [("action", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" ComputeValues", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" x", theme.c_normal), (" :", theme.c_normal), (" Real", theme.c_type), (";", theme.c_normal)],
        [("   inout", theme.c_keyword), (" y", theme.c_normal), (" :", theme.c_normal), (" Real", theme.c_type), (";", theme.c_normal)],
        [("   return", theme.c_keyword), (" z", theme.c_normal), (" :", theme.c_normal), (" Real", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package Actions_4Parameters {
    private import ScalarValues::*;
    private import SysML::*;
    action def ComputeValues {
       in x : Real;
       inout y : Real;
       out z : Real;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Parameters", lines, "Input, Output, Return.", theme, full_code=code_4, sheet_name='Actions', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 5: Send/Accept Signal ---
    lines = [
        [("action", theme.c_keyword), (" communicate", theme.c_normal), (" {", theme.c_normal)],
        [("   attribute", theme.c_keyword), (" sig", theme.c_normal), (" :", theme.c_normal), (" Signal::Stop", theme.c_type), (";", theme.c_normal)],
        [("   send", theme.c_keyword), (" sig", theme.c_normal), (" via", theme.c_keyword), (" pOut", theme.c_normal), (" to", theme.c_keyword), (" ctl", theme.c_normal), (";", theme.c_normal)],
        [("   accept", theme.c_keyword), (" Signal::Resume", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_5 = """package Actions_5SendAcceptSignal {
    private import ScalarValues::*;
    private import SysML::*;
    package Signal { action def Stop; action def Resume; }
    action def Main {
        part pOut;
        part ctl;
        action communicate {
           attribute sig : Signal::Stop;
           send sig via pOut to ctl;
           accept Signal::Resume;
        }
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Send/Accept Signal", lines, "Async communication.", theme, full_code=code_5, sheet_name='Actions', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Succession Flow ---
    lines = [
        [("first", theme.c_keyword), (" start", theme.c_normal), (";", theme.c_normal)],
        [("then", theme.c_keyword), (" process", theme.c_normal), (";", theme.c_normal)],
        [("then", theme.c_keyword), (" finish", theme.c_normal), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Control flow sequence */", theme.c_comment)]
    ]
    code_6 = """package Actions_6Successionfirstthen {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        action start;
        action process;
        action finish;
        first start;
        then process;
        then finish;
        doc /* Control flow sequence */
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Succession (first/then)", lines, "Ordering of actions.", theme, full_code=code_6, sheet_name='Actions', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 7: Assignment ---
    lines = [
        [("assign", theme.c_keyword), (" x", theme.c_normal), (" :=", theme.c_normal), (" 42", theme.c_string), (";", theme.c_normal)],
        [("assign", theme.c_keyword), (" y", theme.c_normal), (" :=", theme.c_normal), (" x + 1", theme.c_normal), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Value assignment */", theme.c_comment)]
    ]
    code_7 = """package Actions_7Assignmentassign {
    private import ScalarValues::*;
    action def Main {
        attribute x : Integer;
        attribute y : Integer;
        assign x := 42;
        assign y := x + 1;
        doc /* Value assignment */
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "7. Assignment (assign)", lines, "Setting values.", theme, full_code=code_7, sheet_name='Actions', wrapper_type='action')
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 8: Trigger ---
    lines = [
        [("accept", theme.c_keyword), (" tick", theme.c_normal), (" :", theme.c_normal), (" Tick", theme.c_type), (" via", theme.c_keyword), (" clock", theme.c_normal), (";", theme.c_normal)],
        [("accept", theme.c_keyword), (" when", theme.c_keyword), (" t > 10.0", theme.c_normal), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Event trigger with guard */", theme.c_comment)]
    ]
    code_8 = """package Actions_8Trigger {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        action def Tick;
        part clock;
        attribute t : Real;
        accept tick : Tick via clock;
        accept when t > 10.0;
        doc /* Event trigger with guard */
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "8. Trigger", lines, "Reacting to events.", theme, full_code=code_8, sheet_name='Actions', wrapper_type='action')
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "actions.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
