import json
import sys

INDEX_FILE = "LLM_skills/Specifications_Index.json"

try:
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
except FileNotFoundError:
    print(f"Error: Index file {INDEX_FILE} not found.")
    sys.exit(1)

targets = [
    ("SysMLv2.pdf", "9.2 Systems Model Library"),
    ("SysMLv2.pdf", "9.3 Metadata Domain Library"),
    ("SysMLv2.pdf", "9.4 Analysis Domain Library"),
    ("SysMLv2.pdf", "9.5 Cause and Effect Domain Library"),
    ("SysMLv2.pdf", "9.7 Geometry Domain Library"),
    ("SysMLv2.pdf", "9.8 Quantities and Units Domain Library"),
    ("KerML.pdf", "9.2 Semantic Model of KerML"),
    ("KerML.pdf", "9.3 Data Type Library"),
    ("KerML.pdf", "9.4 Function Library"),
]

for src, heading_starts_with in targets:
    print(f"\nSearching for {heading_starts_with} in {src}...")
    found = False
    for chunk in chunks:
        if chunk["source"] == src and chunk["heading"].startswith(heading_starts_with):
            print(f"FOUND: {chunk['heading']}")
            # Print first 500 chars to get an idea of the content
            print(chunk["content"][:500] + "...\n")
            found = True
            break
    if not found:
        print(f"NOT FOUND: {heading_starts_with}")
