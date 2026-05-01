package PoolMaintenanceRobot {
    
    // --- Standard Libraries ---
    private import ScalarValues::*;
    private import ISQ::*;
    private import SI::*;
    private import MathFunctions::*;

    // --- Custom Units ---
    package CustomUnits {
        private import MeasurementReferences::*;
        
        // Gallons (Volume)
        attribute <gal> gallon : SimpleUnit {
            doc /* Custom unit for US Gallons */
            :>> quantityDimension = ISQ::volume; 
        }

        // Tablets (Count)
        attribute <tablet> tabletUnit : SimpleUnit {
            doc /* Custom base unit for counting physical chlorine tablets */
            :>> quantityDimension = ISQ::DimensionOne;
        }
        
        // Temperature (Fahrenheit)
        attribute <degF> fahrenheit : SimpleUnit {
            doc /* Custom unit for Fahrenheit */
            :>> quantityDimension = ISQ::thermodynamicTemperature;
        }
    }

    // --- Requirements ---
    package Requirements {
        private import CustomUnits::*;

        requirement def VolumeCalculationReq {
            doc /* The system shall calculate the volume of a Rectangular, Play, or Kidney shaped pool based on user dimension inputs. */
        }
        requirement def ChlorineCalculationReq {
            doc /* The system shall calculate the base number of chlorine tablets required based on pool volume. */
        }
        requirement def EnvironmentalAdjustReq {
            doc /* The system shall adjust the required chlorine amount based on ambient temperature, rain, and evaporation. */
        }
        requirement def SafetyReq {
            doc /* The robot shall securely store chemical tablets to prevent accidental exposure. */
        }
    }

    // --- Data Types and Enumerations ---
    package Types {
        enum def PoolShape {
            Rectangular;
            Kidney;
            Play;
        }
        
        enum def ChlorineType {
            Trichlor3Inch;
            DichlorGranular;
        }
    }

    // --- Analysis & Calculations ---
    package ChemistryAnalysis {
        private import CustomUnits::*;
        private import Types::*;

        // Volume Calculators
        calc def RectangularVolumeCalc {
            in length : Real;
            in width : Real;
            in averageDepth : Real;
            // Volume = L * W * D * 7.48 (converting cu ft to gallons)
            return volume : Real = length * width * averageDepth * 7.48; 
        }
        
        calc def PlayPoolVolumeCalc {
            in length : Real;
            in width : Real;
            in shallowDepth : Real;
            in deepDepth : Real;
            // Approx Volume = L * W * ((Shallow + Deep + Shallow) / 3) * 7.48
            return volume : Real = length * width * ((shallowDepth + deepDepth + shallowDepth) / 3.0) * 7.48; 
        }

        calc def KidneyVolumeCalc {
            in length : Real;
            in widthA : Real;
            in widthB : Real;
            in averageDepth : Real;
            // Approx Kidney Volume = (A + B) * L * 0.45 * D * 7.48
            return volume : Real = (widthA + widthB) * length * 0.45 * averageDepth * 7.48; 
        }

        // Simple Chlorine Calculation
        calc def SimpleChlorineCalc {
            in poolVolumeGal : Real;
            // 1 3-inch tablet per 5000 gallons
            return tabletsNeeded : Real = poolVolumeGal / 5000.0;
        }

        // Complex Chlorine Calculation
        calc def ComplexChlorineCalc {
            in baseTablets : Real;
            in temperatureF : Real;
            in rainInches : Real;
            in evaporationInches : Real;
            
            // Example complex logic: 
            // If temp > 85, need 20% more.
            // If rain > 1 inch, need 10% more (dilution).
            // If evaporation > 0.5 inch, need 5% more.
            
            // For SysMLv2 calc, we can use simple math approximations:
            attribute tempMod : Real = if temperatureF > 85.0 then 1.2 else 1.0;
            attribute rainMod : Real = if rainInches > 1.0 then 1.1 else 1.0;
            attribute evapMod : Real = if evaporationInches > 0.5 then 1.05 else 1.0;
            
            return finalTablets : Real = baseTablets * tempMod * rainMod * evapMod;
        }
    }

    // --- Logical Architecture ---
    package LogicalArchitecture {
        private import Requirements::*;
        private import CustomUnits::*;
        private import Types::*;
        private import ChemistryAnalysis::*;

        part def ChemistryEngine {
            attribute currentTemp : Real [1];
            attribute rainLevel : Real [1];
            attribute evapLevel : Real [1];
            attribute poolVolume : Real [1];
            
            // Usage of the calc
            attribute baseTablets : Real = SimpleChlorineCalc(poolVolume);
            attribute requiredTablets : Real = ComplexChlorineCalc(baseTablets, currentTemp, rainLevel, evapLevel);
            
            satisfy ChlorineCalculationReq;
            satisfy EnvironmentalAdjustReq;
        }

        part def UserInterface {
            attribute selectedShape : PoolShape [1];
            attribute selectedChlorine : ChlorineType [1];
        }

        part def EnvironmentalSensor {
            attribute tempOut : Real [1];
            attribute rainOut : Real [1];
            attribute evapOut : Real [1];
        }

        part def Dispenser {
            attribute tabletCount : Real [1];
            action dispenseTablets {
                in amountToDispense : Real;
            }
            satisfy SafetyReq;
        }

        part def PoolMaintenanceRobot {
            part ui : UserInterface;
            part engine : ChemistryEngine;
            part sensors : EnvironmentalSensor;
            part dispenser : Dispenser;

            // Connections (ICD)
            connection sensorToEngine connect sensors to engine;
            connection uiToEngine connect ui to engine;
            connection engineToDispenser connect engine to dispenser;
        }
    }

    // --- Physical Architecture ---
    package PhysicalArchitecture {
        private import LogicalArchitecture::*;

        part def MicrocontrollerUnit specializes ChemistryEngine;
        part def TouchScreen specializes UserInterface;
        part def WeatherStation specializes EnvironmentalSensor;
        part def MotorizedHopper specializes Dispenser;

        part def PhysicalPoolRobot specializes PoolMaintenanceRobot {
            part redefines ui : TouchScreen;
            part redefines engine : MicrocontrollerUnit;
            part redefines sensors : WeatherStation;
            part redefines dispenser : MotorizedHopper;
        }
    }

    // --- Views and Viewpoints ---
    package RobotViews {
        private import PhysicalArchitecture::*;

        viewpoint def SafetyViewpoint {
            doc /* Focuses on chemical safety and secure storage. */
        }
        
        viewpoint def ChemistryViewpoint {
            doc /* Focuses on the math and algorithms used to calculate chlorine needs. */
        }

        view def RobotSafetyView :> SafetyViewpoint {
            // Expose the dispenser which handles safety
            expose PhysicalArchitecture::MotorizedHopper;
        }

        view def RobotChemistryView :> ChemistryViewpoint {
            expose ChemistryAnalysis::SimpleChlorineCalc;
            expose ChemistryAnalysis::ComplexChlorineCalc;
        }
    }
}
