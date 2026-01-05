import html
import base64
import uuid
import os
import re

# Configuration Flag
SHOW_COPIABLE_CODE = True

# --- SVG Helpers ---
def svg_start(w, h, theme, include_script=True):
    svg = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    svg += f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="font-family: {theme.font_family}; background-color: {theme.bg_color};">\n'
    
    # Add Script for Clipboard Actions
    if include_script:
        svg += """
    <script type="text/javascript">
    <![CDATA[
    function copyToClipboard(elementId) {
        var text = document.getElementById(elementId).textContent;
        // Decode base64 if we use it, but plain text is easier if escaped. 
        // Let's assume standard text content for now, maybe base64 decoded if needed.
        // Actually, let's use base64 to avoid escaping hell in attributes.
        var decoded = atob(text);
        
        navigator.clipboard.writeText(decoded).then(function() {
            console.log('Copying to clipboard was successful!');
            alert('Example copied to clipboard!');
        }, function(err) {
            console.error('Could not copy text: ', err);
            alert('Failed to copy. ' + err);
        });
    }
    ]]>
    </script>
    """
    if theme.branding_svg:
        svg += theme.branding_svg
    return svg

def svg_end():
    return '</svg>'

def rect(x, y, w, h, fill, stroke=None, stroke_width=0, r=10):
    stroke_attr = f'stroke="{stroke}" stroke-width="{stroke_width}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" rx="{r}" ry="{r}" {stroke_attr} />'

def text(x, y, content, size, color, weight="normal", anchor="start", font_family=None):
    font_attr = f'font-family="{font_family}"' if font_family else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" {font_attr}>{html.escape(content)}</text>'

