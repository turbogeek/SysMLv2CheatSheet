# Parts & Attributes

*Defining Structure and Values*

## 1. Definitions vs Usages

SysML v2 clearly separates definitions (types) from usages (instances).
• **part def**: Defines the blueprint of a structural element.
• **part**: A specific usage of that blueprint within another structure.

## 2. Attributes and Values

Attributes capture data properties like mass, power, or status. You typically use the standard ISQ library for physical quantities.
• **attribute def**: Defines a new value type.
• **attribute**: Holds the actual value.

## 3. Decomposition

Structure is built by nesting parts inside other parts (Composite Structure).

## 4. Spacecraft Example

```sysml
package PartsAndAttributes_Tutorial {
    import ISQ::*; // Import standard units
    
    // --- Definitions ---
    part def Engine {
        attribute maxThrust : ForceValue;
        attribute mass : MassValue;
    }
    
    part def FuelTank {
        attribute capacity : VolumeValue;
    }
    
    // --- Composite Definition ---
    part def Spacecraft {
        // Attributes of the spacecraft itself
        attribute totalMass : MassValue;
        attribute callSign : String;
        
        // Parts (Usages)
        // Decomposing Spacecraft into subsystems
        part mainEngine : Engine {
            // Assigning values to attributes
            attribute :>> maxThrust = 500 [kN];
            attribute :>> mass = 1000 [kg];
        }
        
        part reserveEngine : Engine; // Uses defaults if any
        
        part fuelSystem {
            part loxTank : FuelTank;
            part rp1Tank : FuelTank;
        }
    }
    
    // --- Concrete Instance ---
    part myShip : Spacecraft {
        attribute :>> callSign = "Voyager-1";
    }
}
```

