
import subprocess

scripts = [
    "generate_sysml_file.py",
    "generate_actions_core_sheet.py",
    "generate_actions_control_sheet.py",
    "generate_actions_events_sheet.py"
]

for script in scripts:
    print(f"Running {script}...")
    try:
        subprocess.run(["py", script], check=True, cwd="src")
    except Exception as e:
        print(f"Error running {script}: {e}")
