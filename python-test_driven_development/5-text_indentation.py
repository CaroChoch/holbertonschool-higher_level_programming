#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each
    of these characters: ., ? and :

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = False
    new_text = text.replace(". ", ".").replace("? ", "?")\
        .replace(": ", ":")
    for char in new_text:
        if char in [".", "?", ":"]:
            print(char)
            print("")
            flag = True
        else:
            if flag is False:
                print(char, end="")
            else:
                if char != " ":
                    print(char, end="")
                    flag = False
