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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Analysis", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Constraints and Parametrics", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Constraints ---
    svg += utils.text(50, y, "1. Mathematical Constraints", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Constraints define mathematical relationships (equations) that must hold true.",
        "• constraint def: A reusable equation (e.g. F = m * a).",
        "• constraint usage: Applying the equation to specific properties."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Analysis Cases ---
    svg += utils.text(50, y, "2. Analysis Cases", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Analysis cases define specific evaluation scenarios.",
        "• analysis def: Definition of the analysis logic.",
        "• subject: The system being analyzed."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Example ---
    svg += utils.text(50, y, "3. Mass Analysis Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Analysis_Tutorial {
    import ScalarValues::*;
    
    // --- 1. Constraint Definition ---
    constraint def MassEquation {
        in total : Real;
        in p1 : Real;
        in p2 : Real;
        
        // The math
        total == p1 + p2
    }
    
    part def System {
        attribute mass : Real;
        attribute part1Mass : Real;
        attribute part2Mass : Real;
        
        // --- 2. Constraint Usage (Parametrics) ---
        // Binding properties to the equation parameters
        constraint massCheck : MassEquation {
            in total = mass;
            in p1 = part1Mass;
            in p2 = part2Mass;
        }
    }
    
    // --- 3. Analysis Case ---
    analysis def WeightCheck {
        subject system : System;
        
        // Determining if mass is within limits
        return result : Boolean = system.mass < 100.0;
    }
}"""
    
    utils.save_example("Analysis_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["constraint", "def", "part", "attribute", "analysis", "subject", "return", "package", "import", "in"]:
                color = theme.c_keyword
            elif w.startswith("//"):
                color = theme.c_comment
            elif "==" in w or "=" in w:
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
        ("header", "1. Constraints (Parametrics)"),
        ("text", "Constraints define mathematical equations that govern system properties."),
        ("code", "constraint def OhmLaw { in v; in i; in r; v == i * r }"),
        ("header", "2. Analysis Cases"),
        ("text", "Analysis cases specify the logic for evaluating system performance, often involving solving constraints or running simulations."),
        ("header", "3. Mass Analysis Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Analysis_Tutorial.md", "Analysis & Constraints", "Parametrics and Evaluation", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "analysis_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
