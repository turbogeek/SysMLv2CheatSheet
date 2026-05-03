package ExpressionOperatorTests;

// Test various expression operators and calculations

part def Calculator {
    // Arithmetic operators
    attribute sum = 10 + 5;
    attribute difference = 10 - 5;
    attribute product = 10 * 5;
    attribute quotient = 10 / 5;
    attribute modulo = 10 % 3;
    attribute power = 2 ** 8;

    // Comparison operators
    attribute isEqual = (10 == 10);
    attribute isNotEqual = (10 != 5);
    attribute isGreater = (10 > 5);
    attribute isLess = (5 < 10);
    attribute isGreaterOrEqual = (10 >= 10);
    attribute isLessOrEqual = (5 <= 10);

    // Logical operators
    attribute andResult = (true && true);
    attribute orResult = (true || false);
    attribute notResult = (!false);
    attribute xorResult = (true xor false);

    // Conditional operator
    attribute conditionalValue = (10 > 5) ? 100 : 50;

    // Null coalescing
    attribute withDefault = nullableValue ?? 42.0;

    attribute nullableValue : Real[0..1];
}

part def VectorOperations {
    attribute vector1[3] = (1.0, 2.0, 3.0);
    attribute vector2[3] = (4.0, 5.0, 6.0);

    // Collection operations
    attribute dotProduct = vector1 dot vector2;
    attribute concatenated = vector1 + vector2;
}

part def StringOperations {
    attribute firstName = "John";
    attribute lastName = "Doe";

    // String concatenation
    attribute fullName = firstName + " " + lastName;

    // String comparison
    attribute namesMatch = (firstName == "John");
}

calc def computeArea {
    in width : Real;
    in height : Real;
    return width * height;
}

part geometricShape {
    attribute width = 10.0;
    attribute height = 5.0;
    attribute area = computeArea(width, height);
}
