import asyncio
import os
from playwright.async_api import async_playwright

ART_DIR = r"C:\Users\hp\.gemini\antigravity\brain\8c6faad8-6d94-4941-8e8b-9955446c4b2a"

async def test_console():
    console_errors = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        page.on("response", lambda res: console_errors.append(f"404 URL: {res.url}") if res.status == 404 else None)

        print("--- Testing Lenovo TB-8505X (1280x800 Native Landscape) ---")
        await page.goto("http://localhost:8000/pocket.html", wait_until="networkidle")
        await page.wait_for_timeout(600)

        # 1. Capture 1978 Vintage Teakwood Appliance
        path_vintage = os.path.join(ART_DIR, "flagship_1978_vintage_appliance.png")
        await page.screenshot(path=path_vintage)
        print("Captured 1978 Vintage Appliance:", path_vintage)

        # 2. Switch to Carvaan Neo All-Screen Cockpit
        await page.click("#btn-theme-neo")
        await page.wait_for_timeout(600)
        path_neo = os.path.join(ART_DIR, "flagship_carvaan_neo_cockpit.png")
        await page.screenshot(path=path_neo)
        print("Captured Carvaan Neo Cockpit:", path_neo)

        # 3. Open Optical Beamer
        await page.click("#btn-open-beamer")
        await page.wait_for_timeout(500)
        path_beamer = os.path.join(ART_DIR, "flagship_optical_beamer_mesh.png")
        await page.screenshot(path=path_beamer)
        print("Captured Optical Beamer Modal:", path_beamer)

        await browser.close()

    print("\n--- Console Errors Check ---")
    if console_errors:
        print(f"FAILED: Found {len(console_errors)} errors:")
        for err in console_errors:
            print("  -", err)
    else:
        print("PERFECT: 0 console errors!")

if __name__ == "__main__":
    asyncio.run(test_console())
