import random
def encryption(str):
    #encrypted_string = char(len) + salt(even positions) + string(odd positions) + cipherPosition(int)
    rand = random.randint(1,4)
    str = str[::-1]
    n = len(str)
    encrypted_str = [''] * (2*n+1)
    encrypted_str[0] = chr(n%126 + 33)
    for i in range(1,n+1):
        encrypted_str[2*i-1] = chr(ord(str[i-1]) + rand)
    for i in range(1,n):
        encrypted_str[2*i] = chr(random.randint(48,126))
    encrypted_str[2*n] = chr(rand + 40 )
    encrypted = ''.join(encrypted_str)
    return encrypted
    
def decryption(str):
    n = ord(str[0]) - 33
    rand = ord(str[len(str) - 1]) - 40
    decrypted_str = [''] * n
    for i in range(1,n+1):
        decrypted_str[i-1] = chr(ord(str[2*i-1]) - rand)
    decrypted = ''.join(decrypted_str)
    decrypted = decrypted[::-1]
    return decrypted

def option():
    choice = int(input("Enter choice\n1) Encrypt\n2) Decrypt\n"))
    match choice:
        case 1:
            str = input("Enter normal string ")
            print(f"Encryption is {encryption(str)}")
        case 2:
            str = input("Enter encrypted string ")
            print(f"Encryption is {decryption(str)}")

#option()


