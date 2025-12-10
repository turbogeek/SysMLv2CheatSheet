library package <DS_Views> DassaultSystemesViews {
    private import DS_UIComponents::CoreUIComponents::*;
    private import Metaobjects::*;
    private import ScalarValues::*;
    package CoreViews {
        private import DS_Styles::CoreStylesComponents::*;
        abstract view def Visualization;
        abstract view def <sv> 'Symbolic View' :> Visualization {
            part palette [0..1] : Palette::Palette;
            part effectiveStyleSheets : StyleSheet [*] default (explicitlyAppliedStyleSheets, projectActiveStyleSheets);
            part explicitlyAppliedStyleSheets : StyleSheet [*];
            part projectActiveStyleSheets : StyleSheet [*] = ByProjectStyleSheetCollector(self);
            calc def ByProjectStyleSheetCollector {
                in cd;
                return : StyleSheet [*];
                rep projectStyleSheetCollectorScript language "Groovy" /* com.dassault_systemes.modeler.sysml.diagram.ModelBasedStyleSheetCollector.findStyleSheetsByProject(cd); */
            }
            render Views::asInterconnectionDiagram;
        }
        abstract view def <bsv> 'Base Symbolic View' :> sv {
            part baseViewPalette : ViewPalettes::BasePalette :>> palette;
        }
        abstract view def <bgv> 'Base Grid View' :> Visualization, StandardViewDefinitions::grv;
        rendering def TableCellRendering {
            calc getValue { in rowElement [0..1] : Metaobject; }
            attribute isMultiValued [0..1] : Boolean;
        }
        rendering asTableCell : TableCellRendering;
        rendering def BooleanCellRendering :> TableCellRendering;
        rendering def ElementCellRendering :> TableCellRendering;
        rendering def EnumCellRendering :> TableCellRendering;
        rendering def IntegerCellRendering :> TableCellRendering;
        rendering def MetaobjectCellRendering :> TableCellRendering;
        rendering def RealCellRendering :> TableCellRendering;
        rendering def StringCellRendering :> TableCellRendering;
        abstract view def ColumnView {
            attribute isMultiline [0..1] : Boolean;
        }
        view def ColumnByFeatureView :> ColumnView {
            ref item columnFeature [0..1] : KerML::Core::Feature;
        }
        view def ColumnByExpressionView :> ColumnView {
            render asTableCell;
        }
        rendering asTable :> Views::asElementTable {
            view column : ColumnView :> columnView;
        }
        abstract view def <bt> 'Base Table' :> bgv {
            render asTable;
        }
    }
    package SymbolicViews {
        private import CoreViews::*;
        private import ViewPalettes::*;
        view def <gv> 'General View' :> bsv, StandardViewDefinitions::gv {
            part generalViewPalette : GeneralPalette :>> baseViewPalette;
        }
        view def <iv> 'Interconnection View' :> bsv, StandardViewDefinitions::iv {
            part interconnectionViewPalette : InterconnectionPalette :>> baseViewPalette;
        }
        view def <afv> 'Action Flow View' :> bsv, StandardViewDefinitions::afv {
            part actionFlowViewPalette : ActionFlowPalette :>> baseViewPalette;
        }
        view def <stv> 'State Transition View' :> bsv, StandardViewDefinitions::stv {
            part stateTransitionViewPalette : StateTransitionPalette :>> baseViewPalette;
        }
    }
    package SymbolicViewsByExpression {
        private import KerML::*;
        private import SysML::*;
        private import KerML::Root::Element::*;
        private import Actions::ForLoopAction::*;
        private import Actions::WhileLoopAction::*;
        private import SequenceFunctions::*;
        view def NonStandardLibraryElementFilter {
            filter DS_Functions::IsNonStandardLibraryElement();
            doc /* This view definition excludes elements from the standard library.*/
        }
        view def EssentialElementsFilter {
            filter DS_Functions::IsEssentialElement();
            doc /* This view definition filters out various elements that are not supposed to be exposed.*/
        }
        view def TreeView :> EssentialElementsFilter, NonStandardLibraryElementFilter {
            doc /* This view definition displays the common elements in a tree view style.*/
            render Views::asTreeDiagram;
        }
        view def NestedView :> EssentialElementsFilter, NonStandardLibraryElementFilter {
            doc /* This view definition displays the common elements in a nested view style.*/
            render Views::asInterconnectionDiagram;
        }
        view def UsagesNestedView :> NestedView {
            filter not (istype ViewUsage);
            filter not ((self as Element).owner istype Association);
            filter not ((self as Element).owner istype PortDefinition);
            filter not isEmpty((self as Element).owner istype AttributeDefinition) | isEmpty((self as Element).owner istype ItemDefinition);
            doc /* This view definition displays any usage in a nested view style.*/
        }
        view def PartsNestedView :> UsagesNestedView {
            doc /* This view definition displays parts as nested shapes, with connections between them shown as paths.*/
            filter hastype PartUsage | hastype PartDefinition | @ConnectorAsUsage;
        }
        view def 'Parts&PortsNestedView' :> UsagesNestedView {
            doc /* This view definition displays parts and ports as nested shapes, with connections shown as paths.*/
            filter hastype PartUsage | hastype PortUsage | @ConnectorAsUsage;
        }
        view def PartsTreeView :> TreeView {
            doc /* This view definition displays parts in a decomposition tree style.*/
            filter hastype PartUsage | hastype PartDefinition;
        }
        view def ActionsNestedView :> UsagesNestedView {
            doc /* This view definition displays actions and parameters as nested shapes, with connections between them represented as paths.*/
            filter istype ActionUsage | istype ActionDefinition | not isEmpty((self as Usage).direction) | @ConnectorAsUsage | istype TransitionUsage;
        }
        view def ActionsTreeView :> TreeView {
            doc /* This view definition displays actions in a decomposition tree style.*/
            filter hastype ActionUsage | hastype PerformActionUsage;
        }
        view def RequirementsTreeView :> TreeView {
            doc /* This view definition displays requirements in a decomposition tree style.*/
            filter hastype RequirementUsage | hastype RequirementDefinition;
        }
        view def StatesNestedView :> UsagesNestedView {
            doc /* This view definition displays the states as nested shapes, with transitions between them represented as paths.*/
            filter istype StateUsage | istype StateDefinition | istype TransitionUsage | istype ActionUsage | istype SuccessionAsUsage;
        }
    }
    package TabularViews {
        private import CoreViews::*;
        private import SymbolicViewsByExpression::*;
        private import KerML::*;
        private import SysML::*;
        view def <gt> 'Generic Table' :> bt {
            render rendering asTable :>> asTable {
                view 'Declared Name' : ColumnByFeatureView :> column {
                    ref item :>> columnFeature = declaredName meta Feature;
                }
                view 'Declared Short Name' : ColumnByFeatureView :> column {
                    ref item :>> columnFeature = declaredShortName meta Feature;
                }
                view Documentation : ColumnByExpressionView :> column {
                    attribute :>> isMultiline default true;
                    render rendering : StringCellRendering :>> asTableCell {
                        calc :>> getValue {
                            in rowElement : Element;
                            (rowElement.ownedElement as Comment).body
                        }
                    }
                }
                view 'Qualified Name' : ColumnByFeatureView :> column {
                    ref item :>> columnFeature = qualifiedName meta Feature;
                }
                view Owner : ColumnByFeatureView :> column {
                    ref item :>> columnFeature = owner meta Feature;
                }
                view 'Owned Element' : ColumnByFeatureView :> column {
                    ref item :>> columnFeature = ownedElement meta Feature;
                }
            }
        }
        view def <rt> 'Requirements Table' :> bt, NonStandardLibraryElementFilter {
            filter @RequirementUsage or @RequirementDefinition;
            render rendering asTable :>> asTable {
                view 'Declared Name' : ColumnByFeatureView :> column {
                    ref item :>> columnFeature = declaredName meta Feature;
                }
                view 'Req Id' : ColumnByFeatureView :> column {
                    ref item :>> columnFeature = declaredShortName meta Feature;
                }
                view Documentation : ColumnByExpressionView :> column {
                    attribute :>> isMultiline default true;
                    render rendering : StringCellRendering :>> asTableCell {
                        calc :>> getValue {
                            in rowElement : Element;
                            (rowElement.ownedElement as Comment).body
                        }
                    }
                }
            }
        }
    }
    package ViewPalettes {
        private import CodeActionIdentifiers::*;
        part def SelectionCategory :> Palette::ButtonsCategory {
            attribute :>> isCollapsed default false;
            attribute :>> hasVisibleLabels default false;
            attribute :>> label default "Selections";
            attribute :>> description default "Selections";
            part selectionButton : Palette::Button :> abstractButtons {
                perform action : Operations::OperationFromCode :>> operation { in ref = selectionModeAction; }
            }
            part completeCoverageModeButton : Palette::Button :> abstractButtons {
                perform action : Operations::OperationFromCode :>> operation { in ref = completeCoverageModeAction; }
            }
            part selectionMenu : Palette::ButtonsCategory :> abstractButtons {
                part selectSiblingButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = selectSiblingAction; }
                }
                part selectOfTheSameTypeButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = selectOfTheSameTypeAction; }
                }
                part selectConnectedButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = selectConnectedAction; }
                }
                part selectConnectedRecursivelyButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = selectConnectedRecursivelyAction; }
                }
                part selectAllButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = selectAllAction; }
                }
                :>> focusedButton default selectSiblingButton;
            }
        }
        part def ToolsCategory :> Palette::ButtonsCategory {
            attribute :>> isCollapsed default false;
            attribute :>> hasVisibleLabels default false;
            attribute :>> label default "Tools";
            attribute :>> description default "Tools";
            part stickyButton : Palette::Button :> abstractButtons {
                perform action : Operations::OperationFromCode :>> operation { in ref = stickyModeAction; }
            }
            part pusherButton : Palette::Button :> abstractButtons {
                perform action : Operations::OperationFromCode :>> operation { in ref = pusherAction; }
            }
            part magnetButton : Palette::Button :> abstractButtons {
                perform action : Operations::OperationFromCode :>> operation { in ref = magnetAction; }
            }
        }
        part def CommonCategory :> Palette::ButtonsCategory {
            attribute :>> isCollapsed default true;
            attribute :>> hasVisibleLabels default true;
            attribute :>> label default "Common";
            attribute :>> description default "Common";
            part textBoxMenu : Palette::ButtonsCategory :> abstractButtons {
                part textBoxButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = textBoxAction; }
                }
                part textBoxHtmlButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = textBoxHtmlAction; }
                }
            }
            part separatorMenu : Palette::ButtonsCategory :> abstractButtons {
                part horizontalSeparatorButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = horizontalSeparatorAction; }
                }
                part verticalSeparatorButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = verticalSeparatorAction; }
                }
                part rectangularSeparatorButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = rectangularSeparatorAction; }
                }
                :>> focusedButton default horizontalSeparatorButton;
            }
            part docButton : Palette::Button :> abstractButtons {
                perform action : Operations::OperationFromCode :>> operation { in ref = docAction; }
            }
            part commentButton : Palette::Button :> abstractButtons {
                perform action : Operations::OperationFromCode :>> operation { in ref = commentAction; }
            }
            part imageButton : Palette::Button :> abstractButtons {
                perform action : Operations::OperationFromCode :>> operation { in ref = imageAction; }
            }
        }
        part def BasePalette :> Palette::Palette {
            part selectionCategory : SelectionCategory :> buttonCategories;
            part toolsCategory : ToolsCategory :> buttonCategories;
            part commonCategory : CommonCategory :> buttonCategories;
        }
        part def GeneralPalette :> BasePalette {
            part :>> selectionCategory;
            part :>> toolsCategory;
            part :>> commonCategory;
            part itemsPortsAttributesCategory : Palette::ButtonsCategory :> buttonCategories {
                attribute :>> isCollapsed default false;
                attribute :>> hasVisibleLabels default true;
                attribute :>> label default "Items/Ports/Attributes";
                attribute :>> description default "Items/Ports/Attributes";
                part partsMenu : Palette::ButtonsCategory :> abstractButtons {
                    part partUsageButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = partAction; }
                    }
                    part partDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = partDefAction; }
                    }
                    :>> focusedButton default partUsageButton;
                }
                part portsMenu : Palette::ButtonsCategory :> abstractButtons {
                    part portUsageButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = portAction; }
                    }
                    part portDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = portDefAction; }
                    }
                    :>> focusedButton default portUsageButton;
                }
                part itemsButton : Palette::ButtonsCategory :> abstractButtons {
                    part itemUsageButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = itemAction; }
                    }
                    part itemDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = itemDefAction; }
                    }
                    :>> focusedButton default itemUsageButton;
                }
                part attributesMenu : Palette::ButtonsCategory :> abstractButtons {
                    part attributeUsageButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = attributeAction; }
                    }
                    part attributeDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = attributeDefAction; }
                    }
                    :>> focusedButton default attributeUsageButton;
                }
                part timeslicesAndSnapshotsMenu : Palette::ButtonsCategory :> abstractButtons {
                    part timesliceUsageButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = timesliceAction; }
                    }
                    part snapshotUsageButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = snapshotAction; }
                    }
                    part anyTimesliceUsageButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = anyTimesliceAction; }
                    }
                    part anySnapshotUsageButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = anySnapshotAction; }
                    }
                    :>> focusedButton default timesliceUsageButton;
                }
                part refButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = refAction; }
                }
                part enumDefButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = enumDefAction; }
                }
                part metadataDefButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = metadataDefAction; }
                }
            }
            part connectorsCategory : Palette::ButtonsCategory :> buttonCategories {
                attribute :>> isCollapsed default false;
                attribute :>> hasVisibleLabels default true;
                attribute :>> label default "Connectors";
                attribute :>> description default "Connectors";
                part connectionMenu : Palette::ButtonsCategory :> abstractButtons {
                    part connectionButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = connectionAction; }
                    }
                    part naryConnectionButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = naryConnectionAction; }
                    }
                    part connectionDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = connectionDefAction; }
                    }
                    :>> focusedButton default connectionButton;
                }
                part derivationMenu : Palette::ButtonsCategory :> abstractButtons {
                    part derivationButton : Palette::Button :> abstractButtons {
                        attribute :>> label = "derivation";
                        perform action : Operations::OperationFromTemplate :>> operation {
                            in ref = (ElementTemplates::derivationConnectionTemplate meta KerML::Kernel::Package).ownedElement;
                        }
                    }
                    part naryDerivationButton : Palette::Button :> abstractButtons {
                        attribute :>> label = "n-ary derivation";
                        perform action : Operations::OperationFromTemplate :>> operation {
                            in ref = (ElementTemplates::derivationNaryConnectionTemplate meta KerML::Kernel::Package).ownedElement;
                        }
                    }
                    part derivationDefButton : Palette::Button :> abstractButtons {
                        attribute :>> label = "derivation def";
                        perform action : Operations::OperationFromTemplate :>> operation {
                            in ref = (ElementTemplates::derivationConnectionDefTemplate meta KerML::Kernel::Package).ownedElement;
                        }
                    }
                    :>> focusedButton default derivationButton;
                }
                part bindButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = bindAction; }
                }
                part allocationMenu : Palette::ButtonsCategory :> abstractButtons {
                    part allocationButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = allocationAction; }
                    }
                    part allocationDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = allocationDefAction; }
                    }
                    :>> focusedButton default allocationButton;
                }
                part flowMenu : Palette::ButtonsCategory :> abstractButtons {
                    part flowButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = flowAction; }
                    }
                    part flowDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = flowDefAction; }
                    }
                    :>> focusedButton default flowButton;
                }
                part interfaceMenu : Palette::ButtonsCategory :> abstractButtons {
                    part interfaceButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = interfaceAction; }
                    }
                    part naryInterfaceButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = naryInterfaceAction; }
                    }
                    part interfaceDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = interfaceDefAction; }
                    }
                    :>> focusedButton default interfaceButton;
                }
                part successionButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = successionAction; }
                }
                part successionFlowButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = successionFlowAction; }
                }
            }
            part specializationsCategory : Palette::ButtonsCategory :> buttonCategories {
                attribute :>> isCollapsed default true;
                attribute :>> hasVisibleLabels default true;
                attribute :>> label default "Specializations";
                attribute :>> description default "Specializations";
                part subclassificationButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = subclassifactionAction; }
                }
                part featureTypingButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = featureTypingAction; }
                }
                part subsettingButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = subsettingAction; }
                }
                part referenceSubsettingButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = referenceSubsettingAction; }
                }
                part redefinitionButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = redefinitionAction; }
                }
            }
            part otherRelationshipsCategory : Palette::ButtonsCategory :> buttonCategories {
                attribute :>> isCollapsed default true;
                attribute :>> hasVisibleLabels default true;
                attribute :>> label default "Other Relationships";
                attribute :>> description default "Other Relationships";
                part dependencyButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = dependencyAction; }
                }
                part annotationButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = annotationAction; }
                }
                part featureMembershipButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = featureMembershipAction; }
                }
            }
            part actionsCategory : Palette::ButtonsCategory :> buttonCategories {
                attribute :>> isCollapsed default false;
                attribute :>> hasVisibleLabels default true;
                attribute :>> label default "Actions";
                attribute :>> description default "Actions";
                part actionMenu : Palette::ButtonsCategory :> abstractButtons {
                    part actionButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = actionAction; }
                    }
                    part actionDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = actionDefAction; }
                    }
                }
                part performActionButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = performActionAction; }
                }
                part inputMenu : Palette::ButtonsCategory :> abstractButtons {
                    part inRefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = inputRefAction; }
                    }
                    part inItemButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = inputItemAction; }
                    }
                    part inAttributeButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = inputAttributeAction; }
                    }
                    :>> focusedButton default inRefButton;
                }
                part outputMenu : Palette::ButtonsCategory :> abstractButtons {
                    part outRefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = outputRefAction; }
                    }
                    part outItemButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = outputItemAction; }
                    }
                    part outAttributeButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = outputAttributeAction; }
                    }
                    :>> focusedButton default outRefButton;
                }
                part inoutputMenu : Palette::ButtonsCategory :> abstractButtons {
                    part inoutRefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = inoutRefAction; }
                    }
                    part inoutItemButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = inoutItemAction; }
                    }
                    part inoutAttributeButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = inoutAttributeAction; }
                    }
                    :>> focusedButton default inoutRefButton;
                }
                part decideButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = decideAction; }
                }
                part mergeButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = mergeAction; }
                }
                part forkButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = forkAction; }
                }
                part joinButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = joinAction; }
                }
                part startButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = startAction; }
                }
                part doneButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = doneAction; }
                }
                part terminateButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = terminateAction; }
                }
            }
            part otherActionsCategory : Palette::ButtonsCategory :> buttonCategories {
                attribute :>> isCollapsed default true;
                attribute :>> hasVisibleLabels default true;
                attribute :>> label default "Other Actions";
                attribute :>> description default "Other Actions";
                part assignButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = assignAction; }
                }
                part sendButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = sendAction; }
                }
                part acceptButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = acceptAction; }
                }
                part ifButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = ifAction; }
                }
                part whileButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = whileAction; }
                }
                part forButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = forAction; }
                }
            }
            part statesCategory : Palette::ButtonsCategory :> buttonCategories {
                attribute :>> isCollapsed default true;
                attribute :>> hasVisibleLabels default true;
                attribute :>> label default "States";
                attribute :>> description default "States";
                part statesMenu : Palette::ButtonsCategory :> abstractButtons {
                    part stateButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = stateAction; }
                    }
                    part stateDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = stateDefAction; }
                    }
                }
                part exhibitStateButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = exhibitStateAction; }
                }
                part transitionButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = transitionAction; }
                }
            }
            part casesCategory : Palette::ButtonsCategory :> buttonCategories {
                attribute :>> isCollapsed default true;
                attribute :>> hasVisibleLabels default true;
                attribute :>> label default "Cases";
                attribute :>> description default "Cases";
                part useCaseMenu : Palette::ButtonsCategory :> abstractButtons {
                    part useCaseButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = useCaseAction; }
                    }
                    part useCaseDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = useCaseDefAction; }
                    }
                    :>> focusedButton default useCaseButton;
                }
                part includeUseCaseButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = includeUseCaseAction; }
                }
            }
            part requirementsConstraintsCategory : Palette::ButtonsCategory :> buttonCategories {
                attribute :>> isCollapsed default true;
                attribute :>> hasVisibleLabels default true;
                attribute :>> label default "Requirements/Constraints";
                attribute :>> description default "Requirements/Constraints";
                part requirementMenu : Palette::ButtonsCategory :> abstractButtons {
                    part requirementButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = requirementAction; }
                    }
                    part requirementDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = requirementDefAction; }
                    }
                    :>> focusedButton default requirementButton;
                }
                part satisfyRequirementButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = satisfyRequirementAction; }
                }
                part concernMenu : Palette::ButtonsCategory :> abstractButtons {
                    part concernButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = concernAction; }
                    }
                    part concernDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = concernDefAction; }
                    }
                    :>> focusedButton default concernButton;
                }
                part constraintMenu : Palette::ButtonsCategory :> abstractButtons {
                    part constraintButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = constraintAction; }
                    }
                    part constraintDefButton : Palette::Button :> abstractButtons {
                        perform action : Operations::OperationFromCode :>> operation { in ref = constraintDefAction; }
                    }
                    :>> focusedButton default constraintButton;
                }
                part assertConstraintButton : Palette::Button :> abstractButtons {
                    perform action : Operations::OperationFromCode :>> operation { in ref = assertConstraintAction; }
                }
            }
        }
        part def InterconnectionPalette :> GeneralPalette {
            part :>> selectionCategory;
            part :>> toolsCategory;
            part :>> commonCategory;
            part :>> itemsPortsAttributesCategory;
            part :>> connectorsCategory {
                part :>> successionButton [0];
                part :>> successionFlowButton [0];
                part :>> derivationMenu [0];
            }
            part :>> specializationsCategory;
            part :>> otherRelationshipsCategory;
            part :>> actionsCategory [0];
            part :>> otherActionsCategory [0];
            part :>> statesCategory [0];
            part :>> casesCategory [0];
        }
        part def ActionFlowPalette :> GeneralPalette {
            part :>> selectionCategory;
            part :>> toolsCategory;
            part :>> commonCategory;
            part :>> itemsPortsAttributesCategory [0];
            part :>> actionsCategory {
                attribute :>> isCollapsed default false;
            }
            part :>> connectorsCategory {
                part :>> connectionMenu [0];
                part :>> derivationMenu [0];
                part :>> allocationMenu [0];
                part :>> successionButton;
                part :>> successionFlowButton;
                part :>> flowMenu;
                part :>> interfaceMenu [0];
            }
            part :>> specializationsCategory;
            part :>> otherRelationshipsCategory;
            part :>> otherActionsCategory {
                attribute :>> isCollapsed default false;
            }
            part :>> statesCategory [0];
            part :>> casesCategory [0];
            part :>> requirementsConstraintsCategory;
        }
        part def StateTransitionPalette :> GeneralPalette {
            part :>> selectionCategory;
            part :>> toolsCategory;
            part :>> commonCategory;
            part :>> itemsPortsAttributesCategory [0];
            part :>> statesCategory {
                attribute :>> isCollapsed default false;
            }
            part :>> connectorsCategory [0];
            part :>> specializationsCategory;
            part :>> otherRelationshipsCategory;
            part :>> actionsCategory;
            part :>> otherActionsCategory [0];
            part :>> casesCategory [0];
            part :>> requirementsConstraintsCategory;
        }
        package CodeActionIdentifiers {
            private import ScalarValues::*;
            attribute selectionModeAction : String = "SELECTION";
            attribute completeCoverageModeAction : String = "GROUP_SELECTION_MODE";
            attribute selectSiblingAction : String = "SELECT_SIBLING";
            attribute selectOfTheSameTypeAction : String = "SELECT_SAME_TYPE";
            attribute selectConnectedAction : String = "SELECT_CONNECTED_DIRECTLY";
            attribute selectConnectedRecursivelyAction : String = "SELECT_CONNECTED_RECURSIVELY";
            attribute selectAllAction : String = "SELECTALL";
            attribute stickyModeAction : String = "STICKY";
            attribute pusherAction : String = "PUSHER_ACTION";
            attribute magnetAction : String = "MAGNET_ACTION";
            attribute textBoxAction : String = "ADD_TEXT_BOX";
            attribute textBoxHtmlAction : String = "ADD_HTML_TEXT_BOX";
            attribute horizontalSeparatorAction : String = "ADD_SEPARATOR";
            attribute verticalSeparatorAction : String = "ADD_SEPARATOR_VERTICAL";
            attribute rectangularSeparatorAction : String = "ADD_RECTANGULAR_SHAPE";
            attribute subclassifactionAction : String = "ADD_SUBCLASSIFICATION";
            attribute featureTypingAction : String = "ADD_FEATURE_TYPING";
            attribute subsettingAction : String = "ADD_SUBSETTING";
            attribute referenceSubsettingAction : String = "ADD_REFERENCE_SUBSETTING";
            attribute redefinitionAction : String = "ADD_REDEFINITION";
            attribute dependencyAction : String = "ADD_DEPENDENCY";
            attribute docAction : String = "ADD_DOC";
            attribute commentAction : String = "ADD_COMMENT";
            attribute annotationAction : String = "ADD_ANNOTATION";
            attribute featureMembershipAction : String = "ADD_FEATURE_MEMBERSHIP";
            attribute partAction : String = "ADD_PART";
            attribute partDefAction : String = "ADD_PART_DEF";
            attribute portAction : String = "ADD_PORT";
            attribute portDefAction : String = "ADD_PORT_DEF";
            attribute itemAction : String = "ADD_ITEM";
            attribute itemDefAction : String = "ADD_ITEM_DEF";
            attribute attributeAction : String = "ADD_ATTRIBUTE";
            attribute attributeDefAction : String = "ADD_ATTRIBUTE_DEF";
            attribute timesliceAction : String = "ADD_TIMESLICE";
            attribute snapshotAction : String = "ADD_SNAPSHOT";
            attribute anyTimesliceAction : String = "ADD_ANY_TIMESLICE";
            attribute anySnapshotAction : String = "ADD_ANY_SNAPSHOT";
            attribute refAction : String = "ADD_REF";
            attribute enumDefAction : String = "ADD_ENUM_DEF";
            attribute connectionAction : String = "ADD_CONNECTION";
            attribute naryConnectionAction : String = "ADD_NRY_CONNECTION";
            attribute connectionDefAction : String = "ADD_CONNECTION_DEF";
            attribute bindAction : String = "ADD_BIND";
            attribute allocationAction : String = "ADD_ALLOCATION";
            attribute allocationDefAction : String = "ADD_ALLOCATION_DEF";
            attribute flowAction : String = "ADD_FLOW";
            attribute flowDefAction : String = "ADD_FLOW_DEF";
            attribute interfaceAction : String = "ADD_INTERFACE";
            attribute naryInterfaceAction : String = "ADD_NRY_INTERFACE";
            attribute interfaceDefAction : String = "ADD_INTERFACE_DEF";
            attribute successionAction : String = "ADD_SUCCESSION";
            attribute successionFlowAction : String = "ADD_SUCCESSION_FLOW";
            attribute actionAction : String = "ADD_ACTION";
            attribute actionDefAction : String = "ADD_ACTION_DEF";
            attribute performActionAction : String = "ADD_PERFORM_ACTION";
            attribute inputRefAction : String = "ADD_INPUT_REF";
            attribute inputItemAction : String = "ADD_INPUT_ITEM";
            attribute inputAttributeAction : String = "ADD_INPUT_ATTRIBUTE";
            attribute outputRefAction : String = "ADD_OUTPUT_REF";
            attribute outputItemAction : String = "ADD_OUTPUT_ITEM";
            attribute outputAttributeAction : String = "ADD_OUTPUT_ATTRIBUTE";
            attribute inoutRefAction : String = "ADD_INOUTPUT_REF";
            attribute inoutItemAction : String = "ADD_INOUTPUT_ITEM";
            attribute inoutAttributeAction : String = "ADD_INOUTPUT_ATTRIBUTE";
            attribute decideAction : String = "ADD_DECIDE";
            attribute mergeAction : String = "ADD_MERGE";
            attribute forkAction : String = "ADD_FORK";
            attribute joinAction : String = "ADD_JOIN";
            attribute startAction : String = "ADD_START";
            attribute doneAction : String = "ADD_DONE";
            attribute terminateAction : String = "ADD_TERMINATE";
            attribute assignAction : String = "ADD_ASSIGN";
            attribute sendAction : String = "ADD_SEND";
            attribute acceptAction : String = "ADD_ACCEPT";
            attribute ifAction : String = "ADD_IF";
            attribute whileAction : String = "ADD_WHILE";
            attribute forAction : String = "ADD_FOR";
            attribute stateAction : String = "ADD_STATE";
            attribute stateDefAction : String = "ADD_STATE_DEF";
            attribute exhibitStateAction : String = "ADD_EXHIBIT_STATE";
            attribute transitionAction : String = "ADD_TRANSITION";
            attribute useCaseAction : String = "ADD_USE_CASE";
            attribute useCaseDefAction : String = "ADD_USE_CASE_DEF";
            attribute includeUseCaseAction : String = "ADD_INCLUDE_USE_CASE";
            attribute requirementAction : String = "ADD_REQUIREMENT";
            attribute requirementDefAction : String = "ADD_REQUIREMENT_DEF";
            attribute satisfyRequirementAction : String = "ADD_SATISFY_REQUIREMENT";
            attribute concernAction : String = "ADD_CONCERN";
            attribute concernDefAction : String = "ADD_CONCERN_DEF";
            attribute constraintAction : String = "ADD_CONSTRAINT";
            attribute constraintDefAction : String = "ADD_CONSTRAINT_DEF";
            attribute assertConstraintAction : String = "ADD_ASSERT_CONSTRAINT";
            attribute metadataDefAction : String = "ADD_METADATA_DEF";
            attribute imageAction : String = "ADD_IMAGE";
            attribute entryAction : String = "ADD_ENTRY_ACTION";
        }
        package ElementTemplates {
            private import RequirementDerivation::*;
            package derivationConnectionTemplate {
                #derivation connection {
                    end #original requirement;
                    end #derive requirement;
                }
            }
            package derivationNaryConnectionTemplate {
                #derivation connection;
            }
            package derivationConnectionDefTemplate {
                #derivation connection def {
                    end #original requirement;
                    end #derive requirement;
                }
            }
        }
    }
}
