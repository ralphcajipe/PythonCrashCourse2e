"""Writing Multiple Lines"""

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating software.\n")
    file_object.write("I love good tech.")