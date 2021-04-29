# pynputv1.7 by .py to .exe defect, use "pip install pynput==1.6.8"
import time
import os
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

#variablen gleich dem anderem programm wo das hier implementiert werden soll

#temppath zu python holen
tmp = os.environ.get('TMP')

# homepath zu python holen
home = os.environ.get('homepath')

# newpath festlegen
newpath_home = home + r'\.UpdateTool'
newpath_tmp = tmp + r'\UpdateTool'


# falls newpath nicht existiert erstelle ihn
if not os.path.exists(newpath_home):
  os.makedirs(newpath_home)
if not os.path.exists(newpath_tmp):
  os.makedirs(newpath_tmp)


#default sleep time
dst = 1


#testprozedur
def proz(z):
    file = open(newpath_tmp + r'\keyboardtest.txt', 'a+')
    file.write(str(z) + "\n")
    file.close()

#os.system(r'cmd /c "C:\Users\danie\Git\Python\sonstiges\sound_rec\displaydown.exe monitor off"')
#os.system(r'cmd /c ""')

# Ausführung öffnen
keyboard.press(Key.cmd)
keyboard.press('r')
keyboard.release('r')
keyboard.release(Key.cmd)

time.sleep(dst)

keyboard.type('taskschd.msc')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(5)
print("scheduled task musste nun bearbeitet werden")
#os.system(r'cmd /c "C:\Users\danie\Git\Python\sonstiges\sound_rec\displaydown.exe monitor off"')
keyboard.tap(Key.cmd)
#keyboard.press('t')
#keyboard.release('t')

