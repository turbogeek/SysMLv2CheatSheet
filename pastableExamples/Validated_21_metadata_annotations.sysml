package MetadataTests;

// Test metadata definitions and annotations

metadata def Author {
    attribute name : String;
    attribute email : String;
}

metadata def Version {
    attribute number : String;
    attribute date : String;
}

@Author {
    name = "Systems Engineer";
    email = "engineer@example.com";
}
@Version {
    number = "1.0.0";
    date = "2025-11-18";
}
part def DocumentedComponent {
    doc /*
    This component has metadata annotations
    */

    attribute value : Real;
}

// Metadata on requirement
@Author {
    name = "Requirements Engineer";
}
requirement def AnnotatedRequirement {
    subject system;
    require constraint value > 0.0;
}
