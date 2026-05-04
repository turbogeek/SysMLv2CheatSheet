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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Requirements", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Specifying and Verifying Needs", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Definitions ---
    svg += utils.text(50, y, "1. Defining Requirements", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Requirements specify what the system must do.",
        "• requirement def: A reusable requirement type.",
        "• requirement: A specific requirement usage.",
        "• doc: Textual description of the requirement."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Relationships ---
    svg += utils.text(50, y, "2. Traceability Relationships", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "• satisfy: A design element fulfills a requirement.",
        "• verify: A test case proves the requirement is met.",
        "• refine: Adding more detail to a requirement."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Example ---
    svg += utils.text(50, y, "3. System Requirements Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Requirements_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Requirements --- */
    requirement def PerformanceReq {
        doc /* The system shall operate within performance limits. */
    }
    
    requirement <'REQ-101'> 'Breaking Distance' : PerformanceReq {
        doc /* The vehicle must stop within 50 meters from 100km/h. */
        /* Formal attributes */
        attribute maxDistance : Real = 50.0;
        attribute actualDistance : Real;
        /* Formal constraint (CRITICAL: no semicolon after constraint block) */
        assert constraint {
            actualDistance <= maxDistance
        }
    }

    /* --- 2. Satisfaction (Design) --- */
    part def BrakeSystem;
    
    part brakes : BrakeSystem {
        /* Asserting that this part satisfies the requirement */
        satisfy 'Breaking Distance';
    }
    
    /* --- 3. Verification (Testing) --- */
    /* A case to test the requirement */
    verification def BrakeTest {
        /* The requirement being verified */
        subject req : PerformanceReq;
        
        /* The logic (action) of the test */
        action executeTest {
            /* ... test steps ... */
        }
    }
    
    /* Usage of validation */
    verification test1 : BrakeTest {
        objective {
            verify 'Breaking Distance';
        }
    }
}"""
    
    utils.save_example("Requirements_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["requirement", "def", "doc", "part", "satisfy", "verification", "verify", "subject", "action", "package", "import"]:
                color = theme.c_keyword
            elif w.startswith("/*") or w.endswith("*/"):
                color = theme.c_comment
            elif w.startswith("'") or w.startswith("\""):
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
        ("header", "1. Defining Requirements"),
        ("text", "Requirements capture the needs of the system. Note: Always use requirement usages for actual project requirements, and doc /* ... */ for shall statements."),
        ("code", "requirement <'REQ-ID'> 'Name' : RequirementType { doc /* Description */; }"),
        ("header", "2. Traceability"),
        ("list", [
            "**satisfy**: Asserting that a design element (part) meets a requirement.",
            "**verify**: Asserting that a test case proves a requirement (inside an objective block).",
            "**assert constraint { ... }**: Adding formal constraints inside requirements. **CRITICAL**: Do NOT place a semicolon at the end of the constraint block."
        ]),
        ("header", "3. Requirements Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Requirements_Tutorial.md", "Requirements", "Specifying and Verifying Needs", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "requirements_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
