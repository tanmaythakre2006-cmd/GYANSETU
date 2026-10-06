import os
import sys
import subprocess
import zipfile
import shutil

def run_cmd(cmd, desc):
    print(f"==> {desc}...")
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"ERROR: {desc} failed with code {res.returncode}")
        print("STDOUT:", res.stdout)
        print("STDERR:", res.stderr)
        sys.exit(1)
    else:
        if res.stdout.strip():
            print(res.stdout.strip())
        print(f"==> {desc} succeeded!\n")

def main():
    sdk_dir = os.path.expandvars(r"%LOCALAPPDATA%\Android\Sdk")
    build_tools = os.path.join(sdk_dir, "build-tools", "34.0.0")
    android_jar = os.path.join(sdk_dir, "platforms", "android-35", "android.jar")
    
    aapt2 = os.path.join(build_tools, "aapt2.exe")
    d8_jar = os.path.join(build_tools, "lib", "d8.jar")
    zipalign = os.path.join(build_tools, "zipalign.exe")
    apksigner_jar = os.path.join(build_tools, "lib", "apksigner.jar")

    base_dir = os.path.abspath(os.path.dirname(__file__))
    android_dir = os.path.join(base_dir, "android")
    build_dir = os.path.join(android_dir, "build")
    gen_dir = os.path.join(build_dir, "gen")
    classes_dir = os.path.join(build_dir, "classes")
    dex_dir = os.path.join(build_dir, "dex")
    out_dir = os.path.join(base_dir, "assets", "downloads")
    
    os.makedirs(gen_dir, exist_ok=True)
    os.makedirs(classes_dir, exist_ok=True)
    os.makedirs(dex_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)

    # 1. aapt2 compile
    compiled_res = os.path.join(build_dir, "compiled_res.zip")
    res_dir = os.path.join(android_dir, "res")
    run_cmd(f'"{aapt2}" compile --dir "{res_dir}" -o "{compiled_res}"', "1. Compiling Android Resources")

    # 2. aapt2 link
    manifest = os.path.join(android_dir, "AndroidManifest.xml")
    base_apk = os.path.join(build_dir, "base.apk")
    assets_dir = os.path.join(android_dir, "assets")
    run_cmd(
        f'"{aapt2}" link -I "{android_jar}" --manifest "{manifest}" '
        f'-o "{base_apk}" --java "{gen_dir}" -A "{assets_dir}" -0 mp3 -0 jpg -0 png "{compiled_res}"',
        "2. Linking Resources & Packaging Assets (Uncompressed MP3 for zero latency)"
    )

    # 3. javac
    r_java = os.path.join(gen_dir, "com", "gyansetu", "app", "R.java")
    main_java = os.path.join(android_dir, "src", "com", "gyansetu", "app", "MainActivity.java")
    run_cmd(
        f'javac -cp "{android_jar}" -d "{classes_dir}" "{r_java}" "{main_java}"',
        "3. Compiling Java Source Files (FLAG_SECURE & WebView)"
    )

    # 4. d8 (dex)
    class_files = [
        os.path.join(classes_dir, "com", "gyansetu", "app", f)
        for f in os.listdir(os.path.join(classes_dir, "com", "gyansetu", "app"))
        if f.endswith(".class")
    ]
    classes_arg = " ".join([f'"{cf}"' for cf in class_files])
    run_cmd(f'java -cp "{d8_jar}" com.android.tools.r8.D8 --lib "{android_jar}" --output "{dex_dir}" {classes_arg}', "4. Converting to Dalvik Executable (classes.dex)")

    # 5. Insert classes.dex into base.apk
    print("==> 5. Adding classes.dex to base.apk...")
    dex_file = os.path.join(dex_dir, "classes.dex")
    with zipfile.ZipFile(base_apk, 'a', compression=zipfile.ZIP_DEFLATED) as z:
        z.write(dex_file, "classes.dex")
    print("==> 5. Added classes.dex successfully!\n")

    # 6. zipalign
    aligned_apk = os.path.join(build_dir, "aligned.apk")
    if os.path.exists(aligned_apk):
        os.remove(aligned_apk)
    run_cmd(f'"{zipalign}" -p -f 4 "{base_apk}" "{aligned_apk}"', "6. ZipAligning APK (4-byte alignment)")

    # 7. Generate Keystore if needed
    keystore = os.path.join(android_dir, "gyansetu.keystore")
    if not os.path.exists(keystore):
        run_cmd(
            f'keytool -genkeypair -v -keystore "{keystore}" -alias gyansetu '
            f'-keyalg RSA -keysize 2048 -validity 10000 -storepass gyansetu123 -keypass gyansetu123 '
            f'-dname "CN=GyanSetu, OU=DigitalRadio, O=GyanSetu, L=Mumbai, ST=Maharashtra, C=IN"',
            "7. Generating GyanSetu Secure Release Keystore"
        )

    # 8. apksigner
    final_apk = os.path.join(out_dir, "GyanSetu.apk")
    if os.path.exists(final_apk):
        os.remove(final_apk)
    run_cmd(
        f'java -jar "{apksigner_jar}" sign --ks "{keystore}" --ks-pass pass:gyansetu123 '
        f'--ks-key-alias gyansetu --key-pass pass:gyansetu123 --out "{final_apk}" "{aligned_apk}"',
        "8. Cryptographically Signing GyanSetu.apk (v2/v3 APK Signature Scheme)"
    )

    # 9. Verify
    run_cmd(f'java -jar "{apksigner_jar}" verify --verbose "{final_apk}"', "9. Verifying APK Signature")

    apk_size_mb = os.path.getsize(final_apk) / (1024 * 1024)
    print("=" * 60)
    print(f"🎉 SUCCESS! GyanSetu APK Generated Successfully!")
    print(f"📦 Output File: {final_apk}")
    print(f"📊 File Size: {apk_size_mb:.2f} MB (includes all 7 full studio episodes offline)")
    print("=" * 60)

if __name__ == "__main__":
    main()
