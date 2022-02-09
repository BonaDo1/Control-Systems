import time
import board
from analogio import AnalogIn

# Connect an analog sensor to the A1 port of the board you are using. This means a 3V, GND, and signal pin must all be connected.
input = AnalogIn(board.A1)

while True:
    print((get_voltage(input),))
    time.sleep(0.5)
