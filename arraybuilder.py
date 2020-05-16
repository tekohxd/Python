import pyperclip

pictures = []

while True:
    item = input("give item to add to array\ntype 'finish!' to finish\n")

    if item == "finish!":
        lol = "["
        for lol1 in pictures:
            lol = (lol + ',\n"' + lol1 + '"')

        lol = (lol + " ]")
        print(lol)
        pyperclip.copy(lol)
        input("press any key to continue, array has been copied to your keyboard")
        exit()
    pictures.append(item)

