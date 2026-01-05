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
    title_text = "Howdy Kitty SysMLv2 Cheat Sheet" if theme_key == "howdy_kitty" else "SysML v2 Cheat Sheet: BEHAVIOR"
    svg += utils.text(WIDTH/2, 60, title_text, 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: State Definition ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" PracticeSession", theme.c_type), (" {", theme.c_normal)],
        [("   entry", theme.c_keyword), (";", theme.c_normal), (" exit", theme.c_keyword), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Idle", theme.c_type), (";", theme.c_normal)],
        [("   state", theme.c_keyword), (" Serving", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    md_blocks = []
    
    code_1 = """package Behavior_1StateDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    state   def  PracticeSession  {
       entry ;  exit ;
       state  Idle ;
       state  Serving ;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. State Definition", lines, "States and lifecycle actions.", theme, full_code=code_1, sheet_name="Behavior", wrapper_type="structure")
    md_blocks.append(("header", "1. State Definition"))
    md_blocks.append(("text", "States and lifecycle actions."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Transitions ---
    lines = [
        [("transition", theme.c_keyword), (" startServe", theme.c_normal)],
        [("   first", theme.c_keyword), (" Idle", theme.c_type)],
        [("   accept", theme.c_keyword), (" Remote.Start", theme.c_normal)],
        [("   do", theme.c_keyword), (" action", theme.c_keyword), (" log", theme.c_normal), (" :", theme.c_normal), (" Log", theme.c_type), ("(", theme.c_normal), ("'Serving'", theme.c_string), (");", theme.c_normal)],
        [("   then", theme.c_keyword), (" Serving", theme.c_type), (";", theme.c_normal)]
    ]

    code_2 = """package Behavior_2Transitions {
    private import ScalarValues::*;
    private import SysML::*;
    state def Main {
        state Idle;
        state Serving;
        action def Log { in msg : String; }
        action def Start;
        part Remote { action start : Start; }
        transition startServe
           first Idle
           accept Remote.start
           do action log : Log { in msg = 'Serving'; }
           then Serving;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Transitions", lines, "Move between states on triggers.", theme, full_code=code_2, sheet_name="Behavior", wrapper_type="state")
    md_blocks.append(("header", "2. Transitions"))
    md_blocks.append(("text", "Move between states on triggers."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Guards & Effects ---
    lines = [
        [("transition", theme.c_keyword), (" t2", theme.c_normal), (" {", theme.c_normal)],
        [("   first", theme.c_keyword), (" Green", theme.c_type)],
        [("   if", theme.c_keyword), (" traffic == 0", theme.c_normal)],
        [("   do", theme.c_keyword), (" action", theme.c_keyword), (" resetTimer", theme.c_normal)],
        [("   then", theme.c_keyword), (" Red", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_3 = """package Behavior_3GuardsEffects {
    private import ScalarValues::*;
    private import SysML::*;
    state def Main {
        state Green;
        state Red;
        attribute traffic : Integer;
        action resetTimer;
        transition t2 first Green if traffic == 0 do resetTimer then Red;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Guards & Effects", lines, "Conditions and actions on transition.", theme, full_code=code_3, sheet_name="Behavior", wrapper_type="state")
    md_blocks.append(("header", "3. Guards & Effects"))
    md_blocks.append(("text", "Conditions and actions on transition."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3b: Internal Transition ---
    lines = [
        [("state", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Monitoring", theme.c_type), (" {", theme.c_normal)],
        [("   state", theme.c_keyword), (" selfCheck", theme.c_normal), (";", theme.c_normal)],
        [("   transition", theme.c_keyword), (" selfCheck", theme.c_normal)],
        [("      accept", theme.c_keyword), (" tick", theme.c_normal)],
        [("      do", theme.c_keyword), (" action", theme.c_keyword), (" check", theme.c_normal), (" then", theme.c_keyword), (" selfCheck", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_3b = """package Behavior_3bInternalTransition {
    private import ScalarValues::*;
    private import SysML::*;
    state def Monitoring {
       state selfCheck;
       action def tick;
       action check;
       transition t1 first selfCheck accept tick do check then selfCheck;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3b. Internal Transition", lines, "Self-transition pattern.", theme, full_code=code_3b, sheet_name="Behavior", wrapper_type="structure")
    md_blocks.append(("header", "3b. Internal Transition"))
    md_blocks.append(("text", "Self-transition pattern."))
    md_blocks.append(("code", code_3b))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Action Definition ---
    lines = [
        [("action", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Serve", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" speed", theme.c_normal), (" :", theme.c_normal), (" Speed", theme.c_type), (";", theme.c_normal)],
        [("   out", theme.c_keyword), (" result", theme.c_normal), (" :", theme.c_normal), (" Result", theme.c_type), (";", theme.c_normal)],
        [("   first", theme.c_keyword), (" toss", theme.c_normal), (";", theme.c_normal)],
        [("   then", theme.c_keyword), (" strike", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package Behavior_4ActionDefinition {
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
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Action Definition", lines, "Reusable behavior spec.", theme, full_code=code_4, sheet_name="Behavior", wrapper_type="structure")
    md_blocks.append(("header", "4. Action Definition"))
    md_blocks.append(("text", "Reusable behavior spec."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Action Usage ---
    lines = [
        [("action", theme.c_keyword), (" playPoint", theme.c_normal), (" {", theme.c_normal)],
        [("   action", theme.c_keyword), (" serve", theme.c_normal), (" :", theme.c_normal), (" Serve", theme.c_type), (";", theme.c_normal)],
        [("   perform", theme.c_keyword), (" serve", theme.c_normal), (" {", theme.c_normal)],
        [("      in", theme.c_keyword), (" speed", theme.c_normal), (" =", theme.c_normal), (" 60", theme.c_string), (";", theme.c_normal)],
        [("   }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_5 = """package Behavior_5ActionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    action def Serve { in speed : Integer; }
    // Wrapped Snippet (Action Context)
    action def Main {
        action  playPoint  {
           action  serve  :  Serve ;
           perform  serve  {
              in  speed  =  60 ;
           }
        }
    }

    view ExposeExample {
        expose Main;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Action Usage", lines, "Executing an action.", theme, full_code=code_5, sheet_name="Behavior", wrapper_type="action")
    md_blocks.append(("header", "5. Action Usage"))
    md_blocks.append(("text", "Executing an action."))
    md_blocks.append(("code", code_5))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Use Cases ---
    lines = [
        [("use", theme.c_keyword), (" ", theme.c_normal), ("case", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Practice", theme.c_type), (" {", theme.c_normal)],
        [("   subject", theme.c_keyword), (" b", theme.c_normal), (" :", theme.c_normal), (" PickleBot", theme.c_type), (";", theme.c_normal)],
        [("   actor", theme.c_keyword), (" p", theme.c_normal), (" :", theme.c_normal), (" Player", theme.c_type), (";", theme.c_normal)],
        [("   objective", theme.c_keyword), (" {", theme.c_normal)],
        [("      doc", theme.c_keyword), (" /* Improve skills */", theme.c_comment)],
        [("   }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_6 = """package Behavior_6UseCases {
    private import ScalarValues::*;
    private import SysML::*;
    part def PickleBot;
    part def Player;
    use case def Practice {
       subject b : PickleBot;
       actor p : Player;
       objective {
          doc /* Improve skills */
       }
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Use Cases", lines, "High-level user goals.", theme, full_code=code_6, sheet_name="Behavior", wrapper_type="structure")
    md_blocks.append(("header", "6. Use Cases"))
    md_blocks.append(("text", "High-level user goals."))
    md_blocks.append(("code", code_6))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()
    
    if theme_key == 'light':
        utils.save_markdown("behavior_sheet.md", "Behavior Cheat Sheet", "State Machines and Actions", md_blocks, subfolder="cheatsheets")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "behavior.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
