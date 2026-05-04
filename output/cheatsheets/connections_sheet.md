# Connections Cheat Sheet

*Connections and Flows*

## 1. Connection Definition

Defining connection types.

```sysml
package Connections_1ConnectionDefinition {
    private import ScalarValues::*;
    private import SysML::*;
    part def Hub;
    part def Device;
    connection def DeviceConn {
       end hub : Hub;
       end device : Device;
    }
}
```

## 1b. Connection Usage

Connecting parts.

```sysml
package Connections_1bConnectionUsage {
    private import ScalarValues::*;
    private import SysML::*;
    part def Hub;
    part def Device;
    connection def DeviceConn { end hub : Hub; end device : Device; }
    part context {
       part hub : Hub;
       part device : Device;
       connection c1 : DeviceConn
          connect hub to device;
    }
}
```

## 2. Binding Connector (=)

Equating elements. **CRITICAL**: No array indices are allowed (e.g. `a[1] = b[1]` is invalid).

```sysml
package Connections_2BindingConnector {
    private import ScalarValues::*;
    private import SysML::*;
    part def A { port p1; }
    part def B { port p2; }
    part system {
       part a : A;
       part b : B;
       bind a.p1 = b.p2;
       /* CRITICAL: No array indices allowed! Bind multiple items directly: */
       /* bind a.ports = b.ports; */
    }
}
```

## 3. Interface Connection

Flows within interfaces.

```sysml
package Connections_3InterfaceConnection {
    private import ScalarValues::*;
    private import SysML::*;
    /* Wrapped Snippet (Structure Context) */
    interface   def  IData  {
       end  source ;
       end  target ;
       flow  source  to  target ;
    }
}
```

## 4. Succession Flow

Control/Data flow.

```sysml
package Connections_4SuccessionFlow {
    private import ScalarValues::*;
    private import SysML::*;
    action process {
       action step1;
       action step2;
       first step1;
       then step2;
       doc /* Equivalent to: */
       flow from step1 to step2;
    }
}
```

