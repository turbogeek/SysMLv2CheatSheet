package Symbols_6WildcardsAndMultiplicity {
    private import ScalarValues::*;
    /* Wildcard import: direct members only */
    private import SysML::*;
    /* Recursive import: direct and indirect nested members */
    public import Symbols_6WildcardsAndMultiplicity::**;

    /* Single asterisk: unrestricted upper bound */
    part passengers [*];

    /* Single and double asterisk operators in expressions */
    attribute val1 : Real;
    attribute val2 : Real;
    attribute product = val1 * val2;
    attribute power = val1 ** 3;
}