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
    "generate_behavior_sheet.py": ("Behavior", "action"),
}

# Pattern to find duplicates:
# sheet_name='...', wrapper_type='...', sheet_name="...", wrapper_type="..."
# We can match: ", sheet_name=.*?, wrapper_type=.*?" repeating.

for filename, (sheet, wrapper) in updates.items():
    filepath = os.path.join("src", filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}")
        continue
        
    with open(filepath, "r") as f:
        content = f.read()
    
    # We want to remove the SECOND occurrence of the params if they appear consecutively (ignoring quote style)
    # Regex:
    # (, sheet_name=['"].*?['"], wrapper_type=['"].*?['"])\s*(, sheet_name=['"].*?['"], wrapper_type=['"].*?['"])
    
    regex = r"(, sheet_name=['\"].*?['\"], wrapper_type=['\"].*?['\"])\s*(, sheet_name=['\"].*?['\"], wrapper_type=['\"].*?['\"])"
    
    def repl(m):
        # Return only the first group
        return m.group(1)
        
    if re.search(regex, content, re.DOTALL):
        new_content = re.sub(regex, repl, content, flags=re.DOTALL)
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Cleaned {filename}")
    else:
        print(f"No duplicates in {filename}")
