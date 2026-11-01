import asyncio
import sys
from playwright.async_api import async_playwright
sys.stdout.reconfigure(encoding='utf-8')

async def test_beamer():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 390, 'height': 844})
        await page.goto("http://localhost:8000/pocket.html", wait_until="networkidle")
        
        print("Testing Smart 20 MB Optical Vault & Mesh Beamer in pocket.html...")
        
        # 1. Click BEAM button
        await page.click("#btn-beam")
        await page.wait_for_timeout(400)
        
        is_open = await page.evaluate("() => document.getElementById('mesh-modal').classList.contains('open')")
        print(f"  [Beamer Modal Open]: {is_open}")
        assert is_open, "Beamer modal did not open!"
        
        # 2. Check Sender Fountain stream & Stations (including 20 MB Vault option)
        sender_info = await page.evaluate("""() => {
            const ticker = document.getElementById('fountain-ticker-text').textContent;
            const select = document.getElementById('beam-station-select');
            const qrBox = document.getElementById('qr-render-box');
            const dots = document.querySelectorAll('.fountain-dot').length;
            const hasQr = !!(qrBox.querySelector('canvas') || qrBox.querySelector('img'));
            const options = Array.from(select.options).map(o => ({ value: o.value, text: o.text }));
            return {
                ticker: ticker,
                stationsCount: select.options.length,
                options: options,
                dotsCount: dots,
                hasQr: hasQr
            };
        }""")
        print(f"  [Stations Count]: {sender_info['stationsCount']}")
        print(f"  [First Option]: {sender_info['options'][0]['text']}")
        assert sender_info['stationsCount'] >= 14, "Missing Full Vault option in dropdown!"
        assert "FULL VAULT" in sender_info['options'][0]['text'], "Full Vault not first option!"
        
        # 3. Select FULL VAULT and test 20 MB Vault Stream Generation
        await page.select_option("#beam-station-select", "all")
        await page.wait_for_timeout(500)
        
        vault_stream_info = await page.evaluate("""() => {
            const ticker = document.getElementById('fountain-ticker-text').textContent;
            const banner = document.getElementById('sender-status-banner').textContent;
            const pin = document.getElementById('mesh-pin-code').textContent;
            return {
                ticker: ticker,
                banner: banner,
                pin: pin,
                framesCount: senderFountainFrames.length
            };
        }""")
        print(f"  [20 MB Vault Stream Initialized]: {vault_stream_info['banner']}")
        print(f"  [Vault Fountain Frames]: {vault_stream_info['framesCount']} frames (PIN: {vault_stream_info['pin']})")
        assert vault_stream_info['framesCount'] > 0, "Vault frames not generated!"
        
        # 4. Test Switch to Receiver Tab
        await page.click("#tab-receiver-btn")
        await page.wait_for_timeout(300)
        
        rec_info = await page.evaluate("""() => {
            const recPanel = document.getElementById('mesh-receiver-panel');
            const camBtn = document.getElementById('start-cam-btn');
            const flipBtn = document.getElementById('flip-cam-btn');
            const snapBtn = document.getElementById('snap-file-btn');
            return {
                isActive: recPanel.classList.contains('active'),
                camBtnText: camBtn ? camBtn.textContent.trim() : '',
                hasFlipBtn: !!flipBtn,
                hasSnapBtn: !!snapBtn
            };
        }""")
        print(f"  [Receiver Panel Ready]: {rec_info['isActive']} (Cam: {rec_info['camBtnText']}, Snap: {rec_info['hasSnapBtn']})")
        assert rec_info['isActive'], "Receiver panel not active!"
        assert rec_info['hasSnapBtn'], "Snap/Upload fallback button missing!"
        
        # 5. Test Decryption & Installation of 20 MB Vault Payload
        test_vault_install = await page.evaluate("""async () => {
            const testVault = {
                proto: "GS-FULL-VAULT",
                v: 2,
                pin: "GS-9182",
                stationsCount: 2,
                totalSize: "20.4 MB",
                timestamp: Date.now(),
                stations: [
                    { id: "test-v1", num: 91, freq: "91.1", title: "Beamed Vault Special 1", cat: "PHYSICS", dur: "4m 10s", src: "assets/audio/ep1-can-chemistry-explain-consciousness.mp3" },
                    { id: "test-v2", num: 92, freq: "92.2", title: "Beamed Vault Special 2", cat: "CHEMISTRY", dur: "5m 20s", src: "assets/audio/ep2-the-secrets-of-sadabahar.mp3" }
                ]
            };
            
            // Deliver encrypted chunk
            const b64 = btoa(unescape(encodeURIComponent(JSON.stringify(testVault))));
            const total = 1;
            handleIncomingFountainChunk(`GS2|VAULT20M|1|${total}|${testVault.pin}|${b64}`);
            
            await new Promise(r => setTimeout(r, 200));
            
            const vault = JSON.parse(localStorage.getItem('gyansetu_beamed_vault') || '[]');
            const hasV1 = vault.some(x => x.id === "test-v1");
            const hasV2 = vault.some(x => x.id === "test-v2");
            
            return {
                installedV1: hasV1,
                installedV2: hasV2,
                totalInVault: vault.length
            };
        }""")
        print(f"  [20 MB Vault Decryption & Installation]: {test_vault_install}")
        assert test_vault_install['installedV1'] and test_vault_install['installedV2'], "20 MB Vault stations not installed!"
        
        await browser.close()
        print("\n🎉 ALL CUTTING-EDGE 20 MB VAULT & OPTICAL BEAM TESTS PASSED!")

asyncio.run(test_beamer())
