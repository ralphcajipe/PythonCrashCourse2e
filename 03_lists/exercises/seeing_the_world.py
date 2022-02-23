places = ['canada', 'brazil', 'egypt', 'denmark', 'argentina']

print("Here's the ORIGINAL order")
print(places)

print("\nHere's the SORTED list")
print(sorted(places))

print("\nHere's the ORIGINAL order again")
print(places)

print("\nHere's the REVERSE SORTED list")
print(sorted(places, reverse=True))

print("\nHere's the ORIGINAL order again")
print(places)

print("\nHere's the REVERSE list")
places.reverse()
print(places)

print("\nHere's the REVERSE list again")
places.reverse()
print(places)

print("\nHere's the SORT list:")
places.sort()
print(places)

print("\nHere's the SORT REVERSE list:")
places.sort(reverse=True)
print(places)