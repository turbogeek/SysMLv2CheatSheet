package Redefinition_Example {
    part def Vehicle {
        part engine : Engine;
    }
    
    part def ElectricCar :> Vehicle {
        // Replace the generic Engine with an ElectricMotor
        // Multiplicity or Type can change
        part redefines engine : ElectricMotor;
    }
    
    part def ElectricMotor :> Engine;
    part def Engine;
}