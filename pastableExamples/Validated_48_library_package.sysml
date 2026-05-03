package LibraryPackageTests;

// Test library package and standard library usage

library package MathLibrary {
    // Standard library functions
    calc def sqrt {
        in x : Real;
        return : Real;
    }

    calc def abs {
        in x : Real;
        return : Real;
    }

    calc def max {
        in a : Real;
        in b : Real;
        return : Real;
    }

    calc def min {
        in a : Real;
        in b : Real;
        return : Real;
    }
}

library package GeometryLibrary {
    import MathLibrary::*;

    calc def circleArea {
        in radius : Real;
        return 3.14159 * radius * radius;
    }

    calc def pythagorean {
        in a : Real;
        in b : Real;
        return sqrt(a * a + b * b);
    }
}

// Using library packages
import GeometryLibrary::*;

part def Circle {
    attribute radius : Real;
    attribute area = circleArea(radius);
}

part def RightTriangle {
    attribute sideA : Real;
    attribute sideB : Real;
    attribute hypotenuse = pythagorean(sideA, sideB);
}

part myCircle : Circle {
    :>> radius = 5.0;
}

part myTriangle : RightTriangle {
    :>> sideA = 3.0;
    :>> sideB = 4.0;
}
