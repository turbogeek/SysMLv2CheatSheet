# Features & Chaining

*Understanding Structure, Behavior, and feature paths*

## 1. What is a Feature?

In SysML v2, almost everything is a Feature. Features describe the characteristics of a defined type. They can be structural (parts, attributes, ports) or behavioral (actions, states).

## 2. Feature Chaining (Dot Notation)

Feature chaining allows you to access deeply nested features without redefining the entire hierarchy. You can 'reach into' a part to constrain or redefine its internal properties using the dot (.) operator.

```sysml
/* Feature Chaining Example */
part :>> engine.mass = 150 [ISQ::kg];
```

## 3. Modifying Features: Subsets vs Redefines

- **Subsetting (subsets)**: Classifies a feature as a member of a broader set. Both sets exist simultaneously.
- **Redefinition (redefines)**: Replaces an inherited feature completely. The original definition is hidden.

## 4. Full Example Code

```sysml
package Feature_Tutorial_Model {
    private import ISQ::*;
    private import SI::*;

    /* --- 1. Base Definitions --- */
    part def Engine {
        attribute horsepower :> ISQ::power;
        attribute mass :> ISQ::mass;
    }

    part def Wheel;

    part def Vehicle {
        part engine : Engine[1];
        part wheels : Wheel[4];
    }

    /* --- 2. Subsetting Example --- */
    part def Truck :> Vehicle {
        /* 'front' and 'rear' partition the 'wheels' set */
        part frontWheels[2] subsets wheels;
        part rearWheels[2] subsets wheels;
    }

    /* --- 3. Redefinition Example --- */
    part def ElectricMotor :> Engine;
    
    part def ElectricCar :> Vehicle {
        /* Replace generic Engine with ElectricMotor */
        part redefines engine : ElectricMotor;
    }

    /* --- 4. Feature Chaining & Redeclaration Example --- */
    part def SportsCar :> Vehicle {
        /* Feature Chaining: reaching into 'engine' */
        /* Redeclaration (:>>) shorthand for 'redefines' or 'subsets' */
        
        attribute :>> engine.horsepower = 500000 [W];
        
        /* This is structurally equivalent to: */
        /* part :>> engine { */
        /* attribute :>> horsepower = 500000 [W]; */
        /* } */
    }
}
```

