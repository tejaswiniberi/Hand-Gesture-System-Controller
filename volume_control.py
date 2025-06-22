import pyautogui
import time

def volume_up():
    print("Volume Up")
    for _ in range(5):
        pyautogui.press("volumeup")
        time.sleep(0.1)

def volume_down():
    print("Volume Down")
    for _ in range(5):
        pyautogui.press("volumedown")
        time.sleep(0.1)
