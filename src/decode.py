# conversions is a local module!
from conversions import inttochar, chartoint
from re import sub
import sys

def decrypt(text, key):
    text_decrypted = ""
    counter = 0
    # Split the string to get the individual numbers
    num_list = text.split("/")
    # Check if the last entry is empty and if so remove it
    if num_list[-1] == '':
        num_list = num_list[:-1]

    if key == "":
        sys.exit("Error: key cannot be empty")
    # Iterate for every number and decrypt it
    for num in num_list:
        try:
            encrypted_char_int = int(num)
        except ValueError:
            sys.exit(f"Error: invalid value '{num}'")

        # Get the length of the key
        key_len = len(key)
        # Find the character coresponding to the counter. This means it will
        # go through the key at the same time as the string iterates. When the
        # key runs out it goes back to the start
        key_char = key[counter]
        # Convert the char to an int
        key_char_int = chartoint(key_char)

        # THE DECRYPTION EQUATION (x-(n+b*n))/2
        decrypted_char_int = (encrypted_char_int - (key_len + key_char_int * key_len))//2

        # Convert the new decrypted int to a char
        decrypted_char = ""
        try:
            decrypted_char = inttochar(decrypted_char_int)
        except UnicodeDecodeError:
            sys.exit(f"Decoding Error: invalid int '{num}'")
        except OverflowError:
            sys.exit(f"Decoding Error: invalid int '{num}'")
        # Remove all null bytes
        decrypted_char = sub("\x00", "", decrypted_char)

        # When the key doesn't have anymore characters go back to the start
        if counter < key_len-1:
            counter+=1
        else:
            counter=0

        # Add the decrypted char to the string
        text_decrypted += decrypted_char

    return text_decrypted
