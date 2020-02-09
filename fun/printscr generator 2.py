import random
import string
import time
import keyboard
import webbrowser

confirm = input("Are you sure you want to continue . . (y/n)  ")

if confirm != "y":
    exit("Cancelled . .")

print("Starting in 3 seconds . .")
print("Press and hold escape while running to cancel . .")

time.sleep(3)

while True:
    
    if keyboard.is_pressed("esc"):
        exit("Cancelled by user input . .")

    if keyboard.is_pressed('w'):

        randomw = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(5))

    #keyboard.write("https://prnt.sc/" + randomw)
    #keyboard.press_and_release("enter")
    
        webbrowser.open_new_tab("https://prnt.sc/n" + randomw)

        print("wrote", randomw, "\n")

        time.sleep(0.5)