# Python Environment Setup Guide

To manually build the cheat sheets and tutorials in this project, or to develop new generator scripts, you will need a working Python environment.

## Prerequisites

1. **Install Python**: Ensure you have Python 3.8 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
   - *Windows users*: Make sure to check the box "Add Python to PATH" during installation.

2. **Verify Installation**:
   Open a terminal (Command Prompt, PowerShell, or bash) and run:
   ```bash
   python --version
   ```
   You should see your installed Python version.

## Setup Instructions

1. **Clone the Repository (if you haven't already)**:
   ```bash
   git clone https://github.com/turbogeek/SysMLv2CheatSheet.git
   cd SysMLv2CheatSheet
   ```

2. **(Optional but Recommended) Create a Virtual Environment**:
   It's a good practice to use a virtual environment so any dependencies you might add later don't conflict with your system Python.
   ```bash
   # Create a virtual environment named 'venv'
   python -m venv venv

   # Activate the virtual environment (Windows)
   venv\Scripts\activate

   # Activate the virtual environment (macOS/Linux)
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   *Currently, the generator scripts in this project rely entirely on the Python Standard Library and do not require external dependencies like `pip install -r requirements.txt`. However, if you add packages in the future, install them here.*

## Running the Build Script

The build scripts are orchestrated by the `generate_all.py` file located in the root of the repository.

To regenerate all `output/` files (including `skill.md`):

```bash
# Ensure you are in the root directory of the repository
python generate_all.py
```

*Note: You do not need to do this if you are using Git. The `pre-commit` hook automatically runs this script when you make a commit!*
