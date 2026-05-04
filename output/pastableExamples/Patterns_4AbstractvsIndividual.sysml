package Patterns_4AbstractvsIndividual {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    abstract  part  def  Wheel ;
    part  def  Bus  {
      abstract  part  wheel  [4]  :  Wheel ;
    }
    individual  part  myBus  :  Bus  {
      part  frontLeft  :>  wheel ;
    }
}