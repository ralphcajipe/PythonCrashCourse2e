prompt = "How many people are in your dinner group?: "
people = int(input(prompt))

if people > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")