def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    text = text.strip()

    while i < len(text):
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            i += 1

            # skip spaces after punctuation
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1
