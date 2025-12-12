package Metadata_6Hashtags {
    private import ScalarValues::*;
    private import SysML::*;
    
    package Vehicle_Metadata {
        metadata def Vehicle;
        metadata def Engine;
        metadata def Wheel;
    }
    package Car_Example {
        private import Vehicle_Metadata::*;
        
        #Vehicle def Car {
            #Engine part carEngine [1];
            #Wheel part carWheels [4];
        }
    }
}