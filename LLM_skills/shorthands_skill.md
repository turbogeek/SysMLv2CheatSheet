# SysML v2 Shorthand Notations Reference

**Alias:** SysMLv2 Shorthands

## Overview
SysMLv2 supports several shorthand textual notations to simplify declarations and reduce boilerplate. When writing or generating SysMLv2 models, you should recognize and use these shorthands where appropriate to improve readability.

---

### 1. Conjugated Port Usages
A conjugated port usage reverses the direction (`in`, `out`, `inout`) of all directed features on the port definition.
**Shorthand:** Prefix the port definition name with a tilde (`~`).
```sysml
// Equivalent to `port fuelInPort : FuelingPort::'~FuelingPort';`
port fuelInPort : ~FuelingPort;
```

### 2. Feature Values (Bindings and Initialization)
**Shorthand:** Use `=`, `:=`, `default =`, or `default :=` inline in feature declarations instead of explicit `bind` usages.
```sysml
// Fixed binding (equivalent to a nested binding of this usage to the expression)
attribute monthsInYear : Natural = 12;

// Initial value (binding applies only to the starting snapshot)
attribute count[1] : Natural := 0;

// Default values (delayed until instantiation, can be overridden)
attribute mass : Real default 1500.0; // The = is optional for bound defaults
attribute cutoff : Rational default = 0.75;
feature engine[1] : Engine default := standardEngine;
```

### 3. Connection Usages
**Shorthand:** For binary connections, the `connect` and `to` keywords replace explicit `end` declarations. For n-ary connections, `connect(...)` with a comma-separated list can be used. The `connection` keyword itself can be omitted if the declaration part is empty.
```sysml
// Binary shorthand
connect leftWheel to leftHalfAxle;

// Equivalent to explicitly declaring endpoints:
// connection { end ::> leftWheel; end ::> leftHalfAxle; }

// N-ary shorthand
connect(axle, wheel1, wheel2);
```

### 4. Succession and Control Flows
**Shorthand:** Rather than an explicit `succession` declaration with ends, `first` and `then` can be used directly in an action's body. The keyword `then` can also stand alone, implicitly taking the lexically preceding occurrence usage as the source.
```sysml
first action1 then action2; // Explicit source and target
first action3; then action4; // Source and target declared separately

// Implicit source from previous occurrence
action initialize;
then monitor;
then finalize;
```

**Conditional Succession Shorthand:** Using `if` / `then` / `else` to imply `DecisionTransitionAction`.
```sysml
first initialize if isActive then monitor;
if level <= refillLevel then refill;
else continue;
```

### 5. Loops
**Shorthand:** `loop` is a shorthand for `while true`.
```sysml
loop {
    assign charge := MonitorBattery();
} until charge >= 100;
```

### 6. State Actions
**Shorthand:** The `entry`, `do`, and `exit` keywords implicitly assume the `action` keyword. They can also use `reference subsetting` directly.
```sysml
state def OperationalStates {
    // Equivalent to: entry action references initial;
    entry initial;
    
    // Empty entry action
    entry;
    
    // Equivalent to: do action references monitorTemperature;
    do monitorTemperature;
}
```

### 7. Transitions
**Shorthand:** To declare a transition usage without a declaration part, use the `transition` keyword separating the source and target.
```sysml
source_state transition target_state;
```
