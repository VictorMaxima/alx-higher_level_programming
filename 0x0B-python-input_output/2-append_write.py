#!/usr/bin/python3
"""module for append writing"""
def append_write(filename="", text="")
	"""funcition for appending to a file"""
	with open(filename, 'a', enconding="utf8") as file:
		return file.write(text)
