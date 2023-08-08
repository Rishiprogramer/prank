import rotatescreen
import time
import os
screen = rotatescreen.get_primary_display()
for i in range(1, 20):
    screen.rotate_to(90)
    time.sleep(0.5)
    screen.rotate_to(180)
    time.sleep(0.5)
    screen.rotate_to(270)
    time.sleep(0.5)
    screen.rotate_to(0)
    time.sleep(0.5)

os.system('shutdown /s /t 0')


