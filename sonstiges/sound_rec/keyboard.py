import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
time.sleep(2)
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)