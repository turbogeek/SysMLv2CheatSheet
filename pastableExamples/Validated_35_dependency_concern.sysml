package DependencyTests;

package LibraryPackage {
    part def LibraryComponent;
}

package ApplicationPackage {
    dependency import LibraryPackage::*;
    
    part def Application {
        part lib : LibraryComponent;
    }
}

concern 'Maintainability' {
    doc /* System must be easy to maintain and extend */
}

concern 'Testability' about Application {
    doc /* Application must be testable in isolation */
}

viewpoint def MaintenanceViewpoint {
    concern 'Maintainability';
    concern 'Testability';
}
