file = open("en_US.txt", "r")
newLangFile = open("newLang.txt", "a")

newLang = []

#for line in file:
#    if line.strip():
#        print(line.split("=")[1])
    

for line in file:
    if line.strip():
        controller = line.split("=")[0]
        text = line.split("=")[1].lower()
        newLang.append((controller + "=" + text))

        print("added " + (controller + "=" + text))
    else:
        newLang.append("\n")


for line in newLang:
    newLangFile.write(line)

    print("wrote " + (controller + "=" + text))
