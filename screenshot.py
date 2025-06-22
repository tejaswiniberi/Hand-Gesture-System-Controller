# Logic to take screenshotimport pyautogui
import pyautogui
import time

def take_screenshot():
    print("Taking Screenshot...")
    screenshot = pyautogui.screenshot()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot.save(f"screenshot_{timestamp}.png")
    print("Screenshot saved as screenshot_{}.png".format(timestamp))
