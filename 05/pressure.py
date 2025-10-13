from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

P0 = 1013.25

while True:
    P = sense.get_pressure()  
    altitude = 44331 * (1 - (P / P0) ** (1 / 5.2558))
    altitude = round(altitude, 2)

    print(f"Current pressure: {round(P, 2)} hPa")
    print(f"Estimated altitude: {altitude} meters")
    print("-" * 50)

    sleep(5)
