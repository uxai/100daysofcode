print('''
 _____                              _____ _       _               
/  __ \                            /  __ (_)     | |              
| /  \/ __ _  ___  ___  __ _ _ __  | /  \/_ _ __ | |__   ___ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
| \__/\ (_| |  __/\__ \ (_| | |    | \__/\ | |_) | | | |  __/ |   
 \____/\__,_|\___||___/\__,_|_|     \____/_| .__/|_| |_|\___|_|   
                                           | |                    
                                           |_|                    
''')

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
repeat = True

def encrypt(msg, key, method):
    encrypted_msg = ""
    for letter in msg:
        if letter in alphabet:
            l = alphabet.index(letter)
            if key + l < 25:
                encrypted_msg += alphabet[key+l]
            else:
                ind = key + l - 26
                encrypted_msg += alphabet[ind]
        else:
            encrypted_msg += letter
    print(f"Your {method} message is the following:\n{encrypted_msg}")

while repeat == True:
    process = input("Type 'encode' to encrypt or type 'decode' to decrypt: ").lower()
    message = input("Type your message:\n").lower()
    print("----------------")
    shift = int(input("Type the shift number: "))
    print("----------------")

    if process == "encode":
        encrypt(message, shift, "encoded")
    elif process == "decode":
        encrypt(message, shift * -1, "decoded")
    
    print("----------------")
    again = input("Would you like to go again (yes/no)? ")
    if again == "no":
        repeat = False

print("Thanks for using the Caesar Cipher!")