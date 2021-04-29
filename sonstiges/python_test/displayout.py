import os
import time
from pynput.mouse import Button, Controller
mouse = Controller()
i = 1
end_time = time.time() + 10

#os.system(r'cmd /c "C:\Users\danie\Git\Python\sonstiges\sound_rec\displaydown.exe monitor off"')
while time.time() < end_time:
    mouse.position = (0, 0)
    os.system(r'cmd /c "C:\Users\danie\Git\Python\sonstiges\sound_rec\displaydown.exe monitor off"')

    nowpos_x = mouse.position[0]
    nowpos_y = mouse.position[1]
    nextpos_x = mouse.position[0]
    nextpos_y = mouse.position[1]
    if nowpos_x != nextpos_x or nowpos_y != nextpos_y:
        #print("bewegung erkannt")
        os.system(r'cmd /c "C:\Users\danie\Git\Python\sonstiges\sound_rec\displaydown.exe monitor off"')