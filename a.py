file = open("a.txt", "r")
newLangFile = open("new.txt", "a")

newLang = []

for line in file:
    newLang.append(line.replace("'", "`")[:-1] + ", ")

for line in newLang:
    newLangFile.write(line)

    print("wrote " + line)