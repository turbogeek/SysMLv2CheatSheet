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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: ACTION PATTERNS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: While Loop ---
    lines = [
        [("while", theme.c_keyword), (" x < 10", theme.c_normal), (" {", theme.c_normal)],
        [("   assign", theme.c_keyword), (" x", theme.c_normal), (" :=", theme.c_normal), (" x + 1", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_1 = """package WhileLoopExample {
    private import ScalarValues::*;
    action def Main {
        attribute x : Integer = 0;
        action loopAction {
            while x < 10 {
                assign x := x + 1;
            }
        }
    }
    view LoopView {
        expose Main;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. While Loop", lines, "Iterate while condition is true.", theme, full_code=code_1, sheet_name="ActionPatterns", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: For Loop ---
    lines = [
        [("for", theme.c_keyword), (" i", theme.c_normal), (" in", theme.c_keyword), (" 1..10", theme.c_string), (" {", theme.c_normal)],
        [("   do", theme.c_keyword), (" action", theme.c_keyword), (" process(i)", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_2 = """package ForLoopExample {
    private import ScalarValues::*;
    action def Main {
        action process { in i : Integer; }
        action loopAction {
            for i in 1..10 {
                perform process { in i = i; }
            }
        }
    }
    view LoopView {
        expose Main;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. For Loop", lines, "Iterate over a range.", theme, full_code=code_2, sheet_name="ActionPatterns", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2b: Loop Actions (Collection & Infinite) ---
    lines = [
        [("for", theme.c_keyword), (" p", theme.c_normal), (" :", theme.c_normal), (" Power", theme.c_type), (" in", theme.c_keyword), (" profile", theme.c_normal), (" {", theme.c_normal)],
        [("   assign", theme.c_keyword), (" ...", theme.c_comment)],
        [("}", theme.c_normal)],
        [("while", theme.c_keyword), (" x < 10", theme.c_normal), (" {", theme.c_normal), (" ...", theme.c_comment), (" }", theme.c_normal), (" until", theme.c_keyword), (" done", theme.c_normal), (";", theme.c_normal)],
        [("loop", theme.c_keyword), (" {", theme.c_normal), (" ...", theme.c_comment), (" }", theme.c_normal), (" until", theme.c_keyword), (" x > 100", theme.c_normal), (";", theme.c_normal)]
    ]
    code_2b = """package LoopVariationsExample {
    private import ScalarValues::*;
    attribute def Power;
    attribute profile : Power[*];
    action def Main {
        attribute x : Integer = 0;
        attribute done : Boolean = false;
        
        action collectionLoop {
            for p : Power in profile {
                // body
            }
        }
        
        action whileUntilLoop {
            while x < 10 {
                assign x := x + 1;
            } until done;
        }
        
        action infiniteLoop {
            loop {
               assign x := x + 1;
            } until x > 100;
        }
    }
    view LoopView {
        expose Main;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2b. Loop Variations", lines, "Collections, Until, & Infinite Loops.", theme, full_code=code_2b, sheet_name="ActionPatterns", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: If / Else ---
    lines = [
        [("if", theme.c_keyword), (" x > 0", theme.c_normal), (" {", theme.c_normal)],
        [("   assign", theme.c_keyword), (" y", theme.c_normal), (" :=", theme.c_normal), (" 1", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal), (" else", theme.c_keyword), (" {", theme.c_normal)],
        [("   assign", theme.c_keyword), (" y", theme.c_normal), (" :=", theme.c_normal), (" 0", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_3 = """package ActionPatterns_3IfElse {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute x : Integer = 0;
        attribute y : Integer;
        if x > 0 {
           assign y := 1;
        } else {
           assign y := 0;
        }
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. If / Else", lines, "Conditional execution.", theme, full_code=code_3, sheet_name="ActionPatterns", wrapper_type="action")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Accept Variations ---
    lines = [
        [("accept", theme.c_keyword), (" startSignal", theme.c_normal), (" :", theme.c_normal), (" StartSignal", theme.c_type), (";", theme.c_normal)],
        [("comment", theme.c_keyword), (" about", theme.c_normal), (" startSignal", theme.c_normal), (" /* ... */", theme.c_comment)],
        [("accept", theme.c_keyword), (" when", theme.c_keyword), (" temp > 100", theme.c_normal), (";", theme.c_normal)],
        [("accept", theme.c_keyword), (" at", theme.c_keyword), (" schedule", theme.c_normal), (";", theme.c_normal)],
        [("accept", theme.c_keyword), (" after", theme.c_keyword), (" 10 [s]", theme.c_string), (";", theme.c_normal)]
    ]
    code_4 = """package ActionPatterns_4AcceptVariations {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute temp : Real;
        attribute s : Real;
        part schedule;
        action def StartSignal;
        action acceptSomething {
            accept startSignal : StartSignal;
            doc /* about startSignal ... */
            accept when temp > 100;
            accept at schedule;
            accept after 10 [s];
        }
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Accept Variations", lines, "Waiting for events/conditions.", theme, full_code=code_4, sheet_name="ActionPatterns", wrapper_type="action")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Send Variations ---
    lines = [
        [("action", theme.c_keyword), (" sendA", theme.c_normal), (" send", theme.c_keyword), (" startSignal", theme.c_normal), (" via", theme.c_keyword), (" p1", theme.c_normal), (";", theme.c_normal)],
        [("send", theme.c_keyword), (" startSignal", theme.c_normal), (" via", theme.c_keyword), (" p1", theme.c_normal), (";", theme.c_normal)],
        [("doc", theme.c_keyword), (" /* Named vs Unnamed */", theme.c_comment)]
    ]
    code_5 = """package ActionPatterns_5SendVariations {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        action def StartSignal;
        part p1;
        attribute sig : StartSignal;
        action sendA { send sig via p1; }
        send sig via p1;
        doc /* Named vs Unnamed */
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Send Variations", lines, "Named and unnamed sends.", theme, full_code=code_5, sheet_name="ActionPatterns", wrapper_type="action")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Control Nodes ---
    lines = [
        [("fork", theme.c_keyword), (" f1", theme.c_normal), (";", theme.c_normal)],
        [("join", theme.c_keyword), (" j1", theme.c_normal), (";", theme.c_normal)],
        [("decide", theme.c_keyword), (" d1", theme.c_normal), (";", theme.c_normal)],
        [("merge", theme.c_keyword), (" m1", theme.c_normal), (";", theme.c_normal)]
    ]
    code_6 = """package ActionPatterns_6ControlNodes {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        fork  f1 ;
        join  j1 ;
        decide  d1 ;
        merge  m1 ;
    }

    view ExposeExample {
        expose Main;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "6. Control Nodes", lines, "Flow control points.", theme, full_code=code_6, sheet_name="ActionPatterns", wrapper_type="action")
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 7: Advanced Send ---
    lines = [
        [("action", theme.c_keyword), (" sendReading", theme.c_normal), (" send", theme.c_keyword), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" payload", theme.c_normal), (";", theme.c_normal)],
        [("   in", theme.c_keyword), (" sender", theme.c_normal), (" =", theme.c_normal), (" monitor", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("flow", theme.c_keyword), (" val", theme.c_normal), (" to", theme.c_keyword), (" sendReading.payload", theme.c_normal), (";", theme.c_normal)]
    ]
    code_7 = """package ActionPatterns_7AdvancedSend {
    private import ScalarValues::*;
    private import ScalarValues::*;
    private import SysML::*;
    private import Base::*;
    action def Main {
        attribute val : Anything;
        part monitor;
        action sendReading send {
           in payload;
           in sender = monitor;
        }
        flow val to sendReading.payload;
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "7. Advanced Send", lines, "Binding params & flows.", theme, full_code=code_7, sheet_name="ActionPatterns", wrapper_type="action")
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "action_patterns.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
