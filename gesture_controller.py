from actions.volume_control import volume_up, volume_down
from actions.screenshot import take_screenshot
from actions.media_control import play_pause
from actions.open_apps import open_browser
from actions.exit import exit_app
from actions.mouse_control import mouse_control

def perform_action(gesture):
    if gesture == "volume_up":
        volume_up()
    elif gesture == "volume_down":
        volume_down()
    elif gesture == "screenshot":
        take_screenshot()
    elif gesture == "play_pause":
        play_pause()
    elif gesture == "open_browser":
        open_browser()
    elif gesture == "mouse_control":
        mouse_control()
    elif gesture == "exit_app":
        exit_app()
    else:
        print(f"Gesture '{gesture}' not assigned.")
