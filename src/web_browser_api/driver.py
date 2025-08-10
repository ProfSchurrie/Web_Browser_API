import os
import shutil
import undetected_chromedriver as uc

PROFILE_PATH = os.path.expanduser("~/selenium/chrome-profile")
driver: uc.Chrome | None = None

def nuke_chrome_profile():
    """
    Completely remove the Chrome user profile used by Selenium.
    """
    if os.path.exists(PROFILE_PATH):
        shutil.rmtree(PROFILE_PATH)
        print(f"Deleted Chrome profile at {PROFILE_PATH}")
    else:
        print(f"No Chrome profile found at {PROFILE_PATH}")

def get_driver(session_id=None):
    global driver
    if driver is None:
        print("Launching undetected Chrome browser...")
        nuke_chrome_profile()

        options = uc.ChromeOptions()
        options.user_data_dir = PROFILE_PATH
        options.add_argument("--no-first-run")
        options.add_argument("--no-service-autorun")
        options.add_argument("--password-store=basic")
        options.add_argument("--lang=en-US")
        options.add_argument("--window-size=1280,720")
        options.add_argument("--start-maximized")

        driver = uc.Chrome(options=options, headless=False)
        print("Undetected Chrome driver launched successfully.")
    return driver

def close_driver():
    global driver
    if driver is not None:
        driver.quit()
        driver = None
    else:
        print("No Chrome driver launched successfully.")