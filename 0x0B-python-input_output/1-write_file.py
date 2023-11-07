#!/usr/bin/python3
"""module for writing to a file"""
def write_file(filename="", text="")
    """function to write to a file"""
    with open(filename, "w", encoding="utf8") as file:
        return file.write(text)
