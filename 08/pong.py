from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

bat_y = 4
score = 0
x = 0
y = random.randint(0, 7)
d = random.choice([-1, 1])
up_down = -1

r = [[0]*8 for _ in range(8)]

def update_space(x, y, r):
    sense.clear()
    for i in range(8):
        for j in range(8):
            if r[i][j] == 1:
                sense.set_pixel(i, j, (0, 255, 0))
    if 0 <= x <= 7 and 0 <= y <= 7:
        sense.set_pixel(x, y, (255, 0, 0))

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 0:
        bat_y -= 1

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 7:
        bat_y += 1

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

r[7][bat_y] = 1
update_space(x, y, r)

while True:
    sleep(0.3)
    sense.clear()
    r = [[0]*8 for _ in range(8)]
    r[7][bat_y] = 1
    x += d
    y += up_down

    if y <= 0 or y >= 7:
        up_down *= -1
    if x == 7 and y == bat_y:
        d *= -1
        score += 1
    if x > 7 or x < 0:
        break

    update_space(x, y, r)

sense.show_message("Game over! Score: {}".format(score), text_colour=(255, 255, 255))
sense.clear()
