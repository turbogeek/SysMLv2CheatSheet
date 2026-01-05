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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: CONSTRAINTS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Constraint Definition ---
    lines = [
        [("constraint", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" NewtonLaw", theme.c_type), (" {", theme.c_normal)],
        [("  in", theme.c_keyword), (" f", theme.c_normal), (" :", theme.c_normal), (" Force", theme.c_type), (";", theme.c_normal)],
        [("  in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  in", theme.c_keyword), (" a", theme.c_normal), (" :", theme.c_normal), (" Acceleration", theme.c_type), (";", theme.c_normal)],
        [("  ", theme.c_normal), ("f", theme.c_normal), (" =", theme.c_normal), (" m * a", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    md_blocks = []
    
    code_1 = """package Constraints_1ConstraintDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Force;
    attribute def Mass;
    attribute def Acceleration;
    constraint def NewtonLaw {
      in f : Force;
      in m : Mass;
      in a : Acceleration;
      f = m * a;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Constraint Definition", lines, "Defining mathematical relationships.", theme, full_code=code_1, sheet_name="Constraints", wrapper_type="structure")
    md_blocks.append(("header", "1. Constraint Definition"))
    md_blocks.append(("text", "Defining mathematical relationships."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Constraint Usage (Assert) ---
    lines = [
        [("part", theme.c_keyword), (" Car", theme.c_type), (" {", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" mass", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" accel", theme.c_normal), (" :", theme.c_normal), (" Acceleration", theme.c_type), (";", theme.c_normal)],
        [("  attribute", theme.c_keyword), (" force", theme.c_normal), (" :", theme.c_normal), (" Force", theme.c_type), (";", theme.c_normal)],
        [("  assert", theme.c_keyword), (" constraint", theme.c_keyword), (" n1", theme.c_normal), (" :", theme.c_normal), (" NewtonLaw", theme.c_type), (" {", theme.c_normal)],
        [("    in", theme.c_keyword), (" f", theme.c_normal), (" =", theme.c_normal), (" force", theme.c_normal), (";", theme.c_normal)],
        [("    in", theme.c_keyword), (" m", theme.c_normal), (" =", theme.c_normal), (" mass", theme.c_normal), (";", theme.c_normal)],
        [("    in", theme.c_keyword), (" a", theme.c_normal), (" =", theme.c_normal), (" accel", theme.c_normal), (";", theme.c_normal)],
        [("  }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_2 = """package Constraints_2ConstraintUsageAssert {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute def Acceleration;
    attribute def Force;
    constraint def NewtonLaw { in f : Force; in m : Mass; in a : Acceleration; }
    part Car {
      attribute mass : Mass;
      attribute accel : Acceleration;
      attribute force : Force;
      assert constraint n1 : NewtonLaw {
        in f = force;
        in m = mass;
        in a = accel;
      }
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Constraint Usage (Assert)", lines, "Enforcing constraints on parts.", theme, full_code=code_2, sheet_name="Constraints", wrapper_type="structure")
    md_blocks.append(("header", "2. Constraint Usage (Assert)"))
    md_blocks.append(("text", "Enforcing constraints on parts."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2b: Inline Assertion ---
    lines = [
        [("assert", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal)],
        [("  x > 0", theme.c_normal)],
        [("}", theme.c_normal)],
        [("/* Boolean expression */", theme.c_comment)]
    ]
    code_2b = """package Constraints_2bInlineAssertion {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute x : Integer;
        assert constraint {
           x > 0
        }
        /* Boolean expression */
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2b. Inline Assertion", lines, "Simple boolean check.", theme, full_code=code_2b, sheet_name="Constraints", wrapper_type="action")
    md_blocks.append(("header", "2b. Inline Assertion"))
    md_blocks.append(("text", "Simple boolean check."))
    md_blocks.append(("code", code_2b))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 3: Calculation Definition ---
    lines = [
        [("calc", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" calcKineticEnergy", theme.c_type), (" {", theme.c_normal)],
        [("  in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  in", theme.c_keyword), (" v", theme.c_normal), (" :", theme.c_normal), (" Speed", theme.c_type), (";", theme.c_normal)],
        [("  return", theme.c_keyword), (" ke", theme.c_normal), (" :", theme.c_normal), (" Energy", theme.c_type), (";", theme.c_normal)],
        [("  ", theme.c_normal), ("0.5 * m * v^2", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_3 = """package Constraints_3CalculationDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute def Speed;
    attribute def Energy;
    calc def calcKineticEnergy {
      in m : Mass;
      in v : Speed;
      return ke : Energy = 0.5 * m * v^2;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Calculation Definition", lines, "Reusable computation logic.", theme, full_code=code_3, sheet_name="Constraints", wrapper_type="structure")
    md_blocks.append(("header", "3. Calculation Definition"))
    md_blocks.append(("text", "Reusable computation logic."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 4: Calculation Usage ---
    lines = [
        [("attribute", theme.c_keyword), (" kEnergy", theme.c_normal), (" =", theme.c_normal), (" calcKineticEnergy", theme.c_type), ("(", theme.c_normal)],
        [("  m", theme.c_normal), (" =", theme.c_normal), (" 100[kg]", theme.c_string), (",", theme.c_normal)],
        [("  v", theme.c_normal), (" =", theme.c_normal), (" 20[m/s]", theme.c_string)],
        [(")", theme.c_normal), (";", theme.c_normal)],
        [("/* Result assigned to attribute */", theme.c_comment)]
    ]
    code_4 = """package Constraints_4CalculationUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute def Speed;
    attribute def Energy;
    attribute kg;
    attribute m;
    attribute s;
    calc def calcKineticEnergy { in m : Mass; in v : Speed; return ke : Energy; }
    action def Main {
        attribute kEnergy : Energy = calcKineticEnergy(m = 100 [kg], v = 20 [m/s]);
    }
    view ExposeExample { expose Main; }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Calculation Usage", lines, "Invoking calculations.", theme, full_code=code_4, sheet_name="Constraints", wrapper_type="action")
    md_blocks.append(("header", "4. Calculation Usage"))
    md_blocks.append(("text", "Invoking calculations."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 5: Objective (Optimization) ---
    lines = [
        [("objective", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" MinimizeMass", theme.c_type), (" {", theme.c_normal)],
        [("  in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  minimize", theme.c_keyword), (" m", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("constraints_sheet.md", "Constraints Cheat Sheet", "Equations and Assertions", md_blocks, subfolder="cheatsheets")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "constraints.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
