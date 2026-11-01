import asyncio
from playwright.async_api import async_playwright

VIEWPORTS = [
    ("1920x1080_desktop_wide", 1920, 1080),
    ("1440x900_laptop", 1440, 900),
    ("1280x800_laptop_compact", 1280, 800),
    ("1024x768_tablet_landscape", 1024, 768),
    ("820x1180_tablet_portrait", 820, 1180),
    ("430x932_mobile_large", 430, 932),
    ("390x844_mobile_medium", 390, 844),
    ("360x800_mobile_small", 360, 800)
]

async def capture_all(suffix="before"):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, w, h in VIEWPORTS:
            context = await browser.new_context(viewport={'width': w, 'height': h})
            page = await context.new_page()
            await page.goto("http://localhost:8000/index.html", wait_until="networkidle")
            
            # Dismiss gateway modal if present
            try:
                listener_btn = page.locator("#btn-gateway-choose-listener")
                if await listener_btn.is_visible(timeout=1000):
                    await listener_btn.click()
                    await page.wait_for_timeout(300)
            except Exception:
                pass
            
            # Screenshot the top header area
            await page.screenshot(path=f"test_vp_{name}_{suffix}.png")
            print(f"Captured test_vp_{name}_{suffix}.png")
            await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_all("before"))
