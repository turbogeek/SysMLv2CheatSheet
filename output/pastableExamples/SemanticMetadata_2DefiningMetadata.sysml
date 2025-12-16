package Vehicle_Metadata {
    private import Vehicle_Library::*;
    private import Metaobjects::SemanticMetadata;

    // Define 'drive' metadata mapping to 'driveTrains' interface
    metadata def drive specializes SemanticMetadata {
        redefines baseType = driveTrains meta SysML::Usage;
        subsets annotatedElement : SysML::InterfaceUsage;
    }
    
    // Define 'engine' metadata mapping to 'engines' part
    metadata def engine specializes SemanticMetadata {
        redefines baseType = engines meta SysML::Usage;
        subsets annotatedElement : SysML::Usage;
    }

    metadata def wheel specializes SemanticMetadata {
        redefines baseType = wheels meta SysML::Usage;
        subsets annotatedElement : SysML::Usage;
    }

    // Define 'vehicle' metadata mapping to 'Vehicle' definition
    metadata def vehicle specializes SemanticMetadata {
        redefines baseType = Vehicle meta SysML::Definition;
        subsets annotatedElement : SysML::Definition;
    }
}