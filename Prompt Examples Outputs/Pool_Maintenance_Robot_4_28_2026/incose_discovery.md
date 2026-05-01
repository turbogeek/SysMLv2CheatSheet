# INCOSE Systems Engineering Template: Pool Maintenance Robot

## 1. Business or Mission Analysis

### 1.1 Problem Statement
Maintaining proper pool chemistry (specifically chlorine levels) is a tedious and complex task for homeowners. Factors such as pool shape, volume, temperature, rain, and evaporation constantly alter the chemical balance, leading to either unsanitary conditions or over-chlorination. There is a need for an automated system that can accurately calculate and dispense the required amount of chlorine tablets based on environmental variables.

### 1.2 Mission Objectives
- To automate the sanitization of residential pools.
- To accurately calculate the required chlorine based on pool type (Play, Kidney, Rectangular), pool size, and environmental factors (Temperature, Rain, Evaporation).
- To dispense the calculated amount of chlorine tablets automatically.
- To provide an easy-to-understand interface for users to input their pool specifics.

### 1.3 Key Stakeholders (Business Level)
- Homeowners / Pool Owners (Primary Users)
- Pool Maintenance Services (Secondary Users/Distributors)
- Environmental Regulators (Safety and Chemical handling)

## 2. Stakeholder Needs and Requirements Definition

### 2.1 Use Cases / Operational Scenarios
- **Calculate Initial Sanitization**: User inputs pool shape and dimensions; the system calculates the base volume and the initial number of chlorine tablets needed.
- **Adjust for Environment**: The robot senses or receives data regarding temperature, rainfall, and evaporation rates, and recalculates the dynamic chlorine requirement.
- **Dispense Chemicals**: The robot navigates the pool and dispenses the calculated number of tablets safely.
- **User Setup**: User selects the type of chlorine tablet being used (e.g., 3-inch Trichlor).

### 2.2 Measures of Effectiveness (MOEs)
- Accuracy of volume calculation (must be within 5% of actual pool volume).
- Sanitization effectiveness (pool maintains 1-3 ppm Free Chlorine).
- User interaction time (setup should take less than 5 minutes).

## 3. System Requirements Definition

### 3.1 Functional Requirements
- **FR.01**: The system shall calculate the volume of a Rectangular, Play, or Kidney shaped pool based on user dimension inputs.
- **FR.02**: The system shall calculate the base number of chlorine tablets required based on pool volume.
- **FR.03**: The system shall adjust the required chlorine amount based on ambient temperature.
- **FR.04**: The system shall adjust the required chlorine amount based on recent rainfall volume.
- **FR.05**: The system shall adjust the required chlorine amount based on evaporation rates.
- **FR.06**: The system shall dispense the calculated number of chlorine tablets into the pool.

### 3.2 Non-Functional / Quality Requirements
- **NFR.01 (Safety)**: The robot shall securely store chemical tablets to prevent accidental exposure to children or pets.
- **NFR.02 (Reliability)**: The calculation algorithm shall execute with 99.9% uptime and zero arithmetic overflow errors.

### 3.3 System Constraints
- **CON.01**: The robot must operate within standard residential pool environments (freshwater or saltwater).

## 4. Architecture Definition

### 4.1 Logical Architecture / Subsystems
- **UserInterfaceSubsystem**: Handles input of pool shape, dimensions, and chlorine type.
- **ChemistryEngineSubsystem**: Performs calculations for volume and dynamic chemical requirements.
- **EnvironmentalSensorSubsystem**: Measures temperature, rainfall, and evaporation.
- **DispenserSubsystem**: Physically holds and dispenses the tablets.

### 4.2 Interfaces and Interactions
- **UI to ChemistryEngine**: Sends pool dimensions and shape data.
- **Sensor to ChemistryEngine**: Sends environmental modifier data.
- **ChemistryEngine to Dispenser**: Sends the calculated number of tablets to dispense.

### 4.3 System Behavior
- **State 1**: Idle/Waiting for Input.
- **State 2**: Calculating Volume.
- **State 3**: Monitoring Environment & Calculating Dynamic Load.
- **State 4**: Dispensing.

### 4.4 Specific Analysis Goals
- **Chemistry Analysis Goal**: Ensure the `calc def` for chlorine accurately scales up for high temperatures and scales down (or adjusts) for rain dilution.
- **Cost Analysis Goal**: Track the number of tablets dispensed to estimate monthly maintenance costs.

## 5. Design Definition

### 5.1 Physical Components
- **Microcontroller Unit (MCU)**: Hosts the ChemistryEngine logic.
- **Waterproof Touch Screen**: Implements the User Interface.
- **Thermometer & Rain Gauge**: Implements the Environmental Sensors.
- **Motorized Hopper**: Implements the Dispenser Subsystem.

### 5.2 Allocation Matrix
- **MCU** satisfies **ChemistryEngineSubsystem**.
- **Motorized Hopper** satisfies **DispenserSubsystem**.

### 5.3 Tradeoff Studies
- **Tradeoff 1 (Dispenser Mechanism)**: Rotary dial vs. gravity trapdoor. Rotary dial selected for precise tablet counting, satisfying FR.06 and NFR.01.
