import utils
from themes import THEMES

def generate_for_theme(theme_key, theme):
    w, h = 1200, 1600
    svg = utils.svg_start(w, h, theme)
    
    # Title
    svg += utils.text(w/2, 60, "SysML v2 Cheat Sheet: VIEWS & VIEWPOINTS", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(w/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")

    # Layout Config
    col_width = 560
    col_gap = 40
    col1_x = 40
    col2_x = col1_x + col_width + col_gap
    
    cur_y_c1 = 150
    cur_y_c2 = 150

    # --- Column 1: Core Concepts ---
    
    # Card 1: View Definition
    lines = [
        [("view def ReportView {", theme.c_keyword)],
        [("    in part subject;", theme.c_normal)],
        [("}", theme.c_keyword)],
    ]
    expl = "Defines a reusable view structure."
    full = """package Views {
    part def System;
    
    view def ReportView {
        /* Input parameter for subject */
        in subject : System;
    }
}"""
    card, height = utils.draw_card(col1_x, cur_y_c1, col_width, "1. View Definition", lines, expl, theme, full, sheet_name="Views_Sheet")
    svg += card
    cur_y_c1 += height + 20

    # Card 2: View Usage
    lines = [
        [("view report : ReportView {", theme.c_keyword)],
        [("    in subject = mySystem;", theme.c_normal)],
        [("}", theme.c_keyword)],
    ]
    expl = "A concrete usage of a view definition."
    full = """package Views {
    part def System;
    part mySystem : System; 
    view def ReportView { in subject : System; }
    
    /* View Usage */
    view report : ReportView {
        in subject = mySystem;
    }
}"""
    card, height = utils.draw_card(col1_x, cur_y_c1, col_width, "2. View Usage", lines, expl, theme, full, sheet_name="Views_Sheet")
    svg += card
    cur_y_c1 += height + 20

    # Card 3: Viewpoint
    lines = [
        [("viewpoint def SafetyAnalysis;", theme.c_keyword)],
        [("viewpoint <'v1'> 'sa' : SafetyAnalysis;", theme.c_keyword)],
        [("view myView {", theme.c_keyword)],
        [("    satisfy 'sa';", theme.c_normal)],
        [("}", theme.c_keyword)],
    ]
    expl = "Viewpoints define the rules/frame of concern."
    full = """package Views {
    /* 1. Define specific concern/perspective */
    viewpoint def SafetyAnalysis {
        doc "Focus on hazards.";
    }
    
    /* 2. Create viewpoint usage */
    viewpoint <'vp1'> 'sa' : SafetyAnalysis;
    
    /* 3. Link view usage to viewpoint usage */
    view mySafetyView {
        satisfy 'sa';
    }
}"""
    card, height = utils.draw_card(col1_x, cur_y_c1, col_width, "3. Viewpoint", lines, expl, theme, full, sheet_name="Views_Sheet")
    svg += card
    cur_y_c1 += height + 20

    # --- Column 2: Content Control ---

    # Card 4: Expose
    lines = [
        [("view myView {", theme.c_keyword)],
        [("    expose myPart;", theme.c_keyword)],
        [("    expose myPart::**;", theme.c_keyword)],
        [("}", theme.c_keyword)],
    ]
    expl = "Explicitly includes elements in the view."
    full = """package Views {
    part def Car { part engine; part wheels[4]; }
    part myCar : Car;
    
    view myView {
        /* Expose specific element */
        expose myCar;
        
        /* Expose element and all children recursively */
        expose myCar::**; 
    }
}"""
    card, height = utils.draw_card(col2_x, cur_y_c2, col_width, "4. Expose Content", lines, expl, theme, full, sheet_name="Views_Sheet")
    svg += card
    cur_y_c2 += height + 20

    # Card 5: Filter
    lines = [
        [("view myView {", theme.c_keyword)],
        [("    filter @Part;", theme.c_keyword)],
        [("    filter @Action;", theme.c_keyword)],
        [("}", theme.c_keyword)],
    ]
    expl = "Filter included elements by criteria."
    full = """package Views {
    private import ScalarValues::*;
    part def Car;
    part myCar : Car;
    
    view myView {
        expose myCar::**;
        
        /* Keep only Parts */
        filter @PartUsage;
        
        /* Keep only Allocations (CRITICAL: use Usage, not Definition) */
        filter @AllocationUsage;
        
        /* Or exclude specific things (logic depends on library) */
    }
}"""
    card, height = utils.draw_card(col2_x, cur_y_c2, col_width, "5. Filter", lines, expl, theme, full, sheet_name="Views_Sheet")
    svg += card
    cur_y_c2 += height + 20

    # Card 6: Rendering (Styles)
    lines = [
        [("view myView {", theme.c_keyword)],
        [("    render asTable { ... }", theme.c_keyword)],
        [("    style color = 'red';", theme.c_normal)],
        [("}", theme.c_keyword)],
    ]
    expl = "Apply rendering styles or presentation modes."
    full = """package Views {
    /* Assuming standard libraries available */
    view def MyView {
        /* Apply visual style */
        style color = "blue";
        
        /* Define table structure */
        render asTable {
           /* table details */
        }
    }
}"""
    card, height = utils.draw_card(col2_x, cur_y_c2, col_width, "6. Rendering & Style", lines, expl, theme, full, sheet_name="Views_Sheet")
    svg += card
    cur_y_c2 += height + 20
    
    # Legend
    svg += utils.draw_legend(w/2 - 250, h - 80, 500, theme)
    svg += utils.svg_end()

    # Save
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "cheatsheets", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    
    # Also save as tutorial text? 
    # Let's verify file location - usually output/svg/theme/
    output_path = os.path.join(base_dir, "..", "output", "svg", theme_key, "views_sheet.svg")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

    # Generate Markdown for Light Theme
    if theme_key == 'light':
        blocks = [
            ("header", "1. View Definition"),
            ("code", """view def ReportView {
    in subject : System;
}"""),
            ("text", "Defines a reusable view structure."),
            
            ("header", "2. View Usage"),
            ("code", """view report : ReportView {
    in subject = mySystem;
}"""),
            ("text", "Uses a definition to create a specific view."),
            
            ("header", "3. Viewpoint"),
            ("code", """viewpoint def SafetyAnalysis { doc "Focus on hazards"; }
viewpoint <'vp1'> 'sa' : SafetyAnalysis;
view mySafetyView { satisfy 'sa'; }"""),
            ("text", "Connects a view to its stakeholder concern."),
            
            ("header", "4. Expose Content"),
            ("code", """view myView {
    expose myCar;      /* Single element */
    expose myCar::**;  /* Recursive import */
}"""),
            
            ("header", "5. Filter"),
            ("code", """filter @PartUsage; /* Keep only parts */\nfilter @AllocationUsage; /* Keep allocations */"""),
            ("text", "**CRITICAL**: Always filter by Usage (e.g. `@PartUsage`, `@AllocationUsage`), not by Definition."),
            
            ("header", "6. Rendering"),
            ("code", """render asTable { ... }
style color = "red";""")
        ]
        utils.save_markdown("views_sheet.md", "System Views", "Views, Viewpoints, and Filtering", blocks, subfolder="cheatsheets")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
