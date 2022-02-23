"""
Removing an Item Using the pop() Method

The pop() method removes the last item in a list,
but it lets you work with that item after removing it.
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Use pop() method to print a statement
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycled I owned was a {last_owned.title()}.")
