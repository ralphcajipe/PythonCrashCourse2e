"""
You can use rstrip() and replace() on the same line.
This is called chaining methods. In the following code the newline is
stripped from the end of the line and then Python is replaced by C.
The output is identical to the code shown at learning_c.py file.
"""
filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    print(line.rstrip().replace('Python', 'C'))