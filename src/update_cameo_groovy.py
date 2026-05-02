import os
import sys
import argparse
import shutil
import glob
import re

def main():
    parser = argparse.ArgumentParser(description="Update Cameo Automaton plugin with new Groovy jars.")
    parser.add_argument("--cameo-dir", required=True, help="Path to Cameo installation directory")
    parser.add_argument("--groovy-dir", required=True, help="Path to Groovy installation directory")
    parser.add_argument("--lib-folder-name", default="groovy_jars", help="Name of the folder to create inside the plugin to hold the jars")
    
    args = parser.parse_args()
    
    cameo_dir = args.cameo_dir
    groovy_dir = args.groovy_dir
    
    plugin_dir = os.path.join(cameo_dir, "plugins", "com.nomagic.magicdraw.automaton")
    plugin_xml_path = os.path.join(plugin_dir, "plugin.xml")
    
    groovy_lib_dir = os.path.join(groovy_dir, "lib")
    
    if not os.path.exists(plugin_xml_path):
        print(f"Error: Could not find plugin.xml at {plugin_xml_path}")
        sys.exit(1)
        
    if not os.path.exists(groovy_lib_dir):
        print(f"Error: Could not find Groovy lib directory at {groovy_lib_dir}")
        sys.exit(1)
        
    # 1. Copy Jars
    target_jar_dir = os.path.join(plugin_dir, args.lib_folder_name)
    if os.path.exists(target_jar_dir):
        print(f"Cleaning existing jar folder: {target_jar_dir}")
        shutil.rmtree(target_jar_dir)
    os.makedirs(target_jar_dir)
    
    print(f"Copying Groovy jars from {groovy_lib_dir} to {target_jar_dir}...")
    jars = glob.glob(os.path.join(groovy_lib_dir, "*.jar"))
    if not jars:
        print(f"Error: No jars found in {groovy_lib_dir}")
        sys.exit(1)
        
    for jar in jars:
        shutil.copy(jar, target_jar_dir)
        
    # 2. Modify plugin.xml
    print(f"Updating {plugin_xml_path}...")
    with open(plugin_xml_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.splitlines()
    new_lines = []
    
    runtime_end_index = -1
    
    # regex to match groovy jars in library tag
    old_groovy_pattern = re.compile(r'<library\s+name=".*groovy.*\.jar"\s*/>')
    folder_pattern = re.compile(rf'<library\s+name="{args.lib_folder_name}/.*\.jar"\s*/>')
    
    for i, line in enumerate(lines):
        if '</runtime>' in line:
            runtime_end_index = len(new_lines)
            
        # Skip old groovy or custom folder library tags
        if old_groovy_pattern.search(line) or folder_pattern.search(line):
            continue
            
        new_lines.append(line)
        
    if runtime_end_index == -1:
        print("Error: Could not find <runtime> ... </runtime> section in plugin.xml")
        sys.exit(1)
        
    # Insert new jars right before </runtime>
    # Try to determine indentation
    indent = "      "
    if runtime_end_index > 0:
        prev_line = new_lines[runtime_end_index - 1]
        m = re.match(r'^(\s*)', prev_line)
        if m:
            indent = m.group(1)
            if not prev_line.strip():
                indent = "      "
                
    jar_entries = []
    for jar in jars:
        jar_name = os.path.basename(jar)
        jar_entries.append(f'{indent}<library name="{args.lib_folder_name}/{jar_name}"/>')
        
    # Insert new entries
    new_lines = new_lines[:runtime_end_index] + jar_entries + new_lines[runtime_end_index:]
    
    new_content = "\n".join(new_lines)
    
    # Write backup
    backup_path = plugin_xml_path + ".backup"
    print(f"Creating backup at {backup_path}")
    shutil.copy(plugin_xml_path, backup_path)
    
    with open(plugin_xml_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully updated {plugin_xml_path} with {len(jars)} Groovy jars.")

if __name__ == "__main__":
    main()
