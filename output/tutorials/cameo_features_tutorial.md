# Cameo-Specific SysMLv2 Features

*Creating Custom Tables, Style Sheets, Palettes, and Dialogs in Cameo (CATIA Magic)*

## 1. Overview

While standard SysMLv2 provides robust modeling capabilities, Cameo (CATIA Magic) extends it with domain-specific features for creating custom diagrams (Symbolic Views), tables (Tabular Views), style sheets, and custom UI components (Dialogs, Palettes).

These features are accessed by importing specific Dassault Systèmes (DS) packages, such as `DS_Views`, `DS_Styles`, and `DS_UIComponents`.

---

## 2. Custom Style Sheets

Style sheets allow you to conditionally format elements in a view (e.g., coloring requirements based on metadata status).

```sysml
package StyleSheets {
    private import DS_Styles::CoreStylesComponents::Predicates::*;
    private import DS_Styles::CoreStylesComponents::KerMLStyles::*;

    part def StatusStyle :> DS_Styles::CoreStylesComponents::StyleSheet {
        
        part approvedRule :> rule {
            // Condition for when the rule applies
            part :>> condition : FreeFormCondition {
                calc :>> test {
                    GetValueOfMetadataFeature(element, Profile::info::status.metadata) == Profile::Status::approved.metadata
                }
            }
            // Style applied when condition is true
            part :>> style : SymbolStyle {
                attribute :>> penColor : Color = "#006400"; // Dark Green
                attribute :>> lineWidth = 2;
            }
        }
    }
}
```

**Applying the Style Sheet to a View:**
```sysml
view 'colored requirements diagram' : DS_Views::SymbolicViews::gv {
    // Explicitly apply the style sheet
    part : StyleSheets::StatusStyle :> explicitlyAppliedStyleSheets;
}
```

---

## 3. Custom Tabular Views (Tables)

You can define custom requirements tables (`rt`) or generic tables (`gt`) with specific scopes (expose), element filters, and dynamically calculated columns.

```sysml
private import DS_Views::*;

// A Requirements Table
view 'requirements table' : TabularViews::rt {
    expose DroneStakeholderRequirements::**; // Scope
    render rendering :>> asTable {
        view :>> 'Declared Name';
        view :>> 'Req Id';
        view :>> Documentation;
    }
}

// A Generic Table with Custom Calculated Columns
view 'variant table' : CoreViews::bt {
    filter @PartDefinition or @PartUsage;
    expose Drone::DroneVariants::**;
    
    render rendering :>> asTable {
        view : CoreViews::ColumnByFeatureView :> column {
            ref item :>> columnFeature = declaredName meta Feature;
        }
        
        // Custom expression column
        view 'Net Price' : CoreViews::ColumnByExpressionView :> column {
            render rendering : CoreViews::RealCellRendering :>> asTableCell {
                calc :>> getValue {
                    in :>> rowElement : Element;
                    (getNetPrice(rowElement) as LiteralInteger).value ?? 0
                }
                // Custom calculation function
                calc getNetPrice {
                    in e : Element;
                    // ... extraction logic ...
                }
            }
        }
    }
}
```

---

## 4. Custom Palettes and Symbolic Views

You can customize the creation palette (sidebar tools) for a specific symbolic view to provide a tailored modeling environment.

```sysml
private import DS_UIComponents::CoreUIComponents::Palette::*;

view def 'Requirements View' :> DS_Views::CoreViews::bsv {
    part :>> baseViewPalette {
        
        part requirementsCategory :> buttonCategories {
            attribute :>> label default "Requirements";
            
            // Adding a button that creates an element via Code Action
            part reqButton : Button :> abstractButtons {
                perform action : DS_UIComponents::CoreUIComponents::Operations::OperationFromCode :> operation {
                    in ref = DS_Views::ViewPalettes::CodeActionIdentifiers::requirementAction;
                }
            }
            
            // Adding a button that creates an element from a Template
            part softwareButton : Button :> abstractButtons {
                attribute :>> label = "Software Requirement";
                perform action : DS_UIComponents::CoreUIComponents::Operations::OperationFromTemplate :> operation {
                    in ref = softwareReqTemplate::softwareRequirement.metadata;
                }
            }
        }
    }
}
```

---

## 5. Custom View Creation Dialogs

You can inject your custom views and tables into the Cameo "Create View" or "Create Diagram" dialogs.

```sysml
package CustomViewCreationDialogs {
    // 1. Wrap the view in a package acting as a template
    package customRequirementsViewTemplate {
        view : CustomRequirementsView::'Requirements View';
    }

    // 2. Specialize the Creation Dialog
    part def CustomViewCreationDialog :> DS_UIComponents::UIComponents::SysMLViewCreationDialog {
        
        part :>> sysMLViewsMenu {
            part reqViewItem : DS_UIComponents::CoreUIComponents::Dialogs::DialogItem :> abstractItems {
                attribute :>> label default "Custom Requirements View";
                perform action : DS_UIComponents::CoreUIComponents::Operations::OperationFromTemplate :>> operation {
                    in ref = (customRequirementsViewTemplate meta KerML::Kernel::Package).ownedElement;
                }
            }
        }
    }
}
```