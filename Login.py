import time


users = {}
status = ""

def mainMenu():
    global status
    status = input("Do you have an existing account (Y/N)?\nPress Q to quit.\n")
    if status == "y" or "Y":
        existingUser()
    elif status == "n" or "N":
        newUser()
    elif status == "q" or "Q":
        quit()
        
def newUser():
    createLogin = input("Create a Username: ")
    
    if createLogin in users:
        print("\n Username already exists.\n")
    else:
        createPass = input("Choose a password: ")
        users[createLogin] = createPass
        print("\nUser created!\n")
        logins=open("/logins.txt", "a")
        logins.write("\n" + createLogin + " " + createPass)
        logins.close()
        
def existingUser():
    user = input("Enter username: ")
    password = input("Enter password: ")
    
    #Check if user and pass exists
    
    if user in users and users[user] == password:
        print("\nLogin Successful\n")
        print("User:", user, " - Logged in successfully at ", time.asctime())
    else:
        print("\nUser or Password incorrect")
        
while status != "q":
    status = mainMenu()
    
        
    
    
