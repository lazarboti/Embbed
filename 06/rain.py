from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

b = (0, 0, 255)
n = (0, 0, 0)
speed = 0.5

space = [n for _ in range(64)]
sense.set_pixels(space)

def shift_down():
    global space
    new_space = [n for _ in range(64)]
    for y in range(7, 0, -1):
        for x in range(8):
            new_space[y * 8 + x] = space[(y - 1) * 8 + x]
    space = new_space

while True:
    x = random.randint(0, 7)
    space[x] = b
    sense.set_pixels(space)
    time.sleep(speed)
    shift_down()
    sense.set_pixels(space)
