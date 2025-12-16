package Car_Example {
    private import Vehicle_Metadata::*;

    // Using the DSL!
    // #vehicle implies 'part def Car :> Vehicle'
    #vehicle def Car {
        
        // #engine implies 'part carEngine :> engines'
        #engine carEngine[1];
        
        #wheel carWheels[4];
        
        // #drive implies 'interface ... :> driveTrains'
        #drive interface connect [1] carEngine.enginePort 
                              to [2] carWheels.wheelPort;
    }
}