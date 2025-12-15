package CoreTypes_4Integrated {
    import ScalarValues::Real;
    
    scalar def Percent;
    
    item def Fuel;
    
    part def Tank {
        attribute level : Percent; 
        attribute capacity : Real;
    }
    
    part fuelSystem {
        part mainTank : Tank {
            attribute :>> level = 85.5;
            attribute :>> capacity = 50.0;
        }
        
        // Item existing within component
        item currentFuel : Fuel;
    }
}