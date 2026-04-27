import subprocess
import sys
import os
import argparse

def validate_sysml_file(file_path):
    """
    Validates a SysML v2 file using the custom sysml-validator in the adjacent repo.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        return False

    validator_cmd = r"E:\_Documents\git\v2Implementation\sysml-validator\validate.cmd"
    
    if not os.path.exists(validator_cmd):
        print(f"Error: Validator script '{validator_cmd}' not found.", file=sys.stderr)
        return False

    print(f"Validating {file_path}...")
    try:
        # Run the validate.cmd
        result = subprocess.run(
            [validator_cmd, file_path],
            capture_output=True,
            text=True,
            cwd=r"E:\_Documents\git\v2Implementation\sysml-validator"
        )

        # Check output for typical success indicators or return code
        if result.returncode == 0:
            print("Validation successful: No syntax errors found.")
            return True
        else:
            print("Validation FAILED with the following errors:", file=sys.stderr)
            print(result.stdout, file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            return False

    except Exception as e:
        print(f"An error occurred while running the parser: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate a SysML v2 file.")
    parser.add_argument("file", help="Path to the .sysml file to validate")
    
    args = parser.parse_args()
    
    success = validate_sysml_file(args.file)
    sys.exit(0 if success else 1)
