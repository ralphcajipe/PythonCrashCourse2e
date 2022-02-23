# Index Positions Starts at 0, Not 1

# The following asks for the companies at index 1 and index 3:
# item        first     second     third    fourth
companies = ['google', 'amazon', 'twitter', 'tesla']
# +index         0         1          2        3
# -index        -4        -3         -2        -1
print(companies[1])
print(companies[3])

# Special syntax for accessing the last element in a list
# index -1 or index -n
companies = ['google', 'amazon', 'twitter', 'tesla']
print(companies[-1])
print(companies[-2])

# Access list from 'index n' but don't display this element 'index -n'
print(companies[0:3])