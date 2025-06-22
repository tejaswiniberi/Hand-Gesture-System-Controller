# Logic to open apps like Chrome, Notepad etc.import os
import webbrowser

def open_browser():
    print("Opening Chrome...")
    # You can use the path to Chrome executable or a website
    webbrowser.open("https://www.google.com")
