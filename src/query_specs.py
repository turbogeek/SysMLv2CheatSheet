import json
import argparse
import sys
import re

INDEX_FILE = "LLM_skills/Specifications_Index.json"

def score_chunk(chunk, query_words):
    score = 0
    heading = chunk.get("heading", "").lower()
    content = chunk.get("content", "").lower()
    
    for word in query_words:
        word = word.lower()
        # High weight for heading matches
        if word in heading:
            score += 10
        
        # Count occurrences in content
        score += content.count(word)
        
    return score

def main():
    parser = argparse.ArgumentParser(description="Query the SysMLv2 Specifications index.")
    parser.add_argument("query", help="The keyword or phrase to search for (e.g., 'state machine')")
    parser.add_argument("--top", type=int, default=3, help="Number of top results to return")
    args = parser.parse_args()
    
    try:
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            chunks = json.load(f)
    except FileNotFoundError:
        print(f"Error: Index file {INDEX_FILE} not found. Run src/index_specs.py first.", file=sys.stderr)
        sys.exit(1)
        
    query_words = [w for w in re.split(r'\W+', args.query) if w]
    if not query_words:
        print("Invalid query.", file=sys.stderr)
        sys.exit(1)
        
    # Score chunks
    scored_chunks = []
    for chunk in chunks:
        score = score_chunk(chunk, query_words)
        if score > 0:
            scored_chunks.append((score, chunk))
            
    # Sort descending by score
    scored_chunks.sort(key=lambda x: x[0], reverse=True)
    
    if not scored_chunks:
        print(f"No results found for query: '{args.query}'")
        sys.exit(0)
        
    # Output top N
    top_results = scored_chunks[:args.top]
    print(f"=== Top {len(top_results)} Results for '{args.query}' ===\n")
    
    for i, (score, chunk) in enumerate(top_results):
        print(f"--- Result {i+1} (Score: {score}) ---")
        print(f"Source:  {chunk['source']}")
        print(f"Heading: {chunk['heading']}")
        print("-" * 40)
        
        # Limit content output to avoid overwhelming the LLM context window
        content = chunk['content']
        # If content is extremely long, truncate it
        if len(content) > 3000:
            content = content[:3000] + "\n... [TRUNCATED for length] ..."
            
        print(content)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
