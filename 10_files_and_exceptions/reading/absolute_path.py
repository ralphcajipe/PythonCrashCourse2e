"""Absolute file path"""
file_path = 'C:/Users/xl38/Documents/other_files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)