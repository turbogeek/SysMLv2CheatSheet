# SysMLv2CheatSheet

A comprehensive suite of Cheat Sheets, Tutorials, and Language References for Systems Modeling Language (SysML) v2.0. This project automatically generates and aggregates these resources to serve both human engineers and AI models (LLMs) to ensure valid, accurate SysMLv2 syntax and conventions.

## 🌟 Features

- **Comprehensive Cheat Sheets**: Quick references for modeling syntax, relationships, constraints, state machines, etc.
- **In-Depth Tutorials**: Step-by-step guides on SysMLv2 application (e.g., Use Cases, Connections, Flow, Allocations).
- **Automated Generation**: A robust Python pipeline that ensures documentation and AI context files are always synchronized and up-to-date.
- **AI-Ready Skill File**: A consolidated `skill.md` designed specifically to be injected into LLMs to empower them to act as SysMLv2 experts.

## 🚀 The AI Skill File (`skill.md`)

The crown jewel of this repository is **[`output/skill.md`](output/skill.md)**. 

This file is generated automatically on every commit. It combines the core SysMLv2 Language Reference, all individual cheat sheets, and all tutorials into a single, cohesive context file.

### How to use `skill.md` in LLMs

You can use `skill.md` to give any advanced language model the context it needs to write valid SysMLv2. Here is how to load it into popular systems:

- **Antigravity**: Place `skill.md` in your workspace and reference it directly in your task prompts (e.g., "Use `@skill.md` to ensure the code follows these guidelines"), or add it to your persistent knowledge (`.gemini/antigravity/knowledge/`).
- **Claude (Anthropic)**: Add `skill.md` to your Claude Project Knowledge files, or copy/paste its contents into the "System Prompt" / "Project Instructions". 
- **OpenAI (ChatGPT / Custom GPTs)**: Upload `skill.md` to your Custom GPT's Knowledge Base, or provide it as a file attachment in your chat session.
- **Gemini (Google)**: Upload `skill.md` into your Gemini chat session, or if using Google AI Studio, upload it as a system instruction/context file to inform the model's responses.

## 📂 Quick Links to Resources

Whether you are a human learning the syntax or teaching an AI, you can access the resources directly below:

### 🤖 Core AI File
- **[Comprehensive AI Skill Context (`skill.md`)](output/skill.md)**

### 📚 Aggregated References
- **[SysMLv2 Language Reference](docs/SysMLv2_Language_Reference.md)**
- **[All Cheat Sheets Combined](output/SysMLv2_All_CheatSheets.md)**
- **[All Tutorials Combined](output/SysMLv2_All_Tutorials.md)**

### 📝 Individual Cheat Sheets (Highlights)
- [Behavior Sheet](output/cheatsheets/behavior_sheet.md)
- [Requirements Sheet](output/cheatsheets/requirements_sheet.md)
- [Graphical Notations](output/cheatsheets/graphical_sheet.md)
- [Constraints](output/cheatsheets/constraints_sheet.md)
- [Connections](output/cheatsheets/connections_sheet.md)
- [States](output/cheatsheets/states_sheet.md)
- *(Browse the `output/cheatsheets/` folder for the full list)*

### 📖 Individual Tutorials (Highlights)
- [Use Case Tutorial](output/tutorials/UseCase_Tutorial.md)
- [State Machines Tutorial](output/tutorials/StateMachine_Tutorial.md)
- [Ports & Interfaces](output/tutorials/PortsInterfaces_Tutorial.md)
- [Analysis Tutorial](output/tutorials/Analysis_Tutorial.md)
- [Domain Libraries](output/tutorials/DomainLibs_Tutorial.md)
- *(Browse the `output/tutorials/` folder for the full list)*

## 🛠️ Editing and Building the Docs

**⚠️ IMPORTANT: Do not edit the files in the `output/` directory directly!**  
All files in `output/` (including `skill.md`) are generated automatically. If you edit them, your changes will be overwritten.

### How to Correct or Update Content Using AI:
If you find a missing feature, typo, or want to expand the cheat sheets, you should instruct your AI agent (Antigravity or Claude) to directly modify the source Python files.

**Example Prompt for Antigravity/Claude:**
> *"Antigravity, I need to add a new section on 'Custom Tables' to the tutorial. Please look inside the `src/` directory, create a new `generate_custom_tables.py` script based on the examples in `E:\_Documents\_SysMLV2\_ExampleV2Models\SysMLv2 Features Overview`, add it to `generate_all.py`, and run the build script."*

Or for a correction:
> *"Claude, there is a typo in the Behavior Sheet. Please find `src/generate_behavior_sheet.py`, fix the typo in the markdown string, and run `generate_all.py`."*

**Manual Updating Steps:**
1. **Update the Reference Rules**: Edit `docs/SysMLv2_Language_Reference.md` directly.
2. **Update a Cheat Sheet or Tutorial**: Locate the corresponding Python generator script in the `src/` directory (e.g., `src/generate_behavior_sheet.py`). Open the file and update the markdown strings or python logic inside it.
3. **Add a New Cheat Sheet**: 
   - Create a new `generate_your_topic_sheet.py` in the `src/` folder.
   - Add your new script to the `scripts` list inside `src/generate_all.py`.

### Generating the Updates
If you need help configuring your machine to run the scripts, please see the **[Python Environment Setup Guide](docs/Installation%20Guide/Python_Environment_Setup.md)**.

To manually regenerate all markdown files and the `skill.md` file, run the master script from the root of the repository:

```bash
python generate_all.py
```

*(Note: A pre-commit hook is set up to automatically run this script when you commit. Just making the changes to the `src/` files and committing will automatically rebuild the `output/` folder and `skill.md` for you!)*

## 📁 Repository Structure

To help navigate the project, here is an overview of the key directories:

- **`docs/`** - Hand-written documentation. Includes the Installation Guide, User Guide, and the base `SysMLv2_Language_Reference.md`.
- **`src/`** - Python generator scripts that build the various cheat sheets, tutorials, and aggregate documents.
- **`output/`** - Auto-generated artifacts (Markdown files, SysML code snippets, SVGs, and aggregated tutorials/cheat sheets). *Do not edit files here directly.*
- **`LLM_skills/`** - The "Brain" directory designed for AI consumption. Contains `skill.md`, fixing recipes, methodology skills, and the `Specifications_Markdown/` folder containing the raw OMG specifications.
- **`testModels/`** - Sample SysMLv2 models used for testing and validating syntax.
- **`utilityScripts/`** - Miscellaneous helper scripts, such as validation tools used by the pipeline.
- **`TutorialContent/`** - Supplementary materials, such as presentation slides and lab resources for learning.
