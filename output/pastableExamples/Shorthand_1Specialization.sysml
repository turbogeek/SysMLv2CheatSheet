package Shorthand_1Specialization {
    private import ScalarValues::*;
    private import SysML::*;
    part def Vehicle;
    // Wrapped Snippet (Structure Context)
    part  def  Car  :>  Vehicle ;
    doc  /* Equivalent to: 
            part  def  Car  specializes  Vehicle ; */
}