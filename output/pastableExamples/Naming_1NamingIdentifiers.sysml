package Naming_1Identifiers {
    part def VehiclePart;      // PascalCase for Definitions
    part myEngine : VehiclePart; // camelCase for Usages
    
    // Escaped identifiers for special chars or keywords
    part '123-Start'; 
    part 'Space Name';
    
    // Avoid name collisions with keywords
    // part type; // Error: 'type' is reserved
}