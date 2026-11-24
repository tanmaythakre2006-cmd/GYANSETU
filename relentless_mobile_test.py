import os
import shutil
import time
from playwright.sync_api import sync_playwright

WORKSPACE = os.path.abspath(".")
WS_URL = WORKSPACE.replace('\\', '/')
ARTIFACT_DIR = r"C:\Users\hp\.gemini\antigravity\brain\8c6faad8-6d94-4941-8e8b-9955446c4b2a"
os.makedirs(ARTIFACT_DIR, exist_ok=True)

DEVICES = [
    {"name": "Samsung_Galaxy_S23", "width": 360, "height": 800, "dpr": 3.0},
    {"name": "Universal_Android_HD", "width": 390, "height": 844, "dpr": 3.0},
    {"name": "Google_Pixel_8", "width": 412, "height": 915, "dpr": 2.6},
    {"name": "Compact_Budget_Android", "width": 320, "height": 650, "dpr": 2.0}
]

def run_relentless_tests():
    print("=" * 70)
    print("STARTING RELENTLESS MULTI-DEVICE ANDROID PORTRAIT TESTING SUITE")
    print("=" * 70)
    
    audit_results = {}
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for dev in DEVICES:
            dev_name = dev["name"]
            w, h = dev["width"], dev["height"]
            print(f"\n[DEVICE AUDIT] {dev_name} ({w}x{h} px, DPR={dev['dpr']})")
            
            context = browser.new_context(
                viewport={"width": w, "height": h},
                device_scale_factor=dev["dpr"],
                is_mobile=True,
                has_touch=True
            )
            page = context.new_page()
            
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            
            # Load page
            page.goto(f"file:///{WS_URL}/index.html")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(400)
            
            # 1. Gateway Onboarding Test (Bottom Sheet)
            gateway_btn = page.locator("#btn-gateway-choose-listener")
            if gateway_btn.is_visible():
                print(f"  [{dev_name}] Gateway Modal visible as Bottom Sheet. Clicking 'I am a Listener'...")
                shot_gw = os.path.join(WORKSPACE, f"proof_{dev_name}_1_gateway.png")
                page.screenshot(path=shot_gw)
                gateway_btn.click()
                page.wait_for_timeout(400)
            
            # 2. Horizontal Overflow Check
            inner_w = page.evaluate("() => window.innerWidth")
            scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
            has_overflow = scroll_w > inner_w
            print(f"  [{dev_name}] Viewport: innerWidth={inner_w}, scrollWidth={scroll_w}, has_overflow={has_overflow}")
            assert not has_overflow, f"Horizontal overflow detected on {dev_name}! {scroll_w} > {inner_w}"
            
            # 3. Android Top App Bar Check
            top_bar = page.locator(".nav-mobile-layout")
            assert top_bar.is_visible(), f"Android Top App Bar not visible on {dev_name}!"
            print(f"  [{dev_name}] Top App Bar verified: {top_bar.is_visible()}")
            
            # 4. Android Bottom Navigation Bar Check
            bottom_nav = page.locator("#android-bottom-nav")
            assert bottom_nav.is_visible(), f"Android Bottom Navigation Bar not visible on {dev_name}!"
            print(f"  [{dev_name}] Bottom Navigation Bar verified: {bottom_nav.is_visible()}")
            
            # 5. Above-the-fold Hero Screen
            onair_capsule = page.locator(".mob-onair-capsule")
            assert onair_capsule.is_visible(), f"On-Air live capsule not visible on {dev_name}!"
            headline = page.locator(".hero-headline")
            assert headline.is_visible(), f"Hero headline not visible on {dev_name}!"
            retro_duo = page.locator(".hero-retro-duo")
            assert retro_duo.is_visible(), f"Dual Retro Radio selector buttons not visible on {dev_name}!"
            
            shot_hero = os.path.join(WORKSPACE, f"proof_{dev_name}_2_hero.png")
            page.screenshot(path=shot_hero)
            print(f"  [{dev_name}] Captured above-the-fold hero screenshot.")
            
            # 6. Audio Player Dock & Navigation Interaction
            btn_play = page.locator("#player-play-btn")
            assert btn_play.is_visible(), f"Play button in audio dock not visible on {dev_name}!"
            btn_play.click()
            page.wait_for_timeout(300)
            
            # Test Speed Toggle
            btn_speed = page.locator("#speed-toggle-btn")
            if btn_speed.is_visible():
                btn_speed.click()
                page.wait_for_timeout(200)
            
            # Test Navigation Bar Tab Jump (Episodes)
            tab_episodes = page.locator("#bnav-episodes")
            tab_episodes.click()
            page.wait_for_timeout(600)
            
            shot_episodes = os.path.join(WORKSPACE, f"proof_{dev_name}_3_episodes.png")
            page.screenshot(path=shot_episodes)
            print(f"  [{dev_name}] Captured episodes view after bottom-nav click.")
            
            # 7. Test Episode Notes Bottom Sheet
            notes_btn = page.locator(".btn-card-notes").first
            if notes_btn.is_visible():
                notes_btn.scroll_into_view_if_needed()
                notes_btn.click()
                page.wait_for_timeout(400)
                
                notes_modal = page.locator("#notes-modal")
                assert notes_modal.is_visible(), f"Notes modal did not open on {dev_name}!"
                shot_notes = os.path.join(WORKSPACE, f"proof_{dev_name}_4_notes_bottomsheet.png")
                page.screenshot(path=shot_notes)
                print(f"  [{dev_name}] Captured Notes Bottom Sheet screenshot.")
                
                close_notes = page.locator("#close-modal-btn")
                close_notes.click(force=True)
                page.wait_for_timeout(300)
                
            # 8. Scroll to bottom (Vault / Downloads)
            tab_vault = page.locator("#bnav-vault")
            tab_vault.click()
            page.wait_for_timeout(600)
            
            shot_vault = os.path.join(WORKSPACE, f"proof_{dev_name}_5_vault.png")
            page.screenshot(path=shot_vault)
            print(f"  [{dev_name}] Captured Vault / APK downloads view.")
            
            # Ensure no JS runtime errors occurred
            assert len(errors) == 0, f"Errors caught on {dev_name}: {errors}"
            
            audit_results[dev_name] = {
                "status": "PASSED",
                "innerWidth": inner_w,
                "scrollWidth": scroll_w,
                "errors": len(errors)
            }
            
            # Copy all screenshots to artifact dir
            for shot in [shot_gw, shot_hero, shot_episodes, shot_notes, shot_vault]:
                if os.path.exists(shot):
                    shutil.copy(shot, os.path.join(ARTIFACT_DIR, os.path.basename(shot)))
            
            context.close()
            
        browser.close()
        
    print("\n" + "=" * 70)
    print("ALL 4 ANDROID PORTRAIT RESOLUTIONS PASSED WITH ZERO ERRORS!")
    print("=" * 70)
    for dev_name, res in audit_results.items():
        print(f"  ✓ {dev_name}: {res['status']} (W={res['innerWidth']}px, ScrollW={res['scrollWidth']}px)")

if __name__ == "__main__":
    run_relentless_tests()
