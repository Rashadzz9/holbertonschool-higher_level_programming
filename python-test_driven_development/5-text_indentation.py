#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    clean_text = text.strip()
    special_chars = ".?:"
    i = 0
    while i < len(clean_text):
        print(clean_text[i], end="")
        if clean_text[i] in special_chars:
            print("\n")
            while i + 1 < len(clean_text) and clean_text[i + 1] == " ":
                i += 1
        i += 1
