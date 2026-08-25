import board
import digitalio
from adafruit_debouncer import Button

key_pin = digitalio.DigitalInOut(board.GP9)
key_pin.direction = digitalio.Direction.INPUT
key_pin.pull = digitalio.Pull.UP

key = Button(key_pin, value_when_pressed=False)

while True:
    key.update()

    if key.pressed:
        print("q")
