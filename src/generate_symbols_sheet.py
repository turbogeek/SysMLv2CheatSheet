import html
import os
from themes import THEMES
import utils

# --- Configuration ---
WIDTH = 1200
HEIGHT = 1800
MARGIN = 30
COL_GAP = 20
ROW_GAP = 20
COL_WIDTH = (WIDTH - (2 * MARGIN) - COL_GAP) / 2

# --- Content ---
def generate_for_theme(theme_key, theme):
    svg = utils.svg_start(WIDTH, HEIGHT, theme)
    
    # Header
    svg += utils.text(WIDTH/2, 60, "SysML v2 / KerML Cheat Sheet: SYMBOLS & ESCAPES", 40, theme.text_main, "bold", "middle", font_family=theme.title_font)
    svg += utils.text(WIDTH/2, 100, f"Theme: {theme.name}", 20, theme.text_sec, "normal", "middle")
    
    col1_x = MARGIN
    col2_x = MARGIN + COL_WIDTH + COL_GAP
    cur_y_c1 = 150
    cur_y_c2 = 150
    
    md_blocks = []
    
    # --- Card 1: Specialization & Subsetting (:>, :>>) ---
    lines_1 = [
        [("part def", theme.c_keyword), (" Car ", theme.c_type), (":> ", theme.c_keyword), ("Vehicle;", theme.c_type), (" /* Specialization (def) */", theme.c_comment)],
        [("part", theme.c_keyword), (" cars ", theme.c_normal), (":> ", theme.c_keyword), ("vehicles;", theme.c_normal), (" /* Subsetting (usage) */", theme.c_comment)],
        [("part", theme.c_keyword), (" :>> ", theme.c_keyword), ("cars [2..4];", theme.c_normal), (" /* Redefinition (usage) */", theme.c_comment)]
    ]
    code_1 = """package Symbols_1SpecializationAndSubsetting {
    private import ScalarValues::*;
    private import SysML::*;

    part def Vehicle;
    /* Definition Specialization */
    part def Car :> Vehicle;

    part def Garage {
        /* Usage Subsetting */
        part vehicles [*];
        part cars :> vehicles;
    }

    part myGarage : Garage {
        /* Usage Redefinition */
        part :>> cars [2..4];
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "1. Inheritance & Redefinition (:>, :>>)", lines_1, "Inheriting definitions and refining usages.", theme, full_code=code_1, sheet_name="Symbols", wrapper_type="structure")
    md_blocks.append(("header", "1. Inheritance & Redefinition (:>, :>>)"))
    md_blocks.append(("text", "`:>` represents **specialization** when applied to definitions, and **subsetting** when applied to usages. `:>>` represents **redefinition** for overriding usage features."))
    md_blocks.append(("code", code_1))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 2: Typing vs Binding (:) & Namespace (::) ---
    lines_2 = [
        [("attribute", theme.c_keyword), (" x ", theme.c_normal), (": ", theme.c_normal), ("ISQ::mass;", theme.c_type), (" /* Namespace/Type */", theme.c_comment)],
        [("accept", theme.c_keyword), (" e ", theme.c_normal), (": ", theme.c_normal), ("Event;", theme.c_type), (" /* Parameter Binding */", theme.c_comment)]
    ]
    code_2 = """package Symbols_2TypingAndNamespace {
    private import ScalarValues::*;
    private import SysML::*;

    /* Namespace qualification using '::' */
    attribute x : ISQ::mass;

    action def ProcessEvent {
        /* Trigger parameter binding using ':' */
        accept e : Event;
    }
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "2. Typing (:) & Namespace (::)", lines_2, "Namespace separation and type declaration.", theme, full_code=code_2, sheet_name="Symbols", wrapper_type="structure")
    md_blocks.append(("header", "2. Typing (:) & Namespace (::)"))
    md_blocks.append(("text", "`::` is the scope/namespace resolution separator. `:` designates the type of a feature in declarations, or binds event parameter values in `accept` trigger actions."))
    md_blocks.append(("code", code_2))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 3: Conjugation & Unary Operator (~) ---
    lines_3 = [
        [("port", theme.c_keyword), (" inputPort ", theme.c_normal), (": ", theme.c_normal), ("~", theme.c_keyword), ("OutputInterface;", theme.c_type)],
        [("/* Conjugation reverses port features directions */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" inv ", theme.c_normal), ("= ", theme.c_normal), ("~", theme.c_keyword), ("val;", theme.c_normal), (" /* Unary Expression */", theme.c_comment)]
    ]
    code_3 = """package Symbols_3ConjugationAndOperators {
    private import ScalarValues::*;
    private import SysML::*;

    port def OutputInterface;
    /* Conjugated port reverses feature directions */
    port inputPort : ~OutputInterface;

    attribute val : Real;
    /* Unary prefix operator (custom meaning) */
    attribute inv = ~val;
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "3. Port Conjugation & Operators (~)", lines_3, "Inverting interfaces and prefix expressions.", theme, full_code=code_3, sheet_name="Symbols", wrapper_type="structure")
    md_blocks.append(("header", "3. Port Conjugation & Operators (~)"))
    md_blocks.append(("text", "`~` denotes a **conjugated** port/interface type (inverting input/out directions) when prefixing a type. It represents a user-defined **unary prefix operator** in data expressions."))
    md_blocks.append(("code", code_3))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Card 4: Range & Null Coalescing (.., ??) ---
    lines_4 = [
        [("part", theme.c_keyword), (" sensors [1..5];", theme.c_normal), (" /* Multiplicity Range */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" currentStatus ", theme.c_normal), ("= ", theme.c_normal), ("status ", theme.c_normal), ("?? ", theme.c_keyword), ('"Unknown";', theme.c_string)],
        [("attribute", theme.c_keyword), (" rangeList ", theme.c_normal), ("= ", theme.c_normal), ("1..10;", theme.c_normal), (" /* Expression Range */", theme.c_comment)]
    ]
    code_4 = """package Symbols_4RangeAndCoalescing {
    private import ScalarValues::*;
    private import SysML::*;

    /* '..' for multiplicity range */
    part sensors [1..5];

    attribute status : String[0..1];
    /* '??' and '..' in expressions */
    attribute currentStatus = status ?? "Unknown";
    attribute rangeList = 1..10;
}"""
    card, h = utils.draw_card(col1_x, cur_y_c1, COL_WIDTH, "4. Range (..) & Null Coalescing (??)", lines_4, "Bounds ranges and default values.", theme, full_code=code_4, sheet_name="Symbols", wrapper_type="structure")
    md_blocks.append(("header", "4. Range (..) & Null Coalescing (??)"))
    md_blocks.append(("text", "`..` is used to define boundaries in both multiplicity ranges (`[1..5]`) and expression range constructors (`1..10`). `??` is the null-coalescing operator in expressions, providing a fallback value."))
    md_blocks.append(("code", code_4))
    svg += card
    cur_y_c1 += h + ROW_GAP

    # --- Column 2 Cards ---

    # --- Card 5: Equality & Assignment (=, :=, ==, ===) ---
    lines_5 = [
        [("attribute", theme.c_keyword), (" val1 ", theme.c_normal), ("= ", theme.c_normal), ("5;", theme.c_string), (" /* Rigid Value Binding */", theme.c_comment)],
        [("bind", theme.c_keyword), (" a.p1 ", theme.c_normal), ("= ", theme.c_normal), ("b.p2;", theme.c_normal), (" /* Connection Equating */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" val2 ", theme.c_normal), (":= ", theme.c_keyword), ("10;", theme.c_string), (" /* Initial Value */", theme.c_comment)],
        [("isEqual ", theme.c_normal), ("= ", theme.c_normal), ("(a ", theme.c_normal), ("== ", theme.c_keyword), ("b);", theme.c_normal), (" /* Value Equality */", theme.c_comment)],
        [("isSame ", theme.c_normal), ("= ", theme.c_normal), ("(a ", theme.c_normal), ("=== ", theme.c_keyword), ("b);", theme.c_normal), (" /* Occurrence Identity */", theme.c_comment)]
    ]
    code_5 = """package Symbols_5EqualityAndAssignment {
    private import ScalarValues::*;
    private import SysML::*;

    attribute val1 = 5; /* Rigid value binding */
    attribute val2 := 10; /* Initial value (re-assignable) */

    action def Compare {
        in attribute a : Integer;
        in attribute b : Integer;
        out attribute isEqual : Boolean;
        out attribute isSame : Boolean;

        /* Value equality (==) vs Identity same (===) */
        isEqual = (a == b);
        isSame = (a === b);
    }
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "5. Bind, Assign, & Equality (=, :=, ==, ===)", lines_5, "Rigid binding, variables, and comparison types.", theme, full_code=code_5, sheet_name="Symbols", wrapper_type="structure")
    md_blocks.append(("header", "5. Bind, Assign, & Equality (=, :=, ==, ===)"))
    md_blocks.append(("text", "`=` specifies a read-only **binding** or equational constraint. `:=` denotes an **initial value** in declarations, or an **assignment** action. `==` tests **value equality**, and `===` tests **occurrence identity** (same lifetime/identity)."))
    md_blocks.append(("code", code_5))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 6: Wildcards & Multiplicity (*, **) ---
    lines_6 = [
        [("import", theme.c_keyword), (" Pkg::*;", theme.c_normal), (" /* Direct Wildcard Import */", theme.c_comment)],
        [("import", theme.c_keyword), (" Pkg::**;", theme.c_normal), (" /* Deep Wildcard Import */", theme.c_comment)],
        [("part", theme.c_keyword), (" passengers [*];", theme.c_normal), (" /* Multiplicity Unrestricted */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" prod ", theme.c_normal), ("= ", theme.c_normal), ("a ", theme.c_normal), ("* ", theme.c_keyword), ("b;", theme.c_normal), (" /* Multiplication */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" pow ", theme.c_normal), ("= ", theme.c_normal), ("a ", theme.c_normal), ("** ", theme.c_keyword), ("3;", theme.c_string), (" /* Exponentiation */", theme.c_comment)]
    ]
    code_6 = """package Symbols_6WildcardsAndMultiplicity {
    private import ScalarValues::*;
    /* Wildcard import: direct members only */
    private import SysML::*;
    /* Recursive import: direct and indirect nested members */
    public import Symbols_6WildcardsAndMultiplicity::**;

    /* Single asterisk: unrestricted upper bound */
    part passengers [*];

    /* Single and double asterisk operators in expressions */
    attribute val1 : Real;
    attribute val2 : Real;
    attribute product = val1 * val2;
    attribute power = val1 ** 3;
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "6. Wildcards & Multiplicity (*, **)", lines_6, "Imports, multiplicities, and math operations.", theme, full_code=code_6, sheet_name="Symbols", wrapper_type="structure")
    md_blocks.append(("header", "6. Wildcards & Multiplicity (*, **)"))
    md_blocks.append(("text", "`*` represents direct member imports, unrestricted upper bounds in multiplicity `[*]`, and multiplication. `**` represents exponentiation in expressions and recursive/deep wildcard imports.\n\n"
                              "**Contrast of Wildcard Imports (`*` vs `**`):**\n"
                              "Using the example of `wheelAssembly` (which contains direct members `tire`, `rim`, `lugNuts`, where `tire` further contains nested members `bead`, `tread`, `sidewall`):\n"
                              "- `import Structure::wheelAssembly::*;` imports only the **direct members** of `wheelAssembly`: `tire`, `rim`, and `lugNuts` (excluding `wheelAssembly` itself and any nested children of `tire`).\n"
                              "- `import Structure::wheelAssembly::**;` is **target-inclusive** and imports the target `wheelAssembly` itself along with **all direct and indirect nested descendants**: `wheelAssembly`, `tire`, `bead`, `tread`, `sidewall`, `rim`, and `lugNuts`."))
    md_blocks.append(("code", code_6))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 7: Annotations & Classification (@, @@) ---
    lines_7 = [
        [("@", theme.c_keyword), ("SafetyLevel { level = 1; }", theme.c_normal), (" /* Meta Annotation */", theme.c_comment)],
        [("part", theme.c_keyword), (" safePart;", theme.c_normal)],
        [("isSafeType ", theme.c_normal), ("= ", theme.c_normal), ("safePart ", theme.c_normal), ("@ ", theme.c_keyword), ("Part;", theme.c_type), (" /* Direct Type Test */", theme.c_comment)],
        [("isSafeMeta ", theme.c_normal), ("= ", theme.c_normal), ("safePart ", theme.c_normal), ("@@ ", theme.c_keyword), ("Part;", theme.c_type), (" /* Metaclass Test */", theme.c_comment)]
    ]
    code_7 = """package Symbols_7AnnotationsAndClassification {
    private import ScalarValues::*;
    private import SysML::*;

    /* Declaring metadata annotation type */
    metadata def SafetyLevel {
        attribute level : Integer;
    }

    /* '@' applied as annotation */
    @SafetyLevel { level = 1; }
    part safePart;

    attribute isSafeType = safePart @ Part; /* '@' used for Type test */
    attribute isSafeMeta = safePart @@ Part; /* '@@' used for Metaclass test */
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "7. Metadata & Classification (@, @@)", lines_7, "Annotations and runtime type checking.", theme, full_code=code_7, sheet_name="Symbols", wrapper_type="structure")
    md_blocks.append(("header", "7. Metadata & Classification (@, @@)"))
    md_blocks.append(("text", "`@` prefixes metadata annotation usages when decorating elements. In expressions, `@` acts as an **instance-of** type test, and `@@` acts as a **metaclass** instance test."))
    md_blocks.append(("code", code_7))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Card 8: Escape Sequences & Literals (', \", \\) ---
    lines_8 = [
        [("part", theme.c_keyword), (" 'left wheel';", theme.c_string), (" /* Unrestricted Name */", theme.c_comment)],
        [("attribute", theme.c_keyword), (" str ", theme.c_normal), ("= ", theme.c_normal), ('"first\\nsecond with \\"quotes\\"";', theme.c_string)],
        [("part", theme.c_keyword), (" 'it\\\'s a name';", theme.c_string), (" /* Escaped Single Quote */", theme.c_comment)]
    ]
    code_8 = """package Symbols_8EscapesAndLiterals {
    private import ScalarValues::*;
    private import SysML::*;

    part 'wheels';
    /* Single quotes escape names with spaces/symbols */
    part 'left wheel' :> 'wheels';

    /* Double quotes wrap string literals */
    attribute str1 = "standard string";

    /* Backslash escapes special characters in strings and names */
    attribute str2 = "first line\\nsecond line with \\"quotes\\" and \\\\backslash";
    part 'it\\\'s a quoted name' :> 'wheels';
}"""
    card, h = utils.draw_card(col2_x, cur_y_c2, COL_WIDTH, "8. Escapes & Literals (', \", \\)", lines_8, "Identifier escaping and string characters.", theme, full_code=code_8, sheet_name="Symbols", wrapper_type="structure")
    md_blocks.append(("header", "8. Escapes & Literals (', \", \\)"))
    md_blocks.append(("text", "Single quotes enclose **unrestricted names** (identifiers with spaces/symbols). Double quotes enclose **string literals**. Backslash `\\` is the escape character inside both. Standard escape sequences include: `\\'` (single quote), `\\\"` (double quote), `\\\\` (backslash), `\\n` (newline), `\\t` (tab), `\\b` (backspace), `\\f` (form feed)."))
    md_blocks.append(("code", code_8))
    svg += card
    cur_y_c2 += h + ROW_GAP

    # --- Legend ---
    svg += utils.draw_legend(WIDTH/2 - 250, HEIGHT - 80, 500, theme)

    svg += utils.svg_end()

    if theme_key == 'light':
        utils.save_markdown("symbols_sheet.md", "Symbols & Escapes Cheat Sheet", "SysML v2 / KerML Syntax Symbols and Escape Sequences", md_blocks, subfolder="cheatsheets")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "..", "output", "svg", theme_key)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "symbols.svg")
    
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    for key, theme in THEMES.items():
        generate_for_theme(key, theme)
