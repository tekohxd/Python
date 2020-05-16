import random
import string
import keyboard
import time

count = 0

time.sleep(2)

while count < 5:
    count += 1

    keyboard.write("max#")
    randomnum = "".join(random.choice(string.digits) for i in range(4))
    keyboard.write(randomnum)
    time.sleep(0.1)
    keyboard.press_and_release('enter')
    time.sleep(0.5)