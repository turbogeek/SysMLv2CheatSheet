# MagicGrid Methodology Template

This template uses the MagicGrid framework (often used with Cameo/MagicDraw) to gather system information. MagicGrid organizes system definition into three Domains (Problem, Solution, Implementation) intersecting with several Pillars (Requirements, Behavior, Structure, Parametrics). Fill out the grid cells below.

## Domain 1: Problem Domain
*Focuses on Stakeholder Needs, System Context, and high-level requirements. What is the problem?*

### 1.1 Requirements (Problem)
*SysMLv2 Mapping: `requirement def`, `use case def`.*
[List high-level stakeholder needs, mission goals, and primary Use Cases]

### 1.2 Behavior (Problem)
*SysMLv2 Mapping: `action def` (representing Black-Box operational scenarios).*
[Describe the high-level operational scenarios and interactions between the system and external actors]

### 1.3 Structure (Problem)
*SysMLv2 Mapping: `part def` for Context.*
[Define the System Context: the System of Interest (SoI) treated as a black-box, and the external environments/actors it connects to]

### 1.4 Parametrics (Problem)
*SysMLv2 Mapping: `attribute def`, MoEs (Measures of Effectiveness).*
[What are the key performance parameters or measures of effectiveness stakeholders care about?]

## Domain 2: Solution Domain
*Focuses on the logical architecture. How do we logically solve the problem without tying to specific technologies?*

### 2.1 Requirements (Solution)
*SysMLv2 Mapping: `requirement def` (System/Subsystem requirements).*
[Derived technical requirements for the system and its logical subsystems]

### 2.2 Behavior (Solution)
*SysMLv2 Mapping: `action def`, `state def`.*
[White-box behavior. Describe the functional flow, state machines, and logical operations of the system's internal subsystems]

### 2.3 Structure (Solution)
*SysMLv2 Mapping: `part def` (Logical blocks), `port def`, `interface def`.*
[Define the Logical Architecture. What are the internal logical subsystems and how are they connected via ports/interfaces?]

### 2.4 Parametrics (Solution)
*SysMLv2 Mapping: `calc def`, `analysis def`, MoPs (Measures of Performance).*
[Define the mathematical constraints, performance roll-ups, and logical system parameters]

## Domain 3: Implementation Domain
*Focuses on the physical architecture and specific technology choices.*

### 3.1 Requirements (Implementation)
*SysMLv2 Mapping: `requirement def` (Component/Hardware/Software requirements).*
[Specific requirements for the physical hardware or software components]

### 3.2 Behavior (Implementation)
*SysMLv2 Mapping: `action def` (allocated to physical parts).*
[Detailed technical behavior specific to the hardware/software implementations]

### 3.3 Structure (Implementation)
*SysMLv2 Mapping: `part def` (Physical blocks).*
[Define the Physical Architecture: specific processors, mechanical parts, software modules, and their physical connections]

### 3.4 Parametrics (Implementation)
*SysMLv2 Mapping: `calc def`, TPMs (Technical Performance Measures).*
[Specific component tolerances, weights, power consumption limits, etc.]

---
**LLM Instruction:** When generating a SysMLv2 model from this MagicGrid template, maintain strict separation between Problem (Context), Solution (Logical), and Implementation (Physical) elements. Ensure robust traceability using `satisfy` (Implementation/Solution -> Problem) and `allocate` (Implementation -> Solution) relationships.
