package ExhibitPerformTests;

// Test exhibit and perform relationships

action def BasicAction {
    action subAction1;
    action subAction2;
}

part def Component {
    // Exhibit action
    exhibit basicBehavior : BasicAction;
}

part def System {
    part component : Component;
    
    // Perform action
    perform testAction : BasicAction;
}

action def ComplexAction {
    action initialize;
    action execute;
    action cleanup;

    first initialize;
    then execute;
    then cleanup;
}

part systemInstance : System {
    exhibit complexBehavior : ComplexAction;
}
