
def get_current_tab_url(driver) -> str:
    try:
        url = driver.current_url
        print(f"[DEBUG] Current tab URL: {url}")
        return url
    except Exception as e:
        print(f"[DEBUG] Failed to get current tab URL: {e}")
        return ""

def get_page_source(driver, filename: str = "page_source.html"):
    try:
        source = driver.page_source
        with open(filename, "w", encoding="utf-8") as f:
            f.write(source)
        print(f"[DEBUG] Page source written to: {filename}")
    except Exception as e:
        print(f"[DEBUG] Failed to write page source: {e}")
