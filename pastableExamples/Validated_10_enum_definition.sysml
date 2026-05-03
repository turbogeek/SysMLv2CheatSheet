/**
 * POSITIVE TEST: Enum definition and usage
 * EXPECTED: No errors
 * CATEGORY: Enumerations
 */
package PositiveTests {
    enum def Status {
        enum active;
        enum inactive;
        enum maintenance;
    }

    part def Component {
        attribute currentStatus : Status = Status::inactive;
    }
}
