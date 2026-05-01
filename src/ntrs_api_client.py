import argparse
import requests
import json
import sys

def search_ntrs(query, limit=5, year=None):
    url = "https://ntrs.nasa.gov/api/citations/search"
    params = {
        "q": query,
        "size": limit
    }
    
    if year:
        # Simplistic way to add year filter if NTRS supports it in 'q', 
        # or we just append it to the query for better relevance.
        params["q"] = f"{query} year:{year}"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        results = data.get("results", [])
        if not results:
            print(f"No results found for query: '{query}'")
            return

        print(f"Found {len(results)} results for query: '{query}'\n")
        
        for i, item in enumerate(results, 1):
            title = item.get("title", "No Title")
            abstract = item.get("abstract", "No Abstract Available").strip()
            # truncate abstract for readability if it's too long
            if len(abstract) > 500:
                abstract = abstract[:497] + "..."
            
            author_list = item.get("authorAffiliations", [])
            authors = ", ".join([a.get("meta", {}).get("author", {}).get("name", "Unknown") for a in author_list])
            
            published_date = item.get("publications", [{}])[0].get("publicationDate", "Unknown Date")
            document_id = item.get("id", "Unknown ID")
            
            print(f"--- Result {i} ---")
            print(f"Title: {title}")
            print(f"Authors: {authors}")
            print(f"Date: {published_date}")
            print(f"Document ID: {document_id}")
            print(f"Abstract: {abstract}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error querying NTRS API: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query the NASA NTRS API for technical reports and patents.")
    parser.add_argument("query", type=str, help="The search keywords.")
    parser.add_argument("--limit", type=int, default=5, help="Number of results to return (default: 5).")
    parser.add_argument("--year", type=str, default=None, help="Optional year to filter/prioritize.")
    
    args = parser.parse_args()
    search_ntrs(args.query, args.limit, args.year)
