import utils
import themes
import os
import uuid
import base64
from themes import THEMES

def generate_for_theme(theme_key, theme):
    w, h = 1400, 2400 
    svg = utils.svg_start(w, h, theme)
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Filters", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Refining View Content", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Concepts ---
    svg += utils.text(50, y, "1. What are Filters?", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Filters are used inside Views to exclude unwanted elements.",
        "They use expressions to test each element.",
        "• filter <condition>;: Applies the filter logic."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Syntax ---
    svg += utils.text(50, y, "2. Filter Syntax (Cameo)", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Common filtering patterns:",
        "• @MetaClass: Filter by stereotype or metaclass (e.g., @PartUsage).",
        "• hastype Definition: Filter by SysML type definition.",
        "• Logic: Use 'and', 'or', 'not' to combine conditions."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Example ---
    svg += utils.text(50, y, "3. Filtering Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Filters_Tutorial {
    private import DS_Views::SymbolicViews;
    private import Metaobjects::SemanticMetadata;
    
    part def HardwareComponent;
    part def SoftwareComponent;
    
    metadata def Critical;
    
    part system {
        part cpu : HardwareComponent;
        
        part os : SoftwareComponent {
            @Critical;
        }
        
        part driver : SoftwareComponent;
    }
    
    /* --- 1. Filtering by Type --- */
    view hardwareView : SymbolicViews::gv {
        expose system::**;
        
        /* Only show HardwareComponents */
        filter hastype HardwareComponent;
    }
    
    /* --- 2. Filtering by Metadata (Stereotypes) --- */
    view criticalView : SymbolicViews::gv {
        expose system::**;
        
        /* Only show elements tagged as @Critical */
        filter @Critical;
    }
    
    /* --- 3. Complex Logic --- */
    view complexView : SymbolicViews::gv {
        expose system::**;
        
        /* Show elements that are either Hardware or Software */
        filter hastype SoftwareComponent or hastype HardwareComponent;
    }
}"""
    
    utils.save_example("Filters_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["filter", "hastype", "not", "and", "or", "view", "def", "part", "expose", "package", "import", "metadata", "private"]:
                color = theme.c_keyword
            elif w.startswith("/*") or w.endswith("*/"):
                 color = theme.c_comment
            elif w.startswith("@"):
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
        ("header", "1. Filters"),
        ("text", "Filters refine what is shown in a view. They are crucial for creating manageable diagrams from complex models."),
        ("header", "2. Syntax"),
        ("list", [
            "**hastype <Def>**: Checks if an element is a usage of `<Def>`.",
            "**@<Meta>**: Checks if an element has specific metadata applied.",
            "**and, or, not**: Standard boolean logic."
        ]),
        ("header", "3. Filtering Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Filters_Tutorial.md", "Filters", "Refining View Content", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "filters_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
