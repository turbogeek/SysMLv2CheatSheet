package Constraints_2ConstraintUsageAssert {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    attribute def Acceleration;
    attribute def Force;
    constraint def NewtonLaw { in f : Force; in m : Mass; in a : Acceleration; }
    part Car {
      attribute mass : Mass;
      attribute accel : Acceleration;
      attribute force : Force;
      assert constraint n1 : NewtonLaw {
        in f = force;
        in m = mass;
        in a = accel;
      }
    }
}