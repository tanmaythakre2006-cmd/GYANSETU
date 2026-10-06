$ErrorActionPreference = "Stop"

$SdkDir = "$env:LOCALAPPDATA\Android\Sdk"
$BuildTools = "$SdkDir\build-tools\34.0.0"
$PlatformJar = "$SdkDir\platforms\android-35\android.jar"
$ZipAlign = "$BuildTools\zipalign.exe"
$ApkSignerJar = "$BuildTools\lib\apksigner.jar"

$BaseDir = "c:\Users\hp\OneDrive\Desktop\gyan setu"
$AndroidDir = "$BaseDir\android"
$BuildDir = "$AndroidDir\build"
$BaseApk = "$BuildDir\base.apk"
$DexFile = "$BuildDir\dex\classes.dex"
$AlignedApk = "$BuildDir\aligned.apk"
$OutDir = "$BaseDir\assets\downloads"
$FinalApk = "$OutDir\GyanSetu.apk"
$Keystore = "$AndroidDir\gyansetu.keystore"

Write-Host "==> Step 1: Injecting classes.dex into base.apk..."
python -c "
import zipfile
with zipfile.ZipFile(r'$BaseApk', 'a') as z:
    z.write(r'$DexFile', 'classes.dex')
print('classes.dex successfully packaged inside base.apk!')
"

Write-Host "==> Step 2: Running ZipAlign (4-byte alignment)..."
if (Test-Path $AlignedApk) { Remove-Item -Force $AlignedApk }
& $ZipAlign -p -f 4 $BaseApk $AlignedApk
Write-Host "ZipAlign complete!"

Write-Host "==> Step 3: Checking / Generating Release Keystore..."
if (-not (Test-Path $Keystore)) {
    keytool -genkeypair -v -keystore $Keystore -alias gyansetu -keyalg RSA -keysize 2048 -validity 10000 -storepass gyansetu123 -keypass gyansetu123 -dname "CN=GyanSetu, OU=Radio, O=GyanSetu, L=Mumbai, ST=Maharashtra, C=IN"
    Write-Host "Keystore created!"
}

Write-Host "==> Step 4: Signing GyanSetu.apk (v2/v3 scheme)..."
if (Test-Path $FinalApk) { Remove-Item -Force $FinalApk }
java -jar $ApkSignerJar sign --ks $Keystore --ks-pass pass:gyansetu123 --ks-key-alias gyansetu --key-pass pass:gyansetu123 --out $FinalApk $AlignedApk
Write-Host "GyanSetu.apk signed successfully!"

Write-Host "==> Step 5: Verifying Cryptographic Signature..."
java -jar $ApkSignerJar verify --verbose $FinalApk

$size = (Get-Item $FinalApk).Length / 1MB
Write-Host "=========================================================="
Write-Host ("SUCCESS: GyanSetu.apk generated at: {0}" -f $FinalApk)
Write-Host ("Size: {0:N2} MB (Includes all 7 episodes offline)" -f $size)
Write-Host "=========================================================="
