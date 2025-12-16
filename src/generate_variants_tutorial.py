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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Variants", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Product Line Engineering", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Definitions ---
    svg += utils.text(50, y, "1. Variation Points", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Product families share a common core but differ in specific options.",
        "• variation: Defines a placeholder to be filled by a variant.",
        "• variant: A specific option that can fit into the variation point."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Binding ---
    svg += utils.text(50, y, "2. Variant Binding", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Binding selects a specific variant for a specific configuration.",
        "• variant usage: Selecting one of the options."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Example ---
    svg += utils.text(50, y, "3. Engine Options Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Variants_Tutorial {
    
    // abstract definition
    part def Engine;
    
    // --- 1. Variants ---
    part def V6Engine :> Engine;
    part def V8Engine :> Engine;
    part def ElectricMotor :> Engine;
    
    // --- 2. Variation Point ---
    part def Car {
        // 'variation' declares this must be chosen
        variation part engine : Engine;
    }
    
    // --- 3. Configuration (Binding) ---
    // A specific configuration of the Car
    part def SportCar :> Car {
        // Binding the variation point to a specific type
        variant part redefines engine : V8Engine;
    }
    
    part def EcoCar :> Car {
        variant part redefines engine : ElectricMotor;
    }
}"""
    
    utils.save_example("Variants_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "variation", "variant", "redefines", "package", "import"]:
                color = theme.c_keyword
            elif w.startswith("//"):
                color = theme.c_comment
            elif ":>" in w:
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
        ("header", "1. Variation Points"),
        ("text", "Variation points allow you to define configurable elements in a product line."),
        ("header", "2. Variants"),
        ("text", "Variants are the concrete options that can fill a variation point."),
        ("header", "3. Engine Options Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Variants_Tutorial.md", "Variants", "Product Line Engineering", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "variants_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
