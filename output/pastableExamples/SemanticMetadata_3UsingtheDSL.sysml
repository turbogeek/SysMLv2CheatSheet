package Car_Example {
    private import Vehicle_Metadata::*;
    
    #vehicle def Car {
        #engine carEngine [1];
        #wheel carWheels [4];
        
        #drive interface [1] carEngine.enginePort to [2] carWheels.wheelPort;
    }
}