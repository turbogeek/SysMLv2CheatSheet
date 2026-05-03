package MultiplicityTests;

// Test various multiplicity syntaxes

part def Container {
    // Optional (0 or 1)
    part optional[0..1];

    // Required exactly one
    part required[1];

    // One or more
    part oneOrMore[1..*];

    // Zero or more
    part zeroOrMore[*];

    // Specific range
    part range[2..5];

    // Ordered collection
    part ordered items[*] ordered;

    // Non-unique collection
    part nonunique items[*] nonunique;

    // Ordered and non-unique
    part list[*] ordered nonunique;
}

part def Team {
    part member[3..10];
}

part def Network {
    part node[1..*];
    connection link[0..*];
}
