from pynput.mouse import Button, Controller
import time
mouse = Controller()
time.sleep(1)
mouse.position = (1760, 2200)
mouse.click(Button.left)

i = 1
while i > 0:
    print("Current position: " + str(mouse.position))
    time.sleep(1)
