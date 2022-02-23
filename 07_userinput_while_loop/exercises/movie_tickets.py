prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' when you are finished: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
        
    # assign age variable as integer now
    age = int(age)

    if age < 3:
        print(" You get in for free!")
    elif age < 13:
        print(" Your ticket is $10.")
    else:
        print(" Your ticket is $15.")
