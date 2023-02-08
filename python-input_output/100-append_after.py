#!/usr/bin/python3
"""
Function that inserts a line of text to a file, after each line containing
a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing
    a given string in a file.
    Arguments:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """

    with open(filename, 'r') as file:
        contents = file.readlines()

    len = 0

    with open(filename, 'w') as file:
        for lines in contents:
            len += 1
            if search_string in lines:
                contents.insert(len, new_string)
            file.write(lines)





