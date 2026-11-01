import asyncio
from playwright.async_api import async_playwright

async def test_pocket():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # 1. Desktop Pocket
        context_dt = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page_dt = await context_dt.new_page()
        await page_dt.goto("http://localhost:8000/pocket.html", wait_until="domcontentloaded")
        await page_dt.wait_for_timeout(500)
        await page_dt.screenshot(path="test_pocket_desktop.png")
        print("Captured test_pocket_desktop.png")
        await context_dt.close()
        
        # 2. Mobile Pocket
        context_mb = await browser.new_context(viewport={'width': 390, 'height': 844})
        page_mb = await context_mb.new_page()
        await page_mb.goto("http://localhost:8000/pocket.html", wait_until="domcontentloaded")
        await page_mb.wait_for_timeout(500)
        await page_mb.screenshot(path="test_pocket_mobile.png")
        print("Captured test_pocket_mobile.png")
        await context_mb.close()
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_pocket())
