import os

for root, dirs, files in os.walk('e:\\_Documents\\git\\SysMLv2CheatSheet\\src'):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'w.startswith("/* "): */' in content:
                new_content = content.replace('w.startswith("/* "): */', 'w.startswith("//"):')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Fixed {file}')
