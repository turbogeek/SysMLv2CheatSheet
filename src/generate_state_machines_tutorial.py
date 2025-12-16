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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: State Machines", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Event Driven Behavior", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Concepts ---
    svg += utils.text(50, y, "1. States and Transitions", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "State machines describe how a block responds to events over time.",
        "• state def: Definition of the machine.",
        "• state: A condition or situation.",
        "• transition: Moving between states triggered by events."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Mechanics ---
    svg += utils.text(50, y, "2. Mechanics", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "• entry / do / exit: Actions performed during the state.",
        "• accept: Waits for an event trigger (message, signal).",
        "• after: Time-based trigger."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Example ---
    svg += utils.text(50, y, "3. Traffic Light Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package StateMachine_Tutorial {
    import ScalarValues::*;
    
    // Define the component containing the machine
    part def TrafficLight {
        // The machine behavior
        state def LightLogic {
             // Initial entry point
             entry; then Red;
             
             state Red {
                 // Transition after time
                 transition to Green after 20 [ISQ::s];
             }
             
             state Green {
                 transition to Yellow after 30 [ISQ::s];
             }
             
             state Yellow {
                 transition to Red after 5 [ISQ::s];
             }
        }
        
        // Usage of the machine
        state logic : LightLogic;
    }
}"""
    
    utils.save_example("StateMachine_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["state", "def", "part", "entry", "then", "transition", "to", "after", "accept", "package", "import"]:
                color = theme.c_keyword
            elif w.startswith("//"):
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
        ("header", "1. State Machine Concepts"),
        ("text", "State machines define event-driven behavior. A system exists in a 'state' until an event triggers a 'transition'."),
        ("header", "2. Key Syntax"),
        ("list", [
            "**state def**: Defines the state machine structure.",
            "**entry/do/exit**: Actions associated with a state.",
            "**transition to <state>**: Defines the next state.",
            "**accept <event>** / **after <time>**: Triggers for transitions."
        ]),
        ("header", "3. Traffic Light Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("StateMachine_Tutorial.md", "State Machines", "States, Transitions, and Events", blocks)

    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "state_machines_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
