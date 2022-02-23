"""Working with a File's Contents"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

"""Attempt to build a single string containing 
all the digits in the file with no whitespace in it:"""

# Hold the digits of pi
pi_string = ''
# Adds each line of digits to pi_string and removes newline characters
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
