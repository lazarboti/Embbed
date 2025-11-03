from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

snake = [(3, 4), (2, 4), (1, 4)]
direction = (1, 0)
food = (random.randint(0, 7), random.randint(0, 7))
score = 0

def place_food():
    while True:
        f = (random.randint(0, 7), random.randint(0, 7))
        if f not in snake:
            return f

def draw():
    sense.clear()
    for x, y in snake:
        sense.set_pixel(x, y, (0, 255, 0))
    sense.set_pixel(food[0], food[1], (255, 0, 0))

def move_up(event):
    global direction
    if event.action == 'pressed' and direction != (0, 1):
        direction = (0, -1)

def move_down(event):
    global direction
    if event.action == 'pressed' and direction != (0, -1):
        direction = (0, 1)

def move_left(event):
    global direction
    if event.action == 'pressed' and direction != (1, 0):
        direction = (-1, 0)

def move_right(event):
    global direction
    if event.action == 'pressed' and direction != (-1, 0):
        direction = (1, 0)

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_left = move_left
sense.stick.direction_right = move_right

draw()

while True:
    sleep(0.3)
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    if new_head[0] < 0 or new_head[0] > 7 or new_head[1] < 0 or new_head[1] > 7:
        break
    if new_head in snake:
        break

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = place_food()
    else:
        snake.pop()

    draw()

sense.show_message("Game over! Score: {}".format(score), text_colour=(255, 255, 255))
sense.clear()
