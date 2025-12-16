package Vehicle_Metadata {
    private import Vehicle_Library::*;
    private import Metaobjects::SemanticMetadata;

    metadata def drive :> SemanticMetadata {
        :>> baseType = driveTrains meta SysML::Usage;
        :> annotatedElement : SysML::InterfaceUsage;
    }
    metadata def engine :> SemanticMetadata {
        :>> baseType = engines meta SysML::Usage;
        :> annotatedElement : SysML::Usage;
    }
    metadata def wheel :> SemanticMetadata {
        :>> baseType = wheels meta SysML::Usage;
        :> annotatedElement : SysML::Usage;
    }
    metadata def vehicle :> SemanticMetadata {
        :>> baseType = Vehicle meta SysML::Definition;
        :> annotatedElement : SysML::Definition;
    }
}