import os

def generate():
    content = """# OOSEM (Object-Oriented Systems Engineering Method) Template

This template gathers information structured around the core OOSEM phases. Fill out the relevant sections to define the system. An LLM will use this to generate a SysMLv2 model that maps these object-oriented engineering concepts into valid SysML constructs.

## 1. Analyze Stakeholder Needs
*Define the enterprise environment, the problem, and the system context (black-box).*

### 1.1 As-Is / To-Be Enterprise
[Describe the current state of the enterprise and the desired future state after system deployment]

### 1.2 System Context & External Systems
*SysMLv2 Mapping: `part def` for the System of Interest (SoI) and external interacting parts.*
[Identify the System of Interest (SoI) and the external systems/actors it interacts with]

### 1.3 Mission Use Cases
*SysMLv2 Mapping: `use case def`.*
[High-level scenarios describing the system's operational use]

## 2. Analyze System Requirements
*Translate needs into a formal set of system requirements.*

### 2.1 Functional Requirements
*SysMLv2 Mapping: `requirement def`.*
[What the system must functionally achieve]

### 2.2 Performance / Quality Requirements
*SysMLv2 Mapping: `requirement def` with associated `attribute def` for metrics.*
[Constraints, timing, performance metrics]

## 3. Define Logical Architecture
*Decompose the system into logical, technology-independent components.*

### 3.1 Logical Subsystems / Blocks
*SysMLv2 Mapping: `part def` (Logical).*
[List the internal logical blocks that make up the system]

### 3.2 Logical Interfaces
*SysMLv2 Mapping: `interface def`, `port def`.*
[How do the logical blocks communicate? What data/items flow between them?]

### 3.3 Logical Behavior
*SysMLv2 Mapping: `state def`, `action def`.*
[Describe the state machines or activity workflows for the logical blocks]

## 4. Synthesize Candidate Allocated Architectures
*Propose physical/technology-specific architectures that implement the logical architecture.*

### 4.1 Physical Nodes / Components
*SysMLv2 Mapping: `part def` (Physical).*
[Hardware, software components, or human roles]

### 4.2 Allocation Matrix
*SysMLv2 Mapping: `allocation` or `allocate` dependencies.*
[Map which physical component is responsible for which logical block or behavior]

## 5. Optimize and Evaluate Alternatives
*If there are multiple candidate architectures, provide data for trade studies.*

### 5.1 Trade Study Metrics (MoEs / MoPs)
*SysMLv2 Mapping: `analysis def`, `calc def`.*
[List the criteria used to select the best architecture: Cost, Weight, Power, Reliability, etc.]

### 5.2 Selected Architecture Justification
[Briefly explain why the chosen physical architecture was selected]

---
**LLM Instruction:** When generating SysMLv2 from this template, utilize block-based decomposition (`part def` and `part`) to emphasize the object-oriented structure. Ensure that logical behaviors (actions/states) are explicitly allocated to physical parts.
"""
    
    os.makedirs(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'LLM_Assets'), exist_ok=True)
    with open(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'LLM_Assets'), 'oosem_template.md'), 'w') as f:
        f.write(content)
        
if __name__ == '__main__':
    generate()
