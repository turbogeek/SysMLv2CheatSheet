# Names & Imports

*Identifiers, Conventions, and Package Management*

## 1. Identifiers

Standard identifiers in SysML v2 are alphanumeric and can include underscores. They must start with a letter or underscore. You can use 'single quotes' to escape any character sequence.

## 2. Naming Conventions

- **Definitions (PascalCase)**: CamelCase starting with Uppercase. Used for: part defs, action defs, packages.
- **Usages (camelCase)**: CamelCase starting with lowercase. Used for: parts, actions, attributes.

## 3. Imports

Imports bring elements from other packages into scope.
• standard import: Transitive (visible to importers of this package).
• private import: Only visible within this file/package.

## 4. Wildcards (* vs **)

• *: Shallow import (imports direct children).
• **: Recursive import (imports everything deeply).
Warning: Avoid ** in production to prevent namespace pollution!

## 5. Aliasing

Use 'as' to rename imports, resolving conflicts or shortening names.

## 6. Comprehensive Example

```sysml
package Naming_Tutorial {
    // --- Library Definitions ---
    package StandardLibrary {
        part def Widget;
        part def Gadget;
        attribute def Status;
    }
    
    package SpecializedLibrary {
        // Name collision with StandardLibrary
        part def Widget; 
    }

    // --- Imports & Aliasing ---
    // Public import: 'StandardLibrary' is visible to users of 'Naming_Tutorial'
    import StandardLibrary::*;
    
    // Private import: Resolving collision with alias
    private import SpecializedLibrary::Widget as SpecialWidget;

    // --- Definitions & Usages ---
    part def SystemContext {
        // Usage of standard import
        part standardPart : Widget;
        
        // Usage of aliased import
        part specialPart : SpecialWidget;
        
        // Escaped identifier for spaces
        attribute 'System ID' : String;
        
        // Correct Convention: camelCase usage
        part mainGadget : Gadget;
    }
}
```

