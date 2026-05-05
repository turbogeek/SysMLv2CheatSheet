package TestFilter {
    part def HardwareComponent;
    part def SoftwareComponent;
    
    metadata def Critical;
    
    part system {
        part cpu : HardwareComponent;
        part os : SoftwareComponent {
            @Critical;
        }
    }
    
    view criticalView {
        filter hastype SoftwareComponent and not @Critical;
    }
}
