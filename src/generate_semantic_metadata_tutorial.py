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
    
    svg += utils.text(50, 60, "SysML v2 Tutorial: Semantic Metadata", 40, theme.text_main, "bold", font_family=theme.title_font)
    svg += utils.text(50, 100, "Domain Specific Language (DSL) Extension", 24, theme.text_sec, "italic", font_family=theme.title_font)

    y = 150

    # --- Section: Concept ---
    svg += utils.text(50, y, "1. Extending SysML with Metadata", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "Semantic Metadata allows you to define a Domain Specific Language (DSL) on top of SysML.",
        "You map your domain vocabulary (e.g., 'Engine', 'Wheel') to standard SysML concepts.",
        "You can then use the #shorthand syntax to write concise, domain-specific code."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Mechanics ---
    svg += utils.text(50, y, "2. Mechanics", 24, theme.c_keyword, "bold")
    y += 30
    lines = [
        "1. Define Domain Library: Standard SysML definitions (parts, ports).",
        "2. Define Metadata: Mappings using 'metadata def' and 'specializes SemanticMetadata'.",
        "   - baseType: The domain concept (e.g., Engine).",
        "   - annotatedElement: The SysML construct (e.g., SysML::Usage).",
        "3. Use DSL: Apply metadata with #metadataName."
    ]
    for line in lines:
        svg += utils.text(50, y, line, 18, theme.text_main)
        y += 25
    y += 20

    # --- Section: Full Example ---
    svg += utils.text(50, y, "3. Complete Vehicle DSL Example", 24, theme.c_keyword, "bold")
    y += 30
    
    full_code = """package DSLinSysML {
    doc /* https://www.omg.org/cgi-bin/doc?syseng/25-03-07.pdf */
    
    // --- 1. Domain Library (Vocabulary) ---
    library package Vehicle_Library {
        port def DrivePort {
            out attribute torque : ISQ::TorqueValue;
        }
        part def Engine {
            port enginePort : DrivePort;
        }
        part engines : Engine [0..*];
        part def Wheel {
            port wheelPort : ~DrivePort;
        }
        part wheels : Wheel [0..*];
        interface def DriveTrain {
            end [0..1] port drivePort : DrivePort;
            end [0..*] port drivenPort : ~DrivePort;
        }
        abstract interface driveTrains : DriveTrain [0..*];
        
        part def Vehicle {
            part :>> engines;
            part :>> wheels;
            part :>> driveTrains;
        }
    }
    
    // --- 2. Metadata Definitions (The Mapping) ---
    package Vehicle_Metadata {
        private import Vehicle_Library::*;
        private import Metaobjects::SemanticMetadata;
        
        metadata def drive :> SemanticMetadata {
            :>> baseType = driveTrains meta SysML::Usage;
            :> annotatedElement : SysML::InterfaceUsage;
        }
        metadata def engine :> SemanticMetadata {
            :>> baseType = engines meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
        metadata def wheel :> SemanticMetadata {
            :>> baseType = wheels meta SysML::Usage;
            :> annotatedElement : SysML::Usage;
        }
        metadata def vehicle :> SemanticMetadata {
            :>> baseType = Vehicle meta SysML::Definition;
            :> annotatedElement : SysML::Definition;
        }
    }
    
    // --- 3. DSL Usage (The Result) ---
    package Car_Example {
        private import Vehicle_Metadata::*;
        
        #vehicle def Car {
            #engine carEngine [1];
            #wheel carWheels [4];
            #drive interface [1] carEngine.enginePort to [2] carWheels.wheelPort;
        }
    }
}"""
    
    utils.save_example("SemanticMetadata_Tutorial.sysml", full_code)
    
    # Render Code Box
    code_lines_render = []
    for line in full_code.split('\n'):
        parts = []
        words = line.split(' ')
        for w in words:
            color = theme.c_normal
            if w in ["part", "def", "metadata", "library", "package", "import", "private", "port", "interface", "abstract"]:
                color = theme.c_keyword
            elif w.startswith("//") or w.startswith("doc"):
                color = theme.c_comment
            elif w.startswith("#"):
                 color = theme.c_keyword # The DSL keywords
            elif w.startswith(":>>") or w.startswith(":>"):
                 color = theme.c_keyword

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
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "semantic_metadata_tutorial.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
