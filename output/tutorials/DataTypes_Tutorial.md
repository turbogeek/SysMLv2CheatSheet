# Data Types

*Primitives, Values, and Units*

## 1. Standard Primitive Types

SysML v2 provides familiar primitive types in the ScalarValues library:
• **String**: Textual data.
• **Integer**: Whole numbers.
• **Real**: Floating point numbers.
• **Boolean**: True/False flags.

## 2. ISQ Units (Physical Quantities)

For engineering, using standard quantities is critical. The `SI` library publicly imports `ISQ`. Use `ISQ::mass`, `ISQ::electricCharge`, and `ISQInformation::storageCapacity` for proper type definitions.

## 3. Custom Data Types

You can define domain-specific types:
• **attribute def**: A reusable value type definition.
• **struct**: A generalized structured data type.
• **ProjectUnits**: Explicitly define derived units or use `ConversionByPrefix` (e.g. for `mAh`).

## 4. Data Types and Values Example

```sysml
package DataTypes_Tutorial {
    private import ScalarValues::*;
    /* Note: ISQ is automatically imported by SI (public import) */
    private import SI::kg;
    private import MeasurementReferences::ConversionByPrefix;

    /* --- 1. Custom Value Definitions --- */
    /* Specializing a primitive */
    attribute def IDString :> String;
    
    /* Struct for composite data (Kernel level concept often used) */
    attribute def Coordinates {
        attribute x : Real;
        attribute y : Real;
        attribute z : Real;
    }
    
    /* --- 2. Custom Units --- */
    package ProjectUnits {
        attribute <ms> millisecond : DurationUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = milli;
                :>> referenceUnit = s;
            }
        }
        attribute <'mm/h'> 'millimetre per hour' : SpeedUnit = mm / h;
    }

    part def SensorSystem {
        /* --- 3. Using Primitives --- */
        attribute isActive : Boolean = true;
        attribute firmwareVersion : String = "v1.2.4";
        attribute cycleCount : Integer = 0;
        
        /* --- 4. Using ISQ Units --- */
        /* Type checking ensures you can't assign Mass to Length */
        /* Validating physical properties (Recommended) */
        attribute weight :> ISQ::mass = 5.5 [kg];
        attribute scanRange :> ISQ::length = 150 [m];
        
        /* Raw value storage (Context-free) */
        attribute rawData : MassValue = 10.0 [kg];
        
        /* Unit conversion is handled by checks (e.g. [km] -> [m]) */
        attribute speed :> ISQ::speed = 120 [km/h]; 
        
        /* --- 5. Using Custom Types --- */
        attribute sensorID : IDString = "SENS-001";
        attribute location : Coordinates {
             :>> x = 10.0;
             :>> y = 20.0;
             :>> z = 0.0;
        }
        
        /* Information units require ISQInformation */
        attribute memorySize :> ISQInformation::storageCapacity = 64 [ISQInformation::GB];
        
        /* Battery capacity */
        attribute batteryCapacity :> ISQ::electricCharge = 1500 [ProjectUnits::mAh];
    }
}
```

