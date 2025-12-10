class Theme:
    def __init__(self, name, bg_color, card_bg, text_main, text_sec, c_keyword, c_type, c_string, c_comment, c_normal, font_family="'Consolas', 'Monaco', 'Courier New', monospace", title_font="'Segoe UI', 'Arial', sans-serif", branding_svg=""):
        self.name = name
        self.bg_color = bg_color
        self.card_bg = card_bg
        self.text_main = text_main
        self.text_sec = text_sec
        self.c_keyword = c_keyword
        self.c_type = c_type
        self.c_string = c_string
        self.c_comment = c_comment
        self.c_normal = c_normal
        self.font_family = font_family
        self.title_font = title_font
        self.branding_svg = branding_svg

# --- Theme Definitions ---

# 1. Light Theme
THEME_LIGHT = Theme(
    name="light",
    bg_color="#FFFFFF",
    card_bg="#F0F0F0",
    text_main="#000000",
    text_sec="#555555",
    c_keyword="#0000FF",
    c_type="#2B91AF",
    c_string="#A31515",
    c_comment="#008000",
    c_normal="#000000"
)

# 2. Dark Theme
THEME_DARK = Theme(
    name="dark",
    bg_color="#1A1A1D",
    card_bg="#2C2C30",
    text_main="#E0E0E0",
    text_sec="#A0A0A0",
    c_keyword="#FF79C6",
    c_type="#8BE9FD",
    c_string="#F1FA8C",
    c_comment="#50FA7B",
    c_normal="#E0E0E0"
)

# 3. The Dark Side (Star Wars / Far Side Parody)
# Branding: "Death Star Pickleball" - Gray ball with holes, one is the dish
DS_BRANDING = """
<image href="../assets/death_star_pickleball.png" x="1025" y="25" width="150" height="150" />
"""
THEME_DARK_SIDE = Theme(
    name="dark_side",
    bg_color="#000000",
    card_bg="#111111",
    text_main="#FFE81F",
    text_sec="#FF0000",
    c_keyword="#FF0000",
    c_type="#FFE81F",
    c_string="#FFFFFF",
    c_comment="#888888",
    c_normal="#FFE81F",
    title_font="'Century Gothic', 'Verdana', sans-serif", # Thinner, geometric
    branding_svg=DS_BRANDING
)

# 4. Howdy Kitty (Western Cute)
# Branding: Cowboy cats, hearts, and lassos!
HOWDY_BRANDING = """
<image href="../assets/howdy_kitty_branding.png" x="1025" y="25" width="150" height="150" />
"""
THEME_HOWDY_KITTY = Theme(
    name="howdy_kitty",
    bg_color="#FFF0F5",
    card_bg="#FFFFFF",
    text_main="#FF69B4",
    text_sec="#FF1493",
    c_keyword="#FF00FF",
    c_type="#9370DB",
    c_string="#FF6347",
    c_comment="#32CD32",
    c_normal="#FF69B4",
    font_family="'Consolas', 'Monaco', 'Courier New', monospace",
    title_font="'Segoe UI', 'Arial', sans-serif",
    branding_svg=HOWDY_BRANDING
)

# 5. Dassault Systemes / MagicDraw Style
# Based on extracted colors from ViewsInSVG
THEME_DASSAULT = Theme(
    name="dassault",
    bg_color="#FFFFFF",
    card_bg="#DFE1F3", # Light Blue block background
    text_main="#000000",
    text_sec="#555555",
    c_keyword="#000080", # Navy Blue
    c_type="#7F0055",    # Purple-ish
    c_string="#0000FF",  # Blue
    c_comment="#9F530F", # Brown (Note border color)
    c_normal="#000000",
    font_family="'Arial', sans-serif", # Matches SVG font
    title_font="'Arial', sans-serif"
)

THEMES = {
    "light": THEME_LIGHT,
    "dark": THEME_DARK,
    "dark_side": THEME_DARK_SIDE,
    "howdy_kitty": THEME_HOWDY_KITTY,
    "dassault": THEME_DASSAULT
}
