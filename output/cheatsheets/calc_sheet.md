# Calculation Cheat Sheet

*Calculations and Constraints*

## 1. Calculation Definition

Reusable math expressions.

```sysml
package Calculations_1CalculationDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Voltage;
    attribute def Current;
    attribute def Power;
    calc def PowerCalc {
       in v : Voltage;
       in i : Current;
       return p : Power = v * i;
    }
}
```

## 2. Calculation Usage

Performing a calculation.

```sysml
package Calculations_2CalculationUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Voltage; attribute def Current; attribute def Power;
    calc def PowerCalc { in v : Voltage; in i : Current; return p : Power; }
    /* Wrapped Snippet (Action Context) */
    action def Main {
        calc  p_motor  :  PowerCalc  {
           in  v  =  12.0 ;
           in  i  =  5.0 ;
        }
    }

    view ExposeExample {
        expose Main;
    }
}
```

## 4. Constraint Usage

Applying a constraint.

```sysml
package Calculations_4ConstraintUsage {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def Mass;
    constraint def MassLimit { in m : Mass; in limit : Mass; }
    /* Wrapped Snippet (Action Context) */
    action def Main {
        attribute mass : Mass;
        constraint  checkMass  :  MassLimit  {
           in  m  =  mass ;
           in  limit  =  1000.0 ;
        }
    }

    view ExposeExample {
        expose Main;
    }
}
```

## 5. Assertions

Enforcing truth.

```sysml
package Calculations_5Assertions {
    private import ScalarValues::*;
    private import SysML::*;
    action def Main {
        attribute x : Integer;
        attribute y : Integer;
        assert constraint {
           x > 0
        }
        assert constraint {
           not (y < 0)
        }
    }
    view ExposeExample { expose Main; }
}
```

## 6. Requirements

Assumptions and requirements.

```sysml
package Calculations_6Requirements {
    private import ScalarValues::*;
    private import SysML::*;
    requirement def Safety {
       attribute temp : Real;
       attribute pressure : Real;
       assume constraint { temp < 100 }
       require constraint { pressure < 50 }
    }
}
```

