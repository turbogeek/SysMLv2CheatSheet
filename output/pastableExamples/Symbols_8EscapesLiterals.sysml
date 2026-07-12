package Symbols_8EscapesAndLiterals {
    private import ScalarValues::*;
    private import SysML::*;

    part 'wheels';
    /* Single quotes escape names with spaces/symbols */
    part 'left wheel' :> 'wheels';

    /* Double quotes wrap string literals */
    attribute str1 = "standard string";

    /* Backslash escapes special characters in strings and names */
    attribute str2 = "first line\nsecond line with \"quotes\" and \\backslash";
    part 'it\'s a quoted name' :> 'wheels';
}