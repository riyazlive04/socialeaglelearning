import pyautogui
import time

# Function to safely click a point
def safe_click(x, y, delay=0.5):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
    time.sleep(delay)

# STEP 1 - Open Chrome (click Chrome icon on taskbar)
# Replace these with YOUR Chrome icon coordinates
chrome_icon_x = 100
chrome_icon_y = 1050

safe_click(chrome_icon_x, chrome_icon_y, delay=2)

# STEP 2 - Click address bar
# Usually, pressing Ctrl+L focuses the address bar
pyautogui.hotkey('ctrl', 'l')
time.sleep(1)

# STEP 3 - Type search query
search_query = "India vs England score"
pyautogui.typewrite(search_query, interval=0.1)
pyautogui.press('enter')
time.sleep(5)  # Wait for Google to load

# STEP 4 - Locate Cricbuzz link on screen

# Option 1 — Image recognition
# Take a screenshot of the Cricbuzz link text (e.g. "Cricbuzz: Live Cricket Score ...")
# Save it as cricbuzz.png in the same folder

try:
    # locateOnScreen returns None if not found
    cricbuzz_location = pyautogui.locateCenterOnScreen('cricbuzz.png', confidence=0.7)
    if cricbuzz_location:
        safe_click(cricbuzz_location.x, cricbuzz_location.y, delay=3)
        print("Clicked Cricbuzz link.")
    else:
        print("Cricbuzz link not found on screen. Try adjusting confidence or capturing a better screenshot.")
except Exception as e:
    print(f"Error locating Cricbuzz link: {e}")