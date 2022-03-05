# conversions is a local module!
from conversions import chartoint
import sys

def encrypt(text, key):
    text_encrypted = ""
    counter = 0

    if key == "":
        sys.exit("Error: key cannot be empty")
    # Iterate for every character and encrypt it
    for char in text:
        # Convert the current character to int
        char_int = chartoint(char)

        # Get the length of the key
        key_len = len(key)
        # Find the character coresponding to the counter. This means it will
        # go through the key at the same time as the string iterates. When the
        # key runs out it goes back to the start
        key_char = key[counter]
        # Convert the char to an int
        key_char_int = chartoint(key_char)

        # THE ENCRYPTION EQUATION a*2+n+b*n
        encrypted_int = char_int*2 + key_len + key_char_int * key_len

        # When the key doesn't have anymore characters go back to the start
        if counter < key_len-1:
            counter+=1
        else:
            counter=0

        # Add the encrypted number to the string
        # Add a '/' so it can be easily split when the text is decrypted
        text_encrypted += str(encrypted_int) + '/'

    return text_encrypted
