import asyncio
from playwright.async_api import async_playwright

async def run_visual_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # TEST 1: Lenovo TB-8505X (1280 x 800 Landscape) - Theme 1: 1978 Vintage
        print("--- Testing Lenovo TB-8505X (1280x800) - 1978 Vintage Teak ---")
        context_lenovo_1978 = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context_lenovo_1978.new_page()
        await page.goto("http://localhost:8000/pocket.html", wait_until="domcontentloaded")
        await page.wait_for_timeout(600)
        
        # Verify 1978 theme is active
        theme = await page.evaluate("document.getElementById('radio-chassis').getAttribute('data-theme')")
        print(f"Current theme: {theme}")
        
        # Take screenshot of 1978 Vintage Cabinet on Lenovo Tab
        await page.screenshot(path="screenshot_lenovo_1280x800_vintage_1978.png")
        print("Captured screenshot_lenovo_1280x800_vintage_1978.png")
        
        # Check overflow
        scroll_w = await page.evaluate("document.documentElement.scrollWidth")
        scroll_h = await page.evaluate("document.documentElement.scrollHeight")
        print(f"Lenovo 1978: ScrollWidth={scroll_w}, ScrollHeight={scroll_h}")
        await context_lenovo_1978.close()

        # TEST 2: Lenovo TB-8505X (1280 x 800 Landscape) - Theme 2: Carvaan Neo-Edition
        print("--- Testing Lenovo TB-8505X (1280x800) - Carvaan Neo ---")
        context_lenovo_carvaan = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page2 = await context_lenovo_carvaan.new_page()
        await page2.goto("http://localhost:8000/pocket.html", wait_until="domcontentloaded")
        await page2.wait_for_timeout(400)
        
        # Click the master theme switch to toggle to Carvaan Neo
        await page2.click("#master-theme-switch")
        await page2.wait_for_timeout(400)
        
        theme2 = await page2.evaluate("document.getElementById('radio-chassis').getAttribute('data-theme')")
        print(f"Current theme after toggle: {theme2}")
        assert theme2 == 'carvaan-neo', f"Expected carvaan-neo, got {theme2}"
        
        # Take screenshot of Carvaan Neo on Lenovo Tab
        await page2.screenshot(path="screenshot_lenovo_1280x800_carvaan_neo.png")
        print("Captured screenshot_lenovo_1280x800_carvaan_neo.png")
        await context_lenovo_carvaan.close()

        # TEST 3: Mobile Portrait (390 x 844) - Verify Mobile Still Functions
        print("--- Testing Mobile Portrait (390x844) ---")
        context_mob = await browser.new_context(viewport={'width': 390, 'height': 844})
        page3 = await context_mob.new_page()
        await page3.goto("http://localhost:8000/pocket.html", wait_until="domcontentloaded")
        await page3.wait_for_timeout(400)
        await page3.screenshot(path="screenshot_mobile_pocket_portrait.png")
        print("Captured screenshot_mobile_pocket_portrait.png")
        await context_mob.close()

        await browser.close()
        print("ALL VISUAL TESTS COMPLETED!")

if __name__ == "__main__":
    asyncio.run(run_visual_tests())
