# Shorthand Cheat Sheet

*Syntax Shortcuts*

## 1. Specialization (:>)

Shorthand for 'specializes'.

```sysml
package Shorthand_1Specialization {
    private import ScalarValues::*;
    private import SysML::*;
    part def Vehicle;
    /* Wrapped Snippet (Structure Context) */
    part  def  Car  :>  Vehicle ;
    doc  /* Equivalent to: 
            part  def  Car  specializes  Vehicle ; */
}
```

## 2. Subsetting (:>)

Shorthand for 'subsets'.

```sysml
package Shorthand_2Subsetting {
    private import ScalarValues::*;
    private import SysML::*;
    part parts;
    /* Wrapped Snippet (Structure Context) */
    part  engine  :>  parts ;
    doc  /* Equivalent to: 
            part  engine  subsets  parts ; */
}
```

## 3. Redefinition (:>>)

Shorthand for 'redefines'.

```sysml
comment about Shorthand_3Redefinition /* Source: Shorthand_3Redefinition.sysml */
package Shorthand_3Redefinition {
    private import ISQ::*;
    comment /* Wrapped Snippet (Structure Context)
    attribute partMass : ISQBase::mass  =  100.0 ;
    attribute partMass1 :>> partMass  =  101.0 ;   
    attribute  partMass2 redefines  partMass  =  101.0 ;
    comment about partMass1, partMass2 /* :>> and redefines are equivelnt */
}
```

## 4. Conjugation (~)

Shorthand for 'conjugated'.

```sysml
package Shorthand_4Conjugation {
    private import ScalarValues::*;
    private import SysML::*;
    port def Interface;
    /* Wrapped Snippet (Structure Context) */
    port  p  :  ~ Interface ;
    doc  /* Equivalent to: 
            port  p  :  conjugated  Interface ; */
}
```

## 5. Feature Values

Assignment variations.

```sysml
package Shorthand_5FeatureValues {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    attribute  x  =  1 ;  /* Binding (Equality) */
    attribute  y  :=  2 ;  /* Initial Value */
    attribute  z  default  =  3 ;  /* Default Value */
}
```

## 6. Multiplicity

Common shorthands.

```sysml
package Shorthand_6Multiplicity {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    part  many [*] ;  /* 0..* */
    part  one ;  /* 1..1 (Default) */
    part  opt [0..1] ;  /* 0..1 */
}
```

