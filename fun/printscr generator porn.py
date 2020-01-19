import time
import keyboard


confirm = input("Are you sure you want to continue . . (y/n)  ")

if confirm != "y":
    exit("Cancelled . .")

print("Starting in 3 seconds . .")
print("Press and hold escape while running to cancel . .")

time.sleep(3)

count = 0

for code in range(50, 100):

    count += 1

    if count >= 5:
        keyboard.press_and_release("enter")
        count = 0
        time.sleep(7)

    keyboard.write("https://prnt.sc/porn" + str(code))
    keyboard.press("shift")
    keyboard.press_and_release("enter")
    keyboard.release("shift")