#!/usr/bin/python3
"""
This module provides a function that indents text.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = [".", "?", ":"]
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in special_chars or text[c] == "\n":
            if text[c] in special_chars:
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
