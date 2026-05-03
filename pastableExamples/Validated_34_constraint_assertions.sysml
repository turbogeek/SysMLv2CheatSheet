package ConstraintTests;

part def BoundedValue {
    attribute value : Real;
    
    // Constraint
    assert constraint {
        value >= 0.0 && value <= 100.0
    }
    
    // Assume constraint
    assume constraint {
        value != 50.0
    }
}

requirement def ValueRequirement {
    subject val : BoundedValue;
    
    require constraint {
        val.value > 10.0
    }
    
    assume constraint {
        val.value < 90.0
    }
}
