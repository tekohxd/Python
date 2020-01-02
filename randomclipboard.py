import random
import string
import pyperclip

letters = string.ascii_lowercase
randomw = ''.join(random.choice(letters) for i in range(5))
pyperclip.copy(randomw)
print("Clipboard changed to " + randomw)
