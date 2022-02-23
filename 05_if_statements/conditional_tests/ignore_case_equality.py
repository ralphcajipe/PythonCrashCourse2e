# Ignoring Case When Checking for Equality in Python IDLE Shell
# Testing for equality is case sensitive in Python

"""

>>> company = 'Google'
>>> company = 'google'
False

>>> company = 'Google'
>>> company.lower() == 'google'
True


NOTE:
The lower() method/function doesn't change the value that was originally
stored in car, so you can do this kind of comparison without affecting
the original variable.

"""