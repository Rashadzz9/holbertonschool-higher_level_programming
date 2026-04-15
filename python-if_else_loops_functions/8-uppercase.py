#!/usr/bin/python3

def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    for char in str:
        char_code = ord(char)
        if char_code >= 97 and char_code <= 122:
            char_code = char_code - 32
        print("{}".format(chr(char_code)), end="")
    print("")
