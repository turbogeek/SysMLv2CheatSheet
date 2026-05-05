import sys

def fix_fences(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    out_lines = []
    
    for i, line in enumerate(lines):
        is_fence = line.startswith('```')
        
        if is_fence:
            # check if there's a non-blank line before this fence
            if i > 0 and lines[i-1].strip() != '' and not out_lines[-1].strip() == '':
                out_lines.append('\n')
                
        out_lines.append(line)
        
        if is_fence:
            # check if the next line is non-blank (only if this is a closing fence?)
            # Actually, just enforcing blank lines around *any* fence marker works well.
            # But wait, if we are at `line`, the next line hasn't been processed yet.
            # We can check if `lines[i+1]` is non-blank.
            if i + 1 < len(lines) and lines[i+1].strip() != '':
                # Don't add a newline if the next line is just another fence
                if not lines[i+1].startswith('```'):
                    out_lines.append('\n')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)

fix_fences('e:\\_Documents\\git\\SysMLv2CheatSheet\\LLM_skills\\skill.md')
