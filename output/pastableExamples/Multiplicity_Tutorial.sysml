package Multiplicity_Tutorial {
    
    part def Person;
    part def Wheel;
    
    /* --- 1. Package Context --- */
    /* Usage directly in package defaults to [0..*] */
    part looseWheels : Wheel; 

    part def Car {
        /* --- 2. Definition Context --- */
        /* Usage in a definition (part/attr/port) defaults to [1] */
        part engine : Person; /* [1..1] Required */
        
        /* --- Explicit Constraints --- */
        part wheels : Wheel [4]; /* Exactly 4 */
        
        /* --- 3. Inheritance --- */
        /* subsets: inherits parent multiplicity (here [1]) */
        /* We can constrain it further, or leave it. */
        part driver subsets engine; 
        
        /* --- 4. Collections --- */
        /* unique (Default): Set */
        part passengers : Person [0..4]; 
        
        /* ordered nonunique: Sequence */
        attribute lapTimes : ScalarValues::Real [*] ordered nonunique;
    }
    
    action def Drive {
        /* Default parameter multiplicity is [1] */
        in distance : ScalarValues::Integer; 
    }
}