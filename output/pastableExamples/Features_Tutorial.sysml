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