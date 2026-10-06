import os
import json
import subprocess
import urllib.request

os.makedirs('assets/images', exist_ok=True)
os.makedirs('assets/audio', exist_ok=True)

with open('episodes.json', 'r', encoding='utf-8') as f:
    episodes = json.load(f)

# Also show cover
show_cover_url = "https://i.scdn.co/image/ab6765630000ba8ae2c7fa4ef15b37acb687a237"
show_cover_path = "assets/images/show-cover.jpg"
print(f"Downloading show cover...")
subprocess.run(["curl.exe", "-s", show_cover_url, "-o", show_cover_path])

file_slugs = [
    "ep1-how-do-drugs-know",
    "ep2-the-dream-that-gave-us-benzene",
    "ep3-ai-in-chemistry",
    "ep4-why-bananas-are-radioactive",
    "ep5-carbenes",
    "ep6-the-secrets-of-sadabahar"
]

for idx, ep in enumerate(episodes):
    slug = file_slugs[idx] if idx < len(file_slugs) else f"ep{idx+1}"
    
    img_dest = f"assets/images/{slug}.jpg"
    audio_dest = f"assets/audio/{slug}.mp3"
    
    # Download image
    if ep.get('image'):
        print(f"Downloading image for {ep['title']} -> {img_dest}")
        subprocess.run(["curl.exe", "-s", ep['image'], "-o", img_dest])
        ep['local_image'] = img_dest
    
    # Download audio
    if ep.get('preview_audio'):
        print(f"Downloading audio for {ep['title']} -> {audio_dest}")
        subprocess.run(["curl.exe", "-s", ep['preview_audio'], "-o", audio_dest])
        ep['local_audio'] = audio_dest
    
    ep['slug'] = slug
    ep['embed_url'] = f"https://open.spotify.com/embed/episode/{ep['id']}?utm_source=generator"

with open('episodes_enriched.json', 'w', encoding='utf-8') as f:
    json.dump(episodes, f, indent=2)

print("All assets successfully downloaded and indexed!")
