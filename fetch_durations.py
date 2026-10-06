import urllib.request
import json
import re

with open('episodes_enriched.json', 'r', encoding='utf-8') as f:
    episodes = json.load(f)

for ep in episodes:
    embed_url = f"https://open.spotify.com/embed/episode/{ep['id']}"
    req = urllib.request.Request(embed_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        m = re.search(r'"duration":\s*([0-9]+)', html)
        if m:
            dur_ms = int(m.group(1))
            mins = dur_ms // 60000
            secs = (dur_ms % 60000) // 1000
            ep['duration_ms'] = dur_ms
            ep['duration_formatted'] = f"{mins}m {secs:02d}s"
            print(f"{ep['title']}: {mins}m {secs:02d}s")
    except Exception as e:
        print(f"Error fetching duration for {ep['id']}: {e}")

with open('episodes_enriched.json', 'w', encoding='utf-8') as f:
    json.dump(episodes, f, indent=2)

print("Updated durations!")
