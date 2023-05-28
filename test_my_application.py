import re
import os
import time
from playwright.sync_api import sync_playwright


user_dir = '/tmp/playwright'

if not os.path.exists(user_dir):
    os.makedirs(user_dir)


with sync_playwright() as p:



    browser = p.chromium.launch_persistent_context(user_dir ,headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/")

    time.sleep(5)

    print(page.title())

    browser.close()