library package <DS_UIComponents> DassaultSystemesUIComponents {
    package CoreUIComponents {
        private import ScalarValues::*;
        private import Metaobjects::*;
        package Operations {
            abstract action def Operation;
            abstract action def PaletteOperation :> Operation;
            abstract action def DialogOperation :> Operation;
            action def OperationFromCode :> PaletteOperation { in actionId [0..1] : String; }
            action def OperationFromTemplate :> PaletteOperation, DialogOperation { in element [0..1] : Metaobject; }
            action def OperationByMetaclass :> DialogOperation { in elementMetaclass [0..1] : Metaobject; }
        }
        package Components {
            abstract part def AbstractItem {
                attribute label : String;
                attribute description : String;
            }
            abstract part def Item :> AbstractItem {
                perform action operation [0..1] : Operations::Operation;
            }
            abstract part def ItemsCategory :> AbstractItem {
                attribute isCollapsed : Boolean;
                attribute hasVisibleLabels : Boolean;
                part abstractItems [*] : AbstractItem;
            }
            abstract part def Component {
                part itemCategories [*] : ItemsCategory;
            }
        }
        package Palette {
            abstract part def AbstractButton;
            part def Button :> Components::Item, AbstractButton {
                perform action : Operations::PaletteOperation :>> operation;
            }
            part def ButtonsCategory :> Components::ItemsCategory, AbstractButton {
                part abstractButtons : AbstractButton :>> abstractItems;
                ref part focusedButton [0..1] : Button;
            }
            part def Palette :> Components::Component {
                part buttonCategories [*] : ButtonsCategory :>> itemCategories;
            }
        }
        package Dialogs {
            part def DialogItem :> Components::Item {
                perform action : Operations::DialogOperation :>> operation;
            }
            part def DialogItemsCategory :> Components::ItemsCategory {
                part : DialogItem :>> abstractItems;
            }
            abstract part def Dialog :> Components::Component {
                attribute actionName : String;
                part : DialogItemsCategory :>> itemCategories;
            }
            part def RelationshipCreationDialog :> Dialog {
                part :>> itemCategories {
                    attribute isOwnerSource : Boolean;
                }
            }
            part def ElementCreationDialog :> Dialog;
            part def ViewCreationDialog :> Dialog;
        }
    }
    package UIComponents {
        private import KerML::*;
        private import CoreUIComponents::*;
        private import ViewsTemplates::*;
        part def SysMLViewCreationDialog :> Dialogs::ViewCreationDialog {
            attribute :>> actionName default "Create View";
            part sysMLViewsMenu :> itemCategories {
                attribute :>> isCollapsed default false;
                attribute :>> label default "Symbolic Views";
                part gvItem : Dialogs::DialogItem :> abstractItems {
                    attribute :>> label default "General View";
                    perform action : Operations::OperationFromTemplate :>> operation { in ref = (generalViewTemplate meta Package).ownedElement; }
                }
                part ivItem : Dialogs::DialogItem :> abstractItems {
                    attribute :>> label default "Interconnection View";
                    perform action : Operations::OperationFromTemplate :>> operation { in ref = (interconnectionViewTemplate meta Package).ownedElement; }
                }
                part afvItem : Dialogs::DialogItem :> abstractItems {
                    attribute :>> label default "Action Flow View";
                    perform action : Operations::OperationFromTemplate :>> operation { in ref = (actionFlowViewTemplate meta Package).ownedElement; }
                }
                part stvItem : Dialogs::DialogItem :> abstractItems {
                    attribute :>> label default "State Transition View";
                    perform action : Operations::OperationFromTemplate :>> operation { in ref = (stateTransitionViewTemplate meta Package).ownedElement; }
                }
            }
            part sysMLTableMenu :> itemCategories {
                attribute :>> isCollapsed default false;
                attribute :>> label default "Tabular Views";
                part gtItem : Dialogs::DialogItem :> abstractItems {
                    attribute :>> label default "Generic Table";
                    perform action : Operations::OperationFromTemplate :>> operation { in ref = (genericTableTemplate meta Package).ownedElement; }
                }
                part rtItem : Dialogs::DialogItem :> abstractItems {
                    attribute :>> label default "Requirements Table";
                    perform action : Operations::OperationFromTemplate :>> operation { in ref = (requirementsTableTemplate meta Package).ownedElement; }
                }
            }
        }
        package ViewsTemplates {
            package generalViewTemplate {
                view : DS_Views::SymbolicViews::gv;
            }
            package interconnectionViewTemplate {
                view : DS_Views::SymbolicViews::iv;
            }
            package actionFlowViewTemplate {
                view : DS_Views::SymbolicViews::afv;
            }
            package stateTransitionViewTemplate {
                view : DS_Views::SymbolicViews::stv;
            }
            package genericTableTemplate {
                view : DS_Views::TabularViews::gt;
            }
            package requirementsTableTemplate {
                view : DS_Views::TabularViews::rt;
            }
        }
    }
}
