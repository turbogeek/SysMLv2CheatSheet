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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Connections", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Wiring Parts Together", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Connection Basics ---
    svg += utils.text(50, y, "1. Connections", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Connections link ports or parts together to enable interaction.",
        "• connect a to b; : A generic connection.",
        "• binding a = b; : Equivalence (a IS b, or they are wired directly).",
        "  Useful for exposing internal ports to external boundaries."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Example ---
    svg += utils.text(50, y, "2. Wiring Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Connections_Tutorial {
    private import PortsInterfaces_Tutorial::*; /* Import Battery, Computer */
    
    part def System;
    
    part def PowerSystem :> System {
        part battery : Battery;
        part computer : Computer;
        
        /* --- Connection --- */
        /* Connecting compatible ports (PowerInterface vs ~PowerInterface) */
        connect battery.pwrPort to computer.pwrIn;
        
        /* --- Binding (Delegation) --- */
        /* Exposing the computer's ethernet port to the outside world */
        port externalEth : DataLink;
        
        /* 'binding' means internal eth0 IS the same interaction point as externalEth */
        binding externalEth = computer.eth0;
    }
}"""
    
    utils.save_example("Connections_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "connect", "to", "binding", "package", "import", "port"]:
                color = theme.c_keyword
            elif w.startswith("/*") or w.startswith("//"):
                color = theme.c_comment
            elif "=" in w:
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
        ("header", "1. Connection Basics"),
        ("list", [
            "**connect a to b**: Standard connection between two endpoints.",
            "**binding a = b**: Equivalence connection. Often used for **delegation** (exposing an internal part's port to the boundary of the container)."
        ]),
        ("header", "2. Wiring Example"),
        ("text", "This example shows connecting a Battery to a Computer, and binding the internal Ethernet port to the outside."),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Connections_Tutorial.md", "Connections", "Wiring Parts Together", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "connections_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
