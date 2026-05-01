import os
import json
import re
import pymupdf4llm

SPEC_DIR = "Specifications"
MD_OUTPUT_DIR = "LLM_skills/Specifications_Markdown"
INDEX_FILE = "LLM_skills/Specifications_Index.json"

def chunk_markdown(markdown_text, source_file):
    """
    Chunks markdown text by headings (# or ## or ###).
    """
    chunks = []
    # Match headings and everything until the next heading of same or higher level
    # A simpler approach: just split by lines and accumulate until we hit a header
    lines = markdown_text.split('\n')
    current_heading = "Start of Document"
    current_content = []
    
    for line in lines:
        match = re.match(r'^(#{1,4})\s+(.*)', line)
        if match:
            # We hit a new heading. Save the old one if it has content
            if current_content:
                chunks.append({
                    "source": source_file,
                    "heading": current_heading,
                    "content": "\n".join(current_content).strip()
                })
            current_heading = match.group(2).strip()
            current_content = [line]
        else:
            current_content.append(line)
            
    # Add the last chunk
    if current_content:
        chunks.append({
            "source": source_file,
            "heading": current_heading,
            "content": "\n".join(current_content).strip()
        })
        
    # Filter out empty chunks
    return [c for c in chunks if c['content']]

def main():
    if not os.path.exists(MD_OUTPUT_DIR):
        os.makedirs(MD_OUTPUT_DIR)
        
    all_chunks = []
    
    if not os.path.exists(SPEC_DIR):
        print(f"Directory {SPEC_DIR} not found.")
        return

    pdf_files = [f for f in os.listdir(SPEC_DIR) if f.lower().endswith('.pdf')]
    print(f"Found {len(pdf_files)} PDF files in {SPEC_DIR}.")
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(SPEC_DIR, pdf_file)
        md_file = pdf_file.replace('.pdf', '.md')
        md_path = os.path.join(MD_OUTPUT_DIR, md_file)
        
        print(f"Converting {pdf_file} to markdown...")
        try:
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            # Save raw markdown
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_text)
            print(f"Saved markdown to {md_path}")
            
            # Chunk and add to index
            chunks = chunk_markdown(md_text, pdf_file)
            all_chunks.extend(chunks)
            print(f"Extracted {len(chunks)} sections from {pdf_file}")
        except Exception as e:
            print(f"Failed to process {pdf_file}: {e}")

    # Save index
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_chunks, f, indent=2)
    print(f"Index created at {INDEX_FILE} with {len(all_chunks)} total sections.")

if __name__ == "__main__":
    main()
