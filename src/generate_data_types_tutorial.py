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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Data Types", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Primitives, Values, and Units", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Standard Types ---
    svg += utils.text(50, y, "1. Standard Primitive Types", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "SysML v2 provides familiar primitive types in the ScalarValues library.",
        "• String : Textual data (\"Hello\").",
        "• Integer : Whole numbers (42).",
        "• Real : Floating point numbers (3.14).",
        "• Boolean : True/False flags."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: ISQ Units ---
    svg += utils.text(50, y, "2. ISQ Units (Physical Quantities)", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "For engineering, prefer strongly-typed physical quantities over plain Reals.",
        "The ISQ library defines standard quantities and units:",
        "• ISQ::mass, ISQ::length, ISQ::time (Physical Properties).",
        "• MassValue, LengthValue, TimeValue (Raw Data Types)."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Custom Types ---
    svg += utils.text(50, y, "3. Custom Data Types", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "You can define your own domain-specific types:",
        "• attribute def: A reusable value type definition.",
        "• struct (Kernel): A generalized structured data type.",
        "• alias: Rename or restrict existing types."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20
    
    # --- Section: Full Example ---
    svg += utils.text(50, y, "4. Data Types and Values Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package DataTypes_Tutorial {
    private import ScalarValues::*;
    /* Note: ISQ is automatically imported by SI (public import) */
    private import SI::*;
    private import MeasurementReferences::ConversionByPrefix;

    /* --- 1. Custom Value Definitions --- */
    /* Specializing a primitive */
    attribute def IDString :> String;
    
    /* Struct for composite data (Kernel level concept often used) */
    attribute def Coordinates {
        attribute x : Real;
        attribute y : Real;
        attribute z : Real;
    }
    
    /* --- 2. Custom Units --- */
    package ProjectUnits {
        attribute <ms> millisecond : DurationUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = milli;
                :>> referenceUnit = s;
            }
        }
        attribute <'mm/h'> 'millimetre per hour' : SpeedUnit = mm / h;
    }

    part def SensorSystem {
        /* --- 3. Using Primitives --- */
        attribute isActive : Boolean = true;
        attribute firmwareVersion : String = "v1.2.4";
        attribute cycleCount : Integer = 0;
        
        /* --- 4. Using ISQ Units --- */
        /* Type checking ensures you can't assign Mass to Length */
        /* Validating physical properties (Recommended) */
        attribute weight :> ISQ::mass = 5.5 [kg];
        attribute scanRange :> ISQ::length = 150 [m];
        
        /* Raw value storage (Context-free) */
        attribute rawData : MassValue = 10.0 [kg];
        
        /* Unit conversion is handled by checks (e.g. [km] -> [m]) */
        attribute speed :> ISQ::speed = 120 [km/h]; 
        
        /* --- 5. Using Custom Types --- */
        attribute sensorID : IDString = "SENS-001";
        attribute location : Coordinates {
             :>> x = 10.0;
             :>> y = 20.0;
             :>> z = 0.0;
        }
    }
}"""
    
    utils.save_example("DataTypes_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "attribute", "package", "import", "struct"]:
                color = theme.c_keyword
            elif w.startswith("/*") or w.endswith("*/"):
                color = theme.c_comment
            elif w in ["Boolean", "String", "Integer", "Real"]:
                 color = theme.c_type
            elif "[" in w and "]" in w:
                 color = theme.c_type # units
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
    
    blocks = [
        ("header", "1. Standard Primitive Types"),
        ("text", "SysML v2 provides familiar primitive types in the ScalarValues library:\n• **String**: Textual data.\n• **Integer**: Whole numbers.\n• **Real**: Floating point numbers.\n• **Boolean**: True/False flags."),
        ("header", "2. ISQ Units (Physical Quantities)"),
        ("text", "For engineering, using standard quantities is critical. The `SI` library publicly imports `ISQ`, so importing `SI` gives you access to both units (e.g. `[kg]`) and physical quantity types (e.g. `ISQ::mass`)."),
        ("header", "3. Custom Data Types"),
        ("text", "You can define domain-specific types:\n• **attribute def**: A reusable value type definition.\n• **struct**: A generalized structured data type.\n• **ProjectUnits**: Explicitly define derived units or use `ConversionByPrefix`."),
        ("header", "4. Data Types and Values Example"),
        ("code", full_code)
    ]
    if theme_key == 'light':
        utils.save_markdown("DataTypes_Tutorial.md", "Data Types", "Primitives, Values, and Units", blocks)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "data_types_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
