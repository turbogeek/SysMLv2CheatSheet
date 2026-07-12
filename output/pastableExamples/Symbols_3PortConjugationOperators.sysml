package Symbols_3ConjugationAndOperators {
    private import ScalarValues::*;
    private import SysML::*;

    port def OutputInterface;
    /* Conjugated port reverses feature directions */
    port inputPort : ~OutputInterface;

    attribute val : Real;
    /* Unary prefix operator (custom meaning) */
    attribute inv = ~val;
}