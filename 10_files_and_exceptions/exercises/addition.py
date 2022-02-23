print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    try:
        x = input("\nFirst number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("Second number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        answer = x + y
        print(f"The sum of {x} and {y} is {answer}.")
        # print("The sum of {} and {} is {}.".format(x, y, answer))
