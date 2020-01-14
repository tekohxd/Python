import random
import time

username = "null"
balance = 0

def createUser(requestedUsername):
    if checkUserDuplicate(requestedUsername):
        chosenPassword = input("Create a password: ")

        userdata = open("fun/slotmachine thing/userdata.txt", "a")
        userdata.write(requestedUsername + ", " + chosenPassword + ", 50\n")
        userdata.close()
        print("----------")
        print("Your account has been created")
        print("Program will restart in 5 seconds..")
        print("----------")
        time.sleep(5)
        start()
    else:
        newusername = input("That username is already in use\nChoose another username: ")
        createUser(newusername)

def checkUserDuplicate(userToCheck):

    userdata = open("fun/slotmachine thing/userdata.txt", "r")

    for line in userdata:
        if line.split(", ")[0] == userToCheck:
            userdata.close()
            return False
    userdata.close()
    return True
    
def start():
    print("-----")
    print("Welcome to Tekoh slot machine")
    print("\nYou can log into an account, or create a new account")
    print("Each new account has $50 starting balance")
    print("\nType 'login' to log into your account | format: user (press enter), password")
    print("Type 'new' to create a new account")
    choice = input("-----\n\n")

    if choice.lower() == "new":
        print("----------")
        newusername = input("\nPlease enter the username you would like to use: ")

        createUser(newusername)
    elif choice.lower() == "login":
        loginUsername = input("Please enter your username: ")
        loginPassword = input("Please enter your password: ")
        if login(loginUsername, loginPassword):
             print("Login successful..")
        else:
            print("Login fail..")


def login(loginUsername, loginPassword):
    userdata = open("fun/slotmachine thing/userdata.txt", "r")
    for line in userdata:
        if line.split(", ")[0] == loginUsername:
            if line.split(", ")[1] == loginPassword:
                userdata.close()
                return True
    userdata.close()
    return False

            
start()