import random
import string
import time
import keyboard
import pyperclip

confirm = input("Are you sure you want to continue . . (y/n)  ")

if confirm != "y":
    exit("Cancelled . .")

print("Starting in 3 seconds . .")
print("Press and hold escape while running to cancel . .")

time.sleep(3)

while True:

    if keyboard.is_pressed('esc'):
        exit("Cancelled by user input . .")

    randomw = ''.join(random.choice(string.ascii_lowercase) for i in range(5))

    keyboard.write(randomw)

    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('enter')

    print("wrote", randomw, "\n")

    time.sleep(0.2)