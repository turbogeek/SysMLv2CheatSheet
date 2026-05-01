# SysMLv2 & KerML Standard Libraries Skill

This document instructs the LLM on how to properly leverage and extend the standard domain libraries provided by the SysMLv2 and KerML specifications. When modeling complex systems, performing mathematics, simulating physics, or extending custom data/units, you **MUST** consult this guide.

---

## 1. SysMLv2 Domain Libraries

The SysMLv2 standard provides several domain-specific libraries designed to standardize complex systems engineering constructs.

### 1.1 Systems Model Library (Section 9.2)
- **Purpose**: This library defines SysMLv2 itself. It contains the semantic definitions for all standard language constructs.
- **Usage**: You generally do **not** use this as a traditional library for typing your user models. However, you **must** use it when accessing the model metadata directly, such as when writing `filter` expressions or views.
- **Example**: If you want to filter a view to only show parts, you need the `PartDefinition` element from the Systems library.
```sysml
private import Systems::*;
filter @PartDefinition; 
```

### 1.2 Metadata Domain Library (Section 9.3)
- **Purpose**: Used for understanding, applying, and extending semantic metadata across a model (e.g., Risk, Status, Maturity).
- **Usage**: Import this when you need standard metadata annotations, or when you need to extend a base metadata definition to create your own custom annotations.

### 1.3 Analysis Domain Library (Section 9.4)
- **Purpose**: Provides specific extensions of base elements tailored for analysis cases.
- **Usage**: Import when defining complex `analysis def` blocks. It provides standard analytical variables and constraints that bridge the gap between logical architecture and mathematical solvers.

### 1.4 Cause and Effect Domain Library (Section 9.5)
- **Purpose**: Contains a library model of cause-and-effect relationships and metadata supporting its use.
- **Usage**: Highly useful in general modeling as a traditional library. It aids in the simulation and dynamics of systems, allowing you to explicitly model how an occurrence in one part of the system causes a state change or effect in another.

### 1.5 Geometry Domain Library (Section 9.7)
- **Purpose**: Standardizes spatial and geometric properties.
- **Usage**: You **must** import and use this library when the size, shapes, centers of gravity, edges, bounding boxes, or spatial operational contexts of 3D parts are important to the system definition.

### 1.6 Quantities and Units Domain Library (Section 9.8) - **HIGH PRIORITY**
- **Purpose**: Provides the International System of Quantities (ISQ) and standard SI units. SysMLv2 relies heavily on strong typing for physical properties.
- **Usage**: You **must** import this library to type physical attributes (e.g., `ISQ::mass`, `ISQ::speed`).
- **Extending Units**: When standard units are missing, you must extend the library to create custom units (e.g., milliseconds `[ms]`) or compound units (e.g., `[ducks/m]`).

**Example: Creating custom/compound units**
```sysml
package CustomUnits {
    private import SI::*;
    private import MeasurementReferences::*;

    // 1. Prefix Extension (Milliseconds)
    attribute <ms> millisecond : DurationUnit {
        :>> unitConversion : ConversionByPrefix {
            :>> prefix = milli;
            :>> referenceUnit = s;
        }
    }

    // 2. Base Unit Definition (Ducks)
    attribute <duck> ducks : SimpleUnit {
        doc /* Custom base unit for counting ducks */
        :>> quantityDimension = ISQ::DimensionOne; 
    }

    // 3. Compound Unit (Ducks per meter)
    attribute <'ducks/m'> ducksPerMeter : DerivedUnit {
        :>> unitFactor : UnitFactor[2] {
            unitFactor[1] { :>> unit = duck; :>> exponent = 1; }
            unitFactor[2] { :>> unit = m; :>> exponent = -1; }
        }
    }
}
```

---

## 2. KerML Standard Libraries

KerML (Kernel Modeling Language) provides the foundational data structures and mathematical operations that SysMLv2 runs on.

### 2.1 Semantic Model of KerML (Section 9.2)
- **Purpose**: Defines the core semantic model of KerML.
- **Usage**: Similar to the Systems Model Library, this aids in the extension and usage of deep semantic structures. Use this when writing advanced filters, constraints, and queries where the underlying data structure of the model is manipulated.

### 2.2 Data Type Library (Section 9.3)
- **Purpose**: Defines all primitive types (Real, Integer, Boolean, String) and how data structures are described.
- **Usage**: Import `ScalarValues::*` from this library whenever you are defining raw attributes. This library also defines collections and tuples.

### 2.3 Function Library (Section 9.4) - **HIGH PRIORITY**
- **Purpose**: Provides the built-in behaviors for queries, calculations, string manipulation, and mathematics.
- **Usage**: This library should be used **often**. You do not need to reinvent mathematical formulas or array manipulation.

**Example: Using the Function Library**
```sysml
package FunctionExamples {
    private import ScalarValues::*;
    private import CollectionFunctions::*;
    private import StringFunctions::*;
    private import MathFunctions::*;

    calc def ArrayAnalysis {
        in dataArray : Real[0..*];
        in name : String;
        
        // Use CollectionFunctions
        return dataSize : Integer = size(dataArray);
    }
    
    calc def MathAndString {
        in radius : Real;
        // Use MathFunctions
        attribute area : Real = PI() * (radius ** 2);
        
        // Use StringFunctions
        return label : String = concat("The area is: ", ToString(area));
    }
}
```
*Note: When using standard functions like `size()` or `concat()`, ensure you have imported the corresponding `CollectionFunctions::*` or `StringFunctions::*`.*
