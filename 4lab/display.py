from sense_hat import SenseHat
from time import sleep
from random import randint


sense = SenseHat()


def random_colour():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)


name = "Bence"  
for letter in name:
    if letter != " ":
        sense.show_letter(letter, random_colour())
        sleep(1)

sense.clear()