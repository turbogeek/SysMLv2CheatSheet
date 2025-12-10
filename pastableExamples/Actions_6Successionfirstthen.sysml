package Actions_6Successionfirstthen {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Action Context)
    action def Main {
        first start;
        then process;
        then finish;
        doc /* Control flow sequence */
    }

    view ExposeExample {
        expose Main;
    }
}