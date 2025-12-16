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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Parts & Attributes", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Defining Structure and Values", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section 1: Definitions vs Usages ---
    svg += utils.text(50, y, "1. Definitions vs Usages", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "SysML v2 clearly separates definitions (types) from usages (instances).",
        "• part def: Defines the blueprint of a structural element.",
        "• part: A specific usage of that blueprint within another structure."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section 2: Attributes ---
    svg += utils.text(50, y, "2. Attributes and Values", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Attributes capture data properties like mass, power, or status.",
        "You typically use the standard ISQ library for physical quantities.",
        "• attribute def: Defines a new value type (e.g., MassValue).",
        "• attribute: Holds the actual value (e.g., mass = 100 [kg])."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section 3: Decomposition ---
    svg += utils.text(50, y, "3. Decomposition", 24, theme.c_keyword, "bold")
    y += 30
    svg += utils.text(50, y, "Structure is built by nesting parts inside other parts (Composite Structure).", 18, theme.text_main)
    y += 30

    # --- Section 4: Example ---
    svg += utils.text(50, y, "4. Spacecraft Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package PartsAndAttributes_Tutorial {
    import ISQ::*; // Import standard units
    
    // --- Definitions ---
    part def Engine {
        attribute maxThrust : ForceValue;
        attribute mass : MassValue;
    }
    
    part def FuelTank {
        attribute capacity : VolumeValue;
    }
    
    // --- Composite Definition ---
    part def Spacecraft {
        // Attributes of the spacecraft itself
        attribute totalMass : MassValue;
        attribute callSign : String;
        
        // Parts (Usages)
        // Decomposing Spacecraft into subsystems
        part mainEngine : Engine {
            // Assigning values to attributes
            attribute :>> maxThrust = 500 [kN];
            attribute :>> mass = 1000 [kg];
        }
        
        part reserveEngine : Engine; // Uses defaults if any
        
        part fuelSystem {
            part loxTank : FuelTank;
            part rp1Tank : FuelTank;
        }
    }
    
    // --- Concrete Instance ---
    part myShip : Spacecraft {
        attribute :>> callSign = "Voyager-1";
    }
}"""
    
    utils.save_example("PartsAndAttributes_Tutorial.sysml", full_code)
    
    # Render Code
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "attribute", "package", "import"]:
                color = theme.c_keyword
            elif w.startswith("//"):
                color = theme.c_comment
            elif w.startswith(":>>"):
                 color = theme.c_keyword
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
    
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "parts_attributes_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
