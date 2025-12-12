package Metadata_5Extension {
    private import ScalarValues::*;
    private import SysML::*;
    
    doc /* Base metadata */
    metadata def TestPlan {
        attribute tool : String;
    }
    
    doc /* Extended metadata (Inheritance) */
    metadata def LabTest :> TestPlan {
        attribute labId : String;
    }
    
    metadata def VRTest :> TestPlan {
        attribute headsetModel : String;
    }
    
    doc /* Usage with values */
    action runUnitTests {
        @LabTest {
            :>> tool = "JUnit";
            :>> labId = "Lab-101";
        }
    }
    
    action runSimTest {
        @VRTest {
            :>> tool = "Unity";
            :>> headsetModel = "Quest 3";
        }
    }
}