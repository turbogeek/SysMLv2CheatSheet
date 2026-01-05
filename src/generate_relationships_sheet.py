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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: RELATIONSHIPS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Taxonomy (Def vs Usage) ---
    lines = [
        [("part", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Vehicle", theme.c_type), (" {", theme.c_normal)],
        [("   doc", theme.c_keyword), (" /* Definitions use :> */", theme.c_comment)],
        [("}", theme.c_normal)],
        [("part", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Car", theme.c_type), (" :>", theme.c_keyword), (" Vehicle", theme.c_type), (" {", theme.c_normal)],
        [("   part", theme.c_keyword), (" wheel", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)],
        [("part", theme.c_keyword), (" sedan", theme.c_normal), (" :", theme.c_normal), (" Car", theme.c_type), (" {", theme.c_normal)],
        [("   doc", theme.c_keyword), (" /* Usages use :>> */", theme.c_comment)],
        [("   part", theme.c_keyword), (" betterWheel", theme.c_normal), (" :>>", theme.c_keyword), (" wheel", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    md_blocks = []
    
    code_1 = """package 'Example: Taxonomy (Def vs Usage)' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Taxonomy (Def vs Usage)' {
        part def Vehicle {
            doc /* Definitions use specialize */
        }
        part def Car :> Vehicle {
            part wheel;
        }
        part sedan : Car {
            doc /* Usages use redefines/subsets */
            part betterWheel :>> wheel;
        }
    }
    view 'View: 1. Taxonomy (Def vs Usage)' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Taxonomy (Def vs Usage)'::'Taxonomy (Def vs Usage)'::*;
    }
}"""
    
    # Image Path
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "..", "Example _SVGs _from _Cameo", "View_ 1. Taxonomy (Def vs Usage).svg")
    
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Taxonomy (Def vs Usage)", lines, "Specialization matches Definitions.", theme, sheet_name='Relationships', wrapper_type='structure', full_code=code_1, image_path=img_path)
    md_blocks.append(("header", "1. Taxonomy (Def vs Usage)"))
    md_blocks.append(("text", "Specialization matches Definitions."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Structural Links ---
    lines = [
        [("part", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" 'Connection Examples'", theme.c_string), (" {", theme.c_normal)],
        [("   part", theme.c_keyword), (" p1", theme.c_normal), ("; ", theme.c_normal), ("part", theme.c_keyword), (" p2", theme.c_normal), (";", theme.c_normal)],
        [("   connect", theme.c_keyword), (" p1", theme.c_normal), (" to", theme.c_keyword), (" p2", theme.c_normal), (";", theme.c_normal)],
        [("   bind", theme.c_keyword), (" p1", theme.c_normal), (" =", theme.c_normal), (" p2", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_2 = """package 'Example: Structural Links' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Structural Links' {
        part def 'Connection Examples' {
            part p1;
            part p2;
            connect p1 to p2;
            bind p1 = p2;
        }
    }
    view 'View: 2. Structural Links' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Structural Links'::'Structural Links'::*;
    }
}"""
    
    img_path_2 = os.path.join(base_dir, "..", "Example _SVGs _from _Cameo", "View_ 2. Structural Links.svg")
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Structural Links", lines, "Connecting and Binding usages.", theme, sheet_name='Relationships', wrapper_type='structure', full_code=code_2, image_path=img_path_2)
    md_blocks.append(("header", "2. Structural Links"))
    md_blocks.append(("text", "Connecting and Binding usages."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Behavioral Flow ---
    lines = [
        [("action", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" Process", theme.c_type), (" {", theme.c_normal)],
        [("   action", theme.c_keyword), (" step1", theme.c_normal), ("; ", theme.c_normal), ("action", theme.c_keyword), (" step2", theme.c_normal), (";", theme.c_normal)],
        [("   first", theme.c_keyword), (" step1", theme.c_normal), (" then", theme.c_keyword), (" step2", theme.c_normal), (";", theme.c_normal)],
        [("   flow", theme.c_keyword), (" x", theme.c_normal), (" from", theme.c_keyword), (" step1", theme.c_normal), (" to", theme.c_keyword), (" step2", theme.c_normal), (";", theme.c_normal)],
        [("   action", theme.c_keyword), (" __unnamed84", theme.c_normal), (" terminate", theme.c_keyword), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_3 = """package 'Example: Behavioral Flow' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Behavioral Flow' {
        action def Process {
            action step1;
            action step2;
            first step1 then step2;
            attribute x : Integer;
            flow x from step1 to step2;
            view Process : DS_Views::SymbolicViews::afv;
            action __unnamed84 terminate;
            first start then step1;
            first step2 then __unnamed84;
        }
    }
    view 'View: 3. Behavioral Flow' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Behavioral Flow'::'Behavioral Flow'::**;
    }
}"""
    img_path_3 = os.path.join(base_dir, "..", "Example _SVGs _from _Cameo", "View_ 3. Behavioral Flow.svg")
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Behavioral Flow", lines, "Successions (Time) vs Flows (Data).", theme, sheet_name='Relationships', wrapper_type='structure', full_code=code_3, image_path=img_path_3)
    md_blocks.append(("header", "3. Behavioral Flow"))
    md_blocks.append(("text", "Successions (Time) vs Flows (Data)."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Cross-Cutting ---
    lines = [
        [("requirement", theme.c_keyword), (" R1", theme.c_normal), (";", theme.c_normal)],
        [("part", theme.c_keyword), (" p", theme.c_normal), (" satisfy", theme.c_keyword), (" R1", theme.c_normal), (";", theme.c_normal)],
        [],
        [("part", theme.c_keyword), (" abstract", theme.c_normal), (";", theme.c_normal)],
        [("part", theme.c_keyword), (" concrete", theme.c_normal), (" refine", theme.c_keyword), (" abstract", theme.c_normal), (";", theme.c_normal)],
        [],
        [("verification", theme.c_keyword), (" v1", theme.c_normal), (" :", theme.c_normal), (" Test", theme.c_type), (" {", theme.c_normal)],
        [("   subject", theme.c_keyword), (" p", theme.c_normal), (";", theme.c_normal)],
        [("   objective", theme.c_keyword), (" {", theme.c_normal), (" verify", theme.c_keyword), (" r1", theme.c_normal), (";", theme.c_normal), (" }", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package 'Example: Cross-Cutting' {
    private import ScalarValues::*;
    private import SysML::*;
    package 'Cross-Cutting' {
        requirement r1;
        part p satisfy r1;
        
        part abstractPart;
        part concretePart;
        
        refine abstractPart to concretePart;
        
        verification def Test;
        verification v1 : Test {
            subject p;
            objective {
                verify r1;
            }
        }
    }
    view 'View: 4. Cross-Cutting' {
        expose 'Example: Cross-Cutting'::'Cross-Cutting'::*;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Cross-Cutting", lines, "Traceability and Assertions.", theme, sheet_name='Relationships', wrapper_type='structure', full_code=code_4)
    md_blocks.append(("header", "4. Cross-Cutting"))
    md_blocks.append(("text", "Traceability and Assertions."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP
    
    # --- Card 5: Import & Exposure ---
    lines = [
        [("package", theme.c_keyword), (" P1", theme.c_normal), (" {", theme.c_normal)],
        [("   part", theme.c_keyword), (" def", theme.c_keyword), (" A", theme.c_normal), ("; ", theme.c_normal), ("part", theme.c_keyword), (" def", theme.c_keyword), (" B", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal), (" package", theme.c_keyword), (" P2", theme.c_normal), (" {", theme.c_normal)],
        [("   private", theme.c_keyword), (" import", theme.c_keyword), (" P1::A", theme.c_normal), (";", theme.c_normal)],
        [("   public", theme.c_keyword), (" import", theme.c_keyword), (" P1::B", theme.c_normal), (";", theme.c_normal)],
        [("   alias", theme.c_keyword), (" MyA", theme.c_normal), (" for", theme.c_keyword), (" A", theme.c_normal), (";", theme.c_normal)],
        [("   part", theme.c_keyword), (" thing", theme.c_normal), (" :", theme.c_normal), (" A", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_5 = """package 'Example: Import & Exposure' {
    private import ScalarValues::*;
    private import SysML::*;
    package P1 {
        part def A;
        part def B;
    }
    package P2 {
        private import P1::A;
        public import P1::B;
        alias MyA for A;
        part thing : A;
        part otherThing : B;
    }
    view 'View: 5. Import & Exposure' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        expose 'Example: Import & Exposure'::**;
    }
}"""
    img_path_5 = os.path.join(base_dir, "..", "Example _SVGs _from _Cameo", "Example__Import_&_Exposure__View__5._Import_&_Exposure.svg")
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "5. Import & Exposure", lines, "Managing namespace visibility.", theme, sheet_name='Relationships', wrapper_type='structure', full_code=code_5, image_path=img_path_5)
    md_blocks.append(("header", "5. Import & Exposure"))
    md_blocks.append(("text", "Managing namespace visibility."))
    md_blocks.append(("code", code_5))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("relationships_sheet.md", "Relationships Cheat Sheet", "Structural and Behavioral Relationships", md_blocks, subfolder="cheatsheets")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "relationships.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
