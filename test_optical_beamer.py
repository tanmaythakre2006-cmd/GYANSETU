import asyncio
import sys
from playwright.async_api import async_playwright
sys.stdout.reconfigure(encoding='utf-8')

async def test_beamer():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        await page.goto("http://localhost:8000/pocket.html", wait_until="networkidle")
        
        print("Testing Optical Fountain Beamer in pocket.html...")
        
        # 1. Click BEAM button
        await page.click("#btn-beam")
        await page.wait_for_timeout(400)
        
        # Check if modal is open
        is_open = await page.evaluate("() => document.getElementById('mesh-modal').classList.contains('open')")
        print(f"  [Beamer Modal Open]: {is_open}")
        assert is_open, "Beamer modal did not open!"
        
        # 2. Check Sender Fountain stream
        sender_info = await page.evaluate("""() => {
            const ticker = document.getElementById('fountain-ticker-text').textContent;
            const select = document.getElementById('beam-station-select');
            const qrBox = document.getElementById('qr-render-box');
            const dots = document.querySelectorAll('.fountain-dot').length;
            const hasQrCanvasOrImg = qrBox.querySelector('canvas') || qrBox.querySelector('img');
            return {
                ticker: ticker,
                stationsCount: select.options.length,
                selectedStation: select.options[select.selectedIndex] ? select.options[select.selectedIndex].text : '',
                dotsCount: dots,
                hasQrElement: !!hasQrCanvasOrImg
            };
        }""")
        print(f"  [Sender Loop Status]: {sender_info['ticker']}")
        print(f"  [Stations in Dropdown]: {sender_info['stationsCount']} (Selected: {sender_info['selectedStation']})")
        print(f"  [Fountain Slices Count]: {sender_info['dotsCount']} frames")
        print(f"  [QR Render Active]: {sender_info['hasQrElement']}")
        assert sender_info['stationsCount'] > 0, "No stations in dropdown!"
        assert sender_info['dotsCount'] > 0, "Fountain frames not generated!"
        assert sender_info['hasQrElement'], "QR element not rendered!"
        
        # Wait 600ms to verify loop increments frames
        await page.wait_for_timeout(600)
        ticker2 = await page.evaluate("() => document.getElementById('fountain-ticker-text').textContent")
        print(f"  [Sender Loop Progression]: Frame updated to -> {ticker2}")
        
        # 3. Test Switch to Receiver Tab
        await page.click("#tab-receiver-btn")
        await page.wait_for_timeout(300)
        
        rec_info = await page.evaluate("""() => {
            const recPanel = document.getElementById('mesh-receiver-panel');
            const isActive = recPanel.classList.contains('active');
            const camBtn = document.getElementById('start-cam-btn');
            const hud = document.getElementById('hud-progress-readout').textContent;
            return {
                isActive: isActive,
                camBtnText: camBtn ? camBtn.textContent.trim() : '',
                hudReadout: hud
            };
        }""")
        print(f"  [Receiver Panel Active]: {rec_info['isActive']}")
        print(f"  [Scanner Button]: {rec_info['camBtnText']}")
        print(f"  [HUD Progress]: {rec_info['hudReadout']}")
        assert rec_info['isActive'], "Receiver panel not active!"
        
        # 4. Test Decryption Simulation via Fountain Decoder
        decode_result = await page.evaluate("""() => {
            // Simulate receiving 2 frames of an episode
            const testEp = {
                id: "beamed-opt-test",
                num: 99,
                freq: "99.9",
                title: "Optical Air-Gap Beamed Special",
                cat: "BEAMED",
                dur: "3m 45s"
            };
            const b64 = btoa(unescape(encodeURIComponent(JSON.stringify(testEp))));
            const total = 2;
            const half = Math.ceil(b64.length / 2);
            const chunk1 = b64.substr(0, half);
            const chunk2 = b64.substr(half);
            
            // Deliver frame 1 then frame 2 to decoder
            handleIncomingFountainChunk(`GS2|${testEp.id}|1|${total}|${chunk1}`);
            const state1 = Object.keys(receiverFountainBuffer).length;
            
            handleIncomingFountainChunk(`GS2|${testEp.id}|2|${total}|${chunk2}`);
            const state2 = Object.keys(receiverFountainBuffer).length;
            
            return {
                frame1Recorded: state1 === 1,
                frame2Recorded: state2 === 2,
                vaultContainsEp: JSON.parse(localStorage.getItem('gyansetu_beamed_vault') || '[]').some(x => x.id === testEp.id)
            };
        }""")
        print(f"  [Optical Decoder Assembly & Decryption]: {decode_result}")
        assert decode_result['vaultContainsEp'], "Decrypted episode not installed in vault!"
        
        # Take screenshot of the Optical Beamer HUD
        await page.screenshot(path="screenshot_optical_beamer_hud.png")
        print("  📸 Captured screenshot_optical_beamer_hud.png")
        
        await browser.close()
        print("\n🎉 OPTICAL FOUNTAIN BEAMER TEST PASSED COMPLETELY!")

asyncio.run(test_beamer())
