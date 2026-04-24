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
- **[SysMLv2 Language Reference](SysMLv2_Language_Reference.md)**
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
- [Use Case Tutorial](output/tutorials/use_case_tutorial.md)
- [State Machines Tutorial](output/tutorials/state_machines_tutorial.md)
- [Ports & Interfaces](output/tutorials/ports_interfaces_tutorial.md)
- [Analysis Tutorial](output/tutorials/analysis_tutorial.md)
- [Domain Libraries](output/tutorials/domain_libs_tutorial.md)
- *(Browse the `output/tutorials/` folder for the full list)*

## 🛠️ Building the Docs

To manually regenerate all markdown files and the `skill.md` file:

```bash
cd src
python generate_all.py
```

*(Note: A pre-commit hook is set up to automatically run this script when you commit, so your files will always be up to date in the repository.)*
