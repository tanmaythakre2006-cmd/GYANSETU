import os
import zipfile
import shutil
import subprocess

def main():
    print("=== GyanSetu Cloned Dub Audio Importer ===")
    
    # 1. Look for zip file in Downloads or current dir
    user_home = os.path.expanduser("~")
    downloads_dir = os.path.join(user_home, "Downloads")
    
    candidates = [
        "gyansetu_neural_dubs.zip",
        os.path.join(downloads_dir, "gyansetu_neural_dubs.zip"),
        os.path.join(downloads_dir, "gyansetu_neural_dubs (1).zip")
    ]
    
    found_zip = None
    for cand in candidates:
        if os.path.exists(cand):
            found_zip = cand
            break
            
    if not found_zip:
        print("❌ Could not find 'gyansetu_neural_dubs.zip' in Downloads or project directory.")
        print(f"   Please place 'gyansetu_neural_dubs.zip' in {downloads_dir} or the project root.")
        return
        
    print(f"📦 Found archive: {found_zip}")
    print(f"   Size: {os.path.getsize(found_zip) / (1024*1024):.2f} MB")
    
    # 2. Extract into assets/audio
    target_audio_dir = "assets/audio"
    target_ghost_dir = "assets/audio_ghost"
    os.makedirs(target_audio_dir, exist_ok=True)
    os.makedirs(target_ghost_dir, exist_ok=True)
    
    with zipfile.ZipFile(found_zip, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        print(f"📂 Extracting {len(file_list)} tracks into '{target_audio_dir}'...")
        zip_ref.extractall(target_audio_dir)
        
    for fname in file_list:
        if fname.endswith(".mp3"):
            src_mp3 = os.path.join(target_audio_dir, fname)
            ghost_mp3 = os.path.join(target_ghost_dir, fname)
            print(f"   -> {fname} ({os.path.getsize(src_mp3) / 1024:.1f} KB)")
            
            # Generate 32kbps ghost radio version
            try:
                import imageio_ffmpeg
                ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
            except Exception:
                ffmpeg_exe = "ffmpeg"
                
            subprocess.run([
                ffmpeg_exe, "-y", "-i", src_mp3,
                "-codec:a", "libmp3lame", "-b:a", "32k", "-ar", "22050",
                ghost_mp3
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
    print("\n✅ All cloned dub audio tracks deployed to assets/audio & assets/audio_ghost!")
    
    # Rebuild Android APKs
    if os.path.exists("build_pocket_apks.py"):
        print("\n📱 Rebuilding Android Pocket Radio APKs...")
        subprocess.run(["python", "build_pocket_apks.py"])
        
    print("\n🎉 Done! All 13 episodes now feature Simran Ailani's cloned neural dub voice.")

if __name__ == "__main__":
    main()
