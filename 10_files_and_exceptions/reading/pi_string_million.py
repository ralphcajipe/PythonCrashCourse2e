"""Large Files: One Million Digits"""

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

"""
Print the famous first 2 decimal places of pi which is 3.14
Add 2 extra indices for leading 3 and decimal point
"""
# 3.14
print(f"{pi_string[0:4]}...")

# 3.14159
print(f"{pi_string[0:7]}...")

# Print first 50 decimals of pi
print(f"\n{pi_string[0:52]}...")
print(len(pi_string))