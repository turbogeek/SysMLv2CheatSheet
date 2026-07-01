# Variants

*Product Line Engineering*

## 1. Variation Points

Variation points allow you to define configurable elements in a product line.

## 2. Variants

Variants are the concrete options that can fill a variation point.

## 3. Engine Options Example

```sysml
package Variants_Tutorial {
    
    /* abstract definition */
    part def Engine;
    
    /* --- 1. Variants --- */
    part def V6Engine :> Engine;
    part def V8Engine :> Engine;
    part def ElectricMotor :> Engine;
    
    /* --- 2. Variation Point --- */
    part def Car {
        /* 'variation' declares this must be chosen */
        variation part engine : Engine;
    }
    
    /* --- 3. Configuration (Binding) --- */
    /* A specific configuration of the Car */
    part def SportCar :> Car {
        /* Binding the variation point to a specific type */
        variant part redefines engine : V8Engine;
    }
    
    part def EcoCar :> Car {
        variant part redefines engine : ElectricMotor;
    }
}
```

