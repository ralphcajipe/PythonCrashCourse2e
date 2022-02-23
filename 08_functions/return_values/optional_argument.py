# Making an Argument Optional

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


person1 = get_formatted_name('ralph', 'cajipe')
print(person1)

person2 = get_formatted_name('ralph', 'cajipe', 'henrik')
print(person2)
