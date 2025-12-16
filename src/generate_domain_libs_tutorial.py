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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Domain Libraries", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "ISQ, Time, and Geometry", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: ISQ ---
    svg += utils.text(50, y, "1. ISQ (Physical Quantities)", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "The International System of Quantities is built-in.",
        "• import ISQ::*; : Access standard dimensions like Mass, Length, Time.",
        "• Units: [m], [kg], [s], [m/s] are standardized."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Time ---
    svg += utils.text(50, y, "2. Time and Duration", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "SysML v2 has a robust time model.",
        "• Time: Top-level concept.",
        "• Duration: Differences in time (usually [s] or [ms])."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Example ---
    svg += utils.text(50, y, "3. Physics Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package DomainLibs_Tutorial {
    import ISQ::*;
    import SI::*;
    import Time::*;
    
    // --- 1. Using ISQ Types ---
    part def MovingObject {
        attribute mass : MassValue;
        attribute velocity : SpeedValue;
        attribute startingTime : TimeInstantValue;
    }
    
    part car : MovingObject {
        // --- 2. Using Units ---
        attribute redefines mass = 1500 [kg];
        attribute redefines velocity = 120 [km/h];
        
        // --- 3. Time ISO 8601 ---
        attribute redefines startingTime = "2023-10-27T10:00:00Z";
    }
    
    // --- 4. Geometry (Shape Library) ---
    // (Requires Shape library import usually)
    // part wheel : Cylinder { 
    //    attribute radius = 30 [cm];
    // }
}"""
    
    utils.save_example("DomainLibs_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "attribute", "redefines", "package", "import"]:
                color = theme.c_keyword
            elif w.startswith("//"):
                color = theme.c_comment
            elif "[" in w and "]" in w:
                 color = theme.c_string # Units
            
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
        ("header", "1. ISQ & SI"),
        ("text", "The standard libraries provide types for almost all physical quantities."),
        ("code", "import ISQ::*;\nimport SI::*;"),
        ("header", "2. Units"),
        ("text", "Units are first-class citizens using square brackets."),
        ("code", "attribute len = 5 [m];"),
        ("header", "3. Physics Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("DomainLibs_Tutorial.md", "Domain Libraries", "ISQ, SI, and Time", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "domain_libs_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
