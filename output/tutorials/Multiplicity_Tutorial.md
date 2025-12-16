# Multiplicity

*Cardinality, Collections, and Ordering*

## 1. Basic Multiplicity

Multiplicity constraints specify how many instances of a feature can exist.
• **[1]**: Exactly one (Default).
• **[0..1]**: Optional.
• **[*]** or **[0..*]**: Zero or more.

## 2. Collection Types

When multiplicity is > 1, the feature is a collection. You can constrain its nature:
• **ordered**: The order of elements matters.
• **unique**: No duplicates allowed (Default).
• **nonunique**: Duplicates allowed.

## 3. Multiplicity Example

```sysml
package Multiplicity_Tutorial {
    part def Wheel;
    part def Seat;
    part def Passenger;
    
    part def Bus {
        // --- Exact Constraints ---
        // Exactly 6 wheels are required
        part wheels : Wheel [6];
        
        // --- Optionality ---
        // A reserved seat may or may not exist (0 or 1)
        part reservedSeat : Seat [0..1];
        
        // --- Collections ---
        // unique (Default): A specific person can't be in two seats at once (Set)
        part seats : Seat [20..50]; 
        
        // ordered nonunique: Queue of passengers boarding
        // 'ordered': sequence matters (who is first)
        // 'nonunique': technically allows duplicates (though confusing for people!)
        part boardingQueue : Passenger [*] ordered nonunique;
        
        // --- Attribute Arrays ---
        // Recording lap times (Sequence of numbers)
        attribute lapTimes : ScalarValues::Real [*] ordered;
    }
}
```

