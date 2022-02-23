# Default Values

# default value for animal_type
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='rambo')
describe_pet('rambo')
describe_pet(pet_name='harry', animal_type='hamster')