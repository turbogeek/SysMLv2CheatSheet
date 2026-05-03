comment about Shorthand_3Redefinition /* Source: Shorthand_3Redefinition.sysml */
package Shorthand_3Redefinition {
    private import ISQ::*;
    comment /* Wrapped Snippet (Structure Context)
    attribute partMass : ISQBase::mass  =  100.0 ;
    attribute partMass1 :>> partMass  =  101.0 ;   
    attribute  partMass2 redefines  partMass  =  101.0 ;
    comment about partMass1, partMass2 /* :>> and redefines are equivelnt */
}