package AbstractVariationTests;

// Test abstract definitions and variation

abstract part def AbstractComponent {
    attribute id : String;
    attribute value : Real;
}

part def ConcreteComponent :> AbstractComponent {
    attribute :>> id = "COMP-001";
    attribute :>> value = 42.0;
}

variation part def ComponentVariant :> AbstractComponent {
    variant typeA : AbstractComponent {
        attribute :>> id = "TYPE-A";
        attribute :>> value = 100.0;
    }

    variant typeB : AbstractComponent {
        attribute :>> id = "TYPE-B";
        attribute :>> value = 200.0;
    }
}

abstract action def AbstractProcess {
    abstract action step1;
    abstract action step2;
}

action def ConcreteProcess :> AbstractProcess {
    action :>> step1 {
        // Implementation
    }

    action :>> step2 {
        // Implementation
    }
}
