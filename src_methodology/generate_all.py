import os
import subprocess
import sys

def run_script(script_name):
    print(f"Running {script_name}...")
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Build the full path to the script to run
        script_path = os.path.join(script_dir, script_name)
        
        result = subprocess.run([sys.executable, script_path], check=True, capture_output=True, text=True, cwd=os.getcwd())
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}:")
        print(e.stderr)
        sys.exit(1)

def main():
    # List of all generator scripts in execution order
    scripts = [
        "generate_incose.py",
        "generate_oosem.py",
        "generate_magicgrid.py",
        "generate_skill.py"
    ]
    
    # Ensure LLM_Assets directory exists in the root
    os.makedirs('LLM_Assets', exist_ok=True)

    print("Generating SE Methodology Templates...")
    for script in scripts:
        run_script(script)
        
    print("Methodology generation complete.")

if __name__ == '__main__':
    main()
