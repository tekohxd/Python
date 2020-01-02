import random, string

textfile = open("invaded_db.txt", "a")

textfile.write(" -- Invaded DB leaked by Tekoh LOLGETFUCKED (15k IPs) -- \n")
textfile.write("--------------------------------------------------------------------------------------------------------------------\n")

for x in range(15000):
    x = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
    y = ''.join(random.choice(string.digits) for _ in range(2))
    textfile.write(str(x) + " -- " + "192.168.0." + str(y) + "\n")
    print(str(x) + " -- " + "192.168.0." + str(y) + " printed to file")
    textfile.write("--------------------------------------------------------------------------------------------------------------------\n")

textfile.close()