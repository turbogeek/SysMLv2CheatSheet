# Symbols & Escapes Cheat Sheet

*SysML v2 / KerML Syntax Symbols and Escape Sequences*

## 1. Inheritance & Redefinition (:>, :>>)

`:>` represents **specialization** when applied to definitions, and **subsetting** when applied to usages. `:>>` represents **redefinition** for overriding usage features.

```sysml
package Symbols_1SpecializationAndSubsetting {
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
}
```

## 2. Typing (:) & Namespace (::)

`::` is the scope/namespace resolution separator. `:` designates the type of a feature in declarations, or binds event parameter values in `accept` trigger actions.

```sysml
package Symbols_2TypingAndNamespace {
    private import ScalarValues::*;
    private import SysML::*;

    /* Namespace qualification using '::' */
    attribute x : ISQ::mass;

    action def ProcessEvent {
        /* Trigger parameter binding using ':' */
        accept e : Event;
    }
}
```

## 3. Port Conjugation & Operators (~)

`~` denotes a **conjugated** port/interface type (inverting input/out directions) when prefixing a type. It represents a user-defined **unary prefix operator** in data expressions.

```sysml
package Symbols_3ConjugationAndOperators {
    private import ScalarValues::*;
    private import SysML::*;

    port def OutputInterface;
    /* Conjugated port reverses feature directions */
    port inputPort : ~OutputInterface;

    attribute val : Real;
    /* Unary prefix operator (custom meaning) */
    attribute inv = ~val;
}
```

## 4. Range (..) & Null Coalescing (??)

`..` is used to define boundaries in both multiplicity ranges (`[1..5]`) and expression range constructors (`1..10`). `??` is the null-coalescing operator in expressions, providing a fallback value.

```sysml
package Symbols_4RangeAndCoalescing {
    private import ScalarValues::*;
    private import SysML::*;

    /* '..' for multiplicity range */
    part sensors [1..5];

    attribute status : String[0..1];
    /* '??' and '..' in expressions */
    attribute currentStatus = status ?? "Unknown";
    attribute rangeList = 1..10;
}
```

## 5. Bind, Assign, & Equality (=, :=, ==, ===)

`=` specifies a read-only **binding** or equational constraint. `:=` denotes an **initial value** in declarations, or an **assignment** action. `==` tests **value equality**, and `===` tests **occurrence identity** (same lifetime/identity).

```sysml
package Symbols_5EqualityAndAssignment {
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
}
```

## 6. Wildcards & Multiplicity (*, **)

`*` represents direct member imports, unrestricted upper bounds in multiplicity `[*]`, and multiplication. `**` represents exponentiation in expressions and recursive/deep wildcard imports.

**Contrast of Wildcard Imports (`*` vs `**`):**
Using the example of `wheelAssembly` (which contains direct members `tire`, `rim`, `lugNuts`, where `tire` further contains nested members `bead`, `tread`, `sidewall`):
- `import Structure::wheelAssembly::*;` imports only the **direct members** of `wheelAssembly`: `tire`, `rim`, and `lugNuts` (excluding `wheelAssembly` itself and any nested children of `tire`).
- `import Structure::wheelAssembly::**;` is **target-inclusive** and imports the target `wheelAssembly` itself along with **all direct and indirect nested descendants**: `wheelAssembly`, `tire`, `bead`, `tread`, `sidewall`, `rim`, and `lugNuts`.

```sysml
package Symbols_6WildcardsAndMultiplicity {
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
}
```

## 7. Metadata & Classification (@, @@)

`@` prefixes metadata annotation usages when decorating elements. In expressions, `@` acts as an **instance-of** type test, and `@@` acts as a **metaclass** instance test.

```sysml
package Symbols_7AnnotationsAndClassification {
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
}
```

## 8. Escapes & Literals (', ", \)

Single quotes enclose **unrestricted names** (identifiers with spaces/symbols). Double quotes enclose **string literals**. Backslash `\` is the escape character inside both. Standard escape sequences include: `\'` (single quote), `\"` (double quote), `\\` (backslash), `\n` (newline), `\t` (tab), `\b` (backspace), `\f` (form feed).

```sysml
package Symbols_8EscapesAndLiterals {
    private import ScalarValues::*;
    private import SysML::*;

    part 'wheels';
    /* Single quotes escape names with spaces/symbols */
    part 'left wheel' :> 'wheels';

    /* Double quotes wrap string literals */
    attribute str1 = "standard string";

    /* Backslash escapes special characters in strings and names */
    attribute str2 = "first line\nsecond line with \"quotes\" and \\backslash";
    part 'it\'s a quoted name' :> 'wheels';
}
```

