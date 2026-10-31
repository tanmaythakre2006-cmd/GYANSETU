import json
import os

with open('batch_synthesis_manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# Construct Jupyter Notebook JSON structure
notebook = {
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "accelerator": "GPU",
        "colab": {
            "gpuType": "T4",
            "provenance": []
        },
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3"
        },
        "language_info": {
            "name": "python"
        }
    },
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 🎙️ GyanSetu — Simran Ailani 1-Click Neural Voice Cloner (XTTS v2)\n",
                "**Curated by Simran Ailani • Founder & Lead Host**  \n",
                "*Demystifying Complex Ideas • Igniting Curiosity Across the World*\n",
                "\n",
                "---\n",
                "\n",
                "### ⚡ 1-Click Execution:\n",
                "In Google Colab, simply click **Runtime** in the top menu → **Run all** (or press `Ctrl + F9`).\n",
                "\n",
                "This will:\n",
                "1. Connect to a free Google Cloud **Tesla T4 GPU** (16 GB VRAM).\n",
                "2. Load the **Coqui XTTS v2** 2.4-billion-parameter neural voice cloning model.\n",
                "3. Ingest the 12-second clean reference sample of **Simran Ailani**'s voice.\n",
                "4. Synthesize all 14 Hindi & English dub tracks matching her exact vocal timbre, pitch, and cadence.\n",
                "5. Automatically package and trigger a browser download for `gyansetu_neural_dubs.zip` directly to your computer!"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Step 1: Verify Free Cloud GPU Acceleration & Install Dependencies\n",
                "import os\n",
                "import sys\n",
                "import torch\n",
                "import subprocess\n",
                "\n",
                "print(\"🔍 Checking Cloud GPU Acceleration...\")\n",
                "if torch.cuda.is_available():\n",
                "    gpu_name = torch.cuda.get_device_name(0)\n",
                "    vram = torch.cuda.get_device_properties(0).total_memory / (1024**3)\n",
                "    print(f\"✅ High-Speed Cloud GPU Active: {gpu_name} ({vram:.1f} GB VRAM)\")\n",
                "else:\n",
                "    print(\"⚠️ Running on CPU. For 10x faster speed, select Runtime -> Change runtime type -> T4 GPU.\")\n",
                "\n",
                "print(\"\\n📦 Installing Coqui XTTS v2 Neural Engine & FFmpeg...\")\n",
                "subprocess.run([sys.executable, \"-m\", \"pip\", \"install\", \"-q\", \"--no-input\", \"TTS==0.22.0\", \"soundfile\", \"pydub\"], check=True)\n",
                "print(\"✅ All neural voice synthesis packages initialized successfully!\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Step 2: Fetch & Verify Simran Ailani's Clean Reference Voice Sample\n",
                "import os\n",
                "import urllib.request\n",
                "import subprocess\n",
                "\n",
                "os.makedirs(\"reference\", exist_ok=True)\n",
                "os.makedirs(\"raw_wavs\", exist_ok=True)\n",
                "os.makedirs(\"gyansetu_dub_masters\", exist_ok=True)\n",
                "\n",
                "ref_sample_path = \"reference/simran_reference_sample.wav\"\n",
                "\n",
                "# Primary URL from GitHub repository\n",
                "github_url = \"https://raw.githubusercontent.com/tanmaythakre2006-cmd/GYANSETU/main/assets/audio_reference/simran_reference_sample.wav\"\n",
                "# Fallback URL from live Vercel deployment\n",
                "vercel_url = \"https://gyansetu-five.vercel.app/assets/audio/ep1-can-chemistry-explain-consciousness.mp3\"\n",
                "\n",
                "downloaded = False\n",
                "try:\n",
                "    print(\"📥 Fetching Simran Ailani's reference voice sample from repository...\")\n",
                "    urllib.request.urlretrieve(github_url, ref_sample_path)\n",
                "    if os.path.exists(ref_sample_path) and os.path.getsize(ref_sample_path) > 10000:\n",
                "        downloaded = True\n",
                "        print(f\"✅ Primary voice sample verified ({os.path.getsize(ref_sample_path)} bytes)\")\n",
                "except Exception as e:\n",
                "    print(f\"Notice on primary fetch: {e}\")\n",
                "\n",
                "if not downloaded:\n",
                "    print(\"📥 Fetching master audio stream from live GyanSetu production server...\")\n",
                "    temp_mp3 = \"reference/temp_stream.mp3\"\n",
                "    urllib.request.urlretrieve(vercel_url, temp_mp3)\n",
                "    # Extract 12-second speech sample (00:00:04 to 00:00:16) with FFmpeg\n",
                "    subprocess.run([\n",
                "        \"ffmpeg\", \"-y\", \"-ss\", \"00:00:04\", \"-t\", \"12\",\n",
                "        \"-i\", temp_mp3, \"-ar\", \"24000\", \"-ac\", \"1\", \"-c:a\", \"pcm_s16le\",\n",
                "        ref_sample_path\n",
                "    ], check=True)\n",
                "    print(\"✅ Reference sample sliced & formatted into 24kHz mono PCM WAV!\")\n",
                "\n",
                "print(f\"🎯 Reference Sample Ready: {ref_sample_path}\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Step 3: Load Coqui XTTS v2 Neural Voice Model onto GPU\n",
                "from TTS.api import TTS\n",
                "import torch\n",
                "\n",
                "device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n",
                "print(f\"🧠 Priming Coqui XTTS v2 Neural Model on {device.upper()}...\")\n",
                "tts = TTS(\"tts_models/multilingual/multi-dataset/xtts_v2\").to(device)\n",
                "print(\"✅ XTTS v2 Neural Voice Cloner loaded in GPU VRAM and ready for inference!\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Step 4: Batch Synthesize All 14 GyanSetu Dub Tracks in Simran's Voice\n",
                "import time\n",
                "import subprocess\n",
                "\n",
                f"episodes = {json.dumps(manifest, ensure_ascii=False, indent=2)}\n",
                "\n",
                "print(f\"🎙️ Commencing Batch Neural Voice Cloning for {len(episodes)} master tracks...\")\n",
                "batch_start = time.time()\n",
                "\n",
                "for idx, ep in enumerate(episodes, 1):\n",
                "    filename_mp3 = ep['filename']\n",
                "    filename_wav = filename_mp3.replace('.mp3', '.wav')\n",
                "    raw_wav_path = os.path.join('raw_wavs', filename_wav)\n",
                "    final_mp3_path = os.path.join('gyansetu_dub_masters', filename_mp3)\n",
                "    lang = ep['lang']\n",
                "    text = ep['text']\n",
                "    title = ep['title']\n",
                "    \n",
                "    print(f\"\\n------------------------------------------------------------\")\n",
                "    print(f\"[{idx}/{len(episodes)}] Cloning: {title}\")\n",
                "    print(f\"       Target File : {filename_mp3}\")\n",
                "    print(f\"       Language    : {lang.upper()} | Script Length: {len(text)} characters\")\n",
                "    \n",
                "    t0 = time.time()\n",
                "    # XTTS v2 inference with Simran's vocal embedding\n",
                "    tts.tts_to_file(\n",
                "        text=text,\n",
                "        speaker_wav=ref_sample_path,\n",
                "        language=lang,\n",
                "        file_path=raw_wav_path,\n",
                "        split_sentences=True\n",
                "    )\n",
                "    synth_dur = time.time() - t0\n",
                "    \n",
                "    # Convert to standard 128 kbps broadcast MP3\n",
                "    subprocess.run([\n",
                "        \"ffmpeg\", \"-y\", \"-i\", raw_wav_path,\n",
                "        \"-codec:a\", \"libmp3lame\", \"-b:a\", \"128k\", \"-ar\", \"44100\",\n",
                "        final_mp3_path\n",
                "    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)\n",
                "    \n",
                "    mp3_kb = os.path.getsize(final_mp3_path) / 1024\n",
                "    print(f\"       ✅ Synthesized & Encoded in {synth_dur:.1f}s | Output: {mp3_kb:.1f} KB\")\n",
                "\n",
                "total_sec = time.time() - batch_start\n",
                "print(f\"\\n🎉 All {len(episodes)} Dub Tracks Successfully Synthesized in {total_sec/60:.2f} minutes!\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Step 5: Package Archive & Automatically Trigger Browser Download\n",
                "import shutil\n",
                "from google.colab import files\n",
                "\n",
                "zip_base_name = \"gyansetu_neural_dubs\"\n",
                "print(\"📦 Compressing all 14 dub audio tracks into zip archive...\")\n",
                "shutil.make_archive(zip_base_name, \"zip\", \"gyansetu_dub_masters\")\n",
                "final_zip = f\"{zip_base_name}.zip\"\n",
                "\n",
                "zip_size_mb = os.path.getsize(final_zip) / (1024 * 1024)\n",
                "print(f\"✅ Archive generated: {final_zip} ({zip_size_mb:.2f} MB)\")\n",
                "print(\"🚀 Triggering automatic browser download to your laptop now...\")\n",
                "\n",
                "try:\n",
                "    files.download(final_zip)\n",
                "    print(\"🎉 Download initiated! Look for gyansetu_neural_dubs.zip in your browser's Downloads.\")\n",
                "except Exception as e:\n",
                "    print(f\"Notice: If automatic download did not pop up, right-click '{final_zip}' in the Colab file tree on the left and select 'Download'.\")"
            ]
        }
    ]
}

notebook_path = "GyanSetu_Neural_Voice_Clone.ipynb"
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print(f"Generated {notebook_path} ({os.path.getsize(notebook_path)} bytes)")
