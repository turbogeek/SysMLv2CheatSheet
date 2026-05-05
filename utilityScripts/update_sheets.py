import os
import re

updates = {
    "generate_structure_sheet.py": ("Structure", "structure"),
    "generate_cases_sheet.py": ("Cases", "structure"),
    "generate_connections_sheet.py": ("Connections", "structure"),
    "generate_reference_sheet.py": ("Reference", "structure"),
    "generate_relationships_sheet.py": ("Relationships", "structure"),
    "generate_actions_events_sheet.py": ("ActionsEvents", "action"),
    "generate_actions_core_sheet.py": ("ActionsCore", "action"),
    "generate_actions_control_sheet.py": ("ActionsControl", "action"),
    "generate_actions_sheet.py": ("Actions", "action"), 
}

for filename, (sheet, wrapper) in updates.items():
    filepath = os.path.join("src", filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}")
        continue
        
    with open(filepath, "r") as f:
        content = f.read()
    
    def repl(m):
        if "sheet_name=" in m.group(0):
            return m.group(0)
        # Using string replacement to append keywords
        return f"{m.group(1)}, theme, sheet_name='{sheet}', wrapper_type='{wrapper}'"
        
    # Regex: match "utils.draw_card(" ... until ", theme" or ", theme)"
    # We look for ", theme" followed by "," or ")"
    regex = r"(utils\.draw_card\(.*?)(\, +theme)(?=[,\)])"
    
    new_content = re.sub(regex, repl, content, flags=re.DOTALL)
    
    with open(filepath, "w") as f:
        f.write(new_content)
    print(f"Updated {filename}")
