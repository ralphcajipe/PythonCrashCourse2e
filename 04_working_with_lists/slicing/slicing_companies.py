# index         0         1        2         3        4
companies = ['google', 'apple', 'tesla', 'twitter', 'amd']

# Prints first three
print(companies[0:3])   # ['google', 'apple', 'tesla']

# Starts with 'apple' and ends with 'twitter'
print(companies[1:4])   # ['apple', 'tesla', 'twitter']

# Starts at the beginning of the list and ends with twitter or omit index 4
print(companies[:4])    # ['google', 'apple', 'tesla', 'twitter']

# Returns all items from the third item/index 2 up to the end of the list
print(companies[2:])    # ['google', 'apple']

# Prints the last three companies
print(companies[-3:])   # ['tesla', 'twitter', 'amd']


'''
The following slices are more complex.
Take more time to read and understand how it works.
'''
# Start at the beginning and omit the last three companies
print(companies[:-3])   # ['google', 'apple']

# Starts at the beginning and omit the last two companies
print(companies[0:-2])  # ['google', 'apple', 'tesla']

# Prints the last 4 companies but omit index 4
print(companies[-4:4])  # ['apple', 'tesla', 'twitter']