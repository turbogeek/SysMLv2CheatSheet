# Simple Alarm Clock INCOSE Systems Engineering Document

## 1. Business or Mission Analysis

### 1.1 Problem Statement

Users need a reliable, standalone device to wake them up at a specified time to maintain their daily schedules without relying exclusively on complex or distraction-prone devices like smartphones.

### 1.2 Mission Objectives

* Provide a clear, readable display of the current time.
* Allow users to easily set a specific alarm time.
* Sound a noticeable auditory alert when the current time matches the alarm time.

### 1.3 Key Stakeholders (Business Level)

* Primary Users (People waking up)
* Manufacturers
* Retailers
* Service Technicians
* Regulatory Agencies
* Component Suppliers

## 2. Stakeholder Needs and Requirements Definition

### 2.1 Use Cases / Operational Scenarios

* **UC1: Check Time** - User looks at the device to see the current time.
* **UC2: Set Alarm** - User inputs a specific time into the device to trigger an alert.
* **UC3: Wake Up** - The device sounds an alarm at the set time, waking the user. User disables the alarm.
* **UC4: Snooze Alarm** - User presses the snooze button to silence the alarm for 9 minutes.

### 2.2 Measures of Effectiveness (MOEs)

* Time accuracy (drift per month).
* Alarm volume (decibels at 1 meter).
* Display visibility (viewing angle and brightness).

## 3. System Requirements Definition

### 3.1 Functional Requirements

* The system shall display the current time.
* The system shall allow the user to set an alarm time.
* The system shall sound an alarm when the current time matches the alarm time.
* The system shall provide a mechanism to turn off the active alarm.

### 3.2 Non-Functional / Quality Requirements

* The alarm volume shall be at least 70 dB.
* The time display shall be visible in a dark room.
* The system shall be energy efficient, consuming no more than 5 watts of power.
* The system shall be reliable, operating for at least 5 years without failure.
* The system shall be maintainable, allowing for easy repair or replacement of components.

### 3.3 System Constraints

* The system shall operate on standard 120V AC wall power.
* The system shall be housed in a case with dimensions no larger than 10cm x 10cm x 10cm.
