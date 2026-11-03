import asyncio
import os
import shutil
from playwright.async_api import async_playwright

ART_DIR = r"C:\Users\hp\.gemini\antigravity\brain\8c6faad8-6d94-4941-8e8b-9955446c4b2a"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # =====================================================================
        # 1. LENOVO TAB M8 HD (1280 x 800 LANDSCAPE)
        # =====================================================================
        print("=== 1. Capturing Lenovo Tab M8 HD (1280x800 Landscape) ===")
        context_lenovo = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context_lenovo.new_page()
        await page.goto("http://localhost:8000/pocket.html", wait_until="networkidle")
        await page.wait_for_timeout(500)

        # 1A. 1978 Vintage Idle (Station 13 - Nagpur)
        await page.evaluate("""() => {
            if (window.setRadioTheme) window.setRadioTheme('vintage-1978');
            document.getElementById('radio-chassis').setAttribute('data-theme', 'vintage-1978');
        }""")
        await page.wait_for_timeout(300)
        await page.screenshot(path="lenovo_tab_1978_vintage_idle.png")
        print("Saved lenovo_tab_1978_vintage_idle.png")

        # 1B. 1978 Vintage Active Audio Playback (Station 10 - Napoleon)
        await page.evaluate("""() => {
            // Tune to Station 10 (Napoleon)
            if (window.tuneToEpisode) {
                window.tuneToEpisode(3, false); // Index for Napoleon
            }
            // Animate VU meters, spectrum, magic eye, and transport play state
            const needleL = document.getElementById('vu-needle-left');
            const needleR = document.getElementById('vu-needle-right');
            if (needleL) needleL.style.transform = 'rotate(14deg)';
            if (needleR) needleR.style.transform = 'rotate(22deg)';

            const magicEye = document.getElementById('magic-eye-beam');
            if (magicEye) magicEye.style.width = '36px';

            const bars = document.querySelectorAll('.spec-bar');
            const heights = [45, 78, 92, 85, 64, 88, 72, 54, 82, 96, 75, 60, 48, 38, 70, 50];
            bars.forEach((b, i) => {
                b.style.height = `${heights[i % heights.length]}%`;
            });

            const playLabel = document.getElementById('play-label');
            if (playLabel) playLabel.textContent = 'PAUSE';
            const playIcon = document.getElementById('play-icon');
            if (playIcon) playIcon.innerHTML = '&#10074;&#10074;';
            const playBtn = document.getElementById('btn-play');
            if (playBtn) playBtn.classList.add('playing');
        }""")
        await page.wait_for_timeout(300)
        await page.screenshot(path="lenovo_tab_1978_vintage_active_audio.png")
        print("Saved lenovo_tab_1978_vintage_active_audio.png")

        # 1C. 1978 Vintage Cosmos Station Select
        await page.evaluate("""() => {
            if (window.tuneToEpisode) {
                window.tuneToEpisode(12, false); // Station 1 (Cosmos)
            }
            const needleL = document.getElementById('vu-needle-left');
            const needleR = document.getElementById('vu-needle-right');
            if (needleL) needleL.style.transform = 'rotate(4deg)';
            if (needleR) needleR.style.transform = 'rotate(9deg)';
        }""")
        await page.wait_for_timeout(300)
        await page.screenshot(path="lenovo_tab_1978_vintage_station_select.png")
        print("Saved lenovo_tab_1978_vintage_station_select.png")

        # 1D. Carvaan Neo Idle (Station 13 - Nagpur)
        await page.evaluate("""() => {
            if (window.setRadioTheme) window.setRadioTheme('carvaan-neo');
            document.getElementById('radio-chassis').setAttribute('data-theme', 'carvaan-neo');
            if (window.tuneToEpisode) {
                window.tuneToEpisode(0, false);
            }
            const needleL = document.getElementById('vu-needle-left');
            const needleR = document.getElementById('vu-needle-right');
            if (needleL) needleL.style.transform = 'rotate(-38deg)';
            if (needleR) needleR.style.transform = 'rotate(-38deg)';

            const magicEye = document.getElementById('magic-eye-beam');
            if (magicEye) magicEye.style.width = '10px';

            const bars = document.querySelectorAll('.spec-bar');
            bars.forEach(b => b.style.height = '15%');

            const playLabel = document.getElementById('play-label');
            if (playLabel) playLabel.textContent = 'PLAY';
            const playIcon = document.getElementById('play-icon');
            if (playIcon) playIcon.innerHTML = '&#9654;';
            const playBtn = document.getElementById('btn-play');
            if (playBtn) playBtn.classList.remove('playing');
        }""")
        await page.wait_for_timeout(300)
        await page.screenshot(path="lenovo_tab_carvaan_neo_idle.png")
        print("Saved lenovo_tab_carvaan_neo_idle.png")

        # 1E. Carvaan Neo Active Audio Playback (Station 12 - Oops, I Created Life)
        await page.evaluate("""() => {
            if (window.tuneToEpisode) {
                window.tuneToEpisode(1, false);
            }
            const needleL = document.getElementById('vu-needle-left');
            const needleR = document.getElementById('vu-needle-right');
            if (needleL) needleL.style.transform = 'rotate(18deg)';
            if (needleR) needleR.style.transform = 'rotate(26deg)';

            const magicEye = document.getElementById('magic-eye-beam');
            if (magicEye) magicEye.style.width = '38px';

            const bars = document.querySelectorAll('.spec-bar');
            const heights = [60, 85, 95, 90, 75, 98, 80, 65, 88, 100, 82, 70, 55, 45, 78, 62];
            bars.forEach((b, i) => {
                b.style.height = `${heights[i % heights.length]}%`;
            });

            const trackLabel = document.getElementById('pocket-track-label');
            if (trackLabel) trackLabel.textContent = 'ENG DUB';
            const trackBtn = document.getElementById('btn-pocket-track');
            if (trackBtn) trackBtn.classList.add('dub-active');

            const playLabel = document.getElementById('play-label');
            if (playLabel) playLabel.textContent = 'PAUSE';
            const playIcon = document.getElementById('play-icon');
            if (playIcon) playIcon.innerHTML = '&#10074;&#10074;';
            const playBtn = document.getElementById('btn-play');
            if (playBtn) playBtn.classList.add('playing');
        }""")
        await page.wait_for_timeout(300)
        await page.screenshot(path="lenovo_tab_carvaan_neo_active_audio.png")
        print("Saved lenovo_tab_carvaan_neo_active_audio.png")

        # 1F. Carvaan Neo P2P Optical Beamer Modal (Transmitter Tab)
        await page.click("#btn-beam")
        await page.wait_for_timeout(400)
        await page.screenshot(path="lenovo_tab_carvaan_neo_beam_transmitter.png")
        print("Saved lenovo_tab_carvaan_neo_beam_transmitter.png")

        # 1G. Carvaan Neo P2P Optical Beamer Modal (Receiver Tab)
        receiver_tab = await page.query_selector("#mesh-tab-receiver")
        if not receiver_tab:
            tabs = await page.query_selector_all(".mesh-tab-btn")
            for t in tabs:
                txt = await t.text_content()
                if "RECEIVE" in txt or "SCAN" in txt or "RX" in txt:
                    receiver_tab = t
                    break
        if receiver_tab:
            await receiver_tab.click()
            await page.wait_for_timeout(300)
            await page.screenshot(path="lenovo_tab_carvaan_neo_beam_receiver.png")
            print("Saved lenovo_tab_carvaan_neo_beam_receiver.png")

        await context_lenovo.close()

        # =====================================================================
        # 2. MOBILE HANDHELD (390 x 844 PORTRAIT)
        # =====================================================================
        print("=== 2. Capturing Mobile Handheld (390x844 Portrait) ===")
        context_mob = await browser.new_context(viewport={'width': 390, 'height': 844})
        page_mob = await context_mob.new_page()
        await page_mob.goto("http://localhost:8000/pocket.html", wait_until="networkidle")
        await page_mob.wait_for_timeout(400)

        # 2A. Mobile 1978 Vintage Pocket Player
        await page_mob.evaluate("""() => {
            if (window.setRadioTheme) window.setRadioTheme('vintage-1978');
            document.getElementById('radio-chassis').setAttribute('data-theme', 'vintage-1978');
        }""")
        await page_mob.wait_for_timeout(300)
        await page_mob.screenshot(path="mobile_390_1978_vintage_pocket.png")
        print("Saved mobile_390_1978_vintage_pocket.png")

        # 2B. Mobile Carvaan Neo Pocket Player
        await page_mob.evaluate("""() => {
            if (window.setRadioTheme) window.setRadioTheme('carvaan-neo');
            document.getElementById('radio-chassis').setAttribute('data-theme', 'carvaan-neo');
        }""")
        await page_mob.wait_for_timeout(300)
        await page_mob.screenshot(path="mobile_390_carvaan_neo_pocket.png")
        print("Saved mobile_390_carvaan_neo_pocket.png")

        # 2C. Mobile Optical Beamer HUD
        await page_mob.click("#btn-beam")
        await page_mob.wait_for_timeout(400)
        await page_mob.screenshot(path="mobile_390_beam_hud_modal.png")
        print("Saved mobile_390_beam_hud_modal.png")
        await context_mob.close()

        # =====================================================================
        # 3. COMPACT ANDROID (360 x 800 PORTRAIT)
        # =====================================================================
        print("=== 3. Capturing Compact Android (360x800 Portrait) ===")
        context_compact = await browser.new_context(viewport={'width': 360, 'height': 800})
        page_compact = await context_compact.new_page()
        await page_compact.goto("http://localhost:8000/pocket.html", wait_until="networkidle")
        await page_compact.wait_for_timeout(300)
        await page_compact.evaluate("""() => {
            if (window.setRadioTheme) window.setRadioTheme('carvaan-neo');
            document.getElementById('radio-chassis').setAttribute('data-theme', 'carvaan-neo');
        }""")
        await page_compact.wait_for_timeout(300)
        await page_compact.screenshot(path="mobile_360_carvaan_neo.png")
        print("Saved mobile_360_carvaan_neo.png")
        await context_compact.close()

        # =====================================================================
        # 4. TABLET 4:3 (1024 x 768 LANDSCAPE)
        # =====================================================================
        print("=== 4. Capturing Tablet 4:3 (1024x768 Landscape) ===")
        context_tab = await browser.new_context(viewport={'width': 1024, 'height': 768})
        page_tab = await context_tab.new_page()
        await page_tab.goto("http://localhost:8000/pocket.html", wait_until="networkidle")
        await page_tab.wait_for_timeout(300)
        await page_tab.evaluate("""() => {
            if (window.setRadioTheme) window.setRadioTheme('vintage-1978');
            document.getElementById('radio-chassis').setAttribute('data-theme', 'vintage-1978');
        }""")
        await page_tab.wait_for_timeout(300)
        await page_tab.screenshot(path="tablet_1024x768_vintage.png")
        print("Saved tablet_1024x768_vintage.png")
        await context_tab.close()

        await browser.close()

        # =====================================================================
        # COPY ALL CAPTURED SCREENSHOTS TO ARTIFACT DIRECTORY
        # =====================================================================
        all_shots = [
            "lenovo_tab_1978_vintage_idle.png",
            "lenovo_tab_1978_vintage_active_audio.png",
            "lenovo_tab_1978_vintage_station_select.png",
            "lenovo_tab_carvaan_neo_idle.png",
            "lenovo_tab_carvaan_neo_active_audio.png",
            "lenovo_tab_carvaan_neo_beam_transmitter.png",
            "lenovo_tab_carvaan_neo_beam_receiver.png",
            "mobile_390_1978_vintage_pocket.png",
            "mobile_390_carvaan_neo_pocket.png",
            "mobile_390_beam_hud_modal.png",
            "mobile_360_carvaan_neo.png",
            "tablet_1024x768_vintage.png"
        ]
        print("=== Copying Screenshots to Artifact Directory ===")
        for shot in all_shots:
            if os.path.exists(shot):
                dst = os.path.join(ART_DIR, shot)
                shutil.copy2(shot, dst)
                print(f"Copied: {shot} -> {dst}")
        print("ALL SCREENSHOTS CAPTURED AND COPIED SUCCESSFULLY!")

if __name__ == "__main__":
    asyncio.run(main())
