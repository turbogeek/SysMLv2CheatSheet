package Subsetting_Example {
    part def Vehicle {
        part wheels[4];
    }
    
    part def Car :> Vehicle {
        // 'frontWheels' is a specific subset of 'wheels'
        part frontWheels[2] subsets wheels;
        
        // 'rearWheels' is another subset
        part rearWheels[2] subsets wheels;
        
        // Total items in subsets cannot exceed superset multiplicity
    }
}