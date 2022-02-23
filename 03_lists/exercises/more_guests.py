# Invite some people to dinner.
guests = ['tobey maguire', 'andrew garfield', 'tom holland']

guest0 = guests[0].title()
print(f"{guest0}, please come to dinner.")

guest1 = guests[1].title()
print(f"{guest1}, please come to dinner.")

guest2 = guests[2].title()
print(f"{guest2}, please come to dinner.")

# Can't make it to dinner
guest2 = guests[2].title()
print(f"\nSorry, {guest2} can't make it to dinner.")

# Tom can't make it! Let's invite Shameik Moore instead.
del guests[2]
guests.insert(2, 'shameik moore')

# Print the invitations again.
guest0 = guests[0].title()
print(f"\n{guest0}, please come to dinner.")

guest1 = guests[1].title()
print(f"{guest1}, please come to dinner.")

guest2 = guests[2].title()
print(f"{guest2}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'nicholas hammond')
guests.insert(1, 'yuri lowenthal')
guests.append('shinji todo')

guest0 = guests[0].title()
print(f"{guest0}, please come to dinner.")

guest1 = guests[1].title()
print(f"{guest1}, please come to dinner.")

guest2 = guests[2].title()
print(f"{guest2}, please come to dinner.")

guest3 = guests[3].title()
print(f"{guest3}, please come to dinner.")

guest4 = guests[4].title()
print(f"{guest4}, please come to dinner.")

guest5 = guests[5].title()
print(f"{guest5}, please come to dinner.")