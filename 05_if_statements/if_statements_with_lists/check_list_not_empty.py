# Checking That a List Is Not Empty

"""
NOTE:
When the name of a list is used in an if statement,

e.g. if requested_toppings:

Python returns True if the list contains at least one item;
an empty list evaluates to False.
"""

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")