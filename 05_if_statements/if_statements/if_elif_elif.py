# Amusement Park's Admission Cost

"""
NOTE:
Python does not require an `else` block at the end of an if-elif chain.
Sometimes an else block is useful; sometimes it is clearer to use an
additional elif statement that catches the specific condition of interest:
"""
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")