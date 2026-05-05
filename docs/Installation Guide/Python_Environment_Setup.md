# Python Environment Setup Guide

To manually build the cheat sheets and tutorials in this project, or to develop new generator scripts, you will need a working Python environment.

## 1. Install Python (Python 3.8+)

### Windows
1. Download the official installer from [python.org](https://www.python.org/downloads/windows/).
2. **Important**: During installation, make sure to check the box that says **"Add Python to PATH"**.
3. Complete the installation wizard.

### macOS (OSX)
You can install Python using the official installer or via Homebrew.
**Option A: Homebrew (Recommended)**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```
**Option B: Official Installer**
Download and install the package from [python.org](https://www.python.org/downloads/mac-osx/).

### Linux (Ubuntu/Debian)
Python is often pre-installed on Linux, but you may need to install the `python3-venv` package to create virtual environments.
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

*(For Fedora/RHEL, use `sudo dnf install python3`)*

---

## 2. Verify Installation

Open a terminal (Command Prompt, PowerShell, or bash) and verify the installation:

```bash
# On Windows
python --version

# On macOS / Linux
python3 --version
```
You should see a version output (e.g., `Python 3.10.x`).

---

## 3. Clone the Repository

If you haven't already cloned the repository:
```bash
git clone https://github.com/turbogeek/SysMLv2CheatSheet.git
cd SysMLv2CheatSheet
```

---

## 4. (Optional but Recommended) Create a Virtual Environment

It is a best practice to use a virtual environment so any dependencies you might add later don't conflict with your system Python packages.

**Create the Virtual Environment:**
```bash
# On Windows
python -m venv venv

# On macOS / Linux
python3 -m venv venv
```

**Activate the Virtual Environment:**
* **Windows (Command Prompt):** `venv\Scripts\activate.bat`
* **Windows (PowerShell):** `venv\Scripts\Activate.ps1`
* **macOS / Linux:** `source venv/bin/activate`

*(Note: When the virtual environment is active, you will see `(venv)` at the beginning of your terminal prompt. To deactivate it, simply type `deactivate`)*

---

## 5. Install Dependencies

*Currently, the generator scripts in this project rely entirely on the Python Standard Library and do not require external dependencies. However, if a `requirements.txt` is added in the future, install the dependencies like this:*

```bash
# On Windows
python -m pip install -r requirements.txt

# On macOS / Linux
pip3 install -r requirements.txt
```

---

## 6. Running the Build Script

The build scripts are orchestrated by the `generate_all.py` file located in the root of the repository.

To manually regenerate all `output/` files (including `skill.md`), make sure you are in the root directory of the repository and run:

```bash
# On Windows
python generate_all.py

# On macOS / Linux
python3 generate_all.py
```

*Note: You generally do not need to do this manually if you are using Git. The `pre-commit` hook automatically runs this script when you make a commit!*
