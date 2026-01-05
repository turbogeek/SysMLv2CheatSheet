import os
import glob
from themes import THEMES

def generate_master_sheet():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_base = os.path.join(base_dir, "..", "output", "svg")

    # Preferred order for the cheat sheets
    preferred_order = [
        "Index",
        "Structure",
        "Relationships",
        "Requirements",
        "Constraint Patterns",
        "Actions",
        "Action Patterns",
        "State Machines",
        "State Patterns",
        "Use Cases",
        "Calculations",
        "View & Viewpoints",
        "Metadata",
        "Language Reference"
    ]

    for theme_key, theme in THEMES.items():
        theme_dir = os.path.join(output_base, theme_key)
        if not os.path.exists(theme_dir):
            print(f"Skipping {theme_key} - directory not found.")
            continue

        svg_files = glob.glob(os.path.join(theme_dir, "*.svg"))
        
        # Sort files
        def get_sort_key(filepath):
            filename = os.path.basename(filepath)
            name = filename.replace(".svg", "").replace("_", " ").title()
            
            # Map filename variations to preferred order names if needed
            if "Index" in name: return -1 # Always first
            
            # Try to find in preferred list
            # We do loose matching because filenames might vary (e.g. "actions_core" vs "Actions")
            for i, p_name in enumerate(preferred_order):
                if p_name.lower() in name.lower():
                    return i
            
            return 100 # At the end

        svg_files.sort(key=get_sort_key)

        output_file = os.path.join(theme_dir, "Master_Cheatsheet.md")
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# SysML v2 Master Cheat Sheet ({theme.name})\n\n")
            f.write(f"*Theme: {theme.name}*\n\n")
            f.write("---\n\n")

            for svg_path in svg_files:
                filename = os.path.basename(svg_path)
                title = filename.replace(".svg", "").replace("_", " ").title()
                
                # Skip the previous master file if it was somehow picked up (though glob *.svg shouldn't pick it up)
                
                f.write(f"## {title}\n\n")
                f.write(f"![{title}]({filename})\n\n")
                f.write("---\n\n")
        
        print(f"Generated {output_file}")

if __name__ == "__main__":
    generate_master_sheet()
