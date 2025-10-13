from sense_hat import SenseHat
from time import time, sleep

sense = SenseHat()

altitude = 125 
pressure_log = []
time_log = []

while True:
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()

    sea_level_pressure = pressure * (1 - (0.0065 * altitude) / (temperature + 0.0065 * altitude + 273.15)) ** -5.257
    sea_level_pressure = round(sea_level_pressure, 1)

    current_time = time()
    time_log.append(current_time)
    pressure_log.append(sea_level_pressure)

    three_hours_ago = current_time - (3 * 60 * 60)
    while time_log and time_log[0] < three_hours_ago:
        time_log.pop(0)
        pressure_log.pop(0)

    if len(pressure_log) < 2:
        trend = "steady"
    else:
        diff = pressure_log[-1] - pressure_log[0]
        if diff >= 1.6:
            trend = "rising"
        elif diff <= -1.6:
            trend = "falling"
        else:
            trend = "steady"

    Z = None
    forecast = "Forecast not available"

    if trend == "falling" and 985 <= sea_level_pressure <= 1050:
        Z = round(127 - 0.12 * sea_level_pressure)
        table = [
            "Settled Fine",
            "Fine Weather",
            "Fine, Becoming Less Settled",
            "Fairly Fine, Showery Later",
            "Showery, Becoming More Unsettled",
            "Unsettled, Rain Later",
            "Rain at Times, Worse Later",
            "Rain at Times, Becoming Very Unsettled",
            "Very Unsettled, Rain"
        ]
        if 1 <= Z <= 9:
            forecast = table[Z - 1]

    elif trend == "steady" and 960 <= sea_level_pressure <= 1033:
        Z = round(144 - 0.13 * sea_level_pressure)
        table = [
            "Settled Fine",
            "Fine Weather",
            "Fine, Possibly Showers",
            "Fairly Fine, Showers Likely",
            "Showery, Bright Intervals",
            "Changeable, Some Rain",
            "Unsettled, Rain at Times",
            "Rain at Frequent Intervals",
            "Very Unsettled, Rain"
        ]
        if 10 <= Z <= 18:
            forecast = table[Z - 10]

    elif trend == "rising" and 947 <= sea_level_pressure <= 1030:
        Z = round(185 - 0.16 * sea_level_pressure)
        table = [
            "Settled Fine",
            "Fine Weather",
            "Becoming Fine",
            "Fairly Fine, Improving",
            "Fairly Fine, Possibly Showers Early",
    
            "Showery Early, Improving",
            "Changeable, Mending",
            "Rather Unsettled, Clearing Later",
            "Unsettled, Probably Improving",
            "Unsettled, Short Fine Intervals",
            "Very Unsettled, Finer at Times",
            "Stormy, Possibly Improving",
            "Stormy, Much Rain"
        ]
        if 20 <= Z <= 32:
            forecast = table[Z - 20]

    print(f"Temp: {round(temperature, 1)} °C, Pressure: {round(pressure, 1)} hPa, Humidity: {round(humidity, 1)}%")
    print(f"Sea-level pressure: {sea_level_pressure} hPa")
    print(f"Pressure trend: {trend.upper()}")
    if Z:
        print(f"Zambretti number: {Z}")
    print(f"Forecast: {forecast}")
    print("-" * 50)

    sleep(3)
