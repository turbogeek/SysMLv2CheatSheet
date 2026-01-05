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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: CONSTRAINTS & CALCS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Calculation Definition ---
    lines = [
        [("calc", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" PowerCalc", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" v", theme.c_normal), (" :", theme.c_normal), (" Voltage", theme.c_type), (";", theme.c_normal)],
        [("   in", theme.c_keyword), (" i", theme.c_normal), (" :", theme.c_normal), (" Current", theme.c_type), (";", theme.c_normal)],
        [("   return", theme.c_keyword), (" p", theme.c_normal), (" :", theme.c_normal), (" Power", theme.c_type), (" =", theme.c_normal), (" v * i", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    md_blocks = []
    
    code_1 = """package Calculations_1CalculationDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Voltage;
    attribute def Current;
    attribute def Power;
    calc def PowerCalc {
       in v : Voltage;
       in i : Current;
       return p : Power = v * i;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Calculation Definition", lines, "Reusable math expressions.", theme, full_code=code_1, sheet_name="Calculations", wrapper_type="structure")
    md_blocks.append(("header", "1. Calculation Definition"))
    md_blocks.append(("text", "Reusable math expressions."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Calculation Usage ---
    lines = [
        [("calc", theme.c_keyword), (" p_motor", theme.c_normal), (" :", theme.c_normal), (" PowerCalc", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" v", theme.c_normal), (" =", theme.c_normal), (" 12.0", theme.c_string), (";", theme.c_normal)],
        [("   in", theme.c_keyword), (" i", theme.c_normal), (" =", theme.c_normal), (" 5.0", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_2 = """package Calculations_2CalculationUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Voltage; attribute def Current; attribute def Power;
    calc def PowerCalc { in v : Voltage; in i : Current; return p : Power; }
    // Wrapped Snippet (Action Context)
    action def Main {
        calc  p_motor  :  PowerCalc  {
           in  v  =  12.0 ;
           in  i  =  5.0 ;
        }
    }

    view ExposeExample {
        expose Main;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Calculation Usage", lines, "Performing a calculation.", theme, full_code=code_2, sheet_name="Calculations", wrapper_type="action")
    md_blocks.append(("header", "2. Calculation Usage"))
    md_blocks.append(("text", "Performing a calculation."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Constraint Definition ---
    lines = [
        [("constraint", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" MassLimit", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("   in", theme.c_keyword), (" limit", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("   m <= limit", theme.c_normal), (";", theme.c_normal)],
        [("constraint", theme.c_keyword), (" checkMass", theme.c_normal), (" :", theme.c_normal), (" MassLimit", theme.c_type), (" {", theme.c_normal)],
        [("   in", theme.c_keyword), (" m", theme.c_normal), (" =", theme.c_normal), (" self.mass", theme.c_normal), (";", theme.c_normal)],
        [("   in", theme.c_keyword), (" limit", theme.c_normal), (" =", theme.c_normal), (" 1000.0", theme.c_string), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package Calculations_4ConstraintUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    constraint def MassLimit { in m : Mass; in limit : Mass; }
    // Wrapped Snippet (Action Context)
    action def Main {
        attribute mass : Mass;
        constraint  checkMass  :  MassLimit  {
           in  m  =  mass ;
           in  limit  =  1000.0 ;
        }
    }

    view ExposeExample {
        expose Main;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Constraint Usage", lines, "Applying a constraint.", theme, full_code=code_4, sheet_name="Calculations", wrapper_type="action")
    md_blocks.append(("header", "4. Constraint Usage"))
    md_blocks.append(("text", "Applying a constraint."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 5: Assertions ---
    lines = [
        [("assert", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal)],
        [("   x > 0", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("not", theme.c_keyword), (" assert", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal)],
        [("   y < 0", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_5 = """package Calculations_5Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute x : Integer;
        attribute y : Integer;
        assert constraint {
           x > 0
        }
        assert constraint {
           not (y < 0)
        }
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Assertions", lines, "Enforcing truth.", theme, full_code=code_5, sheet_name="Calculations", wrapper_type="action")
    md_blocks.append(("header", "5. Assertions"))
    md_blocks.append(("text", "Enforcing truth."))
    md_blocks.append(("code", code_5))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Requirements ---
    lines = [
        [("requirement", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Safety", theme.c_type), (" {", theme.c_normal)],
        [("   assume", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal), (" temp < 100", theme.c_normal), (" }", theme.c_normal)],
        [("   require", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal), (" pressure < 50", theme.c_normal), (" }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_6 = """package Calculations_6Requirements {
    private import ScalarValues::*;
    private import SysML::*;
    requirement def Safety {
       attribute temp : Real;
       attribute pressure : Real;
       assume constraint { temp < 100 }
       require constraint { pressure < 50 }
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Requirements", lines, "Assumptions and requirements.", theme, full_code=code_6, sheet_name="Calculations", wrapper_type="structure")
    md_blocks.append(("header", "6. Requirements"))
    md_blocks.append(("text", "Assumptions and requirements."))
    md_blocks.append(("code", code_6))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("calc_sheet.md", "Calculation Cheat Sheet", "Calculations and Constraints", md_blocks, subfolder="cheatsheets")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "calc.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
