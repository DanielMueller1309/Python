from pynput.mouse import Button, Controller as MouseController
import time
import os
zeit = 5
mouse = MouseController()
def timed_press(time_in_sec):
    next_time = time.time() + time_in_sec
    while time.time() < next_time:
        mouse.release(Button.left)

end_time = time.time() + zeit
while time.time() < end_time:
    mouse.release(Button.left)
    nowpos_x = mouse.position[0]
    mouse.release(Button.left)
    nowpos_y = mouse.position[1]
    mouse.release(Button.left)
    nextpos_x = mouse.position[0]
    mouse.release(Button.left)
    nextpos_y = mouse.position[1]
    mouse.release(Button.left)
    if nowpos_x != nextpos_x or nowpos_y != nextpos_y:
        mouse.release(Button.left)
        timed_press(0.01)
        mouse.release(Button.left)
        mouse.position = (int(nowpos_x), int(nowpos_y))





#while time.time() < end_time:
#    print("Current position: " + str(mouse.position))
#    #pos = mouse.position
#    nowpos_x = mouse.position[0]
#    nowpos_y = mouse.position[1]
#    if nowpos_x != mouse.position[0] or nowpos_y != mouse.position[1]:
#        mouse.position = (nowpos_x, nowpos_y)
#        time.sleep(0.1)
    #time.sleep(0.1)