silogs = ('tapsilog', 'bacsilog', 'tunasilog',
          'daingsilog', 'veggiesilog')

# silogs[0] = 'tuyosilog'
# TypeError: 'tuple' object does not support item assignment

print("Here's our menu:")
for silog in silogs:
    print(f"- {silog}")

# Menu update
silogs = ('tapsilog', 'bacsilog', 'chicksilog',
          'shrimpsilog', 'veggiesilog')

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for silog in silogs:
    print(f"- {silog}")
