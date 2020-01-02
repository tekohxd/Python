import random

score = 0

#Welcome message for users running the program
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome! Please follow the instructions below to play the game")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#Returns random song, used for choosing a random song every time and keeping it more managed
def randomSong():
    songs = open("songlist.txt", "r")
    return random.choice(list(songs))

#Main game function
def runGame():
    #Lets you access 'score' variable from main program within the function
    global score
    #Gets a random song from the randomSong() function
    chosenSong = randomSong()
    chosenSong1 = chosenSong.split(", ")

    #Splits the artist and the name of the song
    songArtist = chosenSong1[0]
    songName = chosenSong1[1]

    #Creates a string called songName1 with only the first letter of each word in the songName variable
    words = songName.split()
    letters123 = [word[0] for word in words]
    letters = " ".join(letters123)
    songName1 = songName[:-1]

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Artist: " + songArtist)
    print("First Letters: " + letters)
    print("What's the song name?")
    chance1= str(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"))
    
    if chance1.lower() == songName1.lower():
        print("Correct!\n")
        score += 3
        runGame()
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Incorrect!")
        print("You have one more chance!")
        chance2 = str(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"))
        if chance2.lower() == songName1.lower():
            print("Correct!\n")
            score += 1
            runGame()
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Game over! The song was ", chosenSong)
            print("Your score: " + str(score))
            print("Would you like to save your data? Y/N")
            option1 = str(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"))
            if option1.lower() == "y":
                saveData(score, givenLoginEmail)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Data has been saved to file")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            exit()

def saveData(points, email): 
    saveFile = open("userdata.txt", "a")

    saveFile.write("User " + str(email) + ", Score " + str(points) + "\n")
    saveFile.close()

givenLoginEmail = "a"
givenLoginPass = "a" 
loginValid = 0
logins = open("logins.txt", "r")

def begin():
    option = str(input("Would you like to play the game or view save data?\nD to view save data\nG to play the game\n"))

    if option.lower() == "d":
        saveFile = open("userdata.txt", "r")
        #Iterates through all scores, printing them all and finding the high score
        highest = 0
        for line in saveFile:
            print(line[:-1])
            line1 = line.split(", Score ")
            line11 = line1[1]
            if int(line11[:-1]) > highest:
                highest = int(line11[:-1])
        print("----------------------\n")
        begin()

    print("\n\n")
    #Login system
    

    #Message to greet user while they are prompted to log in
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You will now need to login with your given details!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

    givenLoginEmail = input("Please enter your email\n")
    givenLoginPass = input("Please enter your password\n")

    for line in logins:

        line1 = line.split(", ")
        password = line1[1]

        if givenLoginEmail.lower() == line.split(", ")[0]:
            if givenLoginPass == password[:-1]:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Login was successful! Welcome to the game!")
                print("Game rules are as follow")
                print("You will recieve three points for guessing correctly on your first go,")
                print("and one point if you guess correctly on your second go.")
                print("If you are incorrect both times, the game will end!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
                runGame()
    #Code shouldn't reach here unless login was failed
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("- - - Login Failed - - -")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    begin()

begin()