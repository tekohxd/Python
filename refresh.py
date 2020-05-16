import keyboard
import time

confirm = input("Are you sure you want to continue . . (y/n)  ")

if confirm != "y":
    exit("Cancelled . .")

print("Starting in 3 seconds . .")
print("Press and hold escape while running to cancel . .")

time.sleep(3)

while True:

    if keyboard.is_pressed('esc'):
        exit("Cancelled by user input . .")

    keyboard.press_and_release('f5')

    time.sleep(0.4)