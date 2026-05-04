# Reference Cheat Sheet

*Keywords and Types*

## 1. Common Keywords

Core language definitions.

```sysml
package Reference_1CommonKeywords {
    doc /*
      package, import, private import
      attribute def, attribute
      part def, part
      action def, action
      item def, item
      state def, state
      interface def, port def, port
      connection def, connection
      requirement def, requirement
      constraint def, constraint, assert
      analysis def, analysis
      verification def, verification
      view def, view
      metadata def, metadata
    */
}
```

## 2. Primitive Types

Basic data types.

```sysml
package Reference_2PrimitiveTypes {
    private import ScalarValues::*;
    private import Base::*;
    private import SysML::*;
    attribute b : Boolean; /* true, false */
    attribute i : Integer; /* 1, -5, 0 */
    attribute r : Real; /* 3.14, 1.0 */
    attribute s : String; /* 'text' */
    attribute n : Natural; /* 0, 1, * (UnlimitedNatural in v1) */
}
```

## 3. Relationships

Connecting elements.

```sysml
package Reference_3Relationships {
    doc /*
      Generalization ( :> ) - Inheritance
      Subsetting ( :> ) - Hierarchy
      Redefinition ( :>> ) - Specialized replacement
      Reference ( references ) - Pointer
      Conjugation ( ~ ) - Reverse port
      Binding ( = ) - Equality
      Assignment ( := ) - Value set
      Succession ( first..then ) - Ordering
    */
}
```

## 4. Comments

Annotating code.

```sysml
package Reference_4Comments {
    /* Single line */
    /* Multi-line
       comment */
    doc /* Documentation */
    /* Single line */
    /* Multi-line
       comment */
    doc /* Documentation */
    part element;
    comment about element /* text */
}
```

## 5. Multiplicity

Cardinality & Ordering.

```sysml
package Reference_5Multiplicity {
    doc /*
      [1]      - Exactly one (Default)
      [0..1]   - Optional
      [*]      - Zero or more
      [1..*]   - One or more
      [2..5]   - Specific range
    */
}
```

## 6. Visibility

Access control.

```sysml
package Reference_6Visibility {
    doc /*
      public    (default) - Visible everywhere
      private   (private) - Visible only inside
      protected (protected) - Visible to children
    */
}
```

