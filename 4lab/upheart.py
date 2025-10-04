from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = (255, 0, 0)
b = (0, 0, 0)

heart = [
    b, r, r, b, b, r, r, b,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    b, r, r, r, r, r, r, b,
    b, b, r, r, r, r, b, b,
    b, b, b, r, r, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]

def red_heart(event=None):
    for i in range(3):
        sense.set_pixels(heart)
        sleep(0.5)
        sense.clear()
        sleep(0.5)

def blue(event=None):
    sense.clear(0, 0, 255)

def green(event=None):
    sense.clear(0, 255, 0)

def yellow(event=None):
    sense.clear(255, 255, 0)

sense.stick.direction_up = red_heart
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear

while True:
    pass
