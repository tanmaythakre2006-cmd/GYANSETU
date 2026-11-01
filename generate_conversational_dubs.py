import os
import sys
import json
import re
import subprocess
import shutil

sys.stdout.reconfigure(encoding='utf-8')

VENV_PYTHON = os.path.abspath(".venv/Scripts/python.exe")
try:
    import imageio_ffmpeg
    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    FFMPEG = "ffmpeg"

AUDIO_DIR = "assets/audio"
GHOST_DIR = "assets/audio_ghost"
TEMP_DIR = "temp_conversational_build"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(GHOST_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# Load transcripts
with open('assets/data/episodes_transcripts.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content.split('window.GYAN_SETU_TRANSCRIPTS = ')[1].strip()
if json_str.endswith(';'):
    json_str = json_str[:-1].strip()

transcripts_db = json.loads(json_str)

# Mapping of episode ID to output master audio file
AUDIO_MAP = {
    "ep-7": ("ep-1-hindi-master.mp3", None),     # Num 1 (Carbenes)
    "ep-6": ("ep-2-hindi-master.mp3", None),     # Num 2 (AI in Chem)
    "ep-5": ("ep-3-hindi-master.mp3", None),     # Num 3 (Bananas)
    "ep-4": ("ep-4-hindi-master.mp3", None),     # Num 4 (Drugs)
    "ep-3": ("ep-5-hindi-master.mp3", None),     # Num 5 (Benzene)
    "ep-2": ("ep-6-hindi-master.mp3", None),     # Num 6 (Sadabahar)
    "ep-1": ("ep-7-hindi-master.mp3", None),     # Num 7 (Consciousness)
    "ep-8": ("ep-8-hindi-master.mp3", None),     # Num 8 (Character)
    "ep-9": ("ep-9-hindi-master.mp3", None),     # Num 9 (Molecules - Single Warm Voice)
    "ep-10": ("ep-10-hindi-master.mp3", None),   # Num 10 (Napoleon)
    "ep-11": ("ep-11-hindi-master.mp3", None),   # Num 11 (Sky Color)
    "ep-12": ("ep-12-hindi-master.mp3", None),   # Num 12 (Frankenstein)
    "ep-13": ("ep13-nagpur-hindi-master.mp3", "ep13-nagpur-english-master.mp3") # Num 13 (Nagpur)
}

# Voices
VOICE_MALE_HI = "hi-IN-MadhurNeural"
VOICE_FEMALE_HI = "hi-IN-SwaraNeural"
VOICE_MALE_EN = "en-IN-PrabhatNeural"
VOICE_FEMALE_EN = "en-IN-NeerjaExpressiveNeural"

# Natural Conversational Pacing for Student Broadcasts
RATE_FAST = "+8%"
RATE_SOULFUL = "+4%"

def split_into_dialogue_turns(text, lang="hi"):
    """
    Splits a multi-sentence segment into natural conversational turns
    alternating between Male Host (turn 0) and Female Host (turn 1).
    """
    delimiters = r'([।\.\?!]+)'
    raw_parts = re.split(delimiters, text)
    
    sentences = []
    current = ""
    for part in raw_parts:
        if not part:
            continue
        if re.match(delimiters, part):
            current += part
            if len(current.strip()) > 5:
                sentences.append(current.strip())
            current = ""
        else:
            current += part
    if current.strip():
        sentences.append(current.strip())
        
    if not sentences:
        return []
        
    turns = []
    for i, s in enumerate(sentences):
        speaker = "male" if (i % 2 == 0) else "female"
        turns.append((speaker, s))
        
    return turns

def synthesize_clip(text, voice, pitch, rate, out_mp3):
    cmd = [
        VENV_PYTHON, "-m", "edge_tts",
        f"--voice={voice}",
        f"--pitch={pitch}",
        f"--rate={rate}",
        f"--text={text}",
        f"--write-media={out_mp3}"
    ]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"    TTS Error: {res.stderr}")
        return False
    return os.path.exists(out_mp3)

def build_dialogue_track(ep_id, lang, target_mp3_name):
    ep = transcripts_db.get(ep_id)
    if not ep:
        print(f"Skipping {ep_id}: not found in transcripts DB.")
        return
        
    print(f"\n========================================================")
    print(f"🎙️ Building Conversational Dub: {ep_id} ({lang.upper()}) -> {target_mp3_name}")
    segments = ep.get('segments', [])
    print(f"   Segments in episode: {len(segments)}")
    
    # Check if this is a solo single-voice episode (ep-13 or ep-9) or dialogue
    is_monologue = (ep_id in ["ep-13", "ep-9"])
    
    track_clips = []
    
    # Snappy 100ms silence clip for fast turn-taking
    silence_mp3 = os.path.join(TEMP_DIR, "silence_100ms.mp3")
    if not os.path.exists(silence_mp3):
        subprocess.run([
            FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
            "-t", "0.10", "-codec:a", "libmp3lame", "-b:a", "128k", silence_mp3
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    clip_counter = 0
    for s_idx, seg in enumerate(segments):
        txt = seg.get('hindi' if lang == 'hi' else 'english', '').strip()
        if not txt or txt.startswith('['):
            continue
            
        if is_monologue:
            if ep_id == "ep-9":
                # Single expressive, soulful, warm voice for "We Are More Than Molecules"
                voice = VOICE_FEMALE_HI if lang == 'hi' else VOICE_FEMALE_EN
                pitch = "+0Hz"
                rate = RATE_SOULFUL
            else:
                # Documentary voice for Nagpur History
                voice = VOICE_MALE_HI if lang == 'hi' else VOICE_MALE_EN
                pitch = "-12Hz"
                rate = RATE_FAST
                
            clip_path = os.path.join(TEMP_DIR, f"{ep_id}_{lang}_seg{s_idx}.mp3")
            if synthesize_clip(txt, voice, pitch, rate, clip_path):
                track_clips.append(clip_path)
                track_clips.append(silence_mp3)
        else:
            # Dialogue: Split into fast-paced conversational turns
            turns = split_into_dialogue_turns(txt, lang)
            for speaker, turn_txt in turns:
                clip_counter += 1
                clip_path = os.path.join(TEMP_DIR, f"{ep_id}_{lang}_c{clip_counter}.mp3")
                
                if speaker == "male":
                    voice = VOICE_MALE_HI if lang == 'hi' else VOICE_MALE_EN
                    pitch = "-14Hz"
                    rate = RATE_FAST
                else:
                    voice = VOICE_FEMALE_HI if lang == 'hi' else VOICE_FEMALE_EN
                    pitch = "-15Hz"
                    rate = RATE_FAST
                    
                if synthesize_clip(turn_txt, voice, pitch, rate, clip_path):
                    track_clips.append(clip_path)
                    track_clips.append(silence_mp3)
                    
    if not track_clips:
        print(f"   ⚠️ No clips generated for {ep_id}")
        return
        
    # Concatenate all clips using FFMPEG concat demuxer
    concat_list_file = os.path.join(TEMP_DIR, f"concat_{ep_id}_{lang}.txt")
    with open(concat_list_file, 'w', encoding='utf-8') as f:
        for c in track_clips:
            abs_path = os.path.abspath(c).replace('\\', '/')
            f.write(f"file '{abs_path}'\n")
            
    out_master_mp3 = os.path.join(AUDIO_DIR, target_mp3_name)
    print(f"   Concatenating {len(track_clips)} clips into master audio: {out_master_mp3}...")
    
    res = subprocess.run([
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", concat_list_file,
        "-c:a", "libmp3lame", "-b:a", "128k", out_master_mp3
    ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    
    if res.returncode != 0:
        print(f"   Concat error: {res.stderr}")
        return
        
    master_size = os.path.getsize(out_master_mp3) / (1024 * 1024)
    print(f"   ✅ Master generated: {out_master_mp3} ({master_size:.2f} MB)")
    
    # Generate 32kbps Ghost Mode counterpart
    out_ghost_mp3 = os.path.join(GHOST_DIR, target_mp3_name)
    subprocess.run([
        FFMPEG, "-y", "-i", out_master_mp3,
        "-c:a", "libmp3lame", "-b:a", "32k", "-ac", "1", "-ar", "22050",
        out_ghost_mp3
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(out_ghost_mp3):
        ghost_size = os.path.getsize(out_ghost_mp3) / (1024 * 1024)
        print(f"   ✅ Ghost (32kbps) generated: {out_ghost_mp3} ({ghost_size:.2f} MB)")

def main():
    print("=================================================================")
    print("🚀 GENERATING CASUAL STUDENT-GRADE CONVERSATIONAL DUBS (FAST PACED)")
    print("=================================================================")
    
    for ep_id, (hi_track, en_track) in AUDIO_MAP.items():
        if hi_track:
            build_dialogue_track(ep_id, "hi", hi_track)
        if en_track:
            build_dialogue_track(ep_id, "en", en_track)
            
    # Cleanup temp directory
    try:
        shutil.rmtree(TEMP_DIR)
    except Exception:
        pass
        
    print("\n🎉 ALL CASUAL STUDENT-GRADE DUBS SUCCESSFULLY COMPILED!")

if __name__ == "__main__":
    main()
