'''
Stripping Whitespace

NOTE:
    Best to visualize in Python IDLE to see the stripping.
    Declare and assign values to the given variables in the examples below but
    Run without the print() function

EXAMPLE:
    # Stripping whitespace from both sides at once
    favorite_language = ' python '
    favorite_language.strip()
'''

favorite_language = ' python '
print(favorite_language)
# rstrip() method for right side
favorite_language.rstrip()
print(favorite_language)
print("")

# associate stripped value to variable name
favorite_language = ' python '
favorite_language = favorite_language.rstrip()
print(favorite_language)
print("")

# lstrip() method for left side
favorite_language = ' python '
favorite_language.lstrip()
print(favorite_language)
print("")

# strip() for both sides at once
favorite_language = ' python '
favorite_language.strip()
print(favorite_language)