def image(x, y, w, h, path_or_data, is_base64=False):
    if not is_base64:
        with open(path_or_data, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            mime_type = "image/png" # Assumed
            if path_or_data.lower().endswith(".jpg") or path_or_data.lower().endswith(".jpeg"):
                mime_type = "image/jpeg"
            elif path_or_data.lower().endswith(".svg"):
                mime_type = "image/svg+xml"
            href = f"data:{mime_type};base64,{data}"
    else:
        href = path_or_data
        
    return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{href}" />'

def colored_code_line(x, y, segments, size, theme):
    svg_elements = []
    current_x = x
    char_width = 0.6 * size 
    for txt, color in segments:
        weight = "normal"
        style = "normal"
        if color == theme.c_comment:
            style = "italic"
        
        # Manual italic style since text helper doesn't support it directly yet
        font_attr = f'font-family="{theme.font_family}" font-style="{style}"'
        svg_elements.append(f'<text x="{current_x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="start" {font_attr} xml:space="preserve">{html.escape(txt)}</text>')
        current_x += len(txt) * char_width
    return "".join(svg_elements)

def reconstruct_code(code_lines):
    """Reconstructs plain text code from colored segments."""
    lines = []
    for line_segments in code_lines:
        line_text = " ".join([seg[0] for seg in line_segments])
        lines.append(line_text)
    return "\n".join(lines)

# --- File Helpers ---
def save_example(file_name, content):
    """Saves the example to the pastableExamples directory."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(base_dir, "..", "output", "pastableExamples")
    os.makedirs(target_dir, exist_ok=True)
    file_path = os.path.join(target_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    validate_sysml_compliance(file_name, content)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path

def validate_sysml_compliance(context, code):
    """
    Checks SysML code for compliance with strict project rules:
    1. No single-line comments (//).
    2. Explicit strict imports (must be public or private).
    """
    errors = []
    
    # Check 1: Single Line Comments
    # We ignore http:// and https://
    lines = code.split('\n')
    for i, line in enumerate(lines):
        if "//" in line:
            # Simple check to exclude URLs
            if "http://" not in line and "https://" not in line:
                errors.append(f"Line {i+1}: Found single-line comment '//'. Use block comments /* ... */ instead.")

    # Check 2: Explicit Imports
    # Look for 'import ' that is NOT preceded by 'private ' or 'public '
    # This regex looks for 'import' at the start of semantic usage, ignoring whitespace
    # We want to catch "    import X" but allow "    private import X"
    import_pattern = re.compile(r'^\s*import\s+')
    for i, line in enumerate(lines):
        if import_pattern.match(line):
             errors.append(f"Line {i+1}: Found implicit import '{line.strip()}'. Must specify 'public import' or 'private import'.")

    if errors:
        print(f"\n[WARNING] SysML Compliance Issues in '{context}':")
        for e in errors:
            print(f"  - {e}")
        print("")

def save_markdown(file_name, title, subtitle, blocks, subfolder="tutorials"):
    """
    Saves a markdown tutorial.
    blocks: list of (type, content) tuples.
    types: 'text', 'code', 'header', 'list'
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(base_dir, "..", "output", subfolder)
    os.makedirs(target_dir, exist_ok=True)
    file_path = os.path.join(target_dir, file_name)
    
    md_content = f"# {title}\n\n"
    if subtitle:
        md_content += f"*{subtitle}*\n\n"
        
    for block_type, content in blocks:
        if block_type == 'header':
            md_content += f"## {content}\n\n"
        elif block_type == 'text':
            md_content += f"{content}\n\n"
        elif block_type == 'list':
            for item in content:
                md_content += f"- {item}\n"
            md_content += "\n"
        elif block_type == 'image':
            # content is (path, alt_text)
            path, alt = content
            # Ensure relative path for markdown if possible, or just use absolute. 
            # Markdown usually likes relative paths from the markdown file location.
            # ../svg/theme/symbols/file.svg
            md_content += f"![{alt}]({path})\n\n"
        elif block_type == 'code':
            validate_sysml_compliance(f"{file_name} (Code Block)", content)
            md_content += "```sysml\n"
            md_content += f"{content}\n"
            md_content += "```\n\n"
            
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Generated Markdown: {file_path}")
    return file_path

def sanitize_name(name):
    """Sanitizes a string to be a valid SysML identifier."""
    return "".join(c for c in name if c.isalnum() or c == '_')

def wrap_code(snippet, package_name, wrapper_type="action"):
    """Wraps a code snippet in a standard package structure for compilation."""
    # Determine if it's already a package
    if snippet.strip().startswith("package "):
        return snippet
        
    wrapper = f"package {package_name} {{\n"
    wrapper += "    private import ScalarValues::*;\n"
    wrapper += "    private import SI::*;\n"
    wrapper += "    private import SysML::*;\n"
    
    if wrapper_type == "action":
        wrapper += "    /* Wrapped Snippet (Action Context) */\n"
        wrapper += "    action def Main {\n"
        # Indent snippet
        indented = "\n".join(["        " + line for line in snippet.split('\n')])
        wrapper += indented
        wrapper += "\n    }\n"
    elif wrapper_type == "state":
        wrapper += "    /* Wrapped Snippet (State Context) */\n"
        wrapper += "    state def Main {\n"
        # Indent snippet
        indented = "\n".join(["        " + line for line in snippet.split('\n')])
        wrapper += indented
        wrapper += "\n    }\n"
    else:
        # Structure context (or default)
        wrapper += "    /* Wrapped Snippet (Structure Context) */\n"
        # Indent snippet
        indented = "\n".join(["    " + line for line in snippet.split('\n')])
        wrapper += indented
        wrapper += "\n"

    # Add View (only if action? or always? generic view maybe)
    # The view is mostly for exposing the main action. 
    if wrapper_type == "action":
         wrapper += """
    view ExposeExample {
        expose Main;
    }
"""
    wrapper += "}"
    return wrapper

def draw_card(x, y, col_width, title, code_lines, explanation, theme, full_code=None, image_path=None, sheet_name="General", wrapper_type="action"):
    base_h = 60 + (len(code_lines) * 25) + 60
    img_h = 0
    if image_path:
        img_h = 200 # Fixed height
    h = base_h + img_h
    svg = rect(x, y, col_width, h, theme.card_bg)
    svg += text(x + 20, y + 35, title, 24, theme.c_type, "bold", font_family=theme.title_font)
    
    # Copy Button Logic
    if SHOW_COPIABLE_CODE:
        safe_title = sanitize_name(title)
        safe_sheet = sanitize_name(sheet_name)
        # Create a somewhat unique package name
        package_name = f"{safe_sheet}_{safe_title}"

        final_code = full_code
        if final_code:
             # If full code is provided, we still want to save it.
             # We assume full_code matches the package logic or is valid standard code.
             # We use the generated package name for the filename.
             filename = f"{package_name}.sysml"
             save_example(filename, final_code)
        else:
            # Auto-generate
            print(f"DEBUG: Auto-generating code for {package_name}")
            raw_snippet = reconstruct_code(code_lines)
            print(f"DEBUG: Reconstructed len: {len(raw_snippet)}")
            
            final_code = wrap_code(raw_snippet, package_name, wrapper_type)
            
            # Save to file
            filename = f"{package_name}.sysml"
            # print(f"DEBUG: Saving {filename}")
            save_example(filename, final_code)
            
        code_id = f"code_{uuid.uuid4().hex}"
        b64_code = base64.b64encode(final_code.encode('utf-8')).decode('utf-8')
        
        # Hidden data element
        svg += f'<text id="{code_id}" style="display:none;">{b64_code}</text>'
        
        # Button UI
        btn_x = x + col_width - 80
        btn_y = y + 10
        svg += f'<g onclick="copyToClipboard(\'{code_id}\')" style="cursor: pointer;">'
        # Tooltip (Title element)
        svg += f'<title>{html.escape(final_code)}</title>'
        svg += rect(btn_x, btn_y, 70, 30, theme.c_keyword, r=5)
        # Check branding/theme for button text color if strictly needed, white is usually safe on keyword color
        svg += text(btn_x + 35, btn_y + 20, "COPY", 14, "#FFFFFF", "bold", "middle")
        svg += '</g>'

    cy = y + 70
    
    # Image
    if image_path:
        img_w = col_width - 40
        svg += image(x + 20, cy, img_w, img_h, image_path)
        cy += img_h + 20
        
    for line in code_lines:
        svg += colored_code_line(x + 20, cy, line, 16, theme)
        cy += 25
    svg += text(x + 20, cy + 20, explanation, 16, theme.text_sec, "italic")
    return svg, h

def draw_legend(x, y, width, theme):
    svg = ""
    # Background for legend
    svg += rect(x, y, width, 50, theme.card_bg, r=5)
    
    # Legend Items
    items = [
        ("Keyword", theme.c_keyword),
        ("Type", theme.c_type),
        ("String", theme.c_string),
        ("Comment", theme.c_comment),
        ("Normal", theme.c_normal)
    ]
    
    cur_x = x + 20
    cy = y + 30
    svg += text(cur_x, cy, "Key:", 16, theme.text_main, "bold")
    cur_x += 50
    
    for label, color in items:
        # Draw a small box or just text? Text is better.
        svg += text(cur_x, cy, label, 16, color, "bold")
        cur_x += len(label) * 10 + 30
        
    return svg
