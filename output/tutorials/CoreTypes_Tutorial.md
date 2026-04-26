# Core Types

*Parts, Items, Attributes, and Enumerations*

## 1. Parts vs Items

SysML v2 distinguishes between physical/logical structure and information/flow.
• **part**: Has mass, energy, or spatial extent (e.g., Engine, Server).
• **item**: Represents distinct headers or mass that flows (e.g., Water, DataMessage).

## 2. Attributes & Scalars

Attributes store data values within definitions.
• **attribute def**: Defines a reusable data type.
• **attribute**: A usage of a definition holding a value.

## 3. Enumerations

Enumerations define a fixed set of literals. Useful for states, modes, or configuration options.

## 4. Core Types Example

```sysml
package CoreTypes_Tutorial {
    private import ScalarValues::*;
    
    /* --- 1. Enumerations --- */
    enum def Status {
        enum Active;
        enum Idle;
        enum Error;
    }

    /* --- 2. Attributes & Scalars --- */
    attribute def MassValue :> Real;
    
    /* --- 3. Parts (Structure) --- */
    part def StorageTank {
        attribute capacity : MassValue = 1000.0;
        attribute currentStatus : Status = Status::Idle;
    }

    /* --- 4. Items (Flow/Substance) --- */
    item def Water;
    
    part def WaterSystem {
        part tank1 : StorageTank;
        part tank2 : StorageTank;
        
        /* Items flow or are stored */
        item storedWater : Water;
    }
}
```

