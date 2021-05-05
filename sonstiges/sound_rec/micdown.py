from pynput.keyboard import Key, Controller as KeyboardController
keyboard = KeyboardController()
import os
import time


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

#word = 'tab'
#keyboard.press(Key)
#keyboard.release(Key.word)
#start
key_tap(1, Key.cmd)

time.sleep(0.3)

#einstellungen eingeben und öffnen
keyboard.type('einstellungen')
time.sleep(0.3)
key_tap(1, Key.enter)

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
#umschalten mic symbol
key_tap(1, Key.space)
time.sleep(0.3)
#einstellungen schließen
key_combi(2, [Key.alt_l, Key.f4])
time.sleep(0.3)
