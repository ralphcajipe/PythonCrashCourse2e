"""Appending to a File"""

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love artificial intelligence.\n")
    file_object.write("I love clean and readable code.\n")