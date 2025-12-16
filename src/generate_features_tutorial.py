import utils
import themes
import os
import uuid
import base64
import html
from themes import THEMES

def generate_for_theme(theme_key, theme):
    # Dimensions match Use Case Tutorial
    w, h = 1400, 2200 
    svg = utils.svg_start(w, h, theme)
    
    # Title
    svg += utils.text(50, 60, "SysML v2 Tutorial: Features & Chaining", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Understanding Structure, Behavior, and feature paths", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section 1: What is a Feature? ---
    svg += utils.text(50, y, "1. What is a Feature?", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "In SysML v2, almost everything is a Feature. Features describe the characteristics of a defined type.",
        "They can be structural (parts, attributes, ports) or behavioral (actions, states).",
        "Valid features are defined by their type and multiplicity."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section 2: Feature Chaining ---
    svg += utils.text(50, y, "2. Feature Chaining (Dot Notation)", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Feature chaining allows you to access deeply nested features without redefining the entire hierarchy.",
        "You can 'reach into' a part to constrain or redefine its internal properties using the dot (.) operator."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 10
    
    # Chaining Code Snippet
    chain_code = [
        [("part", theme.c_keyword), (" def", theme.c_keyword), (" Engine", theme.c_type), (" { ", theme.c_normal), ("attribute", theme.c_keyword), (" mass;", theme.c_normal), (" }", theme.c_normal)],
        [("part", theme.c_keyword), (" def", theme.c_keyword), (" Car", theme.c_type), (" { ", theme.c_normal), ("part", theme.c_keyword), (" engine : Engine;", theme.c_normal), (" }", theme.c_normal)],
        [],
        [("part", theme.c_keyword), (" def", theme.c_keyword), (" PerformanceCar", theme.c_type), (" :>", theme.c_normal), (" Car", theme.c_type), (" {", theme.c_normal)],
        [("  ", theme.c_normal), ("// Feature Chaining:", theme.c_comment)],
        [("  ", theme.c_normal), ("// Constrain the 'mass' of the 'engine' without redefining 'engine'", theme.c_comment)],
        [("  ", theme.c_normal), ("attribute", theme.c_keyword), (" :>>", theme.c_normal), (" engine.mass", theme.c_normal), (" = ", theme.c_normal), ("150", theme.c_string), (" [ISQ::kg];", theme.c_normal)],
        [("}", theme.c_normal)]
    ]
    
    # Draw simple code box for chaining
    chain_h = len(chain_code) * 25 + 20
    svg += utils.rect(50, y, 1300, chain_h, theme.card_bg, stroke=theme.c_type, stroke_width=1)
    cy = y + 20
    for line in chain_code:
        svg += utils.colored_code_line(70, cy, line, 16, theme)
        cy += 25
    y += chain_h + 30

    # --- Section 3: Subsetting & Redefinition ---
    svg += utils.text(50, y, "3. Modifying Features: Subsets vs Redefines", 24, theme.c_keyword, "bold")
    y += 30
    
    cols = [
        ("Subsetting (subsets)", "Classifies a feature as a member of a broader set.\nExample: 'frontWheels' is a subset of 'wheels'.\nBoth sets exist simultaneously."),
        ("Redefinition (redefines)", "Replaces an inherited feature completely.\nExample: 'engine' is replaced by 'electricMotor'.\nThe original definition is hidden in this context.")
    ]
    
    cx = 50
    for title, desc in cols:
        svg += utils.text(cx, y, title, 20, theme.c_type, "bold")
        for dline in desc.split('\n'):
            svg += utils.text(cx, y + 25, dline, 16, theme.text_main)
            y += 25
        y += 10
    y += 20

    # --- Section 4: Comprehensive Example ---
    svg += utils.text(50, y, "4. Full Example Code", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Feature_Tutorial_Model {
    import ISQ::*;

    // --- 1. Base Definitions ---
    part def Engine {
        attribute horsepower : PowerValue;
        attribute mass : MassValue;
    }

    part def Wheel;

    part def Vehicle {
        part engine : Engine[1];
        part wheels : Wheel[4];
    }

    // --- 2. Subsetting Example ---
    part def Truck :> Vehicle {
        // 'front' and 'rear' partition the 'wheels' set
        part frontWheels[2] subsets wheels;
        part rearWheels[2] subsets wheels;
    }

    // --- 3. Redefinition Example ---
    part def ElectricMotor :> Engine;
    
    part def ElectricCar :> Vehicle {
        // Replace generic Engine with ElectricMotor
        part redefines engine : ElectricMotor;
    }

    // --- 4. Feature Chaining & Redeclaration Example ---
    part def SportsCar :> Vehicle {
        // Feature Chaining: reaching into 'engine'
        // Redeclaration (:>>) shorthand for 'redefines' or 'subsets'
        
        attribute :>> engine.horsepower = 500 [hp];
        
        // This is structurally equivalent to:
        // part :>> engine {
        //    attribute :>> horsepower = 500 [hp];
        // }
    }
}"""
    
    # Save Example File
    utils.save_example("Features_Tutorial.sysml", full_code)
    
    # Render Code Box
    # Split code into lines for rendering
    code_lines_render = []
    for line in full_code.split('\n'):
        # Simple syntax highlighting heuristic for display
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "attribute", "package", "import", "subsets", "redefines"]:
                color = theme.c_keyword
            elif w.startswith("//"):
                color = theme.c_comment
            elif w.endswith(";") or w.endswith("{") or w.endswith("}"):
                color = theme.c_normal # Punctuation
            elif w.startswith(":>>") or w.startswith(":>"):
                 color = theme.c_keyword
            
            # Special case for comments - make rest of line comment
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
        # Reconstruct line for rendering
        svg += utils.colored_code_line(70, cy, line_parts, 16, theme)
        cy += 25
        
    y += code_h + 30
    
    svg += utils.svg_end()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "features_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
