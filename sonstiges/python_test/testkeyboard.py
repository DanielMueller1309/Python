from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
time.sleep(3)
keyboard.press(Key.alt_l)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.release(Key.alt_l)
time.sleep(3)
keyboard.type('hallowelt')
#keyboard.tap(Key.alt_l)
