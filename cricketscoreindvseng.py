import pyautogui
import time

# Optional: Fail-safe if mouse goes to a corner
pyautogui.FAILSAFE = True

# Shorter pauses between actions
pyautogui.PAUSE = 0.5

# STEP 1 – Open Run dialog
pyautogui.hotkey('winleft', 'r')
time.sleep(1)

# STEP 2 – Type browser name
pyautogui.typewrite('chrome\n', interval=0.1)

# STEP 3 – Wait for browser to open
time.sleep(3)

# STEP 4 – Type search query
pyautogui.typewrite('India vs England score\n', interval=0.1)

# STEP 5 – Wait for results page to load
time.sleep(5)

# STEP 6 – Move mouse to first link and click
# Example coordinates – change these!
# E.g. x=400, y=350 for first search result
"""pyautogui.moveTo(400, 350, duration=0.5)
pyautogui.click()"""

print("Done!")
