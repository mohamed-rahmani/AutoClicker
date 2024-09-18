import time
import subprocess
import threading
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="p")
STOP_KEY = KeyCode(char="o")

clicking = False

def clicker():
    while True:
        if clicking:
            subprocess.call(['xdotool', 'click', '1'])
        time.sleep(0.001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
    if key == STOP_KEY:
        clicking = False

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()