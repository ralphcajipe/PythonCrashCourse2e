# Removing an Item by Value Using remove() Method

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

"""
You can also use the remove() method to work with a value that's being
removed from a list. Let's remove the value 'ducati' and print a reaspm for
removing it from the list. See example below.
"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")