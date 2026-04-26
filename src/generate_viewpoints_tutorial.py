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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Views", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Presenting the Model", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Definitions ---
    svg += utils.text(50, y, "1. Views and Viewpoints", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Models are complex; Views present specific subsets of information.",
        "• viewpoint: Defines the purpose and rules for a view.",
        "• view def: Defines how to construct the view.",
        "• view: A usage that renders the view."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Filtering ---
    svg += utils.text(50, y, "2. Exposing and Filtering", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "You rarely show everything.",
        "• expose: Selects which elements to include.",
        "• filter: Removes elements based on criteria using OCL-like syntax."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Example ---
    svg += utils.text(50, y, "3. System Description View", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Viewpoint_Tutorial {
    private import ScalarValues::*;
    
    /* The subject */
    part def Car {
        attribute mass : Real;
        part engine;
        part wheels;
    }
    
    /* --- 1. Viewpoint Definition --- */
    viewpoint def MassReport {
        doc "A report focusing only on mass properties.";
    }
    
    /* --- 2. Viewpoint Usage --- */
    viewpoint <'VP-002'> 'mass report viewpoint' : MassReport {
        doc "Focuses on mass properties of the vehicle";
    }
    
    /* --- 3. View Definition --- */
    view def MassView {
        /* The subject being viewed */
        in car : Car;
        
        /* --- 4. Exposing Elements --- */
        /* Show the car itself */
        expose car;
        
        /* Show sub-parts */
        expose car.engine;
        
        /* Filter: Only show attributes ending in 'Mass' (conceptual) */
        /* filter @Attribute ==> name.endsWith("sw") */
    }
    
    /* --- 5. View Usage --- */
    part myCar : Car;
    
    view report : MassView {
        in car = myCar;
        satisfy 'mass report viewpoint';
    }
}"""
    
    utils.save_example("Viewpoints_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["view", "def", "viewpoint", "expose", "filter", "part", "attribute", "package", "import", "in"]:
                color = theme.c_keyword
            elif w.startswith("/*") or w.endswith("*/"):
                color = theme.c_comment
            elif w.startswith("\"") or w.startswith("'"):
                 color = theme.c_string
            
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
        ("header", "1. Viewpoints and Views"),
        ("text", "Views present a subset of the model for a specific purpose (the Viewpoint)."),
        ("header", "2. Expose and Filter"),
        ("list", [
            "**expose**: Explicitly includes elements in the view.",
            "**filter**: Conditionally excludes elements."
        ]),
        ("header", "3. Mass Report Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Viewpoints_Tutorial.md", "Viewpoints & Views", "Presenting the Model", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "viewpoints_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
