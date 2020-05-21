import urllib.request
import os

size = 64

def dl_png(name, size):
    url = "https://mc-heads.net/avatar/" + name + "/" + str(size)
    try:
        urllib.request.urlretrieve(url, "./downloads/" + name + ".png")
    except:
        try:
            os.mkdir("downloads")
            urllib.request.urlretrieve(url, "./downloads/" + name + ".png")
        except:
            exit("error creating folder and/or downloading skin")


print("Minecraft head downloader by Tekoh (tekoh.wtf)")
print("Seperate usernames by , to download multiple")
print("press ctrl + c at anytime to close program")

while True:
    name = str(input("Enter a username: "))

    if "," in name:
        for n in name.split(", "):
            print("downloading " + n + "..")
            dl_png(n, size)
            print("downloaded to /downloads/" + n + ".png")
        continue

    print("downloading..")
    dl_png(name, size)
    print("downloaded to /downloads/" + name + ".png")