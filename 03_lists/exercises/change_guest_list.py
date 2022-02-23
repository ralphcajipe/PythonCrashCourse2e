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




