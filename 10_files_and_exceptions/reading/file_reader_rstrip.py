"""Remove extra blank line at the end of output."""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())