# INCOSE Systems Engineering Template

This template is designed to gather information according to the standard INCOSE Systems Engineering Handbook life cycle stages. Fill out each section as thoroughly as possible. An LLM can then use this document to generate a compliant SysMLv2 model.

## 1. Business or Mission Analysis
*Define the problem space, the organization's strategic goals, and the operational gaps this system is intended to fill.*

### 1.1 Problem Statement
[Describe the problem or opportunity]

### 1.2 Mission Objectives
[List the high-level goals of the system/project]

### 1.3 Key Stakeholders (Business Level)
*SysMLv2 Mapping: `part def` with `actor` or `stakeholder` applied.*
[List primary organizations, sponsors, or user groups]

## 2. Stakeholder Needs and Requirements Definition
*Capture what the stakeholders need the system to do from their perspective, without dictating the technical solution.*

### 2.1 Use Cases / Operational Scenarios
*SysMLv2 Mapping: `use case def`.*
[Describe how stakeholders will interact with the system]

### 2.2 Measures of Effectiveness (MOEs)
*SysMLv2 Mapping: `attribute def` or constraint blocks.*
[List the criteria by which the stakeholders will judge the system's success]

## 3. System Requirements Definition
*Translate stakeholder needs into technical, verifiable system requirements.*

### 3.1 Functional Requirements
*SysMLv2 Mapping: `requirement def`.*
[What the system must do]

### 3.2 Non-Functional / Quality Requirements
*SysMLv2 Mapping: `requirement def`.*
[Performance, safety, security, reliability, etc.]

### 3.3 System Constraints
*SysMLv2 Mapping: `requirement def` or `constraint def`.*
[Design constraints, standards, regulations]

## 4. Architecture Definition
*Define the conceptual and logical layout of the system.*

### 4.1 Logical Architecture / Subsystems
*SysMLv2 Mapping: `part def`.*
[List the major conceptual blocks/subsystems and their responsibilities]

### 4.2 Interfaces and Interactions
*SysMLv2 Mapping: `interface def`, `port def`, `connection`.*
[Describe how the subsystems communicate or exchange matter/energy/data]

### 4.3 System Behavior
*SysMLv2 Mapping: `action def`, `state def`.*
[Describe state transitions, core algorithms, or functional flows]

## 5. Design Definition
*Allocate the logical architecture to specific physical or technical implementations.*

### 5.1 Physical Components
*SysMLv2 Mapping: `part def` (often inheriting from logical parts).*
[List specific hardware, software, or human elements]

### 5.2 Allocation Matrix
*SysMLv2 Mapping: `allocation` relationships or `allocate` dependencies.*
[Describe which physical component satisfies which logical component or requirement]

---
**LLM Instruction:** When processing this file, ensure that every requirement listed in Section 3 has a corresponding `satisfy` relationship from an architectural element in Section 4 or 5.
