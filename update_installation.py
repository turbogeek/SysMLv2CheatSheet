import os

# Update Installation_Guide.md
guide_path = r"e:\_Documents\git\SysMLv2CheatSheet\docs\Installation Guide\Installation_Guide.md"
with open(guide_path, 'r', encoding='utf-8') as f:
    guide_content = f.read()

old_clone_guide = """#### 3. Clone the SysML v2 Implementation:
   * Run the following command to clone the SysML v2 validation engine:

     ```bash
     git clone https://github.com/Systems-Modeling/SysML-v2-Release.git v2Implementation
     ```

   * *(Note: If your organization has a specific fork of the SysML-v2-Release or the validator, use that URL instead).*"""

new_clone_guide = """#### 3. Clone the SysML v2 Validator:
   * Run the following command to clone the SysML v2 validation engine:

     ```bash
     git clone https://github.com/turbogeek/sysmlv2-validator.git sysml-validator
     ```

   * *(Note: This replaces the older SysML-v2-Release dependency).*"""

guide_content = guide_content.replace(old_clone_guide, new_clone_guide)
guide_content = guide_content.replace(
    "script will correctly find the validator at `../v2Implementation/sysml-validator/validate.cmd`",
    "script will correctly find the validator at `../sysml-validator/validate.cmd`"
)
guide_content = guide_content.replace(
    "v2Implementation",
    "sysml-validator"
)

with open(guide_path, 'w', encoding='utf-8') as f:
    f.write(guide_content)

# Update validate_model.py
val_path = r"e:\_Documents\git\SysMLv2CheatSheet\validate_model.py"
with open(val_path, 'r', encoding='utf-8') as f:
    val_content = f.read()

old_val_fallback = """        # Fallback: The validator resides at the same level as this git project by default
        validator_dir = os.path.abspath(os.path.join(script_dir, "..", "v2Implementation", "sysml-validator"))"""

new_val_fallback = """        # Fallback: The validator resides at the same level as this git project by default
        validator_dir = os.path.abspath(os.path.join(script_dir, "..", "sysml-validator"))
        if not os.path.exists(validator_dir):
            validator_dir = os.path.abspath(os.path.join(script_dir, "..", "sysmlv2-validator"))"""

val_content = val_content.replace(old_val_fallback, new_val_fallback)

with open(val_path, 'w', encoding='utf-8') as f:
    f.write(val_content)

print("Updated installation guide and validate_model.py")
