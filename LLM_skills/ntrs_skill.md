# NTRS Technical Data Harvesting Skill

This skill provides instructions for AI Agents to search the NASA Technical Reports Server (NTRS) when performing Systems Engineering Concept Discovery, Trade Studies, or analyzing specific system constraints (such as performance, safety, cost, or weight). 

## When to use this skill
- When the user asks you to model a system that involves aerospace, advanced technology, or complex engineering domains where real-world research would be beneficial.
- When performing Tradeoff Studies and you need realistic Measures of Performance (MoP) or Measures of Effectiveness (MoE).
- When looking for patents or prior art during the "Concept Discovery" phase of INCOSE, OOSEM, or MagicGrid.
- When requested directly by the user.

## How to use this skill
You have access to a Python script that wraps the public NTRS OpenAPI: `src/ntrs_api_client.py`.

1. **Identify the research need**: Extract keywords from the user's prompt (e.g., "hypersonic drone", "lithium battery safety").
2. **Run the script**: Use your command-line capability to execute the script from the repository root:
   ```bash
   python src/ntrs_api_client.py "hypersonic drone" --limit 5
   ```
3. **Optional Year Filter**: If you need recent research, you can add the `--year` parameter:
   ```bash
   python src/ntrs_api_client.py "battery thermal runaway" --limit 3 --year 2023
   ```
4. **Analyze the Output**: The script will return a list of document titles, authors, publication dates, document IDs, and abstracts. 
5. **Integrate Findings**: Read the abstracts and extract relevant engineering data (metrics, constraints, lessons learned, or design approaches). Incorporate this data into your SysMLv2 models as `Doc` comments, `requirement`s, or justification for physical architecture choices during tradeoff studies. 
6. **Cite the Source**: Always add a comment or documentation element in the SysMLv2 code citing the NASA NTRS Document ID and Title when you use its data.
