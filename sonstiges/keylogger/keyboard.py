# pynputv1.7 by .py to .exe defect, use "pip install pynput==1.6.8"
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
#time.sleep(2)
keyboard.press(Key.alt_l)
keyboard.tap(Key.tab)

#keyboard.press(Key.cmd)
#keyboard.release(Key.cmd)