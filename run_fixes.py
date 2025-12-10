
import subprocess

scripts = [
    "generate_sysml_file.py",
    "generate_constraints_sheet.py",
    "generate_structure_sheet.py"
]

for script in scripts:
    print(f"Running {script}...")
    try:
        subprocess.run(["py", script], check=True, cwd="src")
    except Exception as e:
        print(f"Error running {script}: {e}")
