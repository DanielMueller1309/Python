# pynputv1.7 by .py to .exe defect, use "pip install pynput==1.6.8"
import time
import os
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()
# tmp zu python holen
tmp = os.environ.get('tmp')

#default sleep time
dst = 1

# newpath festlegen
newpath = tmp + r'\UpdateTool'
#testprozedur
def proz(z):
    file = open(newpath + r'\keyboardtest.txt', 'a+')
    file.write(str(z) + "\n")
    file.close()

# homepath zu python holen
home = os.environ.get('homepath')

os.system(r'cmd /c "C:\Users\danie\Git\Python\sonstiges\sound_rec\displaydown.exe monitor off"')
os.system(r'cmd /c ""')
# Ausführung öffnen
keyboard.press(Key.cmd)
keyboard.press('r')
keyboard.release('r')
keyboard.release(Key.cmd)

time.sleep(dst)

keyboard.type('taskschd.msc')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
os.system(r'cmd /c "C:\Users\danie\Git\Python\sonstiges\sound_rec\displaydown.exe monitor off"')