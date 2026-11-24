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

def test_full_platform():
    print("=" * 70)
    print("STARTING TEST SUITE: CURIOSITY MAILBAG, THOUGHT DECK & CLASSROOM BRIEF")
    print("=" * 70)

    passed_devices = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for dev in DEVICES:
            dev_name = dev["name"]
            w, h = dev["width"], dev["height"]
            print(f"\n[DEVICE AUDIT] {dev_name} ({w}x{h} px)")

            context = browser.new_context(
                viewport={"width": w, "height": h},
                device_scale_factor=dev["dpr"],
                is_mobile=True,
                has_touch=True
            )
            page = context.new_page()

            page_errors = []
            page.on("pageerror", lambda err: page_errors.append(str(err)))

            page.goto(f"file:///{WS_URL}/index.html")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(400)

            # 1. Gateway Dismissal if present
            gateway_btn = page.locator("#btn-gateway-choose-listener")
            if gateway_btn.is_visible():
                gateway_btn.click()
                page.wait_for_timeout(300)

            # 2. Check Horizontal Scroll
            inner_w = page.evaluate("() => window.innerWidth")
            scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
            assert scroll_w <= inner_w, f"Horizontal overflow on {dev_name}: {scroll_w} > {inner_w}"
            print(f"  [{dev_name}] Zero Horizontal Overflow Verified: scrollWidth={scroll_w} <= innerWidth={inner_w}")

            # 3. Test Curiosity Mailbag ("Ask Simran")
            bnav_studio = page.locator("#bnav-studio")
            assert bnav_studio.is_visible(), f"Bottom Nav 'Ask Simran' button not visible on {dev_name}"
            bnav_studio.click()
            page.wait_for_timeout(400)

            mailbag_modal = page.locator("#live-studio-modal")
            assert mailbag_modal.is_visible(), f"Mailbag modal did not open on {dev_name}"
            print(f"  [{dev_name}] Curiosity Mailbag Modal opened successfully!")

            # Take screenshot of Mailbag
            shot_mb = os.path.join(ARTIFACT_DIR, f"proof_{dev_name}_mailbag.png")
            page.screenshot(path=shot_mb)

            # Fill in question form
            name_input = page.locator("#ask-name")
            loc_input = page.locator("#ask-location")
            q_input = page.locator("#ask-question-text")
            submit_btn = page.locator("#btn-submit-mailbag-form")

            name_input.fill("Aarav Mehta")
            loc_input.fill("DPS Bangalore")
            q_input.fill("How do solid-state electrolytes prevent lithium dendrites from short-circuiting battery cells?")
            submit_btn.click()
            page.wait_for_timeout(400)

            receipt_box = page.locator("#mailbag-receipt-box")
            assert receipt_box.is_visible(), f"Mailbag receipt not shown on {dev_name}"
            receipt_id = page.locator("#mailbag-receipt-id-tag").inner_text()
            assert "GS-ASK-" in receipt_id, f"Invalid receipt ID: {receipt_id}"
            print(f"  [{dev_name}] Mailbag Form submitted successfully! Receipt: {receipt_id}")

            # Close Mailbag modal
            page.locator("#close-live-studio-btn").click()
            page.wait_for_timeout(300)

            # 4. Test Multimodal Visual Thought Deck
            hero_thought_btn = page.locator("#btn-hero-thought-deck")
            assert hero_thought_btn.is_visible(), f"Hero Thought Deck button not visible on {dev_name}"
            hero_thought_btn.click()
            page.wait_for_timeout(400)

            thought_modal = page.locator("#thought-deck-modal")
            assert thought_modal.is_visible(), f"Thought Deck modal not visible on {dev_name}"
            diagram_svg = page.locator("#thought-diagram-canvas-wrap svg")
            assert diagram_svg.is_visible(), f"Thought Deck SVG diagram not visible on {dev_name}"
            thought_cards = page.locator(".thought-card")
            assert thought_cards.count() >= 3, f"Expected 3 thought cards, found {thought_cards.count()}"
            print(f"  [{dev_name}] Multimodal Visual Thought Deck verified with SVG and {thought_cards.count()} concept cards!")

            # Screenshot Thought Deck
            shot_td = os.path.join(ARTIFACT_DIR, f"proof_{dev_name}_thought_deck.png")
            page.screenshot(path=shot_td)

            # Close Thought Deck
            page.locator("#close-thought-deck-btn").click()
            page.wait_for_timeout(300)

            # 5. Test 1-Page Printable Classroom Inquiry Brief
            hero_brief_btn = page.locator("#btn-hero-classroom-brief")
            assert hero_brief_btn.is_visible(), f"Hero Classroom Brief button not visible on {dev_name}"
            hero_brief_btn.click()
            page.wait_for_timeout(400)

            brief_modal = page.locator("#classroom-brief-modal")
            assert brief_modal.is_visible(), f"Classroom Brief modal not visible on {dev_name}"
            
            big_idea = page.locator("#brief-sheet-big-idea").inner_text()
            assert len(big_idea) > 10, "Big Idea text missing in Classroom Brief"

            sparks = page.locator("#brief-sheet-sparks li")
            assert sparks.count() == 3, f"Expected 3 teacher debate sparks, found {sparks.count()}"

            vocab_items = page.locator(".sheet-vocab-item")
            assert vocab_items.count() >= 3, f"Expected at least 3 vocab terms, found {vocab_items.count()}"

            exp_text = page.locator("#brief-sheet-experiment").inner_text()
            assert len(exp_text) > 10, "Everyday observation experiment text missing"

            print_btn = page.locator("#btn-print-brief")
            assert print_btn.is_visible(), f"Print button not visible on {dev_name}"

            print(f"  [{dev_name}] Classroom Brief verified with Big Idea, 3 Debate Sparks, 3 Vocab Definitions & Frugal Experiment!")

            # Screenshot Classroom Brief
            shot_cb = os.path.join(ARTIFACT_DIR, f"proof_{dev_name}_classroom_brief.png")
            page.screenshot(path=shot_cb)

            # Close Classroom Brief
            page.locator("#close-classroom-brief-btn").click()
            page.wait_for_timeout(300)

            # 6. Strict constraint check: NO quizzes or checkpoints
            quiz_elements = page.locator("[class*='quiz'], [id*='quiz'], [class*='checkpoint'], [id*='checkpoint']").all()
            assert len(quiz_elements) == 0, f"Found unexpected quiz/checkpoint elements: {quiz_elements}"
            print(f"  [{dev_name}] Strict Constraint Verified: Zero quizzes/checkpoints in DOM.")

            # Check for console page errors
            assert len(page_errors) == 0, f"Page errors encountered on {dev_name}: {page_errors}"

            context.close()
            passed_devices.append(dev_name)

        browser.close()

    print("\n" + "=" * 70)
    print(f"ALL TESTS PASSED 100% ACROSS {len(passed_devices)} ANDROID DEVICES!")
    print("=" * 70)

if __name__ == "__main__":
    test_full_platform()
