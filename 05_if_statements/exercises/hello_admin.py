usernames = ['admin', 'dal-mi', 'do-san', 'ji-pyeong', 'in-jae']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for loggin in again.")
