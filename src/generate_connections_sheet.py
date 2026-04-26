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
    svg += utils.text(WIDTH/2, 60, "SysML v2 Cheat Sheet: CONNECTIONS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: PickleBot Networking ({theme.name})", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    # --- Card 1: Connection Def ---
    lines = [
        [("connection", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" DeviceConn", theme.c_type), (" {", theme.c_normal)],
        [("   end", theme.c_keyword), (" hub", theme.c_normal), (" :", theme.c_normal), (" Hub", theme.c_type), (";", theme.c_normal)],
        [("   end", theme.c_keyword), (" device", theme.c_normal), (" :", theme.c_normal), (" Device", theme.c_type), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    md_blocks = []
    
    code_1 = """package Connections_1ConnectionDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    part def Hub;
    part def Device;
    connection def DeviceConn {
       end hub : Hub;
       end device : Device;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Connection Definition", lines, "Defining connection types.", theme, full_code=code_1, sheet_name='Connections', wrapper_type='structure')
    md_blocks.append(("header", "1. Connection Definition"))
    md_blocks.append(("text", "Defining connection types."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 1b: Connection Usage ---
    lines = [
        [("part", theme.c_keyword), (" context", theme.c_normal), (" {", theme.c_normal)],
        [("   connection", theme.c_keyword), (" c1", theme.c_normal), (" :", theme.c_normal), (" DeviceConn", theme.c_type)],
        [("      connect", theme.c_keyword), (" hub", theme.c_normal), (" to", theme.c_keyword), (" device", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_1b = """package Connections_1bConnectionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    part def Hub;
    part def Device;
    connection def DeviceConn { end hub : Hub; end device : Device; }
    part context {
       part hub : Hub;
       part device : Device;
       connection c1 : DeviceConn
          connect hub to device;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1b. Connection Usage", lines, "Connecting parts.", theme, full_code=code_1b, sheet_name='Connections', wrapper_type='structure')
    md_blocks.append(("header", "1b. Connection Usage"))
    md_blocks.append(("text", "Connecting parts."))
    md_blocks.append(("code", code_1b))
    svg += card
    cur_y_c1 += h + ROW_GAP
    
    # --- Card 2: Binding Connector ---
    lines = [
        [("part", theme.c_keyword), (" system", theme.c_normal), (" {", theme.c_normal)],
        [("   part", theme.c_keyword), (" a", theme.c_normal), (" :", theme.c_normal), (" A", theme.c_type), (";", theme.c_normal)],
        [("   part", theme.c_keyword), (" b", theme.c_normal), (" :", theme.c_normal), (" B", theme.c_type), (";", theme.c_normal)],
        [("   bind", theme.c_keyword), (" a.p1", theme.c_normal), (" =", theme.c_normal), (" b.p2", theme.c_normal), (";", theme.c_normal)],
        [("   doc", theme.c_keyword), (" /* Arrays lack indices: */", theme.c_comment)],
        [("   bind", theme.c_keyword), (" a.ports", theme.c_normal), (" =", theme.c_normal), (" b.ports", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_2 = """package Connections_2BindingConnector {
    private import ScalarValues::*;
    private import SysML::*;
    part def A { port p1; }
    part def B { port p2; }
    part system {
       part a : A;
       part b : B;
       bind a.p1 = b.p2;
       /* CRITICAL: No array indices allowed! Bind multiple items directly: */
       /* bind a.ports = b.ports; */
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Binding Connector (=)", lines, "Equating elements (no array indices).", theme, full_code=code_2, sheet_name='Connections', wrapper_type='structure')
    md_blocks.append(("header", "2. Binding Connector (=)"))
    md_blocks.append(("text", "Equating elements. **CRITICAL**: No array indices are allowed (e.g. `a[1] = b[1]` is invalid)."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Interface Connection ---
    lines = [
        [("interface", theme.c_keyword), (" ", theme.c_normal), ("def", theme.c_keyword), (" IData", theme.c_type), (" {", theme.c_normal)],
        [("   end", theme.c_keyword), (" source", theme.c_normal), (";", theme.c_normal)],
        [("   end", theme.c_keyword), (" target", theme.c_normal), (";", theme.c_normal)],
        [("   flow", theme.c_keyword), (" source", theme.c_normal), (" to", theme.c_keyword), (" target", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_3 = """package Connections_3InterfaceConnection {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context */)
    interface   def  IData  {
       end  source ;
       end  target ;
       flow  source  to  target ;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "3. Interface Connection", lines, "Flows within interfaces.", theme, full_code=code_3, sheet_name='Connections', wrapper_type='structure')
    md_blocks.append(("header", "3. Interface Connection"))
    md_blocks.append(("text", "Flows within interfaces."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 4: Succession Flow ---
    lines = [
        [("action", theme.c_keyword), (" process", theme.c_normal), (" {", theme.c_normal)],
        [("   step1", theme.c_normal), (" then", theme.c_keyword), (" step2", theme.c_normal), (";", theme.c_normal)],
        [("   doc", theme.c_keyword), (" /* Equivalent to: */", theme.c_comment)],
        [("   flow", theme.c_keyword), (" from", theme.c_keyword), (" step1", theme.c_normal), (" to", theme.c_keyword), (" step2", theme.c_normal), (";", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    code_4 = """package Connections_4SuccessionFlow {
    private import ScalarValues::*;
    private import SysML::*;
    action process {
       action step1;
       action step2;
       first step1;
       then step2;
       doc /* Equivalent to: */
       flow from step1 to step2;
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "4. Succession Flow", lines, "Control/Data flow.", theme, full_code=code_4, sheet_name='Connections', wrapper_type='structure')
    md_blocks.append(("header", "4. Succession Flow"))
    md_blocks.append(("text", "Control/Data flow."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("connections_sheet.md", "Connections Cheat Sheet", "Connections and Flows", md_blocks, subfolder="cheatsheets")
    
    output_dir = os.path.join("..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "connections.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
