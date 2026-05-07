import os

file_path = r"e:\_Documents\git\SysMLv2CheatSheet\LLM_skills\shorthands_skill.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '//' in line and 'http://' not in line and 'https://' not in line:
        idx = line.find('//')
        comment_text = line[idx+2:].strip()
        lines[i] = f"{line[:idx]}/* {comment_text} */\n"

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Updated shorthands_skill.md")
