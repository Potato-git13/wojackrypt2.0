# import local modules
from encode import encrypt
from decode import decrypt
# import external modules
import argparse
import sys

# Command line arguments
def getOpts(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="The Wojackrypt2.0 CLI")

    parser.add_argument("-ct", "--clitext", help="the CLI input text")
    parser.add_argument("-ck", "--clikey", help="the CLI input key")
    parser.add_argument("-e", "--encrypt", action="store_true", help="encrypt text with the key")
    parser.add_argument("-d", "--decrypt", action="store_true", help="decrypt text with the key")
    parser.add_argument("-if", "--input-file", help="get text from a file")
    parser.add_argument("-ik", "--input-key", help="get the key from a file")
    parser.add_argument("-of", "--output-file", help="write the output text to a file, if the file already exists it overrides it")
    options = parser.parse_args(args)
    return options

options = getOpts(sys.argv[1:])

# ERRORS:

# Text input related errors:
if options.clitext == None and options.input_file == None:
    sys.exit("Error: no text input specified. -h for help")
elif options.clitext and options.input_file:
    sys.exit("Error: only one text input method is allowed")
# Key input related errors
if options.clikey == None and options.input_key == None:
    sys.exit("Error: no key input specified. -h for help")
elif options.clikey and options.input_key:
    sys.exit("Error: only one key input method is allowed")
# Mode input related errors:
if options.encrypt == False and options.decrypt == False:
    sys.exit("Error: no mode specified. -h for help")
elif options.encrypt == True and options.decrypt == True:
    sys.exit("Error: only one mode is allowed")

# Define text
text = ""
if options.clitext:
    text = options.clitext
elif options.input_file:
    # Cover all of the edge cases
    try:
        with open(options.input_file, "r") as fp:
            text = fp.read()
    except FileNotFoundError:
        sys.exit(f"Error: the input file '{options.input_file}' was not found")
    except PermissionError:
        sys.exit(f"Error: permission to the file '{options.input_file}' denied")
    except IsADirectoryError:
        sys.exit(f"Error: '{options.input_file}' is a directory")

# Define key
key = ""
if options.clikey:
    key = options.clikey
elif options.input_key:
    # Cover all of the edge cases
    try:
        with open(options.input_key, "r") as fp:
            key = fp.read()
    except FileNotFoundError:
        sys.exit(f"Error: the input file '{options.input_key}' was not found")
    except PermissionError:
        sys.exit(f"Error: permission to the file '{options.input_key}' denied")
    except IsADirectoryError:
        sys.exit(f"Error: '{options.input_key}' is a directory")

# Encryption mode
if options.encrypt:
    encrypted_text = encrypt(text, key)
    if options.output_file == None:
        print(encrypted_text)
    else:
        # Cover all of the edge cases
        try:
            with open(options.output_file, "w") as fp:
                fp.write(encrypted_text)
        except FileNotFoundError:
            sys.exit(f"Error: the input file '{options.output_file}' was not found")
        except PermissionError:
            sys.exit(f"Error: permission to the file '{options.output_file}' denied")
        except IsADirectoryError:
            sys.exit(f"Error: '{options.output_file}' is a directory")
# Decryption mode
elif options.decrypt:
    decrypted_text = decrypt(text, key)
    if options.output_file == None:
        print(decrypted_text)
    else:
        # Cover all of the edge cases
        try:
            with open(options.output_file, "w") as fp:
                fp.write(decrypted_text)
        except FileNotFoundError:
            sys.exit(f"Error: the output file '{options.output_file}' could not be created")
        except PermissionError:
            sys.exit(f"Error: permission to create the file '{options.output_file}' denied")
        except IsADirectoryError:
            sys.exit(f"Error: '{options.output_file}' is a directory")
