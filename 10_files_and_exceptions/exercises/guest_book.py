filename = 'guest_book.txt'

prompt = "\nYour name please? "

print("Enter 'quit' when you are finished.")
while True:
    name = input(prompt)
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name)
        print(f"Hi {name}, you've been added to the guest book.")
