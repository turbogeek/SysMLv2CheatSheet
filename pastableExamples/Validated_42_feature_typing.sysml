package FeatureTypingTests;

// Test feature typing, chains, and value expressions

part def Component {
    attribute config : Configuration;

    // Feature chains
    attribute :>> configName = config.name;
    attribute configValue = config.settings.primaryValue;

    // Typed features
    part sensor : Sensor typed by TemperatureSensor;

    // Feature value binding
    port dataPort : DataPort {
        attribute :>> rate = 100.0;
    }
}

part def Configuration {
    attribute name : String;
    part settings : Settings;
}

part def Settings {
    attribute primaryValue : Real;
    attribute secondaryValue : Real;
}

part def Sensor;
part def TemperatureSensor :> Sensor;

port def DataPort {
    attribute rate : Real;
}

part def System {
    part component : Component {
        // Inline feature value assignment
        :>> config {
            :>> name = "DefaultConfig";
            :>> settings {
                :>> primaryValue = 42.0;
            }
        }
    }
}
