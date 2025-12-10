package StatePatterns_1EntryDoExit {
    private import ScalarValues::*;
    private import SysML::*;
    // Wrapped Snippet (Structure Context)
    state def Active {
       entry action : logStart;
       do action : maintain;
       exit action : logEnd;
    }
}