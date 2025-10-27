from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

p = [2, 3]
light_len = 3
space_size = 8
speed = 1/7

r = (255, 0, 0)
n = (0, 0, 0)

space = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 r, r, r, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
]

sense.set_pixels(space)

def shift_right():
    global p, space
    for i in range(light_len):
        space[3 * 8 + (p[0] - i)] = n
    p[0] += 1
    for i in range(light_len):
        x = p[0] - i
        if 0 <= x < 8:
            space[3 * 8 + x] = r
    sense.set_pixels(space)

def shift_left():
    global p, space
    for i in range(light_len):
        space[3 * 8 + (p[0] - i)] = n
    p[0] -= 1
    for i in range(light_len):
        x = p[0] - i
        if 0 <= x < 8:
            space[3 * 8 + x] = r
    sense.set_pixels(space)

def main():
    global p
    while True:
        while True:
            shift_right()
            time.sleep(speed)
            if p[0] == space_size - 1:
                break
        while True:
            shift_left()
            time.sleep(speed)
            if p[0] == light_len - 1:
                break

try:
    main()
except KeyboardInterrupt:
    sense.clear()

