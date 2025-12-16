import utils
import themes
import os
import uuid
import base64
import html
from themes import THEMES

def generate_for_theme(theme_key, theme):
    w, h = 1400, 2400 
    svg = utils.svg_start(w, h, theme)
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Ports & Interfaces", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Defining Interactions Points", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Ports ---
    svg += utils.text(50, y, "1. Ports", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Ports define distinct interaction points on the boundary of a part.",
        "They allow you to encapsulate internal structure and only expose specific interfaces.",
        "• port name : Type;",
        "• directed port (in, out, inout): Specifies data flow direction."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Interfaces ---
    svg += utils.text(50, y, "2. Interface Definitions", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Interfaces define the contract for interaction (what flows in/out).",
        "• interface def: Reusable definition of ports/flows.",
        "• Conjugation (~): Flips the direction of flows (e.g., Plug vs Socket)."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Example ---
    svg += utils.text(50, y, "3. Power & Data Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package PortsInterfaces_Tutorial {
    import ScalarValues::*;
    
    // --- 1. Interface Definitions ---
    // Physical connection interface
    interface def PowerInterface {
        // 'out' means power leaves this port locally
        out powerLevel : Real;
    }
    
    // Logical data interface
    interface def DataLink {
        // flow of messages
        in command : String;
        out status : String;
    }

    // --- 2. Component Definitions ---
    part def Battery {
        // Provides power (Source)
        port pwrPort : PowerInterface;
    }

    part def Computer {
        // Consumes power (Sink)
        // '~' (Tilde) conjugates the interface: 'out' becomes 'in'
        port pwrIn : ~PowerInterface;
        
        // Data port
        port eth0 : DataLink;
    }
}"""
    
    utils.save_example("PortsInterfaces_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "interface", "port", "package", "import", "in", "out", "inout"]:
                color = theme.c_keyword
            elif w.startswith("//"):
                color = theme.c_comment
            elif w.startswith("~"):
                 color = theme.c_type # Conjugation
            elif "String" in w or "Real" in w:
                 color = theme.c_type
            
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
    
    # Separate Markdown Generation
    blocks = [
        ("header", "1. Ports"),
        ("text", "Ports define distinct interaction points on the boundary of a part. They allow you to encapsulate internal structure and only expose specific interfaces."),
        ("list", [
            "**port name : Type**: Basic port declaration.",
            "**directed port (in, out, inout)**: Specifies data flow direction."
        ]),
        ("header", "2. Interface Definitions"),
        ("list", [
            "**interface def**: Reusable definition of ports/flows.",
            "**Conjugation (~)**: Flips the direction of flows (e.g., Plug vs Socket). If an interface has `out pwr`, the conjugated version has `in pwr`."
        ]),
        ("header", "3. Power & Data Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("PortsInterfaces_Tutorial.md", "Ports & Interfaces", "Defining Interactions Points", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "ports_interfaces_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
