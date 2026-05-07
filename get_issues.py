import urllib.request
import json

req = urllib.request.urlopen('https://api.github.com/repos/turbogeek/SysMLv2CheatSheet/issues')
issues = json.loads(req.read().decode('utf-8'))

with open('issues_full.txt', 'w', encoding='utf-8') as f:
    for i in issues:
        f.write(f"Issue {i['number']}: {i['title']}\n")
        f.write(f"{i['body']}\n\n{'='*40}\n\n")
