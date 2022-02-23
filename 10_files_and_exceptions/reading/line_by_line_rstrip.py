"""Reading Line by Line with rstrip()"""
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        """Using rstrip() on each line in the print() call
        eliminates extra blank lines."""
        print(line.rstrip())