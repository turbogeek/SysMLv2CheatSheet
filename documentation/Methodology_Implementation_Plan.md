# Automating SE Methodology Templates for SysMLv2

This plan outlines the architecture for introducing a secondary `skill.md` file focused strictly on Systems Engineering processes: INCOSE, OOSEM, and MagicGrid.

The goal is to provide markdown templates that a user (or LLM) can fill out. Once filled, these structured markdown documents will guide the generation of a compliant SysMLv2 model.

> [!IMPORTANT]
> **User Review Required**
> Please review the proposed directory structure and the core phases included in each methodology template. If there are specific SysMLv2 mapping patterns you prefer for MagicGrid or OOSEM, let me know in your feedback.

## Open Questions

1.  **SysMLv2 Mapping:** Should the methodology templates include explicit SysMLv2 syntax snippets alongside the prompts, or should they remain purely conceptual (to be translated later by the AI using the primary `skill.md`)?
2.  **Integration:** Should this new generator pipeline (`src_methodology/generate_all.py`) be triggered by the existing root `generate_all.py` and Git hooks, or kept entirely separate?

## Proposed Changes

We will create a new directory structure dedicated to methodology templates to keep them separate from the core SysMLv2 language syntax cheat sheets.

---

### Methodology Source Generators (`src_methodology/`)

We will create Python scripts that generate the Markdown templates. This ensures the templates can be easily maintained and version-controlled, identical to the primary cheat sheet architecture.

#### [NEW] `src_methodology/generate_incose.py`
Generates `incose_template.md` covering standard INCOSE life cycle stages:
*   Business or Mission Analysis
*   Stakeholder Needs and Requirements Definition
*   System Requirements Definition
*   Architecture Definition
*   Design Definition

#### [NEW] `src_methodology/generate_oosem.py`
Generates `oosem_template.md` mapping to OOSEM phases:
*   Analyze Stakeholder Needs
*   Analyze System Requirements
*   Define Logical Architecture
*   Synthesize Candidate Allocated Architectures
*   Optimize and Evaluate Alternatives

#### [NEW] `src_methodology/generate_magicgrid.py`
Generates `magicgrid_template.md` covering the matrix structure:
*   **Problem Domain:** Black-box analysis, Use Cases, Measures of Effectiveness.
*   **Solution Domain:** White-box architecture, Logical structure/behavior.
*   **Implementation Domain:** Specific technology allocations.

#### [NEW] `src_methodology/generate_skill.py`
Compiles the templates and instructions into a master `methodology_skill.md`. This file tells the LLM: "Here are the SE frameworks. When asked to use one, ask the user to fill out the corresponding template, then translate that into SysMLv2."

#### [NEW] `src_methodology/generate_all.py`
The master orchestrator for the methodology templates.

---

### Output Directory (`output_methodology/`)

This directory will hold the generated files.

#### [NEW] `output_methodology/incose_template.md`
#### [NEW] `output_methodology/oosem_template.md`
#### [NEW] `output_methodology/magicgrid_template.md`
#### [NEW] `output_methodology/methodology_skill.md` (The final artifact for the LLM)

## Verification Plan

### Automated Tests
1.  Run `python src_methodology/generate_all.py` to ensure all files generate without errors.
2.  Verify the existence of the 4 files in `output_methodology/`.

### Manual Verification
1.  Read the resulting `methodology_skill.md` to ensure the instructions prompt the LLM appropriately to use the templates.
2.  Provide a sample "filled out" template to the LLM to verify if it can translate the conceptual SE data into valid SysMLv2 using the primary `skill.md` context.
