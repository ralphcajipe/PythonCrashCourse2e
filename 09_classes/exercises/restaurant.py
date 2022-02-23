class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"\n{self.restaurant_name} is a {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"\n{self.restaurant_name} is open! Come on in!")


# Make Instance
restaurant = Restaurant('ultimate shawarma', 'middle eastern')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
