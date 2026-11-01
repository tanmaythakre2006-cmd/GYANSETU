import asyncio
from playwright.async_api import async_playwright

async def test_host_flow():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # Test 1: Desktop Host Flow
        print("--- Testing Desktop Host Flow ---")
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()
        await page.goto("http://localhost:8000/index.html", wait_until="domcontentloaded")
        await page.wait_for_timeout(500)
        
        # Dismiss listener gate if present
        try:
            btn = page.locator("#btn-gateway-choose-host")
            if await btn.is_visible(timeout=1000):
                await btn.click()
            else:
                await page.locator("#nav-host-login-btn").click()
        except Exception:
            await page.locator("#nav-host-login-btn").click()
            
        await page.wait_for_timeout(300)
        
        # Fill host login
        await page.fill("#gateway-host-email", "simranailani2@gmail.com")
        await page.fill("#gateway-host-password", "22102024")
        await page.click("button.btn-host-signin")
        await page.wait_for_timeout(500)
        
        # Check active host badge
        is_host = await page.evaluate("document.body.classList.contains('is-host')")
        print(f"Desktop Host Authenticated: {is_host}")
        assert is_host, "Host class not present on body"
        
        # Screenshot logged in desktop state
        await page.screenshot(path="test_host_logged_in_desktop.png")
        print("Captured test_host_logged_in_desktop.png")
        await context.close()
        
        # Test 2: Mobile Host Flow
        print("--- Testing Mobile Host Flow ---")
        context_mob = await browser.new_context(viewport={'width': 390, 'height': 844})
        page_mob = await context_mob.new_page()
        await page_mob.goto("http://localhost:8000/index.html", wait_until="domcontentloaded")
        await page_mob.wait_for_timeout(500)
        
        try:
            btn_mob = page_mob.locator("#btn-gateway-choose-host")
            if await btn_mob.is_visible(timeout=1000):
                await btn_mob.click()
            else:
                await page_mob.locator("#mob-nav-host-login-btn").click()
        except Exception:
            await page_mob.locator("#mob-nav-host-login-btn").click()
            
        await page_mob.wait_for_timeout(300)
        await page_mob.fill("#gateway-host-email", "simranailani2@gmail.com")
        await page_mob.fill("#gateway-host-password", "22102024")
        await page_mob.click("button.btn-host-signin")
        await page_mob.wait_for_timeout(500)
        
        is_host_mob = await page_mob.evaluate("document.body.classList.contains('is-host')")
        print(f"Mobile Host Authenticated: {is_host_mob}")
        assert is_host_mob, "Mobile host class not present on body"
        
        await page_mob.screenshot(path="test_host_logged_in_mobile.png")
        print("Captured test_host_logged_in_mobile.png")
        await context_mob.close()
        
        await browser.close()
        print("ALL HOST AUTH TESTS PASSED PERFECTLY!")

if __name__ == "__main__":
    asyncio.run(test_host_flow())
