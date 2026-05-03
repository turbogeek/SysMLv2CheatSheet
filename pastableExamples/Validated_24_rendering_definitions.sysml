package RenderingTests;

// Test rendering definitions for views

private import Views::*;

rendering def CustomDiagram {
    attribute layout : String;
    attribute style : String;
}

rendering customStyle : CustomDiagram {
    attribute layout = "hierarchical";
    attribute style = "UML";
}

part def Component {
    part subComponent1;
    part subComponent2;
}

view 'Component Structure' : SymbolicView {
    expose Component::**;
    render customStyle;
}

viewpoint def StructuralViewpoint {
    concern 'Show system decomposition';

    rendering :>> defaultRendering = customStyle;
}

view 'Detailed View' : SymbolicView satisfies StructuralViewpoint {
    expose Component::*;
    render asDefault;
}
