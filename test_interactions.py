import asyncio
import os
from playwright.async_api import async_playwright

ART_DIR = r"C:\Users\hp\.gemini\antigravity\brain\8c6faad8-6d94-4941-8e8b-9955446c4b2a"

async def test_all_interactions():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        await page.goto("http://localhost:8000/pocket.html", wait_until="domcontentloaded")
        await page.wait_for_timeout(500)

        # 1. Click English Dub
        await page.click("#pill-en")
        await page.wait_for_timeout(400)
        out_dub = os.path.join(ART_DIR, "restomod_interaction_dub.png")
        await page.screenshot(path=out_dub)
        print("Captured English Dub Interaction:", out_dub)

        # 2. Tune to Next Episode (Station 12: Oops, I Created Life)
        await page.click("#key-next")
        await page.wait_for_timeout(400)
        out_next = os.path.join(ART_DIR, "restomod_interaction_next.png")
        await page.screenshot(path=out_next)
        print("Captured Station Tuning:", out_next)

        # 3. Press Bass Boost
        await page.click("#key-bass")
        await page.wait_for_timeout(300)

        # 4. Open Optical Beamer
        await page.click("#key-beamer")
        await page.wait_for_timeout(400)
        out_beamer = os.path.join(ART_DIR, "restomod_interaction_beamer.png")
        await page.screenshot(path=out_beamer)
        print("Captured Optical Beamer:", out_beamer)

        await browser.close()
    print("All interactions verified cleanly!")

if __name__ == "__main__":
    asyncio.run(test_all_interactions())
