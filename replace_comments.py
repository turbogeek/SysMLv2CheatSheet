import os

for root, dirs, files in os.walk('e:\\_Documents\\git\\SysMLv2CheatSheet\\src'):
    for file in files:
        if file.endswith('.py') and file != 'utils.py':
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            changed = False
            for i, line in enumerate(lines):
                if '//' in line and 'http://' not in line and 'https://' not in line:
                    idx = line.find('//')
                    comment = line[idx+2:].rstrip('\n\r')
                    
                    closures = ''
                    for ending in ['"""),', '""")', '"),', '")', '",', '"', '}', ']', ')']:
                        if comment.endswith(ending):
                            closures = ending
                            comment = comment[:-len(ending)]
                            break
                            
                    comment = comment.strip()
                    new_comment = f'/* {comment} */' + closures
                    new_line = line[:idx] + new_comment + '\n'
                    lines[i] = new_line
                    changed = True
                    
            if changed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                print(f'Updated {file}')
