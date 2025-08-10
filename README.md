# Web Browser API

Human-like browser automation helpers built on undetected-chromedriver, Selenium, and PyAutoGUI.

Features:
- Launch undetected Chrome (undetected-chromedriver) with a dedicated user profile.
- Human-like mouse movement and typing via PyAutoGUI.
- Simple helpers to click elements, hold, switch tabs, focus the window, and OCR the browser area via Tesseract.

Python 3.10+ is required. On Linux, some features require xdotool (for focusing windows) and Tesseract OCR for `pytesseract`.

## Quick Start

```python
from web_browser_api import get_driver, move_mouse, type_like_human, click_element

# Start undetected Chrome
driver = get_driver()

# ... your Selenium code to open a page and find an element
# element = driver.find_element(...)

# Move the mouse and click using human-like movement
# click_element(driver, element)

# Type text into the active field like a human
# type_like_human("Hello world!\n")
```

## API Overview

Top-level exports from `web_browser_api`:
- get_driver, close_driver, nuke_chrome_profile
- switch_to_latest_tab, focus_chrome_window
- generate_password, generate_bot_identity
- type_like_human, human_pause, move_mouse
- get_element_center, click_element, click_and_hold_element, click_and_hold_pos
- extract_text_from_chrome_window

## License

See LICENSE file.
