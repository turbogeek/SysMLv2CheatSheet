import utils
import themes
import os
import uuid
import base64
import html
from themes import THEMES

def generate_for_theme(theme_key, theme):
    w, h = 1400, 2200 
    svg = utils.svg_start(w, h, theme)
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Multiplicity", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Cardinality, Collections, and Ordering", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Basic Multiplicity ---
    svg += utils.text(50, y, "1. Basic Multiplicity", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Multiplicity constraints specify how many instances of a feature can exist.",
        "Syntax: [min..max]",
        "• [1] : Exactly one (Default if unspecified).",
        "• [0..1] : Optional (Zero or one).",
        "• [*] or [0..*] : Zero or more (Unbounded)."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Collection Types ---
    svg += utils.text(50, y, "2. Collection Types", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "When multiplicity is > 1, the feature is a collection. You can constrain its nature:",
        "• ordered : The order of elements matters (List/Sequence).",
        "• unique : No duplicates allowed (Set).",
        "• nonunique : Duplicates allowed (Bag).",
        "Default is 'unique' (Set) if only multiplicity is given."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Full Example ---
    svg += utils.text(50, y, "3. Multiplicity Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Multiplicity_Tutorial {
    part def Wheel;
    part def Seat;
    part def Passenger;
    
    part def Bus {
        // --- Exact Constraints ---
        // Exactly 6 wheels are required
        part wheels : Wheel [6];
        
        // --- Optionality ---
        // A reserved seat may or may not exist (0 or 1)
        part reservedSeat : Seat [0..1];
        
        // --- Collections ---
        // unique (Default): A specific person can't be in two seats at once (Set)
        part seats : Seat [20..50]; 
        
        // ordered nonunique: Queue of passengers boarding
        // 'ordered': sequence matters (who is first)
        // 'nonunique': technically allows duplicates (though confusing for people!)
        part boardingQueue : Passenger [*] ordered nonunique;
        
        // --- Attribute Arrays ---
        // Recording lap times (Sequence of numbers)
        attribute lapTimes : ScalarValues::Real [*] ordered;
    }
}"""
    
    utils.save_example("Multiplicity_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "attribute", "package", "ordered", "unique", "nonunique"]:
                color = theme.c_keyword
            elif w.startswith("//"):
                color = theme.c_comment
            elif "[" in w or "]" in w:
                 # heuristic for multiplicity brackets
                 if w.startswith("[") or w.endswith("]"):
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
    
    svg += utils.svg_end()
    
    blocks = [
        ("header", "1. Basic Multiplicity"),
        ("text", "Multiplicity constraints specify how many instances of a feature can exist.\n• **[1]**: Exactly one (Default).\n• **[0..1]**: Optional.\n• **[*]** or **[0..*]**: Zero or more."),
        ("header", "2. Collection Types"),
        ("text", "When multiplicity is > 1, the feature is a collection. You can constrain its nature:\n• **ordered**: The order of elements matters.\n• **unique**: No duplicates allowed (Default).\n• **nonunique**: Duplicates allowed."),
        ("header", "3. Multiplicity Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Multiplicity_Tutorial.md", "Multiplicity", "Cardinality, Collections, and Ordering", blocks)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "multiplicity_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
