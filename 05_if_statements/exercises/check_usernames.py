# Checking Usernames

current_users = ['penny', 'Leonard', 'sheldon', 'howard', 'raj']
new_users = ['ralph', 'henrik', 'cajipe', 'Howard', 'leonard']

current_users_lower = [user.lower() for user in current_users]

""" 
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
"""

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is taken. Please try another.")
    else:
        print(f"Great, {new_user} is still available.")
