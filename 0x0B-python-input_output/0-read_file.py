#!/usr/bin/python3
"""Module for read file"""
def read_file(filename="")
    """reads a text file and prints it"""
    with open(filename, "r", encoding="utf8") as file
        for line in file:
            print(line, end="")
