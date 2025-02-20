from encryption import *
from passwordManager import *

def signup():
    f = open(r".\data.txt","a+")
    f.seek(0)
    data = f.readlines()
    while True:
        flag = False
        username = input("Enter your username: ")
        for line in data:
            encryptedUsername,encryptedPassword = line.strip().split(' , ')
            decryptedUsername = decryption(encryptedUsername)
            if  decryptedUsername == username:
                flag = True
                break
        if(flag):
            choice = input("Username already taken.. To login press y or press any other key to continue signup process ")
            if  choice=='y':
                login()
        else:
            break
    password = input("Enter a secure password: ")
    encryptedUsername = encryption(username)
    encryptedPassword = encryption(password)
    f.write(encryptedUsername + " , " + encryptedPassword)
    print("Account created successfully!!")
    f.write("\n")
    f.close()
    options()

def login():
    f = open(r".\data.txt","a+")
    f.seek(0)
    username = input("Enter your username: ")
    data = f.readlines()
    flag = False
    for line in data:
        encryptedUsername,encryptedPassword = line.strip().split(' , ')
        decryptedUsername = decryption(encryptedUsername)
        if  decryptedUsername == username:
                flag = True
                break
    if(flag == False):
        key = input("Username not found in database.. Press y if you want to Sign Up or any other key to exit ")
        if  key.lower() == "y":
            signup()
    else:
        f.seek(0)
        data = f.readlines()
        password = input("Enter your password: ")
        for line in data:
            encryptedUsername,encryptedPassword = line.strip().split(' , ')
            decryptedPassword = decryption(encryptedPassword)
            if  decryptedPassword == password:
                    print("Access granted!")
                    f.close()
                    accountOptions(username.strip())
                    return
        print("Wrong password, access denied!")
        f.close()
        options()

def options():
    while True:
        choice = int(input("Welcome to our Password Manager!!\nSelect a choice:\n1) Log In\n2) Sign Up (If new user)\n3) Quit\n"))
        if  choice == 1 or choice == 2 or choice == 3:
            break
        else:
            print("Invalid input. Try again..")
    match choice:
        case 1:
            login()
        case 2:
            signup()
        case 3:
            print("Thanks for using my software..")
            quit()

options()

