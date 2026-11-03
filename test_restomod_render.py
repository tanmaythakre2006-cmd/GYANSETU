import asyncio
import os
from playwright.async_api import async_playwright

ART_DIR = r"C:\Users\hp\.gemini\antigravity\brain\8c6faad8-6d94-4941-8e8b-9955446c4b2a"

async def test_restomod():
    console_errors = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        page.on("response", lambda res: console_errors.append(f"404 URL: {res.url}") if res.status == 404 else None)
        page.on("console", lambda msg: console_errors.append(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)

        print("--- Rendering Lenovo TB-8505X (1280x800 Native Landscape) ---")
        await page.goto("http://localhost:8000/pocket.html", wait_until="domcontentloaded")
        await page.wait_for_timeout(600)

        out_path = os.path.join(ART_DIR, "restomod_tablet_appliance_v1.png")
        await page.screenshot(path=out_path)
        print("Captured Screenshot:", out_path)

        await browser.close()

    print("\n--- Console Check ---")
    if console_errors:
        print(f"FAILED: Found {len(console_errors)} errors:")
        for err in console_errors:
            print("  -", err)
    else:
        print("SUCCESS: 0 console errors!")

if __name__ == "__main__":
    asyncio.run(test_restomod())
