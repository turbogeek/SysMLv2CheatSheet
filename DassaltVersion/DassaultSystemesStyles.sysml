library package <DS_Styles> DassaultSystemesStyles {
    package CoreStylesComponents {
        package KerMLStyles {
            private import ScalarValues::Boolean;
            private import ScalarValues::Integer;
            private import ScalarValues::String;
            private import ScalarValues::Real;
            metadata def InvisibleInDialog;
            attribute def Color :> String;
            attribute def Font :> String;
            enum def PathStyleEnum {
                Rectilinear;
                Oblique;
                Bezier;
            }
            enum def OrientationEnum {
                Horizontal;
                Vertical;
            }
            enum def LineStyleEnum {
                Solid;
                Dashed;
                Dotted;
                DenselyDotted;
                DenselyDashed;
                LooselyDashed;
                ModeratelyDashed;
                EvenlyDashed;
                DashedDotted;
                LongDashedDotted;
                LongDashedDashed;
                DashedDoubleDotted;
                LongDashedDoubleDotted;
                LongDashedDoubleDashed;
                DoubleDashedDotted;
                DoubleDashedDoubleDotted;
            }
            enum def TextVerticalPositionEnum {
                Top;
                Center;
                Bottom;
            }
            enum def TextHorizontalPositionEnum {
                Left;
                Center;
                Right;
            }
            view def SymbolStyle {
                attribute lineWidth : Integer default 1 {
                    doc locale "en" /* Specify the width of the symbol's outline.*/
                    doc locale "de" /* Geben Sie die Linienbreite des Symbols an. */
                }
                attribute fillColor : Color default "#FFF0F0F0" {
                    doc /* Specify the color of the symbol's header. */
                }
                attribute useFillColor : Boolean default true {
                    doc /* Specify whether to use a specific color for the symbol's header.*/
                }
                attribute penColor : Color default "#FF424242" {
                    doc /* Specify the color of the symbol's outline.*/
                }
                attribute textColor : Color default "#000000" {
                    doc /* Specify the color of the symbol's text.*/
                }
                attribute font : Font default "Roboto,0,11" {
                    doc /* Specify the font style of the symbol's text.*/
                }
                attribute wrap : Boolean default false {
                    doc /* Specify whether the text should wrap to fit the width of the element symbol.*/
                }
            }
            view def ShapeStyle :> SymbolStyle {
                attribute contentFillColor : Color default "#FFFFFFFF" {
                    doc /* Specify the color of the symbol's body.*/
                }
                attribute textVerticalPosition : TextVerticalPositionEnum default textVerticalPosition::Top {
                    doc /* Specify the element name position for the symbol. */
                }
                attribute compartmentFillColor : Color default "#FFF0F0F0";
                attribute compartmentTextColor : Color default "#000000";
            }
            view def SymbolicViewStyle :> SymbolStyle {
                attribute useGradientFill : Boolean default false;
            }
            view def BarShapeStyle :> ShapeStyle {
                attribute orientation : OrientationEnum default orientation::Horizontal {
                    doc /* Specify the orientation for the symbol. */
                }
            }
            view def ShapeOnBorderStyle :> SymbolStyle;
            view def PathStyle :> SymbolStyle {
                attribute pathStyle : PathStyleEnum default pathStyle::Rectilinear {
                    doc /* Specify the style of the path. */
                }
            }
            view def ElementStyle {
                attribute showShortName : Boolean default true {
                    doc /* Specify whether the element's declared short name should be displayed on the element symbol.*/
                }
                attribute showName : Boolean default true {
                    doc /* Specify whether the element's declared name should be displayed on the element symbol.*/
                }
            }
            view def ElementTrimmableTextStyle :> ElementStyle {
                attribute showFullText : Boolean default false {
                    doc /* Specify whether element values should be displayed in full or abbreviated. Modifying this property affects the values displayed in both the selected symbol's name and its compartments. Modifying this property does not affect element values displayed in the metadata compartment. */
                }
            }
            view def TypeStyle :> ElementTrimmableTextStyle {
                attribute showSpecialization : Boolean default true {
                    doc /* Specify whether the specialization textual symbols should be displayed in the element name (e.g., the textual symbol :> or the keyword specializes, in the case of subclassification).  */
                }
                attribute showQualifiedNameForSpecialization : Boolean default false {
                    doc /* Specify whether the specialization's full qualified name should be displayed in the element name. */
                }
                attribute showModifiers : Boolean default true {
                    doc /* Specify whether the element's modifiers (e.g., in, ref, abstract, etc.) should be displayed on the element symbol. The property does not control the individual and portion kind (timeslice, snapshot) modifiers.*/
                }
            }
            view def BasicFeatureStyle :> TypeStyle {
                attribute showValue : Boolean default false {
                    doc /* Specify whether the element's defined value should be displayed.*/
                }
            }
            view def ConnectorStyle :> BasicFeatureStyle {
                attribute showPayload : Boolean default true {
                    doc /* Specify whether the payload name and sign should be displayed on the connector path. */
                }
            }
            view def FeatureStyle :> BasicFeatureStyle {
                attribute showInheritedSign : Boolean default true {
                    doc /* Specify whether the inherited sign should be displayed on the symbol. */
                }
            }
            view def CompartmentStyle {
                attribute showCompartment : Boolean default true {
                    doc /* Specify whether the compartment should be displayed or suppressed.*/
                }
            }
            view def BasicFeatureCompartmentStyle :> CompartmentStyle, BasicFeatureStyle;
            view def FeatureCompartmentStyle :> BasicFeatureCompartmentStyle, FeatureStyle {
                attribute showInherited : Boolean default false {
                    doc /* Specify whether the inherited elements should be displayed on the symbol.*/
                }
            }
            view def ImageShapeStyle :> ShapeStyle;
            view def TextBoxStyle :> ShapeStyle;
            view def SeparatorStyle :> SymbolStyle {
                attribute textHorizontalPosition : TextHorizontalPositionEnum default textHorizontalPosition::Left {
                    doc /* Specify the text position for the vertical and horizontal separator symbols.*/
                }
                attribute lineStyle : LineStyleEnum default lineStyle::Dashed {
                    doc /* Specify the line style for the vertical and horizontal separator symbols. */
                }
            }
            view def LinearSeparatorStyle :> SeparatorStyle {
                attribute orientation : OrientationEnum default orientation::Horizontal {
                    doc /* Specify the orientation for the symbol. */
                }
            }
            view def RectangularShapeStyle :> SeparatorStyle, TextBoxStyle {
                attribute isRounded : Boolean default true {
                    doc /* Specify whether the rectangular shape symbol's corners should be rounded. */
                }
            }
        }
        package SysMLStyles {
            private import KerMLStyles::*;
            private import ScalarValues::Boolean;
            view def SwimlanesStyle :> ShapeStyle;
            view def MetadataCompartmentStyle :> CompartmentStyle, ElementTrimmableTextStyle;
            view def FeaturesOfMetadataCompartmentStyle :> CompartmentStyle, ElementTrimmableTextStyle;
            view def DocumentationCompartmentStyle :> CompartmentStyle, ElementTrimmableTextStyle;
            view def SubjectCompartmentStyle :> FeatureCompartmentStyle;
            view def ActorsCompartmentStyle :> FeatureCompartmentStyle;
            view def StakeholdersCompartmentStyle :> FeatureCompartmentStyle;
            view def ObjectiveCompartmentStyle :> BasicFeatureCompartmentStyle;
            view def IncludeUseCasesCompartmentStyle :> FeatureCompartmentStyle;
            view def AttributesCompartmentStyle :> FeatureCompartmentStyle;
            view def ParametersCompartmentStyle :> FeatureCompartmentStyle;
            view def PerformActionsCompartmentStyle :> FeatureCompartmentStyle;
            view def SatisfyRequirementsCompartmentStyle :> FeatureCompartmentStyle;
            view def ItemsCompartmentStyle :> FeatureCompartmentStyle;
            view def ActionsCompartmentStyle :> FeatureCompartmentStyle;
            view def ExhibitStatesCompartmentStyle :> FeatureCompartmentStyle;
            view def ConstraintsCompartmentStyle :> FeatureCompartmentStyle;
            view def RequireCompartmentStyle :> FeatureCompartmentStyle;
            view def AssumeCompartmentStyle :> FeatureCompartmentStyle;
            view def AssertCompartmentStyle :> FeatureCompartmentStyle;
            view def FramesCompartmentStyle :> FeatureCompartmentStyle;
            view def EnumsCompartmentStyle :> BasicFeatureCompartmentStyle;
            view def EndsCompartmentStyle :> FeatureCompartmentStyle;
            view def PartsCompartmentStyle :> FeatureCompartmentStyle;
            view def PortsCompartmentStyle :> FeatureCompartmentStyle;
            view def WhileConditionCompartmentStyle :> CompartmentStyle, ElementTrimmableTextStyle;
            view def UntilConditionCompartmentStyle :> CompartmentStyle, ElementTrimmableTextStyle;
            view def ForIterationCompartmentStyle :> CompartmentStyle, ElementTrimmableTextStyle;
            view def IfConditionCompartmentStyle :> CompartmentStyle, ElementTrimmableTextStyle;
            view def MembersCompartmentStyle :> CompartmentStyle, TypeStyle {
                attribute showOnlyOwned : Boolean default true {
                    doc /* Specify whether only the owned elements or imported ones, too, should be displayed in the symbol compartment.*/
                }
            }
            view def StyleSheetRulesCompartmentStyle :> FeatureCompartmentStyle;
        }
        package Predicates {
            abstract part def Condition;
            part def ByElementMetaclassCondition :> Condition {
                ref item elementMetaclass [1..*] : Metaobjects::Metaobject;
            }
            part def ByMetadataAnnotationCondition :> Condition {
                ref item annotatingMetadataType [1..*] : Metaobjects::Metaobject;
            }
            part def ByDiagramTypeCondition :> Condition {
                ref item diagramType [1..*] : Metaobjects::Metaobject;
            }
            part def FreeFormCondition :> Condition {
                calc test {
                    in element : Metaobjects::Metaobject;
                    in diagram : Metaobjects::Metaobject;
                    return : ScalarValues::Boolean;
                }
            }
        }
        part def Policy {
            part rule [*];
        }
        part def StyleSheet :> Policy {
            part styleSheetCondition : Predicates::Condition;
            part :>> rule [*] {
                part condition : Predicates::Condition;
                part style;
            }
        }
        part def StyleConfiguration {
            part activeStyleSheets : StyleSheet [*];
        }
    }
    package StyleSheets {
        private import CoreStylesComponents::*;
        private import Predicates::*;
        private import ColorDefinitions::*;
        private import CompartmentVisibilityDefinitions::*;
        private import KerMLStyles::*;
        private import SysMLStyles::*;
        part def DefaultStyleSheet :> StyleSheet {
            /* ---------VIEW---------- */
            part viewRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::ViewUsage.metadata, SysML::Systems::ViewDefinition.metadata);
                }
                view :>> style : AbstractLightBlueStyle;
            }
            /* -------------PART/PORT---------*/
            part partPortRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::PartUsage.metadata, SysML::Systems::PartDefinition.metadata, SysML::Systems::PortUsage.metadata,
                                                     SysML::Systems::PortDefinition.metadata);
                }
                view :>> style : AbstractGreenStyle;
            }
            part partPortShapeOnBorderRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::PartUsage.metadata, SysML::Systems::PortUsage.metadata);
                }
                view :>> style : AbstractGreenOnBorderStyle, FeatureStyle {
                    #InvisibleInDialog attribute :>> showModifiers;
                }
            }
            /* -------------USE CASE---------*/
            part useCaseRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::UseCaseUsage.metadata, SysML::Systems::UseCaseDefinition.metadata);
                }
                view :>> style : AbstractDeepOrangeStyle {
                    part parameterCompartment : ParametersCompartmentStyle {
                        attribute :>> showCompartment default false;
                    }
                }
            }
            /* -----LITERAL EXPRESSIONS---------*/
            part literalExpressionRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = KerML::Kernel::LiteralExpression.metadata;
                }
                view :>> style : AbstractRedStyle;
            }
            /* -------------CALC---------*/
            part calculationRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::CalculationUsage.metadata, SysML::Systems::CalculationDefinition.metadata);
                }
                view :>> style : AbstractCyanStyle;
            }
            /* ------STATE-------- */
            part stateRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::StateUsage.metadata, SysML::Systems::StateDefinition.metadata,
                                                     SysML::Systems::ExhibitStateUsage.metadata);
                }
                view :>> style : AbstractDeepOrangeStyle {
                    part actionsCompartment : ActionsCompartmentStyle {
                        attribute :>> showCompartment default true;
                    }
                }
            }
            part transitionAsPathRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::TransitionUsage.metadata;
                }
                view :>> style : PathStyle, ConnectorStyle {
                    #InvisibleInDialog attribute :>> showName;
                    #InvisibleInDialog attribute :>> showShortName;
                    #InvisibleInDialog attribute :>> showSpecialization;
                    #InvisibleInDialog attribute :>> showQualifiedNameForSpecialization;
                    #InvisibleInDialog attribute :>> showModifiers;
                    #InvisibleInDialog attribute :>> showValue;
                    #InvisibleInDialog attribute :>> showPayload;
                    #InvisibleInDialog attribute :>> showFullText;
                }
            }
            part transitionAsShapeRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::TransitionUsage.metadata;
                }
                view :>> style : ShapeStyle, FeatureStyle {
                    #InvisibleInDialog attribute :>> showValue;
                    #InvisibleInDialog attribute :>> showFullText;
                }
            }
            /* -------------ACTION---------*/
            part doneRule :> rule {
                part :>> condition : FreeFormCondition {
                    calc :>> test {
                        element == done.metadata
                    }
                }
                view :>> style : SymbolStyle, FeatureStyle {
                    attribute :>> fillColor default "#FFFFFF";
                    #InvisibleInDialog attribute :>> textColor;
                    #InvisibleInDialog attribute :>> font;
                    #InvisibleInDialog attribute :>> wrap;
                    #InvisibleInDialog attribute :>> showShortName;
                    #InvisibleInDialog attribute :>> showName;
                    #InvisibleInDialog attribute :>> showFullText;
                    #InvisibleInDialog attribute :>> showSpecialization;
                    #InvisibleInDialog attribute :>> showQualifiedNameForSpecialization;
                    #InvisibleInDialog attribute :>> showModifiers;
                    #InvisibleInDialog attribute :>> showValue;
                    #InvisibleInDialog attribute :>> showInheritedSign;
                }
            }
            part startRule :> rule {
                part :>> condition : FreeFormCondition {
                    calc :>> test {
                        element == start.metadata
                    }
                }
                view :>> style : SymbolStyle, FeatureStyle {
                    #InvisibleInDialog attribute :>> fillColor;
                    #InvisibleInDialog attribute :>> useFillColor;
                    #InvisibleInDialog attribute :>> textColor;
                    #InvisibleInDialog attribute :>> font;
                    #InvisibleInDialog attribute :>> wrap;
                    #InvisibleInDialog attribute :>> showShortName;
                    #InvisibleInDialog attribute :>> showName;
                    #InvisibleInDialog attribute :>> showFullText;
                    #InvisibleInDialog attribute :>> showSpecialization;
                    #InvisibleInDialog attribute :>> showQualifiedNameForSpecialization;
                    #InvisibleInDialog attribute :>> showModifiers;
                    #InvisibleInDialog attribute :>> showValue;
                    #InvisibleInDialog attribute :>> showInheritedSign;
                }
            }
            part terminateActionRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::TerminateActionUsage.metadata;
                }
                view :>> style : SymbolStyle, FeatureStyle {
                    attribute :>> fillColor default "#FFFFFF";
                    #InvisibleInDialog attribute :>> showFullText;
                    #InvisibleInDialog attribute :>> showValue;
                    #InvisibleInDialog attribute :>> showModifiers;
                }
            }
            part forkJoinUsageRule :> rule {
                view :>> style : BarShapeStyle, FeatureStyle {
                    #InvisibleInDialog attribute :>> fillColor default "#FFFFFF";
                    #InvisibleInDialog attribute :>> useFillColor;
                    attribute :>> fillColor default "#FFFFFF";
                    attribute :>> textColor default "#000000";
                    attribute :>> penColor default "#424242";
                    #InvisibleInDialog attribute :>> contentFillColor;
                    #InvisibleInDialog attribute :>> showFullText;
                    #InvisibleInDialog attribute :>> showModifiers;
                    #InvisibleInDialog attribute :>> showValue;
                }
            }
            part mergeDecideRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::DecisionNode.metadata, SysML::Systems::MergeNode.metadata);
                }
                view :>> style : SymbolStyle, FeatureStyle {
                    attribute :>> fillColor default "#FFFFFF";
                    #InvisibleInDialog attribute :>> showFullText;
                    #InvisibleInDialog attribute :>> showModifiers;
                    #InvisibleInDialog attribute :>> showValue;
                }
            }
            part actionUsageRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::PerformActionUsage.metadata, SysML::Systems::ActionUsage.metadata);
                }
                view :>> style : AbstractOrangeStyle;
            }
            part actionDefRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::ActionDefinition.metadata;
                }
                view :>> style : AbstractOrangeStyle {
                    part parametersCompartment : ParametersCompartmentStyle {
                        attribute :>> showCompartment default true;
                    }
                }
            }
            /* -------------ENUM---------*/
            part enumRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::EnumerationDefinition.metadata, SysML::Systems::EnumerationUsage.metadata);
                }
                view :>> style : AbstractDeepPurpleStyle, TypeStyle {
                    #InvisibleInDialog attribute :>> showModifiers;
                }
            }
            /* -------------ATTRIBUTE---------*/
            part attributeRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::AttributeUsage.metadata, SysML::Systems::AttributeDefinition.metadata);
                }
                view :>> style : AbstractDeepPurpleStyle;
            }
            part attributeUsageShapeOnBorderRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::AttributeUsage.metadata;
                }
                view :>> style : AbstractOrangeOnBorderStyle, FeatureStyle {
                    #InvisibleInDialog attribute :>> showModifiers;
                }
            }
            /* -------------REFERENCE---------*/
            part referenceUsageRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::ReferenceUsage.metadata;
                }
                view :>> style : AbstractOrangeStyle;
            }
            part referenceShapeOnBorderRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::ReferenceUsage.metadata;
                }
                view :>> style : AbstractOrangeOnBorderStyle, FeatureStyle {
                    #InvisibleInDialog attribute :>> showModifiers;
                }
            }
            /* -------------CONCERN---------*/
            part concernRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::ConcernUsage.metadata, SysML::Systems::ConcernDefinition.metadata);
                }
                view :>> style : AbstractRedStyle;
            }
            /* -------------REQUIREMENT---------*/
            part requirementRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::RequirementUsage.metadata, SysML::Systems::RequirementDefinition.metadata);
                }
                view :>> style : AbstractPinkStyle {
                    part attributesCompartment : AttributesCompartmentStyle {
                        attribute :>> showCompartment default true;
                    }
                    part documentationCompartmentStyle : DocumentationCompartmentStyle {
                        attribute :>> showCompartment default true;
                    }
                }
            }
            part metadataRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::MetadataUsage.metadata, SysML::Systems::MetadataDefinition.metadata);
                }
            }
            /* -------------ITEM---------*/
            part itemRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::ItemUsage.metadata, SysML::Systems::ItemDefinition.metadata);
                }
                view :>> style : AbstractRedStyle;
            }
            part itemShapeOnBorderRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::ItemUsage.metadata;
                }
                view :>> style : AbstractOrangeOnBorderStyle, FeatureStyle {
                    #InvisibleInDialog attribute :>> showModifiers;
                }
            }
            /* -------------CONSTRAINT---------*/
            part constraintRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::ConstraintUsage.metadata, SysML::Systems::ConstraintDefinition.metadata,
                                                     KerML::Kernel::OperatorExpression.metadata);
                }
                view :>> style : AbstractBlueStyle;
            }
            /* -------------OCCURRENCE---------*/
            part occurrenceRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (SysML::Systems::EventOccurrenceUsage.metadata, SysML::Systems::OccurrenceUsage.metadata,
                                                     SysML::Systems::OccurrenceDefinition.metadata);
                }
                view :>> style : AbstractYellowStyle;
            }
            /* -------------PACKAGE---------*/
            part packageRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = KerML::Kernel::Package.metadata;
                }
                view :>> style : AbstractIndigoStyle, HideAllCompartments {
                    part :>> metadataCompartment {
                        attribute :>> showCompartment default true;
                        attribute :>> showFullText default true;
                    }
                }
            }
            /* -------------SWIMLANES---------*/
            part swimlaneRule :> rule {
                view :>> style : SwimlanesStyle, HideAllCompartments {
                    attribute :>> fillColor default "#D9EEDA";
                    attribute :>> penColor default "#123D15";
                    attribute :>> lineWidth default 1;
                    attribute :>> textColor default "#000000";
                    part :>> metadataCompartment {
                        :>> showCompartment default true;
                        :>> showFullText default true;
                    }
                }
            }
            /* --------------ANNOTATION ELEMENT------------------- */
            part repRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = KerML::Root::TextualRepresentation.metadata;
                }
                view :>> style : AbstractGreyStyle {
                    #InvisibleInDialog attribute :>> contentFillColor;
                }
            }
            part docRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = KerML::Root::Documentation.metadata;
                }
                view :>> style : AbstractWhiteStyle {
                    attribute :>> wrap default true;
                    #InvisibleInDialog attribute :>> contentFillColor;
                }
            }
            part commentRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = KerML::Root::Comment.metadata;
                }
                view :>> style : AbstractYellowStyle {
                    attribute :>> wrap default true;
                    #InvisibleInDialog attribute :>> contentFillColor;
                }
            }
            /* -----------------TEXTBOX-------------*/
            part textBoxRule :> rule {
                part :>> style : TextBoxStyle {
                    attribute :>> useFillColor default false;
                    #InvisibleInDialog attribute :>> contentFillColor;
                }
            }
            /* -----------------SEPARATORS------------- */
            part separatorRule :> rule {
                view :>> style : SeparatorStyle {
                    attribute :>> useFillColor default false;
                }
            }
            /* -------CLASSIFIER-------- */
            part classifierRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = KerML::Core::Classifier.metadata;
                }
                view :>> style : AbstractAmberStyle;
            }
            /* --------NAMESPACE------- */
            part namespaceRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = KerML::Root::Namespace.metadata;
                }
                view :>> style : AbstractYellowStyle;
            }
            part shapeRule :> rule {
                view :>> style : ShapeStyle {
                    attribute :>> lineWidth default 1;
                }
            }
            part pathRule :> rule {
                view :>> style : PathStyle {
                    attribute :>> useFillColor default false;
                }
            }
            /* -----Removing from styles UI-------- */
            part removePropertiesPathsRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = (KerML::Root::Annotation.metadata, KerML::Root::Membership.metadata, KerML::Core::Specialization.metadata);
                }
                view :>> style : PathStyle, ElementStyle {
                    #InvisibleInDialog attribute :>> showShortName;
                    #InvisibleInDialog attribute :>> showName;
                    #InvisibleInDialog attribute :>> fillColor;
                    #InvisibleInDialog attribute :>> useFillColor;
                    #InvisibleInDialog attribute :>> textColor;
                    #InvisibleInDialog attribute :>> font;
                    #InvisibleInDialog attribute :>> wrap;
                }
            }
            part removePropertiesImportRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = KerML::Root::Import.metadata;
                }
                view :>> style : PathStyle, ElementStyle {
                    #InvisibleInDialog attribute :>> showShortName;
                    #InvisibleInDialog attribute :>> showName;
                    #InvisibleInDialog attribute :>> fillColor;
                    #InvisibleInDialog attribute :>> useFillColor;
                }
            }
            /* -----------suppress compartment rules for usage/definition---------- */
            part usageRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::Usage.metadata;
                }
                view :>> style : UsagesAndDefCompartments;
            }
            part definitionRule :> rule {
                part :>> condition : ByElementMetaclassCondition {
                    ref item :>> elementMetaclass = SysML::Systems::Definition.metadata;
                }
                view :>> style : UsagesAndDefCompartments;
            }
        }
        part def BlackAndWhiteStyleSheet :> DefaultStyleSheet {
            part shapeRuleBW :> rule {
                view :>> style : AbstractWhiteStyle;
            }
            part shapeOnBorderBW :> rule {
                view :>> style : AbstractWhiteOnBorderStyle;
            }
        }
        package ColorDefinitions {
            view def AbstractGreenStyle :> ShapeStyle {
                attribute :>> fillColor default "#E3F2E3";
                attribute :>> compartmentFillColor default "#F6FBF6";
                attribute :>> penColor default "#123D15";
            }
            view def AbstractGreenOnBorderStyle :> ShapeOnBorderStyle {
                attribute :>> fillColor default "#D9EEDA";
                attribute :>> penColor default "#123D15";
            }
            view def AbstractDeepOrangeStyle :> ShapeStyle {
                attribute :>> fillColor default "#FFE3DA";
                attribute :>> compartmentFillColor default "#FDF6F5";
                attribute :>> penColor default "#7C2308";
            }
            view def AbstractLightBlueStyle :> ShapeStyle {
                attribute :>> fillColor default "#D4F1FE";
                attribute :>> compartmentFillColor default "#F3FBFE";
                attribute :>> penColor default "#013965";
            }
            view def AbstractCyanStyle :> ShapeStyle {
                attribute :>> fillColor default "#D4F4F8";
                attribute :>> compartmentFillColor default "#F3FBFD";
                attribute :>> penColor default "#003E41";
            }
            view def AbstractOrangeStyle :> ShapeStyle {
                attribute :>> fillColor default "#FFEED4";
                attribute :>> compartmentFillColor default "#FFFAF3";
                attribute :>> penColor default "#612200";
            }
            view def AbstractOrangeOnBorderStyle :> ShapeOnBorderStyle {
                attribute :>> fillColor default "#FFE8C5";
                attribute :>> penColor default "#612200";
            }
            view def AbstractDeepPurpleStyle :> ShapeStyle {
                attribute :>> fillColor default "#E6DEF3";
                attribute :>> compartmentFillColor default "#F8F5FB";
                attribute :>> penColor default "#20125F";
            }
            view def AbstractDeepPurpleOnBorderStyle :> ShapeOnBorderStyle {
                attribute :>> fillColor default "#DDD3EF";
                attribute :>> penColor default "#20125F";
            }
            view def AbstractRedStyle :> ShapeStyle {
                attribute :>> fillColor default "#FFDADD";
                attribute :>> compartmentFillColor default "#FFF7F8";
                attribute :>> penColor default "#540D0D";
            }
            view def AbstractRedOnBorderStyle :> ShapeOnBorderStyle {
                attribute :>> fillColor default "#FFCDD2";
                attribute :>> penColor default "#540D0D";
            }
            view def AbstractPinkStyle :> ShapeStyle {
                attribute :>> fillColor default "#FCE0EA";
                attribute :>> compartmentFillColor default "#FEF5F8";
                attribute :>> penColor default "#580933";
            }
            view def AbstractBlueStyle :> ShapeStyle {
                attribute :>> fillColor default "#D9ECFD";
                attribute :>> compartmentFillColor default "#F4FAFE";
                attribute :>> penColor default "#082E69";
            }
            view def AbstractYellowStyle :> ShapeStyle {
                attribute :>> fillColor default "#FFFCDE";
                attribute :>> compartmentFillColor default "#FFFEF5";
                attribute :>> penColor default "#9F530F";
            }
            view def AbstractIndigoStyle :> ShapeStyle {
                attribute :>> fillColor default "#DFE1F3";
                attribute :>> compartmentFillColor default "#F6F7FB";
                attribute :>> penColor default "#111752";
            }
            view def AbstractAmberStyle :> ShapeStyle {
                attribute :>> fillColor default "#FFF5D4";
                attribute :>> compartmentFillColor default "#FFFCF3";
                attribute :>> penColor default "#A64800";
            }
            view def AbstractGreyStyle :> ShapeStyle {
                attribute :>> fillColor default "#ECECEC";
                attribute :>> compartmentFillColor default "#FAFAFA";
                attribute :>> penColor default "#4A4A4A";
            }
            view def AbstractWhiteStyle :> ShapeStyle {
                attribute :>> fillColor default "#FFFFFF";
                attribute :>> compartmentFillColor default "#FFFFFF";
                attribute :>> penColor default "#FF424242";
            }
            view def AbstractWhiteOnBorderStyle :> ShapeOnBorderStyle {
                attribute :>> fillColor default "#FFFFFF";
                attribute :>> penColor default "#FF424242";
            }
        }
        package CompartmentVisibilityDefinitions {
            part def UsagesAndDefCompartments {
                part metadataCompartment : MetadataCompartmentStyle {
                    attribute :>> showFullText default true;
                }
                part featuresOfMetadataCompartment : FeaturesOfMetadataCompartmentStyle {
                    attribute :>> showCompartment default true;
                }
                part documentationCompartment : DocumentationCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part subjectCompartment : SubjectCompartmentStyle {
                    attribute :>> showCompartment default true;
                    #InvisibleInDialog attribute :>> showModifiers default false;
                }
                part actorsCompartment : ActorsCompartmentStyle {
                    attribute :>> showCompartment default true;
                    #InvisibleInDialog attribute :>> showModifiers default false;
                }
                part stakeholdersCompartment : StakeholdersCompartmentStyle {
                    attribute :>> showCompartment default true;
                    #InvisibleInDialog attribute :>> showModifiers default false;
                }
                part objectiveCompartment : ObjectiveCompartmentStyle {
                    attribute :>> showCompartment default true;
                    #InvisibleInDialog attribute :>> showModifiers default false;
                }
                part includesCompartment : IncludeUseCasesCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part attributesCompartment : AttributesCompartmentStyle {
                    attribute :>> showCompartment default false;
                    attribute :>> showValue default true;
                }
                part parametersCompartment : ParametersCompartmentStyle {
                    attribute :>> showCompartment default false;
                    attribute :>> showValue default true;
                }
                part performActionCompartment : PerformActionsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part satisfyRequirementCompartment : SatisfyRequirementsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part itemsCompartment : ItemsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part actionsCompartment : ActionsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part exhibitStatesCompartment : ExhibitStatesCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part constraintsCompartment : ConstraintsCompartmentStyle {
                    attribute :>> showCompartment default true;
                }
                part requireCompartment : RequireCompartmentStyle {
                    attribute :>> showCompartment default true;
                    #InvisibleInDialog attribute :>> showModifiers default false;
                }
                part assumeCompartment : AssumeCompartmentStyle {
                    attribute :>> showCompartment default true;
                    #InvisibleInDialog attribute :>> showModifiers default false;
                }
                part assertCompartment : AssertCompartmentStyle {
                    attribute :>> showCompartment default true;
                    attribute :>> showModifiers default false;
                }
                part framesCompartment : FramesCompartmentStyle {
                    attribute :>> showCompartment default true;
                    #InvisibleInDialog attribute :>> showModifiers default false;
                }
                part partsCompartment : PartsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part portsCompartment : PortsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part enumsCompartment : EnumsCompartmentStyle {
                    attribute :>> showValue default true;
                    #InvisibleInDialog attribute :>> showModifiers;
                }
                part endsCompartment : EndsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part whileConditionCompartment : WhileConditionCompartmentStyle {
                    attribute :>> showCompartment default true;
                }
                part untilConditionCompartment : UntilConditionCompartmentStyle {
                    attribute :>> showCompartment default true;
                }
                part forIterationCompartment : ForIterationCompartmentStyle {
                    attribute :>> showCompartment default true;
                }
                part ifConditionCompartment : IfConditionCompartmentStyle {
                    attribute :>> showCompartment default true;
                }
                part membersCompartment : MembersCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part styleSheetRulesCompartment : StyleSheetRulesCompartmentStyle {
                    attribute :>> showCompartment default true;
                }
            }
            part def HideAllCompartments {
                doc /* hide all compartments definition */
                part metadataCompartment : MetadataCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part featuresOfMetadataCompartment : FeaturesOfMetadataCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part documentationCompartment : DocumentationCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part subjectCompartment : SubjectCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part actorsCompartment : ActorsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part stakeholdersCompartment : StakeholdersCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part objectiveCompartment : ObjectiveCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part includesCompartment : IncludeUseCasesCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part attributesCompartment : AttributesCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part parametersCompartment : ParametersCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part performActionsCompartment : PerformActionsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part satisfyRequirementsCompartment : SatisfyRequirementsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part itemsCompartment : ItemsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part actionsCompartment : ActionsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part exhibitStatesCompartment : ExhibitStatesCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part constraintsCompartment : ConstraintsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part requireCompartment : RequireCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part assumeCompartment : AssumeCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part assertCompartment : AssertCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part framesCompartment : FramesCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part partsCompartment : PartsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part portsCompartment : PortsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part enumsCompartment : EnumsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part endsCompartment : EndsCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part whileConditionCompartment : WhileConditionCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part untilConditionCompartment : UntilConditionCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part forIterationCompartment : ForIterationCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part ifConditionCompartment : IfConditionCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part membersCompartment : MembersCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
                part styleSheetRulesCompartment : StyleSheetRulesCompartmentStyle {
                    attribute :>> showCompartment default false;
                }
            }
        }
    }
}
