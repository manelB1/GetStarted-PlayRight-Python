import re
import os
import time
from playwright.sync_api import sync_playwright
from playwright_recaptcha import recaptchav2


user_dir = '/tmp/playwright'

if not os.path.exists(user_dir):
    os.makedirs(user_dir)


with sync_playwright() as p:

    browser = p.chromium.launch_persistent_context(user_dir, headless=False)
    page = browser.new_page()

    page.goto(
        "https://www.google.com/recaptcha/api2/demo", wait_until="networkidle"
    )

    time.sleep(5)
    
    
    with recaptchav2.SyncSolver(page) as solver:
        token = solver.solve_recaptcha()
        print(token)

        browser.close()