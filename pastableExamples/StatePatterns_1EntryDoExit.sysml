package StatePatterns_1EntryDoExit {
    private import ScalarValues::*;
    private import SysML::*;
    action def logStart;
    action def maintain;
    action def logEnd;
    state def Active {
       entry action : logStart;
       do action : maintain;
       exit action : logEnd;
    }
}