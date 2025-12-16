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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Actions", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Defining Behavior and Activity", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Action Basics ---
    svg += utils.text(50, y, "1. Action Definitions", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Actions represent behavior. They can be defined and then used.",
        "• action def: reusable behavior definition.",
        "• action: A specific step in a process."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Control Flow ---
    svg += utils.text(50, y, "2. Flow and Control", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Actions are connected by succession flows to define order.",
        "• first action : Declares the starting point.",
        "• then: Keyword for immediate succession (shorthand for flow).",
        "• merge / decision: Control nodes for branching loop logic."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Example ---
    svg += utils.text(50, y, "3. Processing Pipeline", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Actions_Tutorial {
    import ScalarValues::*;
    
    // reusable action
    action def LogStatus { in msg : String; }

    action def ProcessData {
        // Defining steps
        action step1;
        action step2;
        action step3;
        
        // --- Control Flow ---
        // 'first' implies the entry point
        first step1;
        
        // 'then' implies succession (step1 completes before step2 starts)
        flow from step1 to step2; // explicit
        
        // Shorthand for flow:
        // step2 then step3; 
        
        // --- Parallelism ---
        action branchA;
        action branchB;
        
        // Forking: step3 triggers both branches
        flow from step3 to branchA;
        flow from step3 to branchB;
        
        // --- Using Definitions ---
        action logger : LogStatus {
            in msg = "Processing Complete";
        }
        
        // Joining: both must finish before logger runs
        flow from branchA to logger;
        flow from branchB to logger;
    }
}"""
    
    utils.save_example("Actions_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["action", "def", "flow", "from", "to", "first", "then", "package", "import", "in", "out"]:
                color = theme.c_keyword
            elif w.startswith("//"):
                color = theme.c_comment
            elif "String" in w:
                 color = theme.c_type
            elif "\"" in w:
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
        ("header", "1. Action Basics"),
        ("text", "Actions represent distinct steps of behavior.\n• **action def**: A reusable definition.\n• **action**: A usage (step)."),
        ("header", "2. Flows and Control"),
        ("list", [
            "**first**: Marks the starting action.",
            "**flow**: Explicit succession (`flow from a to b`).",
            "**then**: Shorthand succession (`a then b`).",
            "**fork/join**: Implicit when multiple flows leave or enter an action."
        ]),
        ("header", "3. Processing Pipeline Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Actions_Tutorial.md", "Actions & Behavior", "Modeling Activity Diagrams", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "actions_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
