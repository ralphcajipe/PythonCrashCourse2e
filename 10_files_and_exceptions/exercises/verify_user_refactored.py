"""Refactored verify_user.py"""
import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    """if username is not empty"""
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    # Let's prompt for a new username.
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")


greet_user()

"""
The return statement means the code in the function stops running after
printing the welcome back message. When the username doesn’t exist, or 
the username is incorrect, the return statement is never reached. 
The second part of the function will only run when the if statements fail, 
so we don’t need an else block. Now the function prompts for a new 
username when either if statement fails.

The only thing left to address is the nested if statements. This can be 
cleaned up by moving the code that checks whether the username is correct 
to a separate function. If you can do that, you might try making a new
function called check_username() and see if you can remove the nested 
if statement from greet_user().
"""
