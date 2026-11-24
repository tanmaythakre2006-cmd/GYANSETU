import os
from playwright.sync_api import sync_playwright

WORKSPACE = os.path.abspath(".")
WS_URL = WORKSPACE.replace('\\', '/')
ARTIFACT_DIR = r"C:\Users\hp\.gemini\antigravity\brain\8c6faad8-6d94-4941-8e8b-9955446c4b2a"

def test_tablet():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Standard Tablet Viewport (iPad / Android Tablet: 1024x768)
        context = browser.new_context(viewport={"width": 1024, "height": 768})
        page = context.new_page()

        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))

        page.goto(f"file:///{WS_URL}/tablet.html")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(500)

        # Verify #btn-toggle-crt is gone
        crt_btn = page.locator("#btn-toggle-crt")
        assert not crt_btn.is_visible(), "CRT toggle button should not exist!"

        # Verify crt overlay is gone
        crt_overlay = page.locator("#crt-scope-overlay")
        assert crt_overlay.count() == 0, "CRT overlay DOM should be removed!"

        # Verify LCD screen and hero info are clean and visible
        smart_lcd = page.locator("#smart-lcd-screen")
        assert smart_lcd.is_visible(), "Smart LCD screen should be visible!"

        track_title = page.locator("#lcd-title")
        assert track_title.is_visible(), "Track title should be visible!"

        # Capture proof screenshot
        shot_path = os.path.join(ARTIFACT_DIR, "proof_tablet_clean_restored.png")
        page.screenshot(path=shot_path)
        print(f"Verified clean tablet console without CRT oscilloscope! Screenshot: {shot_path}")
        print(f"Errors encountered: {errors}")
        assert len(errors) == 0, f"Page errors: {errors}"

        browser.close()

if __name__ == "__main__":
    test_tablet()
