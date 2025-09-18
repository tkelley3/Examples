## This uses functions, which is not something the students would be expected to know at this point, but in the past I have expanded this assignment out when we covered functions.

# Define a function to create the encryption key. Not something the students should know, but the easiest way to do it.
def create_encryption_key():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.?!-"
    return {char: i for i, char in enumerate(characters)}

def encrypt(input_string):
    key = create_encryption_key

    encrypted_text = ""
    for char in input_string:
        if char.lower() in key:
            encrypted_text += key[char.lower()]
        else:
            encrypted_text += char

    return encrypted_text

# here is where i open the file provided by the professor and outputs a TextIOWrapper
def encrypt_file(file_name):
    output_file = open("encrypt.txt", "w")
    with open(file_name, "r") as file:
        for line in file:
            encrypted_line = encrypt(line)
            output_file.write(encrypted_line)
    output_file.close()
    return None

# some example usage for encrypt()
input_string = "Hello World"
encrypted_text = encrypt(input_string)
print(f"The encrypted text for the input {input_string} is {encrypted_text}.")

# changed here instead of hardcoding the file name, the file name is inputted and encrypted
input_file_name = input("Enter the input file name: ")
encrypted_file = encrypt_file(input_file_name)
print("The text file was encrypted successfully.")
