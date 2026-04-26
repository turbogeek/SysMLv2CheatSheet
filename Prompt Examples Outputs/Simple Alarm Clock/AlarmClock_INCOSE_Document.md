# INCOSE Systems Engineering Template: Simple Alarm Clock

## 1. Business or Mission Analysis

### 1.1 Problem Statement
Users need a reliable and simple way to keep track of the current time and be awakened at a specific pre-set time. Traditional methods or smart devices might be overly complex or prone to failure if power is lost or they require extensive configuration. The proposed simple alarm clock provides a dedicated, easy-to-use device for these essential functions.

### 1.2 Mission Objectives
- To display the current time clearly and accurately.
- To allow the user to easily set an alarm time.
- To sound an audible alarm when the current time matches the set alarm time.
- To provide a simple means to disable the alarm.

### 1.3 Key Stakeholders (Business Level)
*SysMLv2 Mapping: `part def` with `actor` or `stakeholder` applied.*
- **User / Sleeper:** The primary person using the alarm clock to wake up on time.
- **Manufacturer:** The organization building and selling the alarm clock.

## 2. Stakeholder Needs and Requirements Definition

### 2.1 Use Cases / Operational Scenarios
*SysMLv2 Mapping: `use case def`.*
- **View Time:** The User observes the current time displayed on the clock.
- **Set Alarm:** The User interacts with the clock's interface to specify the desired wake-up time.
- **Wake Up / Sound Alarm:** The system automatically sounds an alert when the alarm time is reached.
- **Dismiss Alarm:** The User turns off the sounding alarm.

### 2.2 Measures of Effectiveness (MOEs)
*SysMLv2 Mapping: `attribute def` or constraint blocks.*
- **Time Accuracy:** The clock must not deviate more than 1 minute per month.
- **Alarm Volume:** The alarm must be loud enough to wake a sleeping user (e.g., > 70 dB).
- **Usability:** The process of setting an alarm should take less than 15 seconds for an average user.

## 3. System Requirements Definition

### 3.1 Functional Requirements
*SysMLv2 Mapping: `requirement def`.*
- **REQ-FUNC-01 (Display Time):** The system shall continuously display the current time in hours and minutes.
- **REQ-FUNC-02 (Set Alarm Time):** The system shall provide a mechanism for the user to set an alarm time.
- **REQ-FUNC-03 (Trigger Alarm):** The system shall trigger an audible alarm when the current time matches the set alarm time.
- **REQ-FUNC-04 (Dismiss Alarm):** The system shall provide a mechanism to stop the audible alarm once it is triggered.

### 3.2 Non-Functional / Quality Requirements
*SysMLv2 Mapping: `requirement def`.*
- **REQ-PERF-01 (Volume):** The alarm volume shall be at least 70 dB measured at a distance of 1 meter.
- **REQ-PERF-02 (Accuracy):** The internal clock shall maintain time with an accuracy of +/- 1 minute per month.
- **REQ-ELEC-01 (Power Source):** The system shall operate on standard household AC power with an optional battery backup.

### 3.3 System Constraints
*SysMLv2 Mapping: `requirement def` or `constraint def`.*
- **CON-01 (Size):** The system footprint shall not exceed 15 cm x 15 cm to fit on a standard nightstand.

## 4. Architecture Definition

### 4.1 Logical Architecture / Subsystems
*SysMLv2 Mapping: `part def`.*
- **Logical System:** `LogicalAlarmClock`
- **Subsystem 1:** `Timekeeper` - Maintains current time and alarm time.
- **Subsystem 2:** `UserInterface` - Handles inputs (setting time/alarm, dismissing alarm) and outputs (displaying time).
- **Subsystem 3:** `AlarmTrigger` - Compares current time to alarm time and controls the sound emission.

### 4.2 Interfaces and Interactions
*SysMLv2 Mapping: `interface def`, `port def`, `connection`.*
- `UserInterface` sends 'SetAlarmTime' data to `Timekeeper`.
- `Timekeeper` continuously provides 'CurrentTime' and 'AlarmTime' to `AlarmTrigger`.
- `AlarmTrigger` sends 'SoundSignal' to the `UserInterface` (specifically, its sound output component).

### 4.3 System Behavior
*SysMLv2 Mapping: `action def`, `state def`.*
- **State: NormalOperation:** Clock is displaying time.
- **State: AlarmSounding:** Alarm has been triggered and is sounding.
- **Transition:** NormalOperation -> AlarmSounding (triggered when CurrentTime == AlarmTime).
- **Transition:** AlarmSounding -> NormalOperation (triggered by User dismissing alarm).

## 5. Design Definition

### 5.1 Physical Components
*SysMLv2 Mapping: `part def` (often inheriting from logical parts).*
- **Physical System:** `PhysicalAlarmClock`
- **Component 1:** `Microcontroller` (Realizes Timekeeper and AlarmTrigger logic)
- **Component 2:** `LED_Display` (Realizes visual part of UserInterface)
- **Component 3:** `Buzzer` (Realizes audio part of UserInterface/AlarmTrigger)
- **Component 4:** `Buttons` (Realizes input part of UserInterface)
- **Component 5:** `PowerSupply` (AC adapter and battery backup)

### 5.2 Allocation Matrix
*SysMLv2 Mapping: `allocation` relationships or `allocate` dependencies.*
- `PhysicalAlarmClock` -> `LogicalAlarmClock`
- `Microcontroller` -> `Timekeeper`
- `Microcontroller` -> `AlarmTrigger`
- `LED_Display` -> `UserInterface` (visual output)
- `Buzzer` -> `UserInterface` (audio output)
- `Buttons` -> `UserInterface` (inputs)

---
**LLM Instruction:** When processing this file, ensure that every requirement listed in Section 3 has a corresponding `satisfy` relationship from an architectural element in Section 4 or 5.
