from pynput.mouse import Button, Controller as MouseController
import time
import os
mouse = MouseController()


end_time = time.time() + 4

while time.time() < end_time:
    #mouse.position = (0, 0)

    nowpos_x = mouse.position[0]
    nowpos_y = mouse.position[1]
    nextpos_x = mouse.position[0]
    nextpos_y = mouse.position[1]
    if nowpos_x != nextpos_x or nowpos_y != nextpos_y:
        time.sleep(0.1)
        mouse.position = (int(nowpos_x), int(nowpos_y))
        os.system(r'cmd /c "C:\Users\danie\Git\Python\sonstiges\Sondersoftware\displaydown.exe monitor off"')






#while time.time() < end_time:
#    print("Current position: " + str(mouse.position))
#    #pos = mouse.position
#    nowpos_x = mouse.position[0]
#    nowpos_y = mouse.position[1]
#    if nowpos_x != mouse.position[0] or nowpos_y != mouse.position[1]:
#        mouse.position = (nowpos_x, nowpos_y)
#        time.sleep(0.1)
    #time.sleep(0.1)