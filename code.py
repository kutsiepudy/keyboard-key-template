import board
import digitalio
from adafruit_debouncer import Button
from adafruit_debouncer import Keyboard
from adafruit_debouncer import Keycode

keyboard = Keyboard(usb_hid.device)



key_pin = digitalio.DigitalInOut(board.GP9)
key_pin.direction = digitalio.Direction.INPUT
key_pin.pull = digitalio.Pull.UP
key = Button(key_pin, value_when_pressed=False)

while True:
    key.update()

    if key.pressed:
        keyboard.press(Keycode.Q)

    if key.released:
        keyboard.release(Keycode.Q)
