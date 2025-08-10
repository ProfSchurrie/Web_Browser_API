import random
import string
import time
import pyautogui
from faker import Faker
import undetected_chromedriver as uc
from .driver import get_driver
from .move_mouse import _move_mouse_poly
import subprocess
import pytesseract

fake = Faker()

def switch_to_latest_tab(driver):
    try:
        driver.switch_to.window(driver.window_handles[-1])
        print("Switched to the latest tab.")
    except Exception as e:
        print(f"Error switching tabs: {e}")


def focus_chrome_window():
    # This will search for a Chrome window and activate it
    subprocess.run(["xdotool", "search", "--onlyvisible", "--class", "chrome", "windowactivate"])
    time.sleep(0.2)  # short delay to ensure focus


def generate_password():
    lowers = random.choices(string.ascii_lowercase, k=5)
    uppers = random.choices(string.ascii_uppercase, k=5)
    digits = random.choices(string.digits, k=5)
    symbols = random.choices("!@#$%&*", k=2)

    all_chars = lowers + uppers + digits + symbols
    random.shuffle(all_chars)
    return ''.join(all_chars)


def generate_bot_identity():
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = f"{first_name.lower()}.{last_name.lower()}" + ''.join(random.choices(string.digits, k=8))
    password = generate_password()
    return {"first_name": first_name, "last_name": last_name, "username": username, "password": password}


def type_like_human(text):
    """Type text into the currently focused element as real keypresses.
    - Sends characters using OS-level key events via pyautogui.
    - Adds small random delays to mimic human typing.
    """
    for char in text:
        if char == "\n":
            pyautogui.press("enter")
        elif char == "\t":
            pyautogui.press("tab")
        else:
            # write handles upper/lower case and special characters
            pyautogui.write(char)
        time.sleep(random.uniform(0.05, 0.15))

def human_pause(min_sec=0.3, max_sec=1.2):
    time.sleep(random.uniform(min_sec, max_sec))

def move_mouse(driver:uc.Chrome, x, y, total_dur=1.5, jitter=8, titlebar_h=108):
    _move_mouse_poly(driver, x, y, total_dur=total_dur, titlebar_h=titlebar_h)


def get_element_center(element):
    # Get element's position and size from Selenium
    location = element.location
    size = element.size

    # Middle point in browser coordinate space
    center_x = location['x'] + size['width'] / 2
    center_y = location['y'] + size['height'] / 2

    return center_x, center_y

def click_element(driver, element):
    (posx, posy) = get_element_center(element)
    move_mouse(driver, posx, posy)
    pyautogui.click()

def click_and_hold_element(driver, element, seconds=2):
    posx, posy = get_element_center(element)
    move_mouse(driver, posx, posy)
    pyautogui.mouseDown()         # press and hold
    time.sleep(seconds)           # hold for s seconds
    pyautogui.mouseUp()           # release

def click_and_hold_pos(driver, pos, seconds=2, break_func=None):
    move_mouse(driver, pos[0], pos[1])
    pyautogui.mouseDown()         # press and hold
    if break_func is not None:
        for i in range(seconds*3):
            if not break_func():
                break
            time.sleep(1/3)
    else:
        time.sleep(seconds)

    pyautogui.mouseUp()           # release


def extract_text_from_chrome_window(driver):
    # Get browser window position/size
    rect = driver.get_window_rect()
    screenshot = pyautogui.screenshot(region=(rect['x'], rect['y'], rect['width'], rect['height']))

    text = pytesseract.image_to_string(screenshot)
    return text


if __name__ == "__main__":
    driver = get_driver()
    move_mouse(driver, 0,0, total_dur=2)
    print(pyautogui.position())
