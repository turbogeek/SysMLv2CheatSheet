import utils
import themes
import os
import uuid
import base64
from themes import THEMES

def generate_for_theme(theme_key, theme):
    w, h = 1400, 2600 
    svg = utils.svg_start(w, h, theme)
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Evaluation", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Calculations, Analysis & Verification", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Concepts ---
    svg += utils.text(50, y, "1. Evaluation Basics", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "SysML v2 supports executable analysis and verification.",
        "• calc def: Reusable mathematical calculations.",
        "• analysis def: Trade studies and optimizations.",
        "• verification def: Test cases to verify requirements.",
        "• constraint: Boolean conditions that must be true."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Syntax ---
    svg += utils.text(50, y, "2. Key Elements", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Common patterns:",
        "• require constraint { ... }: Enforce mathematical rules in Requirements.",
        "• return ...: Return values from calculations or analyses.",
        "• objective: Define the goal of a verification or analysis (e.g., verify X, minimize Y)."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Example ---
    svg += utils.text(50, y, "3. Complete Evaluation Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Evaluation_Tutorial {
    private import ScalarValues::*;
    private import AnalysisCases::*;
    
    /* --- 1. Calculations --- */
    calc def PowerCalc {
        in force : Real;
        in velocity : Real;
        return power : Real = force * velocity;
    }

    package System {
        part engine {
            attribute force : Real = 1000.0;
            attribute maxPower : Real = 50000.0;
            
            /* Using the calculation */
            attribute currentPower : Real = PowerCalc(force, 25.0);
        }
    }

    /* --- 2. Requirements & Constraints --- */
    requirement def PowerLimit {
        attribute actualPower : Real;
        attribute limit : Real;
        
        /* Boolean check */
        require constraint {
            actualPower <= limit
        }
    }
    
    /* Requirement Usage at package level to allow verification */
    requirement checkPower : PowerLimit;

    part myEngine : System::engine {
        /* Satisfaction */
        satisfy checkPower {
            attribute :>> actualPower = myEngine.currentPower;
            attribute :>> limit = myEngine.maxPower;
        }
    }

    /* --- 3. Verification Case --- */
    verification def PowerTest {
        subject system : System::engine;
        
        objective {
            /* Verify that the requirement is met */
            verify checkPower {
                subject = system;
            }
        }
    }

    /* --- 4. Analysis (Trade Study) --- */
    analysis def Optimization {
        subject candidates : System::engine [1..*];
        
        objective maximizeObj {
            subject candidates = Optimization::candidates;
        }
        
        /* Define how we measure 'goodness' */
        calc evaluate {
            in part cand :> candidates;
            return result : Real = cand.currentPower;
        }
    }
}"""
    
    utils.save_example("Evaluation_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["calc", "def", "part", "requirement", "require", "constraint", "satisfy", "verification", "subject", "objective", "analysis", "return", "in", "package", "private", "import", "attribute"]:
                color = theme.c_keyword
            elif w.startswith("/*") or w.endswith("*/"):
                 color = theme.c_comment
            
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
        ("header", "1. Evaluation Overview"),
        ("text", "SysML v2 integrates analysis and verification directly into the model."),
        ("header", "2. Components"),
        ("list", [
            "**calc def**: Defines mathematical functions.",
            "**constraint**: Defines boolean rules (often used in Requirements).",
            "**verification**: Defines test cases to verify requirements.",
            "**analysis**: Defines trade studies to compare alternatives or optimize parameters."
        ]),
        ("header", "3. Evaluation Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Evaluation_Tutorial.md", "Evaluation", "Calculations and Analysis", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "evaluation_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
