import random, string

textfile = open("discord_codes.txt", "a")

for x in range(1000000):
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(14))
    textfile.write("discord.gift/" + str(x) + "\n")
    print("discord.gift/" + str(x) + " printed to file")

