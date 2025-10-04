from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
b = (0, 0, 0)       
w = (255, 255, 255) 
right_arrow = [
    b, b, b, b, w, b, b, b,
    b, b, b, b, w, w, b, b,
    b, b, b, w, b, w, b, b,
    w, w, w, b, b, w, w, b,
    w, w, w, b, b, w, w, b,
    b, b, b, w, b, w, b, b,
    b, b, b, b, w, w, b, b,
    b, b, b, b, w, b, b, b
]


while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                sense.show_letter("U")
            elif event.direction == "down":
                sense.show_letter("D")
            elif event.direction == "left":
                sense.show_letter("L")
            elif event.direction == "right":
                sense.set_pixels(right_arrow)
            elif event.direction == "middle":
                sense.show_letter("M")
            
           
            sleep(0.5)
            sense.clear()
