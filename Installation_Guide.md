# SysML v2 Automated Validation Pipeline: Installation & Setup Guide

This guide provides step-by-step instructions to set up your environment to use the SysML v2 LLM automated validation pipeline. It covers installing Git, Python, Java (required for the SysML parser), cloning the necessary repositories, and testing your setup.

These instructions assume you are starting from a completely fresh machine.

---

## 1. Prerequisites Download & Installation

The pipeline relies on three core technologies:

* **Git**: To download and manage the repositories.
* **Java (JDK 21+ or Cameo JRE)**: To run the official SysML v2 validator engine.
* **Python (3.10+)**: To run the automation and auto-fix scripts.
* **VS Code (Optional but Recommended)**: As your code editor.

### Windows Setup

#### 1. Install Git

* Go to the [Git for Windows download page](https://gitforwindows.org/).
* Download the installer and run it. You can click "Next" through all the default options.

#### 2. Install Python

* Go to the [Python Downloads page for Windows](https://www.python.org/downloads/windows/).
* Download the latest Python 3.11 or 3.12 installer.
* **CRITICAL:** When you start the installer, check the box at the very bottom that says **"Add Python to PATH"** before clicking "Install Now".

#### 3. Configure Java (via Cameo)

* CATIA Magic (Cameo) ships with its own specific version of Java (e.g., Eclipse Adoptium 21.0.10). Rather than installing a standalone version of Java, you must use the Cameo-provided JRE so your command-line scripts run in the exact same environment.
* Find where Cameo is installed (e.g., `C:\Program Files\Cameo Systems Modeler`).
* In your Windows Search, type **"Environment Variables"** and select "Edit the system environment variables".
* Click **"Environment Variables..."**.
* Under System Variables, click **"New..."** and add:
  * Variable name: `JAVA_HOME`
  * Variable value: `<Your Cameo Install Dir>\jre` (e.g., `C:\Program Files\Cameo Systems Modeler\jre`)
* Next, find the **`Path`** variable, click **"Edit..."**, and add a new entry for `%JAVA_HOME%\bin`.

#### 4. Test Windows Installation

* Open a new Command Prompt (`cmd`) or PowerShell.
* Run the following commands to verify installation:

  ```cmd
  git --version
  python --version
  java -version
  ```

  *(If any of these say "command not found", restart your computer to ensure PATH variables update.)*

---

### macOS (OSX) Setup

The easiest way to install tools on macOS is using **Homebrew**.

#### 1. Install Homebrew (if you don't have it)

* Open the **Terminal** app.
* Paste the following command and press Enter:

  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

#### 2. Install Git and Python

* In the Terminal, run:

  ```bash
  brew install git
  brew install python
  ```

**3. Configure Java (via Cameo)**

* Cameo on macOS also bundles its own JRE inside the application package (e.g., `/Applications/Cameo Systems Modeler.app/Contents/PlugIns/jre/Contents/Home`).
* Add the following to your shell profile (e.g., `~/.zshrc`):

  ```bash
  export JAVA_HOME="/Applications/Cameo Systems Modeler.app/Contents/PlugIns/jre/Contents/Home"
  export PATH="$JAVA_HOME/bin:$PATH"
  ```

#### 4. Test macOS Installation

* Restart your Terminal and run:

  ```bash
  git --version
  python3 --version
  java -version
  ```

  *(Note: On macOS, you will use `python3` instead of `python` in your terminal).*

---

## 2. Cloning the Repositories

You need two repositories: the SysML v2 Reference Implementation (which contains the Java parser) and the CheatSheet/Scripts repository (which contains our Python wrappers).

1. Open your Terminal or Command Prompt.
2. Navigate to your documents folder (or wherever you want to store your code):

   ```bash
   cd Documents
   mkdir git
   cd git
   ```

#### 3. Clone the SysML v2 Implementation:
   * Run the following command to clone the SysML v2 validation engine:

     ```bash
     git clone https://github.com/Systems-Modeling/SysML-v2-Release.git v2Implementation
     ```

   * *(Note: If your organization has a specific fork of the SysML-v2-Release or the validator, use that URL instead).*

#### 4. Clone the LLM Scripts Repository:
   * Clone the repository containing the prompt engineering assets and validation scripts:

     ```bash
     git clone https://github.com/turbogeek/SysMLv2CheatSheet.git SysMLv2CheatSheet
     ```

---

## 3. Validating the Scripts

The Python wrapper script (`validate_model.py`) automatically determines where the Java validator is located.
As long as you cloned both repositories into the same parent folder (e.g., `Documents/git/` as shown in Step 2), the script will correctly find the validator at `../v2Implementation/sysml-validator/validate.cmd` (or `.sh`).

You do **not** need to manually edit paths inside `validate_model.py`.

---

## 4. Installing Antigravity (VS Code Assistant)

To use the automated pipeline efficiently, you will need the **Antigravity** extension for Visual Studio Code. This acts as your intelligent AI pair programmer.

#### 1. Install Antigravity

* Open **Visual Studio Code**.
* Go to the **Extensions** view by clicking the square icon on the left sidebar (or press `Ctrl+Shift+X` on Windows, `Cmd+Shift+X` on macOS).
* Search for **Antigravity** in the marketplace.
* Click **Install**.
* *(Follow any on-screen prompts to sign in or configure your API key).*

#### 2. Create Your Workspace

* Create a new folder on your computer where you want to test and build your models (e.g., `Documents/SysML_Tests`).
* In VS Code, go to **File > Open Folder...** and select the folder you just created.

#### 3. Open Antigravity

* Open the Antigravity chat panel by clicking the Antigravity icon in the sidebar.
* You are now ready to start generating models!

---

## 5. Testing the Pipeline with Antigravity

Let's test the entire pipeline by using Antigravity to generate a simple SysMLv2 model and then validating it.

1. **Ask Antigravity to Generate a Model:**
   In the Antigravity chat panel, paste the following prompt (which instructs the AI to use the cheat sheet files you cloned earlier). *Make sure to update the paths in the prompt to point to your `SysMLv2CheatSheet` folder!*

   > Please create a simple requirements document, logical SysMLv2 model, and physical SysMLv2 model for a simple LED lightbulb. Follow the process in `../git/SysMLv2CheatSheet/LLM_skills/methodology_skill.md`, use the template in `../git/SysMLv2CheatSheet/LLM_Assets/incose_template.md`, and apply the rules in `../git/SysMLv2CheatSheet/LLM_skills/skill.md`. Don't worry about MagicGrid. Use the `validate_model.py` script to validate the model after each iteration.

2. **Save the Output:**
   Antigravity can create files for you automatically. Ask it to save the generated SysMLv2 code into a new file named `test_lightbulb.sysml` in your new workspace folder.

3. **Run the Validator:**
   Open a terminal inside VS Code (`Ctrl+~` or `Terminal > New Terminal`) and run the validation script by pointing it to where you cloned the repository.
   * **Windows:**

     ```cmd
     python ..\git\SysMLv2CheatSheet\validate_model.py test_lightbulb.sysml
     ```

   * **macOS:**

     ```bash
     python3 ../git/SysMLv2CheatSheet/validate_model.py test_lightbulb.sysml
     ```

   *(Be sure to adjust the `../git/` path if you cloned your repository somewhere else!)*

4. **Iterate and Fix:**
   * If the output says `Validation successful: No syntax errors found.`, your installation is perfect!
   * If the output prints out errors (e.g., `ERROR: Line 15...`), copy that exact error output and paste it back to Antigravity. It will use its `fix_recipies.md` knowledge to correct the code and give you a new version. Repeat until it passes!

5. **Teach Antigravity New Tricks (Updating Fix Recipes):**
   SysML v2 is complex, and sometimes Antigravity will encounter an error that it doesn't know how to fix yet. When this happens:
   * Figure out the correct SysML v2 syntax (you can refer to the `SysMLv2_Language_Reference.md` or official docs).
   * Explain the correct fix to Antigravity in the chat.
   * Explictly tell Antigravity: *"Add this problem and solution to `../git/SysMLv2CheatSheet/LLM_skills/fix_recipies.md`."*
   * Antigravity will automatically update the markdown file, so it (and you) will never make that same mistake again!

## 6. Configuring Cameo to run Groovy natively

For Cameo Systems Modeler to fully take advantage of running Groovy from the context of the tool (rather than just from the command line), we need to update its Automation Plugin to load the newly installed Groovy JARs.

Because the Cameo installation directory and Groovy installation directory vary per user, we provide a Python utility script to automate this patching process.

1. Open a terminal (Command Prompt or PowerShell).
2. Run the patching script located in the `src/` directory, providing the paths to your Cameo installation and your Groovy installation:

   ```cmd
   python src\update_cameo_groovy.py --cameo-dir "C:\Program Files\Cameo Systems Modeler" --groovy-dir "C:\Program Files\Groovy"
   ```

*(This script will back up your `plugin.xml`, copy all `.jar` files from the Groovy `lib` folder into the Cameo Automaton plugin, and automatically append them to the `<runtime>` section of the XML configuration).*

## 7. Editing Documentation & Architecture Rules

It is critical to understand how the documentation files in this repository are structured so that any manual edits you make are not overwritten.

* **`LLM_skills/skill.md` (AUTO-GENERATED ⚠️)**: This file is the compiled "brain" for the LLM. It is completely overwritten every time you commit (via `generate_combined_docs.py`). **Do not edit this file directly.**
* **`SysMLv2_Language_Reference.md` (SAFE TO EDIT ✅)**: This is the primary source file for core SysMLv2 syntax rules. Edits made here are automatically embedded at the top of `skill.md` during the next build.
* **`LLM_skills/fix_recipies.md` (SAFE TO EDIT ✅)**: This standalone file contains syntax error solutions and is manually curated.
* **`LLM_skills/pattern_fix_recipies.md` (SAFE TO EDIT ✅)**: Similar to fix recipes, this file contains semantic and pattern-matching rules for errors that the official validator doesn't catch.
* **`src/` python scripts (SAFE TO EDIT ✅)**: If you need to update a tutorial or cheat sheet, you must edit the respective python generator script in the `src/` directory.

## 8. SysMLv2 Test Harness

To test generated `.sysml` code directly within CATIA Magic / Cameo, a local REST API test harness is provided.

1. **Start the Test Harness:**
   * Open Cameo Systems Modeler.
   * Open the Groovy Console or Macro Engine.
   * Load and execute the script: `E:\_Documents\git\sysml-validator\utilityScripts\start-v2language-test-harness.groovy`.
   * The console will output `✅ All REST endpoints registered successfully. Server active on port 8770.`

2. **Automated Testing:**
   * Once the harness is running, you or the AI agent can send a `POST` request to `http://localhost:8770/load-sysml`.
   * The body should be JSON containing the SysML code: `{"sysmlText": "package Test {}"}` or a file path `{"filePath": "C:/path/to/test.sysml"}`.
   * The harness will use the Cameo `SysMLTransientModelBuilder` API to parse and load the file, returning any syntax or compilation errors directly in the HTTP response.

3. **Stop the Test Harness:**
   * When finished, run the stop script: `E:\_Documents\git\sysml-validator\utilityScripts\stop-v2language-test-harness.groovy`.
   * This sends a clean shutdown command to the active server.

### Troubleshooting

* **"Java is not recognized..."**: Ensure you installed JDK 17 and added it to your PATH environment variable.
* **"Validator script not found..."**: Double-check that you cloned the `v2Implementation` repository exactly at the same folder level as `SysMLv2CheatSheet`.
* **"Python is not recognized..."**: Re-run the Python installer and check "Add Python to PATH".

---
*Generated by the automated SysML v2 Pipeline Assistant*
