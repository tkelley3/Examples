

# Define a function to create the encryption key.
def create_encryption_key():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,."
    return {char: i for i, char in enumerate(characters)}
