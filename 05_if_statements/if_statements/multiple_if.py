"""
NOTE:
    Sometimes it's important to check all of the conditions of interest.
    In this case, you should use a series of simple if statements with no
    elif or else blocks. This technique makes sense when more than one
    condition could be True, and you want to act on every condition that is
    True.
"""

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")