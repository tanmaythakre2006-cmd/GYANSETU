import asyncio
import os
from playwright.async_api import async_playwright

ART_DIR = r"C:\Users\hp\.gemini\antigravity\brain\8c6faad8-6d94-4941-8e8b-9955446c4b2a"

async def test_all_interactions():
    console_errors = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        page.on("response", lambda res: console_errors.append(f"404 URL: {res.url}") if res.status == 404 else None)
        page.on("console", lambda msg: console_errors.append(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)

        await page.goto("http://localhost:8000/pocket.html", wait_until="domcontentloaded")
        await page.wait_for_timeout(600)

        # 1. Capture Base Appliance State
        out_base = os.path.join(ART_DIR, "restomod_tablet_appliance_v1.png")
        await page.screenshot(path=out_base)
        print("Captured Base Restomod Appliance:", out_base)

        # 2. Press Play (Vinyl glides out and spins, Emerald LED pulses)
        await page.click("#key-play")
        await page.wait_for_timeout(800)
        out_play = os.path.join(ART_DIR, "restomod_interaction_playing_vinyl.png")
        await page.screenshot(path=out_play)
        print("Captured Playing with Vinyl Reveal:", out_play)

        # 3. Click English Dub
        await page.click("#pill-en")
        await page.wait_for_timeout(400)
        out_dub = os.path.join(ART_DIR, "restomod_interaction_dub.png")
        await page.screenshot(path=out_dub)
        print("Captured English Dub Interaction:", out_dub)

        # 4. Tune to Station 2: Oops, I Created Life
        await page.click("#key-next")
        await page.wait_for_timeout(500)
        out_next = os.path.join(ART_DIR, "restomod_interaction_next.png")
        await page.screenshot(path=out_next)
        print("Captured Station Tuning:", out_next)

        # 5. Open Curator's Archival Visual Inspector & Comment Studio
        await page.click("#btn-open-inspect")
        await page.wait_for_timeout(500)
        # Type a test comment
        await page.fill("#comment-text-input", "Fascinating Victorian laboratory art! The lighting captures the era.")
        await page.click("#btn-post-comment")
        await page.wait_for_timeout(400)
        out_archive = os.path.join(ART_DIR, "restomod_interaction_archive_inspector.png")
        await page.screenshot(path=out_archive)
        print("Captured Archival Photo Inspector & Comments:", out_archive)

        # Close archive modal
        await page.click("#btn-close-archive")
        await page.wait_for_timeout(300)

        # 6. Open Optical Beamer
        await page.click("#key-beamer")
        await page.wait_for_timeout(500)
        out_beamer = os.path.join(ART_DIR, "restomod_interaction_beamer.png")
        await page.screenshot(path=out_beamer)
        print("Captured Optical Beamer:", out_beamer)

        await browser.close()

    print("\n--- Console Check ---")
    if console_errors:
        print(f"FAILED: Found {len(console_errors)} errors:")
        for err in console_errors:
            print("  -", err)
    else:
        print("SUCCESS: 0 console errors across all interactions!")

if __name__ == "__main__":
    asyncio.run(test_all_interactions())
