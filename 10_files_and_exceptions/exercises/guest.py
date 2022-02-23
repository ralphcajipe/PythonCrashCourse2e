prompt = "Please tell me your name: "

guest = input(prompt)

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(guest)
