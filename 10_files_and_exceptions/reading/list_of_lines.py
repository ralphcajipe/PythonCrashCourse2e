"""Making a List of Lines from a File"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

"""Retain access to a file's contents outside the with block."""
for line in lines:
    print(line.rstrip())