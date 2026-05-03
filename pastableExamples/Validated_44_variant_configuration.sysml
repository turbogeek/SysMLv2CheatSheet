package VariantConfigurationTests;

// Test variant configurations and selections

variation part def VehicleConfiguration {
    variant baseModel {
        part engine : Engine {
            attribute power = 150.0;
        }
        part transmission : ManualTransmission;
    }

    variant sportModel {
        part engine : Engine {
            attribute power = 300.0;
        }
        part transmission : AutomaticTransmission;
        part turbo : Turbocharger;
    }

    variant luxuryModel {
        part engine : Engine {
            attribute power = 250.0;
        }
        part transmission : AutomaticTransmission;
        part interior : LuxuryInterior;
    }
}

part def Engine {
    attribute power : Real;
}

part def ManualTransmission;
part def AutomaticTransmission;
part def Turbocharger;
part def LuxuryInterior;

// Configuration selection
part myVehicle : VehicleConfiguration = VehicleConfiguration::sportModel;

variation attribute def OperatingMode {
    variant normalMode;
    variant ecoMode;
    variant sportMode;
}

attribute currentMode : OperatingMode = OperatingMode::normalMode;
