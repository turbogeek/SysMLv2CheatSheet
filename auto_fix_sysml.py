import os
import re
import subprocess
import sys

def apply_fixes(content):
    # Fix 1: satisfy requirement -> satisfy
    content = re.sub(r'\bsatisfy\s+requirement\b', 'satisfy', content)
    # Fix 2: frame concern -> frame
    content = re.sub(r'\bframe\s+concern\b', 'frame', content)
    # Fix 3: KerML::CollectionFunctions
    content = content.replace('KerML::CollectionFunctions::', 'CollectionFunctions::')
    # Fix 4: ordered nonunique braces
    content = re.sub(r'\{\s*ordered\s+nonunique\s*\}', 'ordered nonunique;', content)
    # Fix 5: remove import ProjectUnits and RequirementTypes (if they cause errors)
    content = re.sub(r'^\s*(private\s+)?import\s+ProjectUnits::\*;\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*(private\s+)?import\s+RequirementTypes::\*;\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*(private\s+)?import\s+LogicalDesign::\*;\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*(private\s+)?import\s+PhysicalDesign::\*;\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*(private\s+)?import\s+StakeholderConcerns::\*;\s*$', '', content, flags=re.MULTILINE)
    # Fix 6: Remove inline comments like /* 2 seconds */ at the end of lines in constraints
    content = re.sub(r'(\[[^\]]+\])\s*/\*.*?\*/', r'\1', content)
    return content

def main():
    test_dir = r"E:\_Documents\git\SysMLv2CheatSheet\Prompt Examples Outputs\Test Files"
    fixed_dir = os.path.join(test_dir, "Fixed versions")
    validate_script = r"E:\_Documents\git\SysMLv2CheatSheet\validate_model.py"
    
    if not os.path.exists(fixed_dir):
        os.makedirs(fixed_dir)
        
    files = [f for f in os.listdir(test_dir) if f.endswith('.sysml')]
    
    for filename in files:
        file_path = os.path.join(test_dir, filename)
        fixed_path = os.path.join(fixed_dir, filename)
        
        print(f"Processing {filename}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        fixed_content = apply_fixes(content)
        
        with open(fixed_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
            
        # Run validation on the fixed file
        result = subprocess.run(
            ['python', validate_script, fixed_path],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"SUCCESS: {filename} is now valid!")
        else:
            print(f"FAILED: {filename} still has errors.")
            print("Errors:")
            print(result.stderr)
            
if __name__ == "__main__":
    main()
