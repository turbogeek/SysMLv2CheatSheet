# Names & Imports

*Identifiers, Conventions, and Package Management*

## 1. Identifiers

Standard identifiers in SysML v2 are alphanumeric and can include underscores. They must start with a letter or underscore. You can use 'single quotes' to escape any character sequence. Exception: Units in brackets `[ ]` don't need quotes (e.g., `[km/h]`).

## 2. Naming Conventions

- **Definitions (PascalCase)**: CamelCase starting with Uppercase. Used for: part defs, action defs, packages.
- **Usages (camelCase)**: CamelCase starting with lowercase. Used for: parts, actions, attributes.

## 3. Imports

Imports bring elements from other packages into scope.
• standard import: Transitive (publicly exposes imported elements). Example: `SI` libraries publicly import `ISQ` so you get both units and quantities.
• private import: Only visible within the current package.

## 4. Wildcards (* vs **)

• *: Shallow import (imports direct children).
• **: Recursive import (imports everything deeply).
Warning: Avoid ** in production to prevent namespace pollution!

## 5. Aliasing

Use `alias` to create short names for long qualified names. Sytnax: `alias <NewName> for <OldName>;`.

## 6. Comprehensive Example

```sysml
package Naming_Tutorial {
    private import ScalarValues::*;
    private import SI::*;
    private import ISQ::*;
    
    /* --- Library Definitions --- */
    package StandardLibrary {
        part def Widget;
        part def Gadget;
        attribute def Status;
    }
    
    package SpecializedLibrary {
        /* Name collision with StandardLibrary */
        part def Widget; 
    }

    /* --- Imports & Aliasing --- */
    /* Public import: 'StandardLibrary' is visible to users of 'Naming_Tutorial' */
    /* Real-world example: The 'SI' library has 'public import ISQ::*;' */
    public import StandardLibrary::*;
    
    /* Private import to bring it into scope, though we can also just use alias directly */
    private import SpecializedLibrary::Widget;
    
    /* Alias to resolve collision or create short names */
    alias SpecialWidget for SpecializedLibrary::Widget;

    /* --- Definitions & Usages --- */
    part def SystemContext {
        /* Usage of standard import */
        part standardPart : Widget;
        
        /* Usage of aliased element */
        part specialPart : SpecialWidget;
        
        /* Using the alias defined in the package */
        alias SW for SpecialWidget;
        part anotherPart : SW;
        
        /* Escaped identifier for spaces */
        attribute 'System ID' : String;
        
        /* Correct Convention: camelCase usage */
        part mainGadget : Gadget;
        
        /* Unit reference uses brackets after a value, no quotes needed for special chars */
        attribute speed : Real = 100.0 [km/h];
    }
}
```

