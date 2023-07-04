#!/usr/bin/python3
""" Define the function """


def text_indentation(text):
    """ print test with two new line if the ., ?, : exist"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    a = ""
    x = 0
    while x < len(text) and text[x] == '':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
