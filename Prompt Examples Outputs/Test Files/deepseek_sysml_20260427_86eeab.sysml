/**
 * Stock Ticker Device – SysMLv2 Model
 * 
 * References / Data Sources:
 * - LilyGO T‑Display S3 product page: https://www.lilygo.cc/products/t-display-s3
 * - ESP32‑S3 Datasheet: https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf
 * - ST7789 Display Controller Datasheet: https://www.displayfuture.com/Display/datasheet/controller/ST7789.pdf
 * - SysML v2 Specification (OMG): https://www.omg.org/spec/SysML/
 * - ISQ/SI Model Libraries: included in SysMLv2 standard distribution
 * 
 * This model describes a simple stock ticker device that displays a pre‑programmed 
 * list of stocks (Tesla, Google, Rivian, NASDAQ, DOW) on a screen and allows 
 * scrolling with two buttons. Power is supplied via USB‑C, which also charges 
 * a built‑in battery.
 */

package StockTickerModel {
    // =========================================================================
    // Project‑Specific Units (used throughout the model)
    // =========================================================================
    package ProjectUnits {
        private import SI::*;
        private import MeasurementReferences::ConversionByPrefix;
        
        doc /* Custom units needed where SI does not provide a prefixed symbol. */
        
        attribute <ms> millisecond : DurationUnit {
            :>> unitConversion : ConversionByPrefix {
                :>> prefix = milli;
                :>> referenceUnit = s;
            }
        }
    }

    // =========================================================================
    // Requirement Types Library
    // =========================================================================
    library package RequirementTypes {
        requirement def PerformanceRequirement {
            doc /* A requirement that mandates a specific quantitative metric be met. */
        }
        requirement def UsabilityRequirement {
            doc /* A requirement related to user interaction quality. */
        }
        requirement def PowerRequirement {
            doc /* A requirement concerning electrical power or battery performance. */
        }
        requirement def FunctionalRequirement {
            doc /* A requirement specifying a discrete function the system must provide. */
        }
        
        // Common attributes for requirement templates can be added here.
    }

    // =========================================================================
    // Stakeholder Concerns
    // =========================================================================
    package StakeholderConcerns {
        private import ISQ::*;
        private import RequirementTypes::*;
        
        concern def DisplayResponsiveness {
            subject system : LogicalDesign::StockTickerSystem;
            stakeholder user : People::User;
            require constraint {
                updateLatency <= 2 [ProjectUnits::s]   /* 2 seconds */
            }
            attribute updateLatency :> ISQ::duration;
        }
        
        concern def ButtonFeel {
            subject system : LogicalDesign::StockTickerSystem;
            stakeholder user : People::User;
            require constraint {
                responseTime <= 100 [ProjectUnits::ms]
            }
            attribute responseTime :> ISQ::duration;
        }
        
        concern def BatteryEndurance {
            subject system : LogicalDesign::StockTickerSystem;
            stakeholder user : People::User;
            require constraint {
                batteryLife >= 8 [h]
            }
            attribute batteryLife :> ISQ::duration;
        }
        
        concern def DataAccuracy {
            subject system : LogicalDesign::StockTickerSystem;
            stakeholder user : People::User;
            require constraint {
                stockDataMatchesPredefined
            }
            attribute stockDataMatchesPredefined : Boolean;
        }
    }

    // =========================================================================
    // Actors / People (simple part definitions for stakeholder types)
    // =========================================================================
    package People {
        part def User;   /* generic user */
    }

    // =========================================================================
    // Requirements (System Requirements)
    // =========================================================================
    package Requirements {
        private import RequirementTypes::*;
        private import ProjectUnits::*;
        private import ISQ::*;
        private import StakeholderConcerns::*;
        
        requirement <'REQ-PERF-01'> 'Stock Display Update Latency' : PerformanceRequirement {
            doc /* The system shall update the displayed stock information within 2 seconds of a button press or initialisation. */
            attribute updateLatency :> ISQ::duration = 2 [s];
            
            frame DisplayResponsiveness {
                :>> updateLatency = updateLatency;
            }
        }
        
        requirement <'REQ-PERF-02'> 'Button Response Time' : PerformanceRequirement {
            doc /* The system shall respond to a button press and begin scrolling the stock list within 100 ms. */
            attribute responseTime :> ISQ::duration = 100 [ms];
            
            frame ButtonFeel {
                :>> responseTime = responseTime;
            }
        }
        
        requirement <'REQ-PERF-03'> 'Battery Life' : PowerRequirement {
            doc /* The device shall operate for at least 8 hours on a fully charged battery under normal usage (display on, one button press per 10 seconds). */
            attribute batteryLife :> ISQ::duration = 8 [h];
            
            frame BatteryEndurance {
                :>> batteryLife = batteryLife;
            }
        }
        
        requirement <'REQ-USE-01'> 'Scroll Through Stock List' : UsabilityRequirement {
            doc /* The user shall be able to scroll up and down through the pre‑programmed list of stocks using two dedicated buttons. */
        }
        
        requirement <'REQ-USE-02'> 'Display Stock Information' : UsabilityRequirement {
            doc /* For each stock, the system shall display the ticker symbol, current price, and percentage change. */
        }
        
        requirement <'REQ-FUNC-01'> 'Pre‑Programmed Stock List' : FunctionalRequirement {
            doc /* The device shall store and display five stocks: Tesla, Google, Rivian, NASDAQ index, and DOW index. */
        }
        
        requirement <'REQ-FUNC-02'> 'USB Power and Charging' : FunctionalRequirement {
            doc /* The device shall be powered via a USB‑C connection, and when connected, it shall charge the internal battery. */
        }
    }

    // =========================================================================
    // Use Cases
    // =========================================================================
    package UseCases {
        private import People::User;
        private import LogicalDesign::StockTickerSystem;
        
        use case def ViewStockTicker {
            subject tickerSys : StockTickerSystem;
            actor user : User;
            
            objective {
                doc /* The user views current stock market data for the pre‑programmed stocks. */
            }
            
            include use case scrollStocks : ScrollStocks;
            include use case displayStock : DisplayStock;
        }
        
        use case def ScrollStocks {
            subject tickerSys : StockTickerSystem;
            actor user : User;
            
            objective {
                doc /* The user moves the selection up and down the stock list using the two buttons. */
            }
        }
        
        use case def DisplayStock {
            subject tickerSys : StockTickerSystem;
            actor user : User;
            
            objective {
                doc /* The system renders the stock symbol, price, and percentage change on the screen. */
            }
        }
        
        use case viewTicker : ViewStockTicker {
            doc /* Primary use case of the stock ticker device. */
        }
    }

    // =========================================================================
    // Logical Design (Technology‑Agnostic)
    // =========================================================================
    package LogicalDesign {
        private import ScalarValues::*;
        private import ISQ::*;
        
        // ---------- Data Definitions ----------
        attribute def StockSymbol :> String;
        attribute def PriceValue :> Real;
        attribute def PercentChange :> Real;
        
        item def StockData {
            attribute symbol : StockSymbol;
            attribute price : PriceValue;
            attribute change : PercentChange;
        }
        
        // ---------- Logical Components ----------
        part def StockTickerSystem {
            doc /* Top‑level logical system. */
            part dataManager : StockDataManager;
            part displayController : DisplayController;
            part inputHandler : ButtonInputHandler;
            part powerController : PowerController;
            
            // simple power port for logical power
            port powerIn : LogicalPower;
        }
        
        part def StockDataManager {
            doc /* Holds the static list of stocks and provides the currently selected entry. */
            attribute stocks : StockData[*] { ordered nonunique }
            attribute selectedIndex : Integer = 0;
            
            action nextStock {
                doc /* Move selection to next stock (wrapping). */
                assign selectedIndex := (selectedIndex + 1) % size(stocks);
            }
            action previousStock {
                doc /* Move selection to previous stock (wrapping). */
                assign selectedIndex := (selectedIndex - 1 + size(stocks)) % size(stocks);
            }
        }
        
        part def DisplayController {
            doc /* Manages what is shown on the screen. */
            
            action updateDisplay {
                in currentStock : StockData;
                doc /* Renders symbol, price, and change on the screen. */
            }
        }
        
        part def ButtonInputHandler {
            doc /* Detects button presses and publishes events. */
            
            port upPress : ButtonEventPort;
            port downPress : ButtonEventPort;
            
            action detectPress {
                doc /* Monitors buttons and triggers appropriate data manager action. */
            }
        }
        
        part def PowerController {
            doc /* Manages power states, battery level, and charging logic. */
            attribute batteryLevel :> ISQ::electricCharge;
        }
        
        // ---------- Logical Ports ----------
        port def LogicalPower {
            doc /* Logical power connection; no direction imposed. */
        }
        
        port def ButtonEventPort {
            doc /* Logical event port for button press signals. */
        }
    }

    // =========================================================================
    // Physical Design (T‑Display S3 Board)
    // =========================================================================
    package PhysicalDesign {
        private import ScalarValues::*;
        private import ISQ::*;
        private import ProjectUnits::*;
        
        part def TDisplayS3Board {
            doc /* LilyGO T‑Display S3 development board. */
            
            part mcu : ESP32S3;
            part display : ST7789Display;
            part buttonUp : PushButton;
            part buttonDown : PushButton;
            part usbConnector : USB_CPort;
            part batteryMgr : BatteryCharger;
            part battery : LiPolyBattery;
            
            // Physical connections (not interfaces, just connectivity)
            connect mcu.displayData to display.dataIn;
            connect mcu.buttonUp to buttonUp.signal;
            connect mcu.buttonDown to buttonDown.signal;
            connect usbConnector.powerOut to batteryMgr.powerIn;
            connect batteryMgr.powerOut to mcu.powerIn;
            connect batteryMgr.batteryPort to battery.power;
        }
        
        part def ESP32S3 {
            doc /* ESP32‑S3 microcontroller. */
            attribute clockSpeed :> ISQ::frequency = 240 [MHz];
            
            port powerIn : PowerInput;
            port displayData : DisplayDataPort;
            port buttonUp : GPIOInput;
            port buttonDown : GPIOInput;
        }
        
        part def ST7789Display {
            doc /* 1.9" TFT LCD with ST7789 controller. */
            port dataIn : DisplayDataPort;
        }
        
        part def PushButton {
            doc /* Physical momentary button. */
            port signal : GPIOInput;
        }
        
        part def USB_CPort {
            doc /* USB‑C connector (power only, no data modelled). */
            port powerOut : PowerOutput;
        }
        
        part def BatteryCharger {
            doc /* Battery charging IC (e.g., TP4054/TP4057) */
            port powerIn : PowerInput;
            port powerOut : PowerOutput;
            port batteryPort : BatteryConnector;
        }
        
        part def LiPolyBattery {
            doc /* Rechargeable Li‑Po battery. */
            attribute capacity :> ISQ::electricCharge = 500 [mAh];   /* typical */
            port power : BatteryConnector;
        }
        
        // ---------- Physical Ports ----------
        port def PowerInput {
            doc /* Physical power input. */
        }
        port def PowerOutput {
            doc /* Physical power output. */
        }
        port def DisplayDataPort {
            doc /* Parallel or SPI data lines for the display. */
        }
        port def GPIOInput {
            doc /* GPIO pin for a button (pull‑up/down not modelled). */
        }
        port def BatteryConnector {
            doc /* Connector for the battery: includes power and charging lines. */
        }
    }

    // =========================================================================
    // Allocations (Logical → Physical)
    // =========================================================================
    package Allocations {
        private import LogicalDesign::*;
        private import PhysicalDesign::*;
        
        // Instantiate the two domains
        part logicalSys : StockTickerSystem;
        part physicalBoard : TDisplayS3Board;
        
        // Mapping logical functions to physical components
        allocate logicalSys.dataManager to physicalBoard.mcu;
        allocate logicalSys.displayController to physicalBoard.display;
        allocate logicalSys.inputHandler to physicalBoard.mcu;   /* MCU debounces & processes */
        allocate logicalSys.powerController to physicalBoard.batteryMgr;
        
        // Also map button inputs
        allocate logicalSys.inputHandler.upPress to physicalBoard.buttonUp.signal;
        allocate logicalSys.inputHandler.downPress to physicalBoard.buttonDown.signal;
    }

    // =========================================================================
    // Views (Base Views + Concrete Views)
    // =========================================================================
    package Views {
        private import DS_Views::SymbolicViewsByExpression::*;
        private import DS_Views::TabularViews::*;
        private import SysML::Systems::*;
        
        doc /* Reusable base views following SysMLv2 best practices. */
        
        package <BV> BaseViews {
            view partsView : UsagesNestedView, EssentialElementsFilter, NonStandardLibraryElementFilter;
            view partsTreeView : TreeView, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @PartDefinition;
                filter @PartUsage;
            }
            view requirementsTreeView : RequirementsTreeView, EssentialElementsFilter, NonStandardLibraryElementFilter;
            view allocationsTableView : gt, EssentialElementsFilter, NonStandardLibraryElementFilter {
                filter @AllocationUsage;
            }
        }
        
        // Concrete views placed near their content
        package RequirementsView {
            view reqTree :> BV::requirementsTreeView {
                expose Requirements::*;
            }
        }
        
        package LogicalDesignView {
            view logicalParts :> BV::partsTreeView {
                expose LogicalDesign::**;
            }
        }
        
        package PhysicalDesignView {
            view physicalParts :> BV::partsTreeView {
                expose PhysicalDesign::**;
            }
        }
        
        package AllocationsView {
            view allocationTable :> BV::allocationsTableView {
                expose Allocations::**;
            }
        }
    }
}