# Popping Items from any Position in a List

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

"""
NOTE: Remember that each time you use pop() method,
the item you work with is no longer stored
in the list. See example below.
"""
best = motorcycles.pop(0)
print(f"My best motorcyle is a {best.title()}.")
