import neopixel
from machine import Pin
import time

LED_PIN = 5
LED_COUNT = 90   # 58 + 59

np = neopixel.NeoPixel(Pin(LED_PIN), LED_COUNT)

def clear():
    for i in range(LED_COUNT):
        np[i] = (0, 0, 0)
    np.write()

# -------- TEST 1: Fill colors --------
def color_test():
    while True:
        print("Red")
        for i in range(LED_COUNT):
            np[i] = (50, 0, 0)
        np.write()
        time.sleep(1)

        print("Green")
        for i in range(LED_COUNT):
            np[i] = (0, 50, 0)
        np.write()
        time.sleep(1)

        print("Blue")
        for i in range(LED_COUNT):
            np[i] = (0, 0, 50)
        np.write()
        time.sleep(1)

# -------- TEST 2: Running pixel --------
def chase_test():
    while True:
        for i in range(LED_COUNT):
            clear()
            np[i] = (0, 0, 255)
            np.write()
            time.sleep(0.01)

# -------- TEST 3: Split strips check (58 | 59) --------
def split_test():
    while True:
        print("First strip ON")
        clear()
        for i in range(58):
            np[i] = (0, 50, 0)
        np.write()
        time.sleep(1)

        print("Second strip ON")
        clear()
        for i in range(58, 117):
            np[i] = (0, 0, 50)
        np.write()
        time.sleep(1)

# -------- RUN --------
clear()
# Uncomment ONE at a time:

color_test()
# chase_test()
# split_test()
