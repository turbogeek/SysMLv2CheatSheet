import utils
import themes
import os
import uuid
import base64
import html
from themes import THEMES

def generate_for_theme(theme_key, theme):
    # Dimensions match Use Case / Features Tutorial
    w, h = 1400, 2200 
    svg = utils.svg_start(w, h, theme)
    
    # Title
    svg += utils.text(50, 60, "SysML v2 Tutorial: Names & Imports", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Identifiers, Conventions, and Package Management", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section 1: Identifiers & Naming Rules ---
    svg += utils.text(50, y, "1. Identifiers", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Standard identifiers in SysML v2 are alphanumeric and can include underscores.",
        "They must start with a letter or underscore.",
        "You can use 'single quotes' to escape any character sequence (e.g., 'My Name')."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section 2: Conventions ---
    svg += utils.text(50, y, "2. Naming Conventions", 24, theme.c_keyword, "bold")
    y += 30
    cols = [
        ("Definitions (PascalCase)", "CamelCase starting with Uppercase.\nUsed for: part defs, action defs, packages.\nExample: VehicleSystem, FlightControl"),
        ("Usages (camelCase)", "CamelCase starting with lowercase.\nUsed for: parts, actions, attributes.\nExample: engine, maxSpeed, calculateThrust")
    ]
    cx = 50
    for title, desc in cols:
        svg += utils.text(cx, y, title, 20, theme.c_type, "bold")
        y += 25
        for dline in desc.split('\n'):
            svg += utils.text(cx, y, dline, 16, theme.text_main)
            y += 25
        y += 10
    y += 10

    # --- Section 3: Imports & Scoping ---
    svg += utils.text(50, y, "3. Imports", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Imports bring elements from other packages into scope.",
        "• standard import: Transitive (visible to importers of this package).",
        "• private import: Only visible within this file/package."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section 4: Wildcards ---
    svg += utils.text(50, y, "4. Wildcards (* vs **)", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "• *: Shallow import (imports direct children).",
        "• **: Recursive import (imports everything deeply).",
        "Warning: Avoid ** in production to prevent namespace pollution!"
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section 5: Aliasing ---
    svg += utils.text(50, y, "5. Aliasing", 24, theme.c_keyword, "bold")
    y += 30
    svg += utils.text(50, y, "Use 'as' to rename imports, resolving conflicts or shortening names.", 18, theme.text_main)
    y += 30

    # --- Section 6: Full Example ---
    svg += utils.text(50, y, "6. Comprehensive Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package Naming_Tutorial {
    // --- Library Definitions ---
    package StandardLibrary {
        part def Widget;
        part def Gadget;
        attribute def Status;
    }
    
    package SpecializedLibrary {
        // Name collision with StandardLibrary
        part def Widget; 
    }

    // --- Imports & Aliasing ---
    // Public import: 'StandardLibrary' is visible to users of 'Naming_Tutorial'
    import StandardLibrary::*;
    
    // Private import: Resolving collision with alias
    private import SpecializedLibrary::Widget as SpecialWidget;

    // --- Definitions & Usages ---
    part def SystemContext {
        // Usage of standard import
        part standardPart : Widget;
        
        // Usage of aliased import
        part specialPart : SpecialWidget;
        
        // Escaped identifier for spaces
        attribute 'System ID' : String;
        
        // Correct Convention: camelCase usage
        part mainGadget : Gadget;
    }
}"""
    
    # Save Example File
    utils.save_example("Naming_Tutorial.sysml", full_code)
    
    # Render Code Box
    # Split code into lines for rendering
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "attribute", "package", "import", "private", "as"]:
                color = theme.c_keyword
            elif w.startswith("//"):
                color = theme.c_comment
            elif w.endswith(";") or w.endswith("{") or w.endswith("}"):
                color = theme.c_normal
            elif w.startswith("'") and w.endswith("'"):
                 color = theme.c_string
            
            # Special case for comments
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
    
    # Separate Markdown Generation
    blocks = [
        ("header", "1. Identifiers"),
        ("text", "Standard identifiers in SysML v2 are alphanumeric and can include underscores. They must start with a letter or underscore. You can use 'single quotes' to escape any character sequence."),
        ("header", "2. Naming Conventions"),
        ("list", [
            "**Definitions (PascalCase)**: CamelCase starting with Uppercase. Used for: part defs, action defs, packages.",
            "**Usages (camelCase)**: CamelCase starting with lowercase. Used for: parts, actions, attributes."
        ]),
        ("header", "3. Imports"),
        ("text", "Imports bring elements from other packages into scope.\n• standard import: Transitive (visible to importers of this package).\n• private import: Only visible within this file/package."),
        ("header", "4. Wildcards (* vs **)"),
        ("text", "• *: Shallow import (imports direct children).\n• **: Recursive import (imports everything deeply).\nWarning: Avoid ** in production to prevent namespace pollution!"),
        ("header", "5. Aliasing"),
        ("text", "Use 'as' to rename imports, resolving conflicts or shortening names."),
        ("header", "6. Comprehensive Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("Naming_Tutorial.md", "Names & Imports", "Identifiers, Conventions, and Package Management", blocks)

    # SVG Output
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "naming_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
