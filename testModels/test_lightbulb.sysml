package LightbulbSystem {
    private import ScalarValues::*;
    
    package Requirements {
        requirement def FunctionalRequirement;
        requirement def PerformanceRequirement;
        
        requirement <'REQ-FUNC-01'> 'Provide Illumination' : FunctionalRequirement {
            doc /* The lightbulb shall provide illumination when powered. */
        }
        
        requirement <'REQ-PERF-01'> 'Luminosity Target' : PerformanceRequirement {
            doc /* The lightbulb shall provide at least 800 lumens of light. */
        }
    }
    
    package LogicalArchitecture {
        import Requirements::*;
        
        part def LightSource {
            satisfy 'Provide Illumination';
            satisfy 'Luminosity Target';
        }
        
        part def PowerConverter;
        
        part logicalLightbulb {
            part light : LightSource;
            part power : PowerConverter;
        }
    }
    
    package PhysicalArchitecture {
        import LogicalArchitecture::*;
        
        part def LEDArray;
        part def ACtoDCDriver;
        
        part physicalLightbulb {
            part leds : LEDArray;
            part driver : ACtoDCDriver;
        }
    }
    
    package Allocations {
        import LogicalArchitecture::*;
        import PhysicalArchitecture::*;
        
        allocate physicalLightbulb.leds to logicalLightbulb.light;
        allocate physicalLightbulb.driver to logicalLightbulb.power;
    }
}
