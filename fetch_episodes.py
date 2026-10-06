import urllib.request
import re
import json
from bs4 import BeautifulSoup

episode_ids = [
    '2Gk73JTWsSMZyvFC0mLamY',
    '5ITLHynrv2v5fswL97cEM1',
    '6fljKsecNn8hsWNy0GQXvX',
    '7ADsMwTUznnKSRfqTn4oif',
    '2x9dcG1qYjx4GRjg4fJtDp',
    '3m4qgdk2koLtacQ5UxGQul'
]

episodes = []

for ep_id in episode_ids:
    url = f"https://open.spotify.com/episode/{ep_id}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # Check title
        title = soup.find('title').text if soup.find('title') else ep_id
        
        # Check ld+json
        ld = None
        for s in soup.find_all('script'):
            if s.string and ('@context' in s.string):
                try:
                    data = json.loads(s.string)
                    ld = data
                    break
                except:
                    pass
        
        # Check description
        desc = soup.find('meta', {'name': 'description'})
        desc_text = desc.get('content') if desc else ''
        
        # Check og:image
        img = soup.find('meta', {'property': 'og:image'})
        img_url = img.get('content') if img else ''
        
        # Check audio preview
        audio_preview = soup.find('meta', {'property': 'og:audio'})
        preview_url = audio_preview.get('content') if audio_preview else ''
        
        ep_data = {
            'id': ep_id,
            'url': url,
            'title': ld.get('name') if ld and 'name' in ld else title.split(' - ')[0],
            'description': ld.get('description') if ld and 'description' in ld else desc_text,
            'date': ld.get('datePublished') if ld and 'datePublished' in ld else '',
            'image': img_url,
            'preview_audio': preview_url
        }
        episodes.append(ep_data)
        print(f"Loaded: {ep_data['title']} ({ep_data['date']})")
    except Exception as e:
        print(f"Error for {ep_id}: {e}")

with open('episodes.json', 'w', encoding='utf-8') as f:
    json.dump(episodes, f, indent=2)

print("Saved episodes.json successfully!")
