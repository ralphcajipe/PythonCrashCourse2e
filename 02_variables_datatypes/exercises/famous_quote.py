"""
Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including quotation marks:

    Albert Einstein said, "A person who never made a
    mistake never tried anything new."
"""

# Solution 1
print('Albert Einstein once said, "A person who never made a mistake\n\
never tried anything new."')

print("")

# Solution 2
first_name = "albert"
last_name = "einstein"
quote = '"A person who never made a mistake\n\
never tried anything new."'

print(f"{first_name.title()} {last_name.title()} once said, {quote}")