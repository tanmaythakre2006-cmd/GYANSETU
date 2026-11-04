# -*- coding: utf-8 -*-
"""
Iterative Console Generator & Test Harness
Tracks the 10-cycle refinement loop requested by the user.
"""

import os
import asyncio
from playwright.async_api import async_playwright

ART_DIR = r"C:\Users\hp\.gemini\antigravity\brain\8c6faad8-6d94-4941-8e8b-9955446c4b2a"

def build_iteration_html(iteration_num=1):
    with open('build_clean_flagship_radio.py', 'r', encoding='utf-8') as f:
        content = f.read()
    with open('pocket.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated pocket.html for Iteration {iteration_num}")

async def capture_iteration_screenshot(iteration_num=1):
    out_file = os.path.join(ART_DIR, f"iteration_{iteration_num}_screenshot.png")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        console_errors = []
        page.on("response", lambda res: console_errors.append(f"404 URL: {res.url}") if res.status == 404 else None)
        page.on("console", lambda msg: console_errors.append(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)

        await page.goto("http://localhost:8000/pocket.html", wait_until="domcontentloaded")
        await page.wait_for_timeout(600)

        await page.screenshot(path=out_file)
        print(f"Captured: {out_file}")
        await browser.close()

    if console_errors:
        print(f"Iteration {iteration_num} ERRORS:", console_errors)
    else:
        print(f"Iteration {iteration_num} SUCCESS: 0 console errors!")

if __name__ == '__main__':
    build_iteration_html(1)
    asyncio.run(capture_iteration_screenshot(1))
