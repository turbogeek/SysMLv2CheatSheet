# INCOSE Systems Engineering Discovery Document - Simple Alarm Clock

## 1. Business or Mission Analysis

### 1.1 Problem Statement

People need a reliable and user-friendly way to wake up at a specific time or be reminded of events without manually monitoring the time. Additionally, they need basic environmental safety monitoring (e.g., fire detection) integrated into their bedside devices, reducing the need for multiple standalone smart home hubs.

### 1.2 Mission Objectives

Provide an integrated smart alarm clock that:

- Accurately displays the current time, date, and timezone.
- Allows the user to set a specific alarm time, as well as snooze or stop it.
- Sounds a noticeable alarm when the current time matches the set alarm time.
- Detects smoke or fire and alerts the user immediately, mirroring the reliability of dedicated devices.

### 1.3 Key Stakeholders (Business Level)

- **User**: The person who uses the clock to wake up, be reminded, and stay safe.
- **Manufacturer**: The company producing the alarm clock (e.g., Philips, Sony).
- **Safety Regulators**: Entities ensuring the fire detection meets minimum residential safety standards (e.g., UL, NFPA).

## 2. Stakeholder Needs and Requirements Definition

### 2.1 Use Cases / Operational Scenarios

- **View Time**: The user looks at the clock's display to know the current time.
- **Set Alarm**: The user inputs the desired wake-up time via the clock's interface.
- **Sound Alarm**: The clock detects that the current time matches the alarm time and produces a loud sound to alert the user.
- **Stop Alarm**: The user stops the alarm when it sounds.
- **Snooze Alarm**: The user snoozes the alarm when it sounds.
- **Set Time**: The user sets the current time.
- **Set Date**: The user sets the current date.
- **Set Timezone**: The user sets the current timezone.
- **Fire Alarm**: The clock detects smoke and fire and alerts the user.

### 2.2 Measures of Effectiveness (MOEs)

- **Time Accuracy**: The clock must maintain time accurately to within a minute per month.
- **Alarm Volume**: The alarm sound must be loud enough to wake a sleeping person (e.g., >70 dB for wake-up, >85 dB for fire).
- **Usability**: The interface for setting the alarm and adjusting time/date must be intuitive.
- **Safety**: The fire detection must be reliable, utilizing photoelectric sensing, and trigger within seconds of smoke detection.

## 3. System Requirements Definition

### 3.1 Functional Requirements

- **REQ_FUNC_01 (Display Time)**: The system shall display the current time continuously.
- **REQ_FUNC_02 (Set Alarm)**: The system shall allow the user to set an alarm time.
- **REQ_FUNC_03 (Sound Alarm)**: The system shall sound an alarm when the current time matches the alarm time.
- **REQ_FUNC_04 (Stop Alarm)**: The system shall allow the user to stop an active alarm.
- **REQ_FUNC_05 (Snooze Alarm)**: The system shall allow the user to snooze an active alarm, temporarily silencing it.
- **REQ_FUNC_06 (Set Time/Date)**: The system shall allow the user to set the current time, date, and timezone.
- **REQ_FUNC_07 (Detect Fire)**: The system shall monitor the environment for smoke or fire.
- **REQ_FUNC_08 (Fire Alarm Alert)**: The system shall trigger a distinct, high-priority alarm when fire is detected.

### 3.2 Non-Functional / Quality Requirements

- **REQ_NF_01 (Volume)**: The standard alarm shall be at least 70 dB, and the fire alarm at least 85 dB.
- **REQ_NF_02 (Reliability)**: The system shall trigger the alarm accurately when the set time arrives.
- **REQ_NF_03 (Fire Sensor Reliability)**: The fire detection system must operate with high reliability and minimal false positives, compliant with UL 217.

### 3.3 System Constraints

- **REQ_CON_01 (Power)**: The system must operate on standard household power with a CR2032 battery backup.

## 4. Architecture Definition

### 4.1 Logical Architecture / Subsystems

- **Timekeeping Subsystem**: Keeps track of the current time, date, and timezone.
- **Display Subsystem**: Visually shows the time and date to the user.
- **Alarm Subsystem**: Compares current time with the set alarm time, handles snooze/stop logic, and triggers the alarm.
- **User Interface Subsystem**: Captures user inputs for setting time, date, timezone, and alarm controls (snooze/stop).
- **Environmental Monitoring Subsystem**: Detects smoke and fire in the environment.
- **Sound Subsystem**: Produces auditory alerts for wake-up and fire alarms.

### 4.2 Interfaces and Interactions

- The **User Interface Subsystem** provides user inputs (time settings, alarm settings, snooze, stop) to the **Alarm Subsystem** and **Timekeeping Subsystem**.
- The **Timekeeping Subsystem** sends the current time to the **Display Subsystem** and the **Alarm Subsystem**.
- The **Environmental Monitoring Subsystem** sends a high-priority fire trigger signal to the **Alarm Subsystem**.
- The **Alarm Subsystem** sends trigger signals (wake-up or fire) to the **Sound Subsystem**.

### 4.3 System Behavior

- **Normal State**: Displaying the time.
- **Setting State**: User is setting the time, date, timezone, or alarm.
- **Alarming State**: The wake-up alarm is sounding.
- **Snoozing State**: The wake-up alarm is temporarily paused.
- **Fire Alarming State**: A critical, high-priority fire alarm is sounding.

## 5. Design Definition (Down-Selected Components)

To meet the requirements, specific commercial-off-the-shelf (COTS) components and manufacturers have been down-selected for the physical implementation.

### 5.1 Physical Components

- **ESP32 Microcontroller (Espressif)**: Acts as the central processor, managing timekeeping via NTP over Wi-Fi and core system logic.
- **Philips Segmented LED Display**: The physical screen showing the time clearly in low-light conditions.
- **Murata Piezo Buzzer**: The component producing the sound, capable of reaching >85 dB for fire alerts.
- **Omron Tactile Switches**: Physical interfaces for user input, including a large, durable Snooze button.
- **First Alert Photoelectric Sensor**: A reliable physical sensor for detecting smoke particles with fewer false alarms from cooking.
- **Mean Well 5V AC/DC Power Supply**: Provides stable electrical power to components, integrated with a CR2032 battery backup circuit.

### 5.2 Allocation Matrix

- **ESP32 Microcontroller** satisfies the **Timekeeping Subsystem** and **Alarm Subsystem**.
- **Philips Segmented LED Display** satisfies the **Display Subsystem**.
- **Murata Piezo Buzzer** satisfies the **Sound Subsystem**.
- **Omron Tactile Switches** satisfy the **User Interface Subsystem**.
- **First Alert Photoelectric Sensor** satisfies the **Environmental Monitoring Subsystem**.
