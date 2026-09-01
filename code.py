import board
import digitalio
import time

key_pin = digitalio.DigitalInOut(board.GP9)
key_pin.direction = digitalio.Direction.INPUT
key_pin.pull = digitalio.Pull.UP

DEBOUNCE_DELAY = 0.005
key_state = key_pin.value
last_stable_state = key_pin.value
last_debounce_time = time.monotonic()

while True:
    current_reading = key_pin.value

    if current_reading != key_state:
        last_debounce_time = time.monotonic()
        key_state = current_reading

    if (time.monotonic() - last_debounce_time) > DEBOUNCE_DELAY:
        if current_reading != last_stable_state:
            last_stable_state = current_reading

            if last_stable_state == False:
                print("BUTTON PRESS WORKS")

            else:
                print("BUTTON RELEASE WORKS")
