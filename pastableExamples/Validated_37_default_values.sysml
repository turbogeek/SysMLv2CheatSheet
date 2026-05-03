package DefaultValueTests;

part def Component {
    // Default value with =
    attribute count : Integer = 10;
    
    // Default value with default keyword
    attribute name : String default "Component";
    
    // Default with :=
    attribute status : String := "Active";
}

part def System {
    part component : Component {
        // Override default
        attribute :>> count = 20;
    }
}
