from encryption import *
import os

def view(user):
    file_path = os.path.join(".\\accounts\\", user + ".txt")
    f = open(file_path,"a+")
    f.seek(0)
    data = f.readlines()

    if os.path.getsize(file_path) == 0:
        choice = input("No passwords as of now. To add passwords type a or any other key to revert to menu ")
        if  choice.lower() == 'a':
            add(user)
        else:
            accountOptions(user)

    for line in data:
        parts = line.strip().split(' , ')
        if len(parts) != 2:
            print(f"Skipping malformed line: {line}")
            return

    print("All passwords: ")
    for line in data:
        encryptedUsername,encryptedPassword = line.strip().split(' , ')
        decryptedUsername = decryption(encryptedUsername)
        decryptedPassword = decryption(encryptedPassword)
        print(f"{decryptedUsername} : {decryptedPassword}")
    f.seek(0)
    f.close()
    accountOptions(user)

def add(user):
    file_path = os.path.join(".\\accounts\\", user + ".txt")
    f = open(file_path,"a+")
    username = input("Enter your username ")
    f.seek(0)
    data = f.readlines()
    flag = False
    for line in data:
        encryptedUsername,encryptedPassword = line.strip().split(' , ')
        decryptedUsername = decryption(encryptedUsername)
        if  decryptedUsername == username:
                flag = True
                break
    if(flag == True):
        key = input("Username already exists in database.. To still continue press y ")
        if  key.lower() != "y":
            accountOptions(user)
    else:
        password = input("Enter your password ")
        encryptedUsername = encryption(username)
        encryptedPassword = encryption(password)
        f.write(encryptedUsername + " , " + encryptedPassword)
        print("Added successfully!!")
        f.write("\n")
        f.close()
        accountOptions(user)

def update(user):
    file_path = os.path.join(".\\accounts\\", user + ".txt")
    f = open(file_path,"r+")
    username = input("Enter existing username ")
    f.seek(0)
    data = f.readlines()
    flag = False
    for line in data:
        encryptedUsername,encryptedPassword = line.strip().split(' , ')
        decryptedUsername = decryption(encryptedUsername)
        if  decryptedUsername == username:
                flag = True
                break

    if(flag == False):
        key = input("Username not found in database.. Press y if you want to add new password or any other key to exit ")
        f.close()
        if  key.lower() == "y":
            add(user)
        else:
            accountOptions(user)
    else:
        updatedData = []
        password = input("Enter your new password to be updated ")
        for line in data:
            encryptedUsername,encryptedPassword = line.strip().split(' , ')
            decryptedUsername = decryption(encryptedUsername)
            decryptedPassword = decryption(encryptedPassword)
            if  decryptedUsername == username.strip():
                    newEncryptedPassword = encryption(password)
                    updatedLine = f"{encryptedUsername} , {newEncryptedPassword}\n"
                    updatedData.append(updatedLine)
            else:
                 updatedData.append(line)
        #updatedData.append("\n")
        f.close()
        print(updatedData)
        f = open(file_path,'w+')
        f.writelines(updatedData)
        f.seek(0,2)
        f.close()
        accountOptions(user)

def delete(user):
    file_path = os.path.join(".\\accounts\\", user + ".txt")
    username = input("Enter your username ")
    f.seek(0)
    data = f.readlines()
    flag = False
    for line in data:
        encryptedUsername,encryptedPassword = line.strip().split(' , ')
        decryptedUsername = decryption(encryptedUsername)
        if  decryptedUsername == username:
                flag = True
                break
    
    if(flag == True):
        updatedData = []
        for line in data:
            encryptedUsername,encryptedPassword = line.strip().split(' , ')
            decryptedUsername = decryption(encryptedUsername)
            decryptedPassword = decryption(encryptedPassword)
            if  decryptedUsername != username.strip():
                    updatedData.append(line)
        f.close()
        f = open(file_path,"w")
        f.writelines(updatedData)
        print("Password deleted successfully!")
        f.seek(0,2)
        f.close()
        accountOptions(user)
    else:
        key = input("Username doesn't exist in database.. To add, press y")
        if  key.lower() != "y":
            add(user)
        else:
             accountOptions(user)



def accountOptions(user):
    if not os.path.exists(r"./accounts"):
        os.makedirs(r"./accounts")
    while True:
        choice = int(input("Select a choice:\n1) View passwords\n2) Add a password\n3) Update existing password\n4) Delete a password\n5) Quit\n"))
        if  choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
            break
        else:
            print("Invalid input. Try again..")
    match choice:
            case 1:
                view(user)
            case 2:
                add(user)
            case 3:
                update(user)
            case 4:
                delete(user)
            case 5:
                print("Thanks for using my software..")
                quit()

