import os
import subprocess
import sys

def main():
    test_dir = r"E:\_Documents\git\SysMLv2CheatSheet\Prompt Examples Outputs\Test Files\Fixed versions"
    validate_script = r"E:\_Documents\git\SysMLv2CheatSheet\validate_model.py"
    
    files = [
        "deepseek_sysml_20260426_055020.sysml",
        "deepseek_sysml_20260426_1a7ce4.sysml",
        "deepseek_sysml_20260426_dca19b.sysml"
    ]
    
    output = []
    
    for filename in files:
        file_path = os.path.join(test_dir, filename)
        if not os.path.exists(file_path):
            continue
            
        print(f"Running validator on {filename}...")
        result = subprocess.run(
            ['python', validate_script, file_path],
            capture_output=True,
            text=True
        )
        
        lines = result.stderr.splitlines()
        
        with open(file_path, 'r', encoding='utf-8') as f:
            file_lines = f.readlines()
            
        added_errors = 0
        for line in lines:
            if "ERROR: Line" in line:
                if added_errors >= 3: # max 3 per file
                    break
                    
                # Format: ERROR: Line 435:27 - Name resolution error: ...
                try:
                    parts = line.split('-')
                    line_info = parts[0].strip()
                    error_msg = '-'.join(parts[1:]).strip()
                    
                    line_num_str = line_info.replace('ERROR: Line', '').strip().split(':')[0]
                    line_num = int(line_num_str)
                    
                    code_snippet = file_lines[line_num - 1].strip()
                    
                    output.append(f"**File:** `{filename}`")
                    output.append(f"**Line {line_num}:** `{code_snippet}`")
                    output.append(f"**Error:** `{error_msg}`")
                    output.append("")
                    
                    added_errors += 1
                except Exception as e:
                    pass
                    
    with open("extracted_errors.md", "w") as f:
        f.write('\n'.join(output))

if __name__ == "__main__":
    main()
