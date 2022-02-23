"""Handling the ZeroDivisionError Exception"""

# Using try-except blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")