import os
import shutil
import time
from playwright.sync_api import sync_playwright

WORKSPACE = os.path.abspath(".")
WS_URL = WORKSPACE.replace('\\', '/')
ARTIFACT_DIR = r"C:\Users\hp\.gemini\antigravity\brain\8c6faad8-6d94-4941-8e8b-9955446c4b2a"

def run_verification():
    print("[1/3] Starting Playwright test environment for innovations...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # Test 1: Tablet Console (Vector CRT Oscilloscope & Space Weather HUD)
        print("  -> Testing tablet.html at 1280x800 tablet viewport...")
        context_tab = browser.new_context(viewport={'width': 1280, 'height': 800})
        page_tab = context_tab.new_page()
        page_tab.goto(f"file:///{WS_URL}/tablet.html")
        page_tab.wait_for_load_state('networkidle')
        page_tab.wait_for_timeout(500)
        
        # Check space weather pill
        sw = page_tab.locator('#space-weather-indicator')
        print("  -> Space weather pill visible:", sw.is_visible())
        
        # Click CRT toggle
        btn_crt = page_tab.locator('#btn-toggle-crt')
        btn_crt.click()
        page_tab.wait_for_timeout(400)
        
        crt_overlay = page_tab.locator('#crt-scope-overlay')
        print("  -> CRT overlay visible:", crt_overlay.is_visible())
        
        # Switch to orbital mode
        btn_orbital = page_tab.locator('#btn-mode-orbital')
        btn_orbital.click()
        page_tab.wait_for_timeout(300)
        
        # Switch to waterfall mode
        btn_waterfall = page_tab.locator('#btn-mode-waterfall')
        btn_waterfall.click()
        page_tab.wait_for_timeout(300)
        
        # Switch back to Lissajous mode
        btn_lissajous = page_tab.locator('#btn-mode-lissajous')
        btn_lissajous.click()
        page_tab.wait_for_timeout(500)
        
        shot_crt = os.path.join(WORKSPACE, "proof_crt_oscilloscope.png")
        page_tab.screenshot(path=shot_crt)
        print("  -> Captured proof screenshot:", shot_crt)
        context_tab.close()
        
        # Test 2: Pocket Radio (Acoustic Ion Tether FSK Beamer)
        print("  -> Testing pocket.html at 390x844 mobile viewport...")
        context_pocket = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
        page_pocket = context_pocket.new_page()
        page_pocket.goto(f"file:///{WS_URL}/pocket.html")
        page_pocket.wait_for_load_state('networkidle')
        page_pocket.wait_for_timeout(500)
        
        # Open Mesh Beamer modal
        btn_beam = page_pocket.locator('#btn-beam')
        btn_beam.click()
        page_pocket.wait_for_timeout(400)
        
        # Switch to Acoustic Tether tab
        tab_acoustic = page_pocket.locator('#tab-acoustic-btn')
        tab_acoustic.click()
        page_pocket.wait_for_timeout(300)
        
        panel_acoustic = page_pocket.locator('#mesh-acoustic-panel')
        print("  -> Acoustic panel active:", panel_acoustic.is_visible())
        
        # Click Transmit Acoustic Telemetry
        btn_tx = page_pocket.locator('#btn-transmit-acoustic')
        btn_tx.click()
        page_pocket.wait_for_timeout(800)
        
        shot_acoustic = os.path.join(WORKSPACE, "proof_acoustic_tether.png")
        page_pocket.screenshot(path=shot_acoustic)
        print("  -> Captured proof screenshot:", shot_acoustic)
        context_pocket.close()
        browser.close()
        
    # Copy screenshots to artifact directory
    if os.path.exists(shot_crt):
        shutil.copy(shot_crt, os.path.join(ARTIFACT_DIR, "proof_crt_oscilloscope.png"))
        print("  -> Copied proof_crt_oscilloscope.png to brain artifacts")
    if os.path.exists(shot_acoustic):
        shutil.copy(shot_acoustic, os.path.join(ARTIFACT_DIR, "proof_acoustic_tether.png"))
        print("  -> Copied proof_acoustic_tether.png to brain artifacts")
        
    print("[3/3] Verification complete!")

if __name__ == '__main__':
    run_verification()
