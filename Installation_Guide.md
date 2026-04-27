# SysML v2 Automated Validation Pipeline: Installation & Setup Guide

This guide provides step-by-step instructions to set up your environment to use the SysML v2 LLM automated validation pipeline. It covers installing Git, Python, Java (required for the SysML parser), cloning the necessary repositories, and testing your setup.

These instructions assume you are starting from a completely fresh machine. 

---

## 1. Prerequisites Download & Installation

The pipeline relies on three core technologies:
* **Git**: To download and manage the repositories.
* **Java (JDK 17+)**: To run the official SysML v2 validator engine.
* **Python (3.10+)**: To run the automation and auto-fix scripts.
* **VS Code (Optional but Recommended)**: As your code editor.

### Windows Setup

**1. Install Git**
* Go to the [Git for Windows download page](https://gitforwindows.org/).
* Download the installer and run it. You can click "Next" through all the default options.

**2. Install Python**
* Go to the [Python Downloads page for Windows](https://www.python.org/downloads/windows/).
* Download the latest Python 3.11 or 3.12 installer.
* **CRITICAL:** When you start the installer, check the box at the very bottom that says **"Add Python to PATH"** before clicking "Install Now".

**3. Install Java (JDK 17)**
* Go to the [Adoptium Eclipse Temurin Download page](https://adoptium.net/temurin/releases/?version=17).
* Download the `.msi` installer for Windows x64.
* Run the installer. On the Custom Setup screen, ensure **"Set JAVA_HOME variable"** is selected to be installed on the local drive.

**4. Test Windows Installation**
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

**1. Install Homebrew (if you don't have it)**
* Open the **Terminal** app.
* Paste the following command and press Enter:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

**2. Install Git, Python, and Java**
* In the Terminal, run:
  ```bash
  brew install git
  brew install python
  brew install openjdk@17
  ```
* Symlink Java to the system wrappers so the OS finds it:
  ```bash
  sudo ln -sfn /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk
  ```

**3. Test macOS Installation**
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

3. **Clone the SysML v2 Implementation:**
   * Run the following command to clone the SysML v2 validation engine:
     ```bash
     git clone https://github.com/Systems-Modeling/SysML-v2-Release.git v2Implementation
     ```
   * *(Note: If your organization has a specific fork of the SysML-v2-Release or the validator, use that URL instead).*

4. **Clone the LLM Scripts Repository:**
   * Clone the repository containing the prompt engineering assets and validation scripts:
     ```bash
     git clone https://github.com/turbogeek/SysMLv2CheatSheet.git SysMLv2CheatSheet
     ```

---

## 3. Configuring the Scripts

The Python wrapper script (`validate_model.py`) needs to know where the Java validator is located.

1. Open `SysMLv2CheatSheet/validate_model.py` in your text editor.
2. Find the configuration section at the top of the script.
3. Update the `VALIDATOR_PATH` variable to point to the `validate.cmd` (or `validate.sh` on Mac) script inside your `v2Implementation` folder.
   
   **For Windows:**
   ```python
   VALIDATOR_PATH = r"C:\Users\YourName\Documents\git\v2Implementation\sysml-validator\validate.cmd"
   ```

   **For macOS:**
   ```python
   VALIDATOR_PATH = "/Users/YourName/Documents/git/v2Implementation/sysml-validator/validate.sh"
   ```

---

## 4. Installing Antigravity (VS Code Assistant)

To use the automated pipeline efficiently, you will need the **Antigravity** extension for Visual Studio Code. This acts as your intelligent AI pair programmer.

**1. Install Antigravity**
* Open **Visual Studio Code**.
* Go to the **Extensions** view by clicking the square icon on the left sidebar (or press `Ctrl+Shift+X` on Windows, `Cmd+Shift+X` on macOS).
* Search for **Antigravity** in the marketplace.
* Click **Install**.
* *(Follow any on-screen prompts to sign in or configure your API key).*

**2. Create Your Workspace**
* Create a new folder on your computer where you want to test and build your models (e.g., `Documents/SysML_Tests`).
* In VS Code, go to **File > Open Folder...** and select the folder you just created.

**3. Open Antigravity**
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
   * Explicitly tell Antigravity: *"Add this problem and solution to `../git/SysMLv2CheatSheet/LLM_skills/fix_recipies.md`."*
   * Antigravity will automatically update the markdown file, so it (and you) will never make that same mistake again!

### Troubleshooting
* **"Java is not recognized..."**: Ensure you installed JDK 17 and added it to your PATH environment variable.
* **"The system cannot find the path specified"**: Double-check the `VALIDATOR_PATH` variable in `validate_model.py` to ensure it points to the correct absolute location of the `validate` script.
* **"Python is not recognized..."**: Re-run the Python installer and check "Add Python to PATH".

---
*Generated by the automated SysML v2 Pipeline Assistant*
