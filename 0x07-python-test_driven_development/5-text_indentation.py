#!/usr/bin/python3

"""
module 5-text_indentation
"""


def text_indentation(text):
    """
    adds new lines to paragraphs
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    ch = 0
    while ch < len(text):
        if text[ch] == "." or text[ch] == "?" or text[ch] == ":":
            new_text += text[ch]
            new_text += "\n\n"
            if ch + 1 != len(text) and text[ch + 1] == " ":
                ch += 1
        else:
            new_text += text[ch]
        ch += 1
    print(new_text, end="")
