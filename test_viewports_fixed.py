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

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, w, h in VIEWPORTS:
            context = await browser.new_context(viewport={'width': w, 'height': h})
            page = await context.new_page()
            
            # Seed session storage before load to act as listener
            await page.add_init_script("""
                sessionStorage.setItem('gyansetu_user_role', 'listener');
            """)
            
            await page.goto("http://localhost:8000/index.html", wait_until="domcontentloaded")
            await page.wait_for_timeout(800)
            
            # Ensure toast is hidden for clean screenshot of the navigation
            await page.evaluate("""
                const toast = document.getElementById('network-toast');
                if (toast) toast.classList.remove('show');
            """)
            
            # Take screenshot of the top hero & navigation area
            out_file = f"fixed_vp_{name}.png"
            await page.screenshot(path=out_file)
            print(f"Captured: {out_file}")
            
            # Verify no horizontal scroll on body
            scroll_width = await page.evaluate("document.documentElement.scrollWidth")
            client_width = await page.evaluate("document.documentElement.clientWidth")
            print(f"[{name}] Viewport width={w}, ClientWidth={client_width}, ScrollWidth={scroll_width}")
            if scroll_width > client_width + 1:
                print(f"  WARNING: Horizontal overflow detected on {name} (scrollWidth: {scroll_width} > clientWidth: {client_width})")
            else:
                print(f"  PERFECT: Zero horizontal page overflow on {name}")
                
            await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_tests())
