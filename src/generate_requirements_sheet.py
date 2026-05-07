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
    md_blocks = []
    
    code_1 = """package Requirements_1RequirementDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Time;
    requirement def Performance {
      doc /* The system shall be fast. */
      attribute maxResponse : Time;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Requirement Definition", lines, "Defining requirement types.", theme, full_code=code_1, sheet_name="Requirements", wrapper_type="structure")
    md_blocks.append(("header", "1. Requirement Definition"))
    md_blocks.append(("text", "Defining requirement types."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Requirement Usage ---
    lines = [
        [("requirement", theme.c_keyword), (" <'REQ-001'>", theme.c_string), (" 'Fast'", theme.c_string), (" :", theme.c_normal), (" Performance", theme.c_type), (" {", theme.c_normal)],
        [("  doc", theme.c_keyword), (" /* Response < 10ms */", theme.c_comment)],
        [("  maxResponse", theme.c_normal), (" =", theme.c_normal), (" 10", theme.c_string), (" [ms]", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_2 = """package Requirements_2RequirementUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Time;
    attribute ms;
    requirement def Performance { attribute maxResponse : Time; }
    requirement <'REQ-001'> 'Fast' : Performance {
      doc /* Response < 10ms */
      attribute maxResponse = 10 [ms];
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Requirement Usage", lines, "Specific requirement instances.", theme, full_code=code_2, sheet_name="Requirements", wrapper_type="structure")
    md_blocks.append(("header", "2. Requirement Usage"))
    md_blocks.append(("text", "Specific requirement instances using `<'ID'> 'Name' : Type`."))
    md_blocks.append(("code", code_2))
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
    code_3 = """package Requirements_3Satisfy {
    private import ScalarValues::*;
    private import SysML::*;
    requirement def Performance;
    requirement req1 : Performance;
    part server {
      satisfy req1;
    }
    /* satisfy req1 by server; */
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Satisfy", lines, "Design meets requirement.", theme, full_code=code_3, sheet_name="Requirements", wrapper_type="structure")
    md_blocks.append(("header", "3. Satisfy"))
    md_blocks.append(("text", "Design meets requirement."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 4: Verify Relationship ---
    lines = [
        [("verification", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" TestLatency", theme.c_type), (" {", theme.c_normal)],
        [("  verify", theme.c_keyword), (" req1", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package Requirements_4Verify {
    private import ScalarValues::*;
    private import SysML::*;
    requirement req1;
    verification def TestLatency {
      objective {
          verify req1;
      }
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Verify", lines, "Test case for requirement.", theme, full_code=code_4, sheet_name="Requirements", wrapper_type="structure")
    md_blocks.append(("header", "4. Verify"))
    md_blocks.append(("text", "Test case for requirement."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 5: Constraint Blocks ---
    lines = [
        [("constraint", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" CheckMass", theme.c_type), (" {", theme.c_normal)],
        [("  in", theme.c_keyword), (" m", theme.c_normal), (" :", theme.c_normal), (" Mass", theme.c_type), (";", theme.c_normal)],
        [("  m <= 1000 [kg]", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_5 = """package Requirements_5ConstraintDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute kg;
    constraint def CheckMass {
      in m : Mass;
      m <= 1000 [kg]
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Constraint Definition", lines, "Mathematical rules.", theme, full_code=code_5, sheet_name="Requirements", wrapper_type="structure")
    md_blocks.append(("header", "5. Constraint Definition"))
    md_blocks.append(("text", "Mathematical rules."))
    md_blocks.append(("code", code_5))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 6: Assertions ---
    lines = [
        [("part", theme.c_keyword), (" car", theme.c_normal), (" {", theme.c_normal)],
        [("  assert", theme.c_keyword), (" constraint", theme.c_keyword), (" {", theme.c_normal)],
        [("    mass <= 1000 [kg]", theme.c_normal)],
        [("  }", theme.c_normal), (" /* CRITICAL: No semicolon */", theme.c_comment)],
        [("}", theme.c_normal)]
    ]
    code_6 = """package Requirements_6Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute kg;
    part car {
      attribute mass : Mass;
      assert constraint {
        mass <= 1000 [kg]
      }
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Assert Constraint", lines, "Applying constraints without semicolons.", theme, full_code=code_6, sheet_name="Requirements", wrapper_type="structure")
    md_blocks.append(("header", "6. Assert Constraint"))
    md_blocks.append(("text", "Applying constraints directly. **CRITICAL**: No semicolon at the end of the constraint block."))
    md_blocks.append(("code", code_6))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 7: Trace & Refine ---
    lines = [
        [("requirement", theme.c_keyword), (" req2", theme.c_normal), (" {", theme.c_normal)],
        [("  refine", theme.c_keyword), (" req1", theme.c_normal), (";", theme.c_normal)],
        [("  trace", theme.c_keyword), (" old_doc_item", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_7 = """package Requirements_7TraceRefine {
    private import ScalarValues::*;
    private import SysML::*;
    requirement req1;
    requirement old_doc_item;
    requirement req2 {
      doc /* Using dependency to represent relationships */
      dependency from req2 to req1;
      dependency from req2 to old_doc_item;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "7. Trace & Refine", lines, "Requirement relationships.", theme, full_code=code_7, sheet_name="Requirements", wrapper_type="structure")
    md_blocks.append(("header", "7. Trace & Refine"))
    md_blocks.append(("text", "Requirement relationships."))
    md_blocks.append(("code", code_7))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("requirements_sheet.md", "Requirements Cheat Sheet", "Requirements and Verification", md_blocks, subfolder="cheatsheets")
    
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
