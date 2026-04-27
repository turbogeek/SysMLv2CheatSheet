# INCOSE Systems Engineering Template: Hobbyist Drone

## 1. Business or Mission Analysis

### 1.1 Problem Statement

Consumers want an affordable, easy-to-use hobbyist drone that can be controlled via a smartphone app to capture high-quality video, without requiring extensive training or expensive dedicated controllers.

### 1.2 Mission Objectives

- Deliver a drone capable of flying, hovering, and landing.
- Capture and stream video to a smartphone.
- Keep the retail price at or below $500.
- Provide intuitive control via an iOS/Android application.

### 1.3 Key Stakeholders (Business Level)

- Hobbyist Pilot (End User)
- General Public (Safety and Privacy concerns)
- Regulatory Bodies (e.g., FAA for weight limits and airspace)
- Manufacturer/Business Unit

## 2. Stakeholder Needs and Requirements Definition

### 2.1 Use Cases / Operational Scenarios

- **Setup and Pairing**: User pairs the smartphone app with the drone via Wi-Fi/Bluetooth.
- **Takeoff**: User commands the drone to take off, and it ascends to a stable hover height.
- **Hover**: Drone maintains a stable position and altitude when no directional commands are given.
- **Maneuver**: User pilots the drone (pitch, roll, yaw, throttle) via the app.
- **Record Video**: User starts and stops video recording; video is saved or streamed.
- **Land**: User commands the drone to land safely.
- **Follow Me**: User commands the drone to follow them using visual tracking.
- **Return to Home**: User commands the drone to return to the takeoff position.

### 2.2 Measures of Effectiveness (MOEs)

- Cost to consumer <= $500
- Flight time > 15 minutes per battery
- Video resolution >= 1080p
- App latency < 100ms
- Hover stability within 0.5 meters

## 3. System Requirements Definition

### 3.1 Functional Requirements

- REQ-FUN-01 (Flight Control): The system shall accept directional inputs (pitch, roll, yaw, altitude) from the smartphone app.
- REQ-FUN-02 (Takeoff and Landing): The system shall provide automated takeoff and landing functions.
- REQ-FUN-03 (Hovering): The system shall automatically maintain a stable hover when user inputs are neutral.
- REQ-FUN-04 (Video Capture): The system shall record and stream video to the connected app.
- REQ-FUN-05 (Follow Me): The system shall track and follow the user using visual tracking.
- REQ-FUN-06 (Return to Home): The system shall autonomously return to its takeoff position when commanded.

### 3.2 Non-Functional / Quality Requirements

- REQ-PRF-01 (Endurance): The drone shall have a maximum flight time of at least 15 minutes.
- REQ-PRF-02 (Video Quality): The camera shall capture video at a minimum resolution of 1080p.
- REQ-CST-01 (Cost): The total unit retail price shall not exceed $500.

### 3.3 System Constraints

- REQ-CON-01 (Weight): The drone takeoff weight shall be under 250 grams to avoid FAA registration requirements.
- REQ-CON-02 (Communication): The drone shall use standard Wi-Fi protocols for communication with the smartphone.

## 4. Architecture Definition

### 4.1 Logical Architecture / Subsystems

- **Flight Controller Subsystem**: Manages stabilization, motor mixing, and flight modes.
- **Navigation Subsystem**: Manages positioning, pathfinding, and visual tracking algorithms.
- **Communication Subsystem**: Handles wireless data exchange with the smartphone.
- **Power Subsystem**: Provides and distributes electrical power.
- **Payload Subsystem**: Captures and processes video.
- **Propulsion Subsystem**: Provides thrust and attitude control.

### 4.2 Interfaces and Interactions

- **Comm_to_FlightCtrl**: Communication subsystem sends user commands to the Flight Controller.
- **FlightCtrl_to_Propulsion**: Flight Controller sends PWM/DShot signals to motors.
- **Payload_to_Comm**: Payload subsystem sends video stream to Communication subsystem.
- **Payload_to_Nav**: Payload subsystem sends video data to Navigation subsystem for visual tracking.
- **Nav_to_FlightCtrl**: Navigation subsystem sends positioning and steering commands to Flight Controller.

### 4.3 System Behavior

- Operating States: Off, Booting, Idle/Paired, Flying, Hovering, Landing, Emergency Stop.
- The user triggers 'Takeoff', the system transitions from Idle to Flying/Hovering.

## 5. Design Definition

### 5.1 Physical Components

- **Microcontroller Unit (MCU)**: Serves as the Flight Controller.
- **GPS Module**: Provides geographical positioning data.
- **Vision Processing Unit (VPU)**: Handles visual tracking algorithms.
- **Wi-Fi Module**: Implements the Communication Subsystem.
- **LiPo Battery**: Implements the Power Subsystem.
- **Camera Module**: Implements the Payload Subsystem.
- **Brushless Motors & ESCs**: Implements the Propulsion Subsystem.
- **Smartphone**: User interface device.

### 5.2 Allocation Matrix

- MCU allocates to Flight Controller Subsystem.
- GPS Module allocates to Navigation Subsystem.
- Vision Processing Unit (VPU) allocates to Navigation Subsystem.
- Wi-Fi Module allocates to Communication Subsystem.
- Camera Module allocates to Payload Subsystem.
- Brushless Motors allocate to Propulsion Subsystem.
- LiPo Battery allocates to Power Subsystem.
