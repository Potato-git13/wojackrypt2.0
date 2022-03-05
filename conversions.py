def chartoint(char):
    # Convert the character to byte
    charbyte = bytes(char, "utf-8")
    # Convert the byte to int
    charint = int.from_bytes(charbyte, "big")

    return charint

def inttochar(int):
    # Convert the int to byte
    intbyte = int.to_bytes(4, "big")
    # Convert the byte to char
    intchar = intbyte.decode("utf-8")
    
    return intchar
