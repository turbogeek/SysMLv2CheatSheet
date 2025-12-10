package Views {
    view 'Stakeholder View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc
        /* Hierarchical view of all device components 
         * Standard SysML v2 view usages with NonStandardLibraryElementFilter
         */
        expose CheatSheetValidation::StructureExamples::**;
        /* filter (@RequirementDefinition or @RequirementUsage) and not AcceptActionUsage::isLibraryElement;*/
    }
    view 'ActionExamples View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc /**/
        expose CheatSheetValidation::ActionExamples::**;
    }
    view 'ConnectionExamples View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc /**/
        expose CheatSheetValidation::ConnectionExamples::**;
    }
    view 'ConnectionExamples View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc /**/
        expose CheatSheetValidation::ConnectionExamples::**;
    }
    view 'BehaviorExamples View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc /**/
        expose CheatSheetValidation::BehaviorExamples::**;
    }
    view 'CalcExamples View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc /**/
        expose CheatSheetValidation::CalcExamples::**;
    }
    view 'ActionPatternExamples View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc /**/
        expose CheatSheetValidation::ActionPatternExamples::**;
    }
    view 'StatePatternExamples View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc /**/
        expose CheatSheetValidation::StatePatternExamples::**;
    }
    view 'ShorthandExamples View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc /**/
        expose CheatSheetValidation::ShorthandExamples::**;
    }
    view 'ReferenceExamples View Tree' : DS_Views::SymbolicViewsByExpression::TreeView, DS_Views::SymbolicViewsByExpression::NonStandardLibraryElementFilter {
        doc /**/
        expose CheatSheetValidation::ReferenceExamples::**;
    }
}
