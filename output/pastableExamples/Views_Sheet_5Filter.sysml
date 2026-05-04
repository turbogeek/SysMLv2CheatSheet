package Views {
    private import ScalarValues::*;
    private import SysML::*;
    part def Car;
    part myCar : Car;
    
    view myView {
        expose myCar::**;
        
        /* Keep only Parts */
        filter @PartUsage;
        
        /* Keep only Allocations (CRITICAL: use Usage, not Definition) */
        filter @AllocationUsage;
        
        /* Or exclude specific things (logic depends on library) */
    }
}