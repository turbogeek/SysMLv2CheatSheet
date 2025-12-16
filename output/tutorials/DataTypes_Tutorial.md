# Data Types

*Primitives, Values, and Units*

## 1. Standard Primitive Types

SysML v2 provides familiar primitive types in the ScalarValues library:
• **String**: Textual data.
• **Integer**: Whole numbers.
• **Real**: Floating point numbers.
• **Boolean**: True/False flags.

## 2. ISQ Units (Physical Quantities)

For engineering, prefer strongly-typed physical quantities over plain Reals. The ISQ library defines standard quantities and units like `MassValue [kg]`, `LengthValue [m]`, etc.

## 3. Custom Data Types

You can define domain-specific types:
• **attribute def**: A reusable value type definition.
• **struct**: A generalized structured data type.

## 4. Data Types and Values Example

```sysml
package DataTypes_Tutorial {
    import ScalarValues::*;
    import ISQ::*; 

    // --- 1. Custom Value Definitions ---
    // Specializing a primitive
    attribute def IDString :> String;
    
    // Struct for composite data (Kernel level concept often used)
    attribute def Coordinates {
        attribute x : Real;
        attribute y : Real;
        attribute z : Real;
    }

    part def SensorSystem {
        // --- 2. Using Primitives ---
        attribute isActive : Boolean = true;
        attribute firmwareVersion : String = "v1.2.4";
        attribute cycleCount : Integer = 0;
        
        // --- 3. Using ISQ Units ---
        // Type checking ensures you can't assign Mass to Length
        attribute weight : MassValue = 5.5 [kg];
        attribute scanRange : LengthValue = 150 [m];
        
        // Unit conversion is handled by checks (e.g. [km] -> [m])
        attribute speed : SpeedValue = 120 [km/h]; 
        
        // --- 4. Using Custom Types ---
        attribute sensorID : IDString = "SENS-001";
        attribute location : Coordinates {
             :>> x = 10.0;
             :>> y = 20.0;
             :>> z = 0.0;
        }
    }
}
```

