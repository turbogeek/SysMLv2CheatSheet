# Patterns Cheat Sheet

*Reusable Modeling Patterns*

## 1. Metadata (Annotations)

Tagging elements with data.

```sysml
package Patterns_1MetadataAnnotations {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    metadata   def  Status  {
      attribute  priority  :  Integer ;
      attribute  approved  :  Boolean ;
    }
    part  myPart  {
      metadata  Status  {
        priority  =  1 ;
      }
    }
}
```

## 2. Views

Visualizing the model.

```sysml
package Patterns_2Views {
    private import ScalarValues::*;
    private import SysML::*;
    part def GeneralDiagram;
    /* Wrapped Snippet (Structure Context) */
    view  MyView  :  GeneralDiagram  {
    /* filter Status; */
    }
    /* Rendering specific subsets */
}
```

## 3. Custom Units (Nano Banana)

Defining domain-specific units.

```sysml
package BananaUnits {
    private import ScalarValues::*;
    private import SysML::*;
    attribute def LengthUnit {
        attribute prefix;
        attribute referenceUnit;
    }
    attribute nano;
    attribute <nB> nanoBanana : LengthUnit {
        attribute unitConversion;
        :>> prefix = nano;
        :>> referenceUnit = "Standard Banana";
    }
}
```

## 4. Abstract vs Individual

Templates vs Concrete instances.

```sysml
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
```

