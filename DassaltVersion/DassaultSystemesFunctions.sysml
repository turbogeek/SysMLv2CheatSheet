library package <DS_Functions> DassaultSystemesFunctions {
    private import KerML::*;
    private import ScalarValues::*;
    private import SequenceFunctions::*;
    private import ControlFunctions::*;
    calc def IsEssentialElement {
        in input : Element;
        return res [1] : Boolean;
        rep script language "elementFilter" /* com.dassault_systemes.modeler.sysml.model.EssentialElements::isEssentialInOwnershipContext*/
    }
    calc def IsNonStandardLibraryElement {
        in input : Element;
        return res [1] : Boolean;
        rep script language "elementFilter" /* com.dassault_systemes.modeler.kerml.libraries.StandardLibraries::isNotFromLibrary*/
    }
    calc def IsClassifiedBy {
        in t : Type;
        in parentT : Type [1..*];
        IsClassifiedBy_Implementation(t, parentT, null)
    }
    private calc def IsClassifiedBy_Implementation {
        in t : Type;
        in parentT : Type [1..*];
        in visited : Type [0..*];
        visitedPlusCurrent : Type [*] = (visited, t);
        toVisit : Type [*] = t.ownedSpecialization.general->excluding(visitedPlusCurrent);
        parentT == t or toVisit->exists {
            in x;
            null ?? IsClassifiedBy_Implementation(x, parentT, visitedPlusCurrent)
        }
    }
}
