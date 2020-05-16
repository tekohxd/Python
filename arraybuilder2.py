import pyperclip

array = []
lolx = '[ '

file = open(input("enter the location of the file\n"))

for line in file:
    if line.strip():
        array.append(line[:-1].replace('"', "'"))


for line in array:
    lolx = lolx + '"' + line + '",\n'

lolx = lolx + "]"

print(lolx)
pyperclip.copy(lolx)