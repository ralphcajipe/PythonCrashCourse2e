# Sorting a List Permanently with the sort() Method

# sort in alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

"""
The sort() method changes the order of the list PERMANENTLY.
The cars are now in alphabetical order, and we can never revert to the original order.
"""

# sort in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)