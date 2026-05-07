import os
import re

file_path = r"e:\_Documents\git\SysMLv2CheatSheet\docs\SysMLv2_Language_Reference.md"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Issue 4: Corrupted text
content = content.replace(
    """- **Library Packages:** Always use library package (e.g., library package 'Requirement Templates') to house reusable templates and definitions (def). Place usages (e.g.,
equirement) in actual model context packages.
- **Requirement Definitions vs. Usages:**
equirement def elements should act as reusable abstractions and be relegated to library package. The specific statement/instance of a requirement should be an element usage (
equirement) typed by a definition.
- **Actions and States:** In a similar vein,  ction def or state def define the flows/behavioral blocks. The usage  ction or state sits inside the concrete parts that exhibit or execute them.""",
    """- **Library Packages:** Always use library package (e.g., library package 'Requirement Templates') to house reusable templates and definitions (def). Place usages (e.g., `requirement`) in actual model context packages.
- **Requirement Definitions vs. Usages:** `requirement def` elements should act as reusable abstractions and be relegated to library packages. The specific statement/instance of a requirement should be an element usage (`requirement`) typed by a definition.
- **Actions and States:** In a similar vein, `action def` or `state def` define the flows/behavioral blocks. The usage `action` or `state` sits inside the concrete parts that exhibit or execute them."""
)

# Fix Issue 5: Import Accessibility
content = content.replace(
    """The only reason to use `public` is when the element is to be used everywhere because a `public` is part of the world view. It is better to use the default (no `public` or `private`) so that a user in another package is forced to import.
The only reason to use `private` is when the element is truly not usable or redefinable outside of a context of the package it lives, which in SysMLv2 is rare as we care less about this in engineering than is in software where we don't trust fellow programmers.
When importing, the import must be prefixed with `public` , `private` or `protected` with 'private' being the default import accessibility specified (for example `private import ScalarValues::*;`).""",
    """**Import Visibility (Repository Style Rule):**
Lack of visibility on import statements (plain `import`) is forbidden in this repository. 
While standard SysMLv2 allows plain `import`, this repository's strict best practice is to always use `private import` (e.g., `private import ScalarValues::*;`) to prevent namespace pollution. 
`public import` should be avoided except in rare circumstances when there is a specific need to expose the imported elements to the public or to avoid circular dependencies."""
)

# Fix Issue 6: Invalid Imports
content = content.replace("private import SI::;", "private import SI::*;")
content = content.replace("import ScalarValues::*;\\nimport ISQ::*;\\nimport SI::*;".replace('\\n', '\n'),
                          "private import ScalarValues::*;\\nprivate import ISQ::*;\\nprivate import SI::*;".replace('\\n', '\n'))

# Fix Issue 2: Allocation Styles
old_allocation_snippet = """package LogicalToPhysicalAllocation {
    
    allocation power : Allocation {
        end source : LogicalSystem::power;
        end target : PhysicalSystem::battery;
    }

}"""

new_allocation_snippet = """package LogicalToPhysicalAllocation {
    /* The canonical and generally preferred syntax for allocations */
    allocation allocate PhysicalSystem::battery to LogicalSystem::power;
}"""

content = content.replace(old_allocation_snippet, new_allocation_snippet)
content = content.replace("allocate physicalUsage.comp to logicalUsage.func;", "allocation allocate physicalUsage.comp to logicalUsage.func;")

# Fix Issue 1: `//` single line comments
lines = content.split('\n')
for i, line in enumerate(lines):
    if '//' in line and 'http://' not in line and 'https://' not in line:
        idx = line.find('//')
        comment_text = line[idx+2:].strip()
        lines[i] = f"{line[:idx]}/* {comment_text} */"
content = '\n'.join(lines)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated SysMLv2_Language_Reference.md")
