from pynput.mouse import Button, Controller, Listener
import time
mouse = Controller()

i = 1
while i > 0:
    print("Current position: " + str(mouse.position))
    time.sleep(1)