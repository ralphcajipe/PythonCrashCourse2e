from admin import Admin

# Make Admin instance
ralph = Admin('ralph', 'cajipe', 'rcaj', 'ralphcajipe@gmail.com', 'earth')
ralph.describe_user()

ralph_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
]
ralph.privileges.privileges = ralph_privileges

print(f"\nThe admin {ralph.username} has these privileges: ")
ralph.privileges.show_privileges()
