import os

for root, dirs, files in os.walk('e:\\_Documents\\git\\SysMLv2CheatSheet\\src'):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if '"): */' in content:
                content = content.replace('"): */', '"):')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Fixed {file}')
