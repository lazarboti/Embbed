from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
speed = 0.3
bat = [7, 3]
score = 0
up_down = 1

w = (0,0,0)
r = (255,0,0)
b = (0,0,255)

game_space = [w]*64
game_space[7*8 + bat[1]] = b
game_space[7*8 + bat[1]+1] = b

def update_space(x, y, colour):
    if 0 <= x < 8 and 0 <= y < 8:
        game_space[x*8 + y] = colour
        sense.set_pixels(game_space)

def draw_bat():
    update_space(7, bat[1], b)
    update_space(7, bat[1]+1, b)

def left(event):
    if event.action == 'pressed':
        if bat[1] > 0:
            update_space(7, bat[1]+1, w)
            bat[1] -= 1
            draw_bat()

def right(event):
    if event.action == 'pressed':
        if bat[1] < 6:
            update_space(7, bat[1], w)
            bat[1] += 1
            draw_bat()

sense.stick.direction_left = left
sense.stick.direction_right = right

sense.clear()
draw_bat()
game_alive = True

x = 0
y = random.randint(0,7)
d = random.choice([-1,1])
update_space(x, y, r)

while game_alive:
    sleep(speed)
    if 0 <= x < 8 and 0 <= y < 8:
        update_space(x, y, w)

    x += up_down
    y += d

    if y >= 7:
        y = 7
        d = -1
    elif y <= 0:
        y = 0
        d = 1

    if x >= 7:
        x = 7
        if y == bat[1] or y == bat[1]+1:
            score += 1
            up_down = -1
        else:
            game_alive = False
            break
    elif x <= 0:
        x = 0
        up_down = 1

    update_space(x, y, r)
    draw_bat()

sense.clear()
sense.show_message('Game over!', scroll_speed=0.05, back_colour=w)
sense.show_message('Score: ' + str(score), scroll_speed=0.01, back_colour=w)

