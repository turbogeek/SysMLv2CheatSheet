# Structure Cheat Sheet

*Parts, Attributes, Packages*

## 1. Part Definition

Defining structural blocks.

```sysml
package Structure_1PartDefinition {
    private import ScalarValues::*;
    attribute def Mass;
    part def Engine;
    part def Vehicle {
      attribute massOfVehicle : Mass;
      part engine : Engine;
    }
}
```

## 2. Usage & Multiplicity

Instantiating parts with counts.

```sysml
package Structure_2PartUsage {
    private import ScalarValues::*;
    part def Vehicle;
    part def Wheel;
    part car : Vehicle {
      part wheels[4] : Wheel;
      part doors[2..4];
    }
}
```

## 3. Attributes

Data properties of parts.

```sysml
package Structure_3Attributes {
    private import ScalarValues::*;
    attribute def Status {
        attribute code : Integer;
    }
    part ecu {
        attribute id = "ECU-01";
    }
}
```

## 5. Items

Things that flow.

```sysml
package Structure_5Items {
    private import ScalarValues::*;
    item def Fuel;
    item def Gasoline :> Fuel;
    doc /* Items flow through ports */
}
```

## 6. Packages & Imports

Organizing model elements.

```sysml
package Structure_6Packages {
    package VehicleModel {
        private import ScalarValues::*;
        part car;
    }
}
```

## 7. Inheritance (:>)

Specialization of definitions.

```sysml
package Structure_7Inheritance {
    private import ScalarValues::*;
    part def Vehicle;
    part def ElectricCar :> Vehicle {
        part battery;
    }
}
```

## 8. Enumerations

Predefined sets of values.

```sysml
package Structure_8Enumerations {
    private import ScalarValues::*;
    enum def Color {
        Red; Green; Blue;
    }
}
```

