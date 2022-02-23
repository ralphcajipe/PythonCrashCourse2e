# Invite some people to dinner.
guests = ['tobey maguire', 'andrew garfield', 'tom holland']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# Can't make it to dinner
name = guests[2].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Tom can't make it! Let's invite Shameik Moore instead.
del guests[2]
guests.insert(2, 'shameik moore')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'nicholas hammond')
guests.insert(1, 'yuri lowenthal')
guests.append('shinji todo')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# There should be two people left. Let's invite them.
print(guests)
name = guests[0].title()
print(f"{name.title()}, please come to dinner.")

name = guests[1].title()
print(f"{name.title()}, please come to dinner.")

# Empty out the list.
del guests[0]
del guests[0]

# Prove the list is empty.
print(guests)
