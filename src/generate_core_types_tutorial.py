import utils
import themes
import os
import uuid
import base64
import html
from themes import THEMES

def generate_for_theme(theme_key, theme):
    w, h = 1400, 2200 
    svg = utils.svg_start(w, h, theme)
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Core Types", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Parts, Items, Attributes, and Enumerations", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section 1: Part vs Item ---
    svg += utils.text(50, y, "1. Parts vs Items", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "SysML v2 distinguishes between physical/logical structure and information/flow.",
        "• part: Has mass, energy, or spatial extent (e.g., Engine, Server).",
        "• item: Represents distinct headers or mass that flows (e.g., Water, DataMessage)."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section 2: Attributes & Scalars ---
    svg += utils.text(50, y, "2. Attributes & Scalars", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Attributes store data values within definitions.",
        "• attribute def: Defines a reusable data type (can specialize standard types like Real, Integer).",
        "• attribute: A usage of a definition holding a value.",
        "• **CRITICAL**: Always `private import ScalarValues::*;` at the top of the package to use Boolean, Real, etc."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section 3: Enumerations ---
    svg += utils.text(50, y, "3. Enumerations", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Enumerations define a fixed set of literals.",
        "Useful for states, modes, or configuration options."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section 4: Comprehensive Example ---
    svg += utils.text(50, y, "4. Core Types Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package CoreTypes_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Enumerations --- */
    enum def Status {
        enum Active;
        enum Idle;
        enum Error;
    }

    /* --- 2. Attributes & Scalars --- */
    attribute def MassValue :> Real;
    
    /* --- 3. Parts (Structure) --- */
    part def StorageTank {
        attribute capacity : MassValue = 1000.0;
        attribute currentStatus : Status = Status::Idle;
    }

    /* --- 4. Items (Flow/Substance) --- */
    item def Water;
    
    part def WaterSystem {
        part tank1 : StorageTank;
        part tank2 : StorageTank;
        
        /* Items flow or are stored */
        item storedWater : Water;
    }
}"""
    
    utils.save_example("CoreTypes_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "attribute", "item", "enum", "package", "import"]:
                color = theme.c_keyword
            elif w.startswith("/*") or w.endswith("*/"):
                color = theme.c_comment
            elif w in ["Active", "Idle", "Error"]:
                color = theme.c_string
            elif w.endswith(";") or w.endswith("{") or w.endswith("}"):
                color = theme.c_normal
            
            if any(p[1] == theme.c_comment for p in parts):
                 color = theme.c_comment
            
            parts.append((w + " ", color))
        code_lines_render.append(parts)

    code_h = len(code_lines_render) * 25 + 40
    svg += utils.rect(50, y, 1300, code_h, theme.card_bg, stroke=theme.c_type, stroke_width=1)

    # Copy Button
    code_id = f"code_{uuid.uuid4().hex}"
    b64_code = base64.b64encode(full_code.encode('utf-8')).decode('utf-8')
    svg += f'<text id="{code_id}" style="display:none;">{b64_code}</text>'
    
    btn_x = 50 + 1300 - 80
    btn_y = y + 10
    svg += f'<g onclick="copyToClipboard(\'{code_id}\')" style="cursor: pointer;">'
    svg += f'<title>Copy Code</title>'
    svg += utils.rect(btn_x, btn_y, 70, 30, theme.c_keyword, r=5)
    svg += utils.text(btn_x + 35, btn_y + 20, "COPY", 14, "#FFFFFF", "bold", "middle")
    svg += '</g>'
    
    # Render lines
    cy = y + 30
    for line_parts in code_lines_render:
        svg += utils.colored_code_line(70, cy, line_parts, 16, theme)
        cy += 25
        
    y += code_h + 30
    
    svg += utils.svg_end()
    
    blocks = [
        ("header", "1. Parts vs Items"),
        ("text", "SysML v2 distinguishes between physical/logical structure and information/flow.\n• **part**: Has mass, energy, or spatial extent (e.g., Engine, Server).\n• **item**: Represents distinct headers or mass that flows (e.g., Water, DataMessage)."),
        ("header", "2. Attributes & Scalars"),
        ("text", "Attributes store data values within definitions.\n• **attribute def**: Defines a reusable data type.\n• **attribute**: A usage of a definition holding a value."),
        ("header", "3. Enumerations"),
        ("text", "Enumerations define a fixed set of literals. Useful for states, modes, or configuration options."),
        ("header", "4. Core Types Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("CoreTypes_Tutorial.md", "Core Types", "Parts, Items, Attributes, and Enumerations", blocks)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "core_types_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
