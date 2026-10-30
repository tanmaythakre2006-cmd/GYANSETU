import os
import sys
import subprocess
import zipfile
import shutil
import tempfile

def run_cmd(cmd, desc):
    print(f"==> {desc}...", flush=True)
    res = subprocess.run(cmd, shell=True, text=True)
    if res.returncode != 0:
        print(f"ERROR: {desc} failed with code {res.returncode}", flush=True)
        sys.exit(1)
    print(f"==> {desc} succeeded!\n", flush=True)

def main():
    sdk_dir = os.path.expandvars(r"%LOCALAPPDATA%\Android\Sdk")
    build_tools = os.path.join(sdk_dir, "build-tools", "34.0.0")
    android_jar = os.path.join(sdk_dir, "platforms", "android-35", "android.jar")
    
    aapt2 = os.path.join(build_tools, "aapt2.exe")
    d8_jar = os.path.join(build_tools, "lib", "d8.jar")
    zipalign = os.path.join(build_tools, "zipalign.exe")
    apksigner_jar = os.path.join(build_tools, "lib", "apksigner.jar")

    base_dir = os.path.abspath(os.path.dirname(__file__))
    android_dir = os.path.join(base_dir, "android_pocket")
    build_dir = os.path.join(android_dir, "build")
    gen_dir = os.path.join(build_dir, "gen")
    classes_dir = os.path.join(build_dir, "classes")
    dex_dir = os.path.join(build_dir, "dex")
    out_dir = os.path.join(base_dir, "assets", "downloads")
    keystore = os.path.join(base_dir, "android", "gyansetu.keystore")
    
    os.makedirs(gen_dir, exist_ok=True)
    os.makedirs(classes_dir, exist_ok=True)
    os.makedirs(dex_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)

    # 1. aapt2 compile
    compiled_res = os.path.join(build_dir, "compiled_res.zip")
    res_dir = os.path.join(android_dir, "res")
    run_cmd(f'"{aapt2}" compile --dir "{res_dir}" -o "{compiled_res}"', "1. Compiling Android Resources")

    # 2. Javac compile
    manifest = os.path.join(android_dir, "AndroidManifest.xml")
    run_cmd(
        f'"{aapt2}" link -I "{android_jar}" --manifest "{manifest}" '
        f'--java "{gen_dir}" -o "{os.path.join(build_dir, "temp_link.apk")}" "{compiled_res}"',
        "2. Generating R.java"
    )

    r_java = os.path.join(gen_dir, "com", "gyansetu", "pocketradio", "R.java")
    main_java = os.path.join(android_dir, "src", "com", "gyansetu", "pocketradio", "MainActivity.java")
    run_cmd(
        f'javac -cp "{android_jar}" -d "{classes_dir}" "{r_java}" "{main_java}"',
        "3. Compiling Java Source Files"
    )

    # 3. d8 (dex) via java directly
    class_files = []
    for root, _, files in os.walk(classes_dir):
        for f in files:
            if f.endswith(".class"):
                class_files.append(os.path.join(root, f))
    d8_cmd = ["java", "-cp", d8_jar, "com.android.tools.r8.D8", "--lib", android_jar, "--output", dex_dir] + class_files
    print("==> 4. Converting to Dalvik Executable (classes.dex)...", flush=True)
    d8_res = subprocess.run(d8_cmd, capture_output=True, text=True)
    if d8_res.returncode != 0:
        print("ERROR: D8 failed:", d8_res.stderr, flush=True)
        sys.exit(1)
    print("==> 4. Converting to Dalvik Executable succeeded!\n", flush=True)

    dex_file = os.path.join(dex_dir, "classes.dex")

    # 4. Helper to build variant
    def build_variant(apk_name, include_audio):
        print(f"PACKAGING: {apk_name} (Include audio: {include_audio})", flush=True)
        
        # Use temp directory outside OneDrive to avoid file locks
        temp_dir = tempfile.mkdtemp(prefix=f"gyansetu_{apk_name}_")
        variant_assets = os.path.join(temp_dir, "assets")
        shutil.copytree(os.path.join(android_dir, "assets"), variant_assets)
        
        if not include_audio:
            audio_dir = os.path.join(variant_assets, "assets", "audio")
            if os.path.exists(audio_dir):
                for f in os.listdir(audio_dir):
                    fpath = os.path.join(audio_dir, f)
                    if os.path.isfile(fpath):
                        os.remove(fpath)
        
        base_apk = os.path.join(temp_dir, f"{apk_name}_base.apk")
        run_cmd(
            f'"{aapt2}" link -I "{android_jar}" --manifest "{manifest}" '
            f'-o "{base_apk}" -A "{variant_assets}" -0 mp3 -0 jpg -0 png -0 js "{compiled_res}"',
            f"Packaging Assets for {apk_name}"
        )
        
        with zipfile.ZipFile(base_apk, 'a', compression=zipfile.ZIP_DEFLATED) as z:
            z.write(dex_file, "classes.dex")
            
        aligned_apk = os.path.join(temp_dir, f"{apk_name}_aligned.apk")
        run_cmd(f'"{zipalign}" -p -f 4 "{base_apk}" "{aligned_apk}"', f"ZipAligning {apk_name}")
        
        final_apk = os.path.join(out_dir, f"{apk_name}.apk")
        if os.path.exists(final_apk):
            os.remove(final_apk)
        run_cmd(
            f'java -jar "{apksigner_jar}" sign --ks "{keystore}" --ks-pass pass:gyansetu123 '
            f'--ks-key-alias gyansetu --key-pass pass:gyansetu123 --out "{final_apk}" "{aligned_apk}"',
            f"Cryptographically Signing {apk_name}.apk"
        )
        
        size_mb = os.path.getsize(final_apk) / (1024 * 1024)
        print(f"==> Finished {apk_name}.apk: {size_mb:.2f} MB\n", flush=True)
        
        # Cleanup temp directory
        try:
            shutil.rmtree(temp_dir)
        except Exception:
            pass

    # Build Full Offline Vault (with all 13 episodes)
    build_variant("GyanSetu-PocketRadio", include_audio=True)

    # Build Ultra-Lite Mesh Shell (with zero pre-baked audio)
    build_variant("GyanSetu-PocketRadio-Lite", include_audio=False)

if __name__ == "__main__":
    main()
