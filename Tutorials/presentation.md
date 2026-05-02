---
marp: true
paginate: true
theme: default
style: |
  section {
    background-color: #f8fafc;
    color: #1e293b;
    font-family: 'Inter', sans-serif;
  }
  h1, h2, h3 {
    color: #005386;
    font-family: 'Outfit', sans-serif;
  }
  .error { color: #ef4444; font-weight: bold; }
  .success { color: #10b981; font-weight: bold; }
  .highlight { color: #00A3E0; font-weight: bold; }
---

# Automating SysMLv2 Modeling with AI
Bridging Model-Based Systems Engineering and AI with Antigravity
**SysMLv2 Cheat Sheet Project**

---

## 1. Introduction: Why build this?
- **The Challenge:** SysMLv2 textual modeling syntax is strictly typed and has a steep learning curve.
- **The Solution:** Leverage AI (Antigravity/Gemini) alongside the Model Context Protocol (MCP) to automate the authoring of SysMLv2 models.
- **Methodologies:** Incorporates industry-standard workflows like INCOSE, OOSEM, and MagicGrid via Markdown templates.
- **Goal:** Enable rapid, validated system architecture prototyping with zero syntax errors.

---

## 2. System Architecture & Requirements
- **Local Validation Pipeline:** Python wrappers (`validate_model.py`) run the official Java-based SysMLv2 engine locally to verify AI outputs.
- **Dynamic Paths:** The setup dynamically discovers the `sysml-validator` as long as repositories share the same root folder.
- **AI "Brain":** The repository compiles `SysMLv2_Language_Reference.md` and `fix_recipies.md` into a single `skill.md` for the LLM.
- **Iterative Loop:** Generate -> Test (Parse) -> Fix -> Validate.

---

## 3. Key SysMLv2 Code Snippets
### Definitions vs. Usages (Pool Maintenance Robot)
```sysml
    package LogicalArchitecture {
        // Definition
        part def ChemistryEngine {
            attribute currentTemp : Real [1];
            attribute poolVolume : Real [1];
            satisfy ChlorineCalculationReq;
        }

        part def PoolMaintenanceRobot {
            // Usage
            part engine : ChemistryEngine;
            part sensors : EnvironmentalSensor;
            
            // Connection
            connection sensorToEngine connect sensors to engine;
        }
    }
```

---

## 4. Requirement Satisfaction
```sysml
    package Requirements {
        requirement def ChlorineCalculationReq {
            doc /* The system shall calculate the base number of chlorine tablets required based on pool volume. */
        }
    }
```
*Note: The Logical `ChemistryEngine` satisfies the requirement via the `satisfy ChlorineCalculationReq;` keyword.*

---

## 5. The AI Workflow (MCP + Antigravity)
1. **Prompt Engineering:** AI receives the INCOSE template and methodology skills.
2. **Generation:** AI authors the `.sysml` file.
3. **Execution:** AI triggers `validate_model.py` via the terminal tool.
4. **Validation:** Java SysML parser checks for errors.
5. **Auto-Correction:** If errors exist, AI consults `fix_recipies.md` and patches the code until successful.

---

## 6. Gotchas & Lessons Learned
- <span class="error">Error:</span> Missing standard library imports.
  - <span class="success">Solution:</span> Always include `private import ScalarValues::*;` or `ISQ::*`.
- <span class="error">Error:</span> Confusing Part Definitions with Part Usages.
  - <span class="success">Solution:</span> Use `part def` for types and `part name : Type` inside assemblies.
- <span class="highlight">Pattern Matching:</span> We developed `pattern_fix_recipies.md` to catch semantic errors that the Java parser misses.

---

## 7. Conclusion & Next Steps
- The test harness is fully self-contained and path-agnostic.
- The next phase involves extending visual rendering (e.g., Matrix Views, MagicDraw integrations).
- **Call to Action:** Explore the `Labs` directory to see the generated models (e.g., *Alarm Clock*, *Drone*, *Toaster*, *Pool Robot*).